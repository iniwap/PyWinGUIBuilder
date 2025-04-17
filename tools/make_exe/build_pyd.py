#!/usr/bin/python
# -*- coding: UTF-8 -*-

import os
import sys
import shutil


project_path = os.path.abspath("../../")
project_dirs = [
    "../../scripts/",
    # "../../", #不能编译入口文件，否则找不到
]


def build_pyd():
    # 编译pyd
    os.system("python setup.py build_ext")  # 因为路径问题，这里不自动复制到原文件目录，--inplace

    for c_dir in project_dirs:
        c_files = os.listdir(c_dir)
        for c_file in c_files:
            if ".c" == os.path.splitext(c_file)[1]:
                os.remove(os.path.join(os.path.abspath(c_dir), c_file))

    # 复制build目录下的文件pyd
    pyd_path = "build/lib.win-amd64-3.10/"

    pyd_filelist = []

    def get_pyd_filepath(dir_path, file_list):
        """
        递归获取目录下（文件夹下）所有文件的路径
        """

        try:
            for fp in os.listdir(dir_path):  # 获取文件（夹）名
                file_path = os.path.join(dir_path, fp)  # 将文件（夹）名补全为路径
                if os.path.isdir(file_path):  # 如果是文件夹，则递归
                    get_pyd_filepath(file_path, file_list)
                else:
                    file_list.append(file_path)  # 保存路径
        except Exception as e:  # noqa 841
            pass

        return file_list

    pyd_filelist = get_pyd_filepath(pyd_path, pyd_filelist)
    for pyd_file in pyd_filelist:
        src_path = pyd_file
        dest_path = pyd_file.replace(pyd_path, "/")
        shutil.copy(src_path, project_path + dest_path)


def clear_pyd():
    for pyd_dir in project_dirs:
        pyd_files = os.listdir(pyd_dir)
        for pyd_file in pyd_files:
            if ".pyd" == os.path.splitext(pyd_file)[1]:
                os.remove(os.path.join(os.path.abspath(pyd_dir), pyd_file))


if __name__ == "__main__":
    if len(sys.argv) > 1:  # 第一个是文件名，如果多于1个，说明其他模式启动
        if sys.argv[1] == "-b":
            build_pyd()
        elif sys.argv[1] == "-c":
            clear_pyd()
        else:
            print("请刷入命令行参数：-b(编译)，-c(清除)")
    else:
        print("请刷入命令行参数：-b(编译)，-c(清除)")

# python build_pyd.py
