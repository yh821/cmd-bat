@echo off

set folder=%~dp0../ɢͼ
if not exist %folder% (set folder=%~dp0../ͼ��)

for %%i in (*png *jpg) do (copy /y "%%i" "%folder%")

pause