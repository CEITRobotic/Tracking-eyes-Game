@echo off

set "env_path=env\Scripts\activate.bat"

where python >nul 2>nul
if %errorlevel% neq 0 (
    echo Don't have Python.
) else (
    echo Python is installed.

    where pip >nul 2>nul
    if %errorlevel% neq 0 (
        echo Pip is not installed.
    ) else (
        echo Pip is installed.

        python --version
        pip --version

        if not exist "env" (
          pip install virtualenv
          python -m venv env
        ) else (
          echo Environment already exists
        )

        if exist "env" (
          echo Accessing environment...
          call "%env_path%"
          pip install -r requirement.txt
          cls
          python main.py
        )
    )
)
