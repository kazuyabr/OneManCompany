param(
  [Parameter(ValueFromRemainingArguments = $true)]
  [string[]]$Args
)

$ErrorActionPreference = 'Stop'
Set-StrictMode -Version Latest

Set-Location -LiteralPath $PSScriptRoot

$FirstArg = if ($null -ne $Args -and $Args.Count -gt 0) { [string]$Args[0] } else { '' }

function Write-Info {
  param([string]$Message)
  Write-Host "▸ $Message" -ForegroundColor Cyan
}

function Write-Warn {
  param([string]$Message)
  Write-Host "⚠ $Message" -ForegroundColor Yellow
}

function Write-ErrorExit {
  param([string]$Message)
  Write-Host "✖ $Message" -ForegroundColor Red
  exit 1
}

function Test-UvInstalled {
  return [bool](Get-Command uv -ErrorAction SilentlyContinue)
}

function Ensure-Uv {
  if (Test-UvInstalled) {
    return
  }

  Write-Info 'Installing UV (fast Python package manager)...'
  try {
    Invoke-RestMethod -Uri 'https://astral.sh/uv/install.ps1' | Invoke-Expression
  } catch {
    Write-ErrorExit "Failed to install UV: $($_.Exception.Message)"
  }

  $uvHome = Join-Path $env:USERPROFILE '.local\bin'
  if (Test-Path $uvHome) {
    $env:Path = "$uvHome;$env:Path"
  }

  if (-not (Test-UvInstalled)) {
    Write-ErrorExit 'UV installed but not found in PATH. Restart the terminal and try again.'
  }
}

function Ensure-Venv {
  Ensure-Uv

  if (-not (Test-Path '.venv')) {
    Write-Info 'Creating Python virtual environment (via UV)...'
    & uv venv --python 3.12
    if ($LASTEXITCODE -ne 0) {
      Write-ErrorExit 'Failed to create the Python virtual environment.'
    }
  }

  $pythonExe = Join-Path '.venv' 'Scripts\python.exe'
  if (-not (Test-Path $pythonExe)) {
    Write-ErrorExit 'Virtual environment is incomplete. Remove .venv and run again.'
  }

  Write-Info 'Installing dependencies...'
  & uv pip install -e . -q
  if ($LASTEXITCODE -ne 0) {
    Write-ErrorExit 'Failed to install project dependencies.'
  }
}

function Invoke-InitWizard {
  Ensure-Venv
  Write-Info 'Running setup wizard...'
  & (Join-Path '.venv' 'Scripts\onemancompany-init.exe') @Args
  if ($LASTEXITCODE -ne 0) {
    Write-ErrorExit 'Setup wizard failed.'
  }
}

function Test-InitComplete {
  return (
    (Test-Path '.onemancompany') -and
    (Test-Path '.onemancompany\.env') -and
    (Test-Path '.onemancompany\company\human_resource\employees')
  )
}

function Start-Server {
  Ensure-Venv

  if (-not (Test-InitComplete)) {
    if (Test-Path '.onemancompany') {
      Write-Warn '.onemancompany/ exists but is incomplete — re-running setup wizard'
    } else {
      Write-Warn '.onemancompany/ not found — launching setup wizard first'
    }
    & (Join-Path '.venv' 'Scripts\onemancompany-init.exe')
    if ($LASTEXITCODE -ne 0) {
      Write-ErrorExit 'Setup wizard failed.'
    }
  }

  Write-Info 'Starting OneManCompany...'
  & (Join-Path '.venv' 'Scripts\onemancompany.exe') @Args
  exit $LASTEXITCODE
}

switch -Regex ($FirstArg) {
  '^init$' {
    $scriptArgs = if ($Args.Length -gt 1) { $Args[1..($Args.Length - 1)] } else { @() }
    $Args = $scriptArgs
    Invoke-InitWizard
  }
  '^(--help|-h)$' {
    Write-Host 'Usage: powershell -ExecutionPolicy Bypass -File .\start.ps1 [init | --port PORT | --host HOST]'
    Write-Host ''
    Write-Host 'Commands:'
    Write-Host '  (default)   Start the server (auto-init if needed)'
    Write-Host '  init        Run the setup wizard'
    Write-Host ''
    Write-Host 'Options are passed through to uvicorn (--host, --port, etc.)'
  }
  default {
    Start-Server
  }
}
