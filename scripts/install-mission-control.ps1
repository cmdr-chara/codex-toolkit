[CmdletBinding()]
param(
    [string]$CodexHome = (Join-Path $HOME '.codex')
)

$ErrorActionPreference = 'Stop'
$repoRoot = Split-Path -Parent $PSScriptRoot
$skillSource = Join-Path $repoRoot 'skills\delegate-with-mission-cards'
$agentSource = Join-Path $repoRoot 'agents\mission-control'
$skillTarget = Join-Path $CodexHome 'skills\delegate-with-mission-cards'
$agentTarget = Join-Path $CodexHome 'agents'
$stamp = Get-Date -Format 'yyyyMMdd-HHmmss'
$backupRoot = Join-Path $CodexHome "backups\mission-control-$stamp"

New-Item -ItemType Directory -Force -Path $agentTarget | Out-Null

if (Test-Path -LiteralPath $skillTarget) {
    New-Item -ItemType Directory -Force -Path $backupRoot | Out-Null
    Copy-Item -LiteralPath $skillTarget -Destination (Join-Path $backupRoot 'delegate-with-mission-cards') -Recurse
    Remove-Item -LiteralPath $skillTarget -Recurse
}

Copy-Item -LiteralPath $skillSource -Destination $skillTarget -Recurse

Get-ChildItem -LiteralPath $agentSource -Filter '*.toml' | ForEach-Object {
    $target = Join-Path $agentTarget $_.Name
    if (Test-Path -LiteralPath $target) {
        New-Item -ItemType Directory -Force -Path (Join-Path $backupRoot 'agents') | Out-Null
        Copy-Item -LiteralPath $target -Destination (Join-Path $backupRoot 'agents')
    }
    Copy-Item -LiteralPath $_.FullName -Destination $target -Force
}

Write-Host 'Mission Control installed. Start a fresh Codex task to load it.'
if (Test-Path -LiteralPath $backupRoot) {
    Write-Host "Backups: $backupRoot"
}
