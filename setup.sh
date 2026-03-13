#!/usr/bin/env bash

echo "Setting up Canvas CLI Tool..."

# Move to project root (location of this script)
cd "$(dirname "$0")"

# Check that python3 exists
if ! command -v python3 &> /dev/null
then
    echo "Python3 is required but not installed."
    exit 1
fi

# Create virtual environment if it does not exist
if [ ! -d ".venv" ]; then
    echo "Creating virtual environment..."
    python3 -m venv .venv
fi

# Activate virtual environment
echo "Activating virtual environment..."
source .venv/bin/activate

# Upgrade pip
python -m pip install --upgrade pip

# Install dependencies
if [ -f "requirements.txt" ]; then
    echo "Installing dependencies..."
    pip install -r requirements.txt
else
    echo "requirements.txt not found."
fi

# Check for .env file
if [ ! -f ".env" ]; then
    echo ""
    echo "WARNING: .env file not found."
    echo "Create a .env file with:"
    echo "CANVAS_API_TOKEN=your_canvas_token_here"
    echo "CANVAS_BASE_URL=https://boisestatecanvas.instructure.com"
else
    echo ".env file found."
fi

echo ""
echo "Setup complete."
echo "You can now run commands such as:"
echo "python -m src.main all-courses"
echo "python -m src.main current-courses"
echo "python -m src.main assignments --course-id 12345"