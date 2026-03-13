# setup.ps1

Write-Host "Setting up Canvas CLI Tool..." -ForegroundColor Cyan

# Allow script execution only for this PowerShell session
Set-ExecutionPolicy -Scope Process -ExecutionPolicy RemoteSigned -Force

# Move to the folder this script is in
Set-Location $PSScriptRoot

# Create virtual environment if it does not exist
if (!(Test-Path ".venv")) {
    Write-Host "Creating virtual environment..." -ForegroundColor Yellow
    python -m venv .venv
}

# Activate virtual environment
Write-Host "Activating virtual environment..." -ForegroundColor Yellow
& ".\.venv\Scripts\Activate.ps1"

# Install/update dependencies if requirements.txt exists
if (Test-Path "requirements.txt") {
    Write-Host "Installing dependencies..." -ForegroundColor Yellow
    python -m pip install --upgrade pip
    pip install -r requirements.txt
} else {
    Write-Host "requirements.txt not found." -ForegroundColor Red
}

# Check for .env
if (!(Test-Path ".env")) {
    Write-Host ".env file is missing." -ForegroundColor Red
    Write-Host "Create a .env file in the project root with:" -ForegroundColor Red
    Write-Host "CANVAS_API_TOKEN=your_canvas_token_here"
    Write-Host "CANVAS_BASE_URL=https://boisestatecanvas.instructure.com"
} else {
    Write-Host ".env file found." -ForegroundColor Green
}

Write-Host ""
Write-Host "Setup complete." -ForegroundColor Green
Write-Host "You can now run commands like:" -ForegroundColor Cyan
Write-Host "python -m src.main all-courses"
Write-Host "python -m src.main current-courses"
Write-Host "python -m src.main assignments --course-id 12345"