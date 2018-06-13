@echo off
@echo ##TPBegin##

cd /d %1

set cmd="C:\Program Files\TexurePacker\bin\TexturePacker.exe"
if not exist %cmd% (set cmd="D:\Program Files\TexurePacker\bin\TexturePacker.exe")

setlocal enabledelayedexpansion
for %%i in (*png *jpg) do (set p=!p! %%i)
%cmd% ^
--format unity-texture2d ^
--sheet %1../%3".png" ^
--data %1../%3".tpsheet" ^
--trim-mode %4 ^
--size-constraints POT ^
--max-size %5 ^
--shape-padding %6 ^
--border-padding %6 ^
!p!

@echo ##TPEnd##