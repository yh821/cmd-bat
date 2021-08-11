@echo off

::工程目录
set proj_path="D:\client\u3d_proj"
::更新间隔
set wait_time=180

start /B python update.py %proj_path% %wait_time%

::pause