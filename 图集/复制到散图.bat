@echo off

set folder=%~dp0../É¢Í¼
if not exist %folder% (set folder=%~dp0../Í¼¼¯)

for %%i in (*png *jpg) do (copy /y "%%i" "%folder%")

pause