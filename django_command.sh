#!/bin/bash

# Django Commands Script
# This script provides commonly used Django commands with simple explanations.

# Function to display the menu
show_menu() {
    echo "Django Commands Menu"
    echo "1. Start a new Django project"
    echo "2. Start a new Django app"8
    echo "3. Make migrations"
    echo "4. Apply migrations"
    echo "5. Run the development server"
    echo "6. Create a superuser"
    echo "7. Open Django shell"
    echo "9. Kill process running on port 8000"
    echo "8. Exit"
}

# Function to execute the selected command
execute_command() {
    case $1 in
        1)
            echo "Enter project name:"
            read project_name
            django-admin startproject $project_name
            echo "Project '$project_name' created successfully."
            ;;
        2)
            echo "Enter app name:"
            read app_name
            python manage.py startapp $app_name
            echo "App '$app_name' created successfully."
            ;;
        3)
            python manage.py makemigrations
            echo "Migrations created successfully."
            ;;
        4)
            python manage.py migrate
            echo "Migrations applied successfully."
            ;;
        5)
            python manage.py runserver
            echo "Development server started at http://127.0.0.1:8000/"
            ;;
        6)
            python manage.py createsuperuser
            ;;
        7)
            python manage.py shell
            ;;
        8)
            echo "Exiting..."
            exit 0
            ;;
        # 关闭进程 8000
        9)
            sudo lsof -i:8000
            echo "Enter the PID of the process you want to kill:"
            read pid
            sudo kill -9 $pid
            ;;
        *)
            echo "Invalid option. Please try again."
            ;;
    esac
}

# Main script loop
while true; do
    show_menu
    echo "Enter your choice:"
    read choice
    execute_command $choice
done