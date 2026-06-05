# Point Obsidian's workspace.json at the tracked copy in this personal folder.
#
# Run ONCE per workstation after cloning/pulling, so your tab/pane layout
# follows you across machines without colliding with other users' layouts.
# Creating a symlink on Windows needs Developer Mode ON (Settings > For
# developers) or an elevated shell.
#
#   pwsh .personal/darren@neese.us/obsidian/link-workspace.ps1
#
$ErrorActionPreference = 'Stop'
$target = Join-Path $PSScriptRoot 'workspace.json'                       # the tracked file (sibling of this script)
$repo   = (Resolve-Path (Join-Path $PSScriptRoot '..\..\..')).Path      # repo root
$link   = Join-Path $repo '.obsidian\workspace.json'                    # where Obsidian reads it

if (-not (Test-Path $target)) { throw "Tracked workspace file not found next to this script: $target" }
New-Item -ItemType Directory -Force -Path (Split-Path $link) | Out-Null
if (Test-Path $link) { Remove-Item $link -Force }

# Prefer a symlink (needs Developer Mode/admin); fall back to a hardlink,
# which needs no elevation and behaves identically for a same-volume file.
try {
  New-Item -ItemType SymbolicLink -Path $link -Target $target -ErrorAction Stop | Out-Null
  Write-Host "Linked (symlink): $link  ->  $target"
} catch {
  New-Item -ItemType HardLink -Path $link -Target $target -ErrorAction Stop | Out-Null
  Write-Host "Linked (hardlink): $link  ==  $target"
}
