call .venv\Scripts\Activate
pip install --upgrade pip
pip install -r requirements.txt
reflex init
reflex export --frontend-only
rmdir /s /q public
powershell Expand-Archive -Path frontend.zip -DestinationPath public
del /f frontend.zip
call .venv\Scripts\Deactivate