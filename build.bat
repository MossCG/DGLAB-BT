@echo off
title [DGLAB-BT-EXE] Building......
pyinstaller DGLAB-BT-EXE.spec

title [DGLAB-BT-EXE] Cleaning......
echo Removing temp files.......
del /F /S /Q build
rmdir /S /Q build

title [DGLAB-BT-EXE] Complete!
echo ------------------------------
echo Build complete!
echo File located in ./dist
pause