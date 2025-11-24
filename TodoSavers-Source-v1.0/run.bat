@echo off
echo.
echo  Installing required packages...
pip install --upgrade pip pyinstaller customtkinter >nul 2>&1

echo.
echo  Running to TodoSavers 1.0.py (please wait)...
echo.

python main.py

echo.
echo  DONE!
echo.
pause