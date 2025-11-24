@echo off
echo.
echo  Installing required packages...
pip install --upgrade pip pyinstaller customtkinter >nul 2>&1

echo.
echo  Building TodoSavers 1.0.exe (please wait)...
echo.

pyinstaller --onefile --windowed --name="TodoSavers 1.0" --icon=icon.ico main.py

echo.
echo  DONE!
echo  Your executable is here: dist\TodoSavers 1.0.exe
echo.
pause