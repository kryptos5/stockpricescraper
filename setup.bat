@echo off
cd /d "%~dp0"
echo Creating virtual environment...
python -m venv .venv
echo Activating virtual environment...
call ".venv/Scripts/activate"
echo Installing required packages...
pip install -r ./requirements.txt
call ".venv/Scripts/deactivate"
echo Done!
pause