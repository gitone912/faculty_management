@echo off
rem Navigate to the Desktop directory
cd %userprofile%\Desktop

rem Navigate to the faculty_management directory
cd faculty_management

rem Run the Python manage.py runserver command
python manage.py runserver

rem Pause to keep the command prompt window open
pause
