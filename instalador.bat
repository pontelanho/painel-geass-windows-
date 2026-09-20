@echo off
title Geass Setup - Auto Installer
color 0D

:: 1. VERIFICACAO DE PRIVILEGIOS DE ADMINISTRADOR (Necessario para instalar apps)
>nul 2>&1 "%SYSTEMROOT%\system32\cacls.exe" "%SYSTEMROOT%\system32\config\system"
if '%errorlevel%' NEQ '0' (
    echo [!] Solicitando privilegios de administrador para instalar dependencias...
    goto UACPrompt
) else ( goto gotAdmin )

:UACPrompt
    echo Set UAC = CreateObject^("Shell.Application"^) > "%temp%\getadmin.vbs"
    echo UAC.ShellExecute "%~s0", "", "", "runas", 1 >> "%temp%\getadmin.vbs"
    "%temp%\getadmin.vbs"
    del "%temp%\getadmin.vbs"
    exit /B

:gotAdmin
:: Muda para o diretorio original de onde o script foi chamado
cd /d "%~dp0"

echo ==========================================
echo       GEASS SYSTEM - INSTALADOR
echo ==========================================
echo.

:: 2. VERIFICAR E INSTALAR PYTHON AUTOMATICAMENTE
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo [!] Python nao encontrado no sistema.
    echo [!] A baixar o instalador oficial do Python 3 (isso pode levar um minuto)...
    curl -L -o "%TEMP%\python_installer.exe" "https://www.python.org/ftp/python/3.11.8/python-3.11.8-amd64.exe"

    echo [!] A instalar o Python silenciosamente...
    start /wait "" "%TEMP%\python_installer.exe" /quiet InstallAllUsers=1 PrependPath=1 Include_test=0
    echo [*] Python instalado com sucesso!
) else (
    echo [*] Python ja esta instalado no sistema.
)

:: 3. VERIFICAR E INSTALAR GIT BASH AUTOMATICAMENTE
set "GITBASH=C:\Program Files\Git\git-bash.exe"
if not exist "%GITBASH%" (
    set "GITBASH=C:\Program Files\Git\bin\bash.exe"
)

if not exist "%GITBASH%" (
    echo [!] Git Bash nao encontrado no sistema.
    echo [!] A baixar o Git for Windows (isso pode levar um minuto)...
    curl -L -o "%TEMP%\git_installer.exe" "https://github.com/git-for-windows/git/releases/download/v2.44.0.windows.1/Git-2.44.0-64-bit.exe"

    echo [!] A instalar o Git Bash silenciosamente...
    start /wait "" "%TEMP%\git_installer.exe" /VERYSILENT /NORESTART
    set "GITBASH=C:\Program Files\Git\git-bash.exe"
    echo [*] Git Bash instalado com sucesso!
) else (
    echo [*] Git Bash ja esta instalado no sistema.
)

:: 4. INSTALAR DEPENDENCIAS (REQUESTS)
echo.
echo [!] A instalar biblioteca de integracao (requests)...
:: Usa 'py' primeiro, pois ele reconhece recem-instalados sem precisar fechar o CMD
py -m pip install requests >nul 2>&1
if %errorlevel% neq 0 (
    python -m pip install requests
)
echo [*] Modulos sincronizados.

:: 5. CRIAR ATALHOS (DESKTOP E MENU INICIAR) COM O ICONE GEASS.ICO
echo.
echo [!] A forjar atalhos de acesso...

set "SCRIPT=%TEMP%\CriaAtalho.vbs"
echo Set oWS = WScript.CreateObject("WScript.Shell") > "%SCRIPT%"

:: -> Atalho na Area de Trabalho
echo sLinkFile = "%USERPROFILE%\Desktop\Geass Terminal.lnk" >> "%SCRIPT%"
echo Set oLink = oWS.CreateShortcut(sLinkFile) >> "%SCRIPT%"
echo oLink.TargetPath = "%GITBASH%" >> "%SCRIPT%"
echo oLink.Arguments = "geass.sh" >> "%SCRIPT%"
echo oLink.WorkingDirectory = "%~dp0" >> "%SCRIPT%"
echo oLink.Description = "Geass Intelligence Terminal" >> "%SCRIPT%"
echo oLink.IconLocation = "%~dp0geass.ico" >> "%SCRIPT%"
echo oLink.Save >> "%SCRIPT%"

:: -> Atalho no Menu Iniciar (Lista de Apps do Windows)
echo sLinkFile2 = "%APPDATA%\Microsoft\Windows\Start Menu\Programs\Geass Terminal.lnk" >> "%SCRIPT%"
echo Set oLink2 = oWS.CreateShortcut(sLinkFile2) >> "%SCRIPT%"
echo oLink2.TargetPath = "%GITBASH%" >> "%SCRIPT%"
echo oLink2.Arguments = "geass.sh" >> "%SCRIPT%"
echo oLink2.WorkingDirectory = "%~dp0" >> "%SCRIPT%"
echo oLink2.Description = "Geass Intelligence Terminal" >> "%SCRIPT%"
echo oLink2.IconLocation = "%~dp0geass.ico" >> "%SCRIPT%"
echo oLink2.Save >> "%SCRIPT%"

cscript /nologo "%SCRIPT%" >nul 2>&1
del "%SCRIPT%"

echo.
echo ==========================================
echo [SUCESSO] Sincronizacao concluida!
echo.
echo O Python e o Git Bash foram validados/instalados.
echo Atalhos criados na Area de Trabalho e no Menu Iniciar (Apps).
echo.
echo Pode fechar esta janela e abrir o "Geass Terminal" pelos atalhos.
echo ==========================================
pause
