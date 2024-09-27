@echo off
chcp 65001
color 0f
title [+] - Riot Vanguard Fix Tool - [+]
cls

net session >nul 2>&1
if %errorlevel% neq 0 (
    echo [!] Please run this script as Administrator.
    pause
    exit /b
)


:Tool
cls
echo ----------------------------------------
echo			    Options
echo.
echo use this only when u cant 
echo update Valorant
echo (dependency could not be installed...)
echo.
echo [1]  Deactivate Riot Vanguard
echo [2]  credits
echo [3]  exit
echo.
echo ----------------------------------------
echo.
set /p ans="root@root ~ # "


if %ans%==1 (
    goto main
)
if %ans%==2 (
    goto credits
)
if %ans%==3 (
    goto exit
)


:credits
cls
echo ----------------------------------------
echo     	  Made and Developed by
echo        	 @3n3scan#6908
echo ----------------------------------------
pause
cls
goto Tool


:exit
pause
exit


:controlpanel
cls
appwiz.cpl
echo.
echo ----------------------------------------
echo      	  Successfully Opened
echo     	 Windows Control Panel
echo ----------------------------------------
echo.
pause
goto Tool


:main
cls
echo.
echo ----------------------------------------
echo       Stopping Riot Vanguard services...
echo ----------------------------------------
echo.
timeout 3 > NUL
net stop vgc
net stop vgk
timeout 1 > NUL
echo !!! Successfully stopped Riot Vanguard services !!!
echo.
timeout 5 > NUL
echo ----------------------------------------
echo      		 deleting vgc...
echo ----------------------------------------
echo.
timeout 3 > NUL
sc delete vgc
timeout 1 > NUL
echo !!! Successfully deleted vgc !!!
echo.
timeout 5 > NUL
echo.
echo ----------------------------------------
echo      		deleting vgk...
echo ----------------------------------------
echo.
timeout 3 > NUL
sc delete vgk
timeout 1 > NUL
echo !!! Successfully deleted vgk !!!
echo.
timeout 5 > NUL
pause
cls
goto deletefolder


:deletefolder
cls
echo.
echo ----------------------------------------
echo       Deleting Riot Vanguard folder...
echo ----------------------------------------
echo.
timeout 3 > NUL
takeown /f "C:\Program Files\Riot Vanguard" /r /d y
icacls "C:\Program Files\Riot Vanguard" /grant administrators:F /t
rmdir /s /q "C:\Program Files\Riot Vanguard"
timeout 1 > NUL
echo !!! Riot Vanguard folder deleted !!!
echo.
timeout 5 > NUL
goto controlpanel