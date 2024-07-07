# 启动项目并打开网页，如果已经启动直接打开网页
# 1. 启动项目
#!/bin/bash

PROJECT_DIR="/path/to/your/schedule_project"
PORT=8000
URL="http://127.0.0.1:$PORT"

# Function to check if the server is already running
is_server_running() {
    lsof -i :$PORT | grep LISTEN > /dev/null
    return $?
}

# Function to open the browser
open_browser() {
    open $URL
}

# Navigate to project directory
cd $PROJECT_DIR

# Check if server is running
if is_server_running; then
    echo "Server is already running. Opening the browser..."
    open_browser
else
    echo "Starting the Django server..."
    source env/bin/activate  # Activate virtual environment
    python manage.py runserver &  # Start the server in the background
    sleep 5  # Wait for a few seconds to ensure the server starts
    open_browser
fi