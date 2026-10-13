Set-Location $PSScriptRoot
if (-not (Get-Command webalizer -ErrorAction SilentlyContinue)) {
    throw 'Install Webalizer or use the lab Windows GUI; no Webalizer run is claimed.'
}
New-Item -ItemType Directory -Force reports | Out-Null
webalizer -c webalizer.conf
if ($LASTEXITCODE -ne 0) { throw 'Webalizer failed.' }
