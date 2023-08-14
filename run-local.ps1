# Checks python
if ((Get-Command "python3" -ErrorAction SilentlyContinue) -eq $null) {
    Write-Error "Python 3 isn't installed. Please install" -ForegroundColor Red
    exit 1
}

# Collects details
Write-Host "====== Please provide the following details ======" -ForegroundColor Blue
$username = Read-Host -Prompt 'Please provide your username'
$password = Read-Host -Prompt 'Please provide your password'
$target_url = Read-Host -Prompt 'Please provide the event url'
$hook_url = Read-Host -Prompt 'Please provide a slack webhook url'

# Saves user inputs to .env file
Write-Host "======Saving inputs to .env file ======" -ForegroundColor Green
"USERNAME=" + $username | Out-File -FilePath $PSScriptRoot\.env
"PASSWORD=" + $password >>  $PSScriptRoot\.env
"TARGET_URL=" + $target_url >>  $PSScriptRoot\.env
"HOOK_URL=" + $hook_url >>  $PSScriptRoot\.env

Write-Host "====== Looking for tickets now ======" -ForegroundColor Green
Start-Process -FilePath "python" -Wait -ArgumentList "main.py" -WorkingDirectory $PSScriptRoot -NoNewWindow