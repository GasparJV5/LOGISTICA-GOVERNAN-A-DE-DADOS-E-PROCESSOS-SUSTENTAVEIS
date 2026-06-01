@echo off
cd /d %~dp0

echo ===============================
echo INICIANDO MDR ECOSYSTEM
echo ===============================

REM 🔴 BACKEND (BANCO)
start cmd /k "echo BACKEND INICIADO && python server.py"

timeout /t 3 >nul

REM 🔵 FRONTEND (HTML)
start cmd /k "echo FRONTEND INICIADO && python -m http.server 5500 --bind 10.100.20.142"

timeout /t 3 >nul

REM 🌐 ABRIR NO CHROME
start chrome http://10.100.20.142:5500/testemvp.html

echo.
echo ✅ SISTEMA PRONTO
echo ✅ Banco ativo (porta 5000)
echo ✅ Interface ativa (porta 5500)
echo ✅ Abrindo navegador...

exit
