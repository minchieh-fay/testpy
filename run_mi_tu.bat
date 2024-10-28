@echo off

:: 获取批处理脚本所在目录
set "script_dir=%~dp0"

:: 设置工作目录为脚本所在目录
cd /d "%script_dir%"


python run_mi_tu.py


echo 调试卡住
timeout /t 35 /nobreak  >nul