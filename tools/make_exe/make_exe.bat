
::自动打包生成EXE

@echo off

:start

::将UI文件复制到make_exe环境下
xcopy /Y ..\..\scripts\UI resources\UI\ /e

::首先编译PYD
python build_pyd.py -b

::打包
pyinstaller -y -n GUI ^
-F --key iniwap_gui@2025 ^
../../main.py ^
-i resources/UI/icon.ico ^
--add-data "resources/UI;UI" ^
--add-data "resources/data;data" ^
--noconsole

::生成完成后，删除临时文件PYD
python build_pyd.py -c

::生成安装包，注意这个需要是实际的安装路径，当然也可以设置环境变量
D:\Software\NSIS\makensis.exe gui.nsi

pause