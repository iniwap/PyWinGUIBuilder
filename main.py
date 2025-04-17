# 注意： 所有用到的模块都要在此处导入

import os  # noqa 841
import webbrowser  # noqa 841
import ctypes  # noqa 841
import sys  # noqa 841
import PySimpleGUI as sg  # noqa 841

import scripts.MainGUI as MainGUI


def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except Exception as e:  # noqa841
        return False


def run():
    MainGUI.gui_start()


def admin_run():
    if is_admin():
        run()
    else:
        ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, __file__, None, 0)


if __name__ == "__main__":

    if len(sys.argv) > 1:  # 第一个是文件名，如果多于1个，说明其他模式启动
        if sys.argv[1] == "-d":
            run()
        else:
            admin_run()
    else:
        admin_run()
