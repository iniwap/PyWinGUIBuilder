#!/usr/bin/python
# -*- coding: UTF-8 -*-

"""

主界面

"""

import os
import sys
import webbrowser
import PySimpleGUI as sg


__author__ = "iniwaper@gmail.com"
__copyright__ = "Copyright (C) 2025 iniwap"
# __date__ = "2025/04/17"


class MainGUI(object):
    def __init__(self):
        self._log_list = []
        # 设置主题
        sg.theme("systemdefault")

        menu_list = [
            ["帮助", ["帮助", "关于", "官网"]],
        ]

        layout = [
            [
                sg.Menu(
                    menu_list,
                )
            ],
            [
                sg.Image(
                    s=(640, 450),
                    filename=self.__get_res_path("UI\\bg.png", os.path.dirname(__file__)),
                    key="-BG-IMG-",
                    expand_x=True,
                )
            ],
            [
                sg.Text("", size=(12, 10)),
                sg.InputText(
                    default_text="请输入用户名",
                    size=(18, 1),
                    k="-USER_NAME-",
                    tooltip="输入账号",
                ),
                sg.InputText(
                    default_text="请输入密码",
                    size=(18, 1),
                    k="-USER_PWD-",
                    tooltip="输入密码",
                ),
                sg.Button(button_text="登录", s=(6, 2), k="-LOGIN_BTN-"),
            ],
        ]

        self._window = sg.Window(
            "软件 v1.0",
            layout,
            default_element_size=(12, 1),
            size=(640, 640),  # 展开650
            icon=self.__get_icon(),
        )

    def __get_res_path(self, file_name, basedir):
        if getattr(sys, "frozen", None):
            return os.path.join(sys._MEIPASS, file_name)

        return os.path.join(basedir, file_name)

    def __get_icon(self):
        return self.__get_res_path("UI\\icon.ico", os.path.dirname(__file__))

    def run(self):
        while True:
            event, values = self._window.read()
            print(event)
            if event == sg.WIN_CLOSED:  # always,  always give a way out!
                break
            elif event == "选择原始数据":
                self.convert_attendance_data()
            elif event == "-LOGIN_BTN-":
                sg.popup(
                    "登录成功！",
                    title="系统提示",
                    icon=self.__get_icon(),
                )
            elif event == "关于":
                sg.popup(
                    "关于软件",
                    "当前Version 1.0",
                    "Copyright (C) 2025 iniwap,All Rights Reserved",
                    title="系统提示",
                    icon=self.__get_icon(),
                )
            elif event == "官网":
                webbrowser.open("https://github.com/iniwap")
            elif event == "帮助":
                sg.popup(
                    "————————————操作说明————————————\n"
                    "一、基础软件框架，一键生成windows安装应用程序\n"
                    "二、修改gui.nsi，注意替换成自己的\n"
                    "三、点击tools目录下的make_exe，同目录下生成setup.exe",
                    title="使用帮助",
                    icon=self.__get_icon(),
                )


def gui_start():
    MainGUI().run()


if __name__ == "__main__":
    gui_start()
