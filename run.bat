@echo off
cd /d "%~dp0"
echo Activating virtual environment...
call ".venv/Scripts/activate"
echo Running script...
python "stockpricescraper/StockPriceScraper.py"
call ".venv/Scripts/deactivate"
echo Done!
pause