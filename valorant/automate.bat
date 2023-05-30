@echo off

echo account name Key is 1
echo account name key is 2

set /p "Key=Which Account do you want to play:"
if "%Key%"=="1" (
     set "username=username"
     set "password=pass wordd"
     goto start
) else if "%Key%"=="2" (
     set "username=username2"
     set "password=password"
     goto start
) else (
   echo Invalid username.
   goto :eof
)

:start
start "" "C:\Riot Games\Riot Client\RiotClientServices.exe"
set "appWindowTitle=Riot Client Main"
:LOOP
timeout /t 1 >nul
powershell -command "$appWindow = (new-object -com wscript.shell).AppActivate('%appWindowTitle%'); if ($appWindow) { exit 0 } else { exit 1 }"
if %errorlevel% equ 1 (
    goto :LOOP
) else (
    powershell -command "(new-object -com wscript.shell).SendKeys('%username%')"
    powershell -command "(new-object -com wscript.shell).SendKeys('{TAB}')"
    powershell -command "(new-object -com wscript.shell).SendKeys('%password%')"
    powershell -command "(new-object -com wscript.shell).SendKeys('{ENTER}')"
)
set "appWindowTitle=Riot Client Main"
timeout /t 1 >nul
powershell -command "$appWindow = (new-object -com wscript.shell).AppActivate('%appWindowTitle%'); if ($appWindow) { exit 0 } else { exit 1 }"
if %errorlevel% equ 1 (
    goto :LOOP
) else (
      powershell -command "(new-object -com wscript.shell).SendKeys('{TAB}')"
      powershell -command "(new-object -com wscript.shell).SendKeys('{TAB}')"
      powershell -command "(new-object -com wscript.shell).SendKeys('{TAB}')"
      powershell -command "(new-object -com wscript.shell).SendKeys('{TAB}')"
      powershell -command "(new-object -com wscript.shell).SendKeys('{TAB}')"
      powershell -command "(new-object -com wscript.shell).SendKeys('{ENTER}')"
)
powershell -command "(new-object -com wscript.shell).SendKeys('{TAB}')"
powershell -command "(new-object -com wscript.shell).SendKeys('{TAB}')"
powershell -command "(new-object -com wscript.shell).SendKeys('{TAB}')"
powershell -command "(new-object -com wscript.shell).SendKeys('{TAB}')"
powershell -command "(new-object -com wscript.shell).SendKeys('{TAB}')"
powershell -command "(new-object -com wscript.shell).SendKeys('{ENTER}')"
