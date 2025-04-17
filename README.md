# PyWinGUIBuilder
![Python](https://img.shields.io/badge/Python-3.10+-blue) ![PySimpleGUI](https://img.shields.io/badge/PySimpleGUI-4.60.5+-red) ![pyinstaller](https://img.shields.io/badge/pyinstaller-5.13.0+-pink) ![HM NIS Edit](https://img.shields.io/badge/HM_NIS_Edit-2.0.3+-green) ![License](https://img.shields.io/badge/License-MIT-yellow) ![Stars](https://img.shields.io/github/stars/iniwap/PyWinGUIBuilder?label=收藏)

一个基于 **Python** 和 **PySimpleGUI** 的开源工具，快速打造 Windows GUI 软件（EXE），一键生成安装程序，让开发者专注于 UI 设计和业务逻辑。

![界面预览](image/demo.png)

## 项目介绍
**PyWinGUIBuilder** 是一个简单强大的工具，帮助开发者快速创建 Windows GUI 应用程序。基于 **PySimpleGUI** 提供直观的 UI 框架，集成一键生成 EXE 和安装程序的功能，适合初学者和快速原型开发。开发者只需专注于 UI 设计和业务逻辑，即可生成可分发的 Windows 软件。

🌟**欢迎 Fork 和 Star！** 适合 Python 开发者、Windows 软件开发者和 PySimpleGUI 爱好者。

## 功能特性
- **基础 UI 模板**：提供 PySimpleGUI 实现的简单 UI 框架，易于扩展。
- **一键生成 EXE**：集成 PyInstaller，自动打包 Python 代码为 Windows EXE 文件。
- **安装程序生成**：支持生成标准 Windows 安装程序（Setup.exe）。
- **跨平台开发**：在 Windows 系统上运行，支持 Python 3.10+。
- **高度可定制**：用户可自由修改 UI 布局和业务逻辑。

## 快速开始
### 环境要求
- HM NIS Edit 2.0.3 或更高版本
- Python 3.10 或更高版本
- pyinstaller 5.13.0
- Windows 10/11
- 推荐使用虚拟环境

### 安装步骤
1. 克隆仓库：
   ```bash
   git clone https://github.com/iniwap/PyWinGUIBuilder
   ```
2. 安装依赖：
   ```bash
   pip install --upgrade pyinstaller
   
   pip install -r requirements.txt
   ```
3. 运行示例：
   ```bash
   cd PyWinGUIBuilder
   python .\main.py -d
   ```
4. 修改代码
    本项目只提供最基本的UI及逻辑演示，修改`MainGUI.py`体验，后续扩展请根据自身需求，分离UI、业务逻辑。

## 使用方法
### 制作安装程序（EXE）
- 修改`tools\make_exe\make_exe.bat`中的`HM NIS Edit`为你实际安装的路径
- 双击`make_exe.bat`，即可自动生成GUI_Setup.exe在当前目录下
### 个性化定制
- 双击gui.nsi，使用`HM NIS Edit`打开，可修改软件名、版本号、发行商、网址等
- 可修改`make_exe.bat`中的加密密码、添加更多数据文件
- 自定义图标，修改`scripts\UI`目录下的icon.ico即可，其他资源文件同理

## 常见问题

Q：生成的 EXE 运行报错怎么办？
A：检查出错原因并分析（多是资源问题），尝试重新打包安装、运行。

Q：支持 macOS 或 Linux 吗？
A：当前仅支持 Windows，未来可能扩展。

## 许可证

本项目采用 MIT License 许可证，允许商业用途，但需遵守以下附加条款：

Additional Terms / 附加条款:

English:
- Commercial use requires explicit authorization from the author. If you intend to use this project for commercial purposes, please contact the author iniwap.
  - Contact: Email [iniwaper@gmail.com] or GitHub [https://github.com/iniwap].
- You must not remove or modify the attribution, contact information, or GitHub link provided in this project, including but not limited to the author information in the README and LICENSE files.
- Any unauthorized commercial use or removal of attribution and contact information without the author's written consent will be considered a violation of this license.

中文：
- 商业用途需获得作者的明确授权。如需将本项目用于商业目的，请联系作者 iniwap。
  - 联系方式：邮箱 [iniwaper@gmail.com] 或 GitHub [https://github.com/iniwap]。
- 不得移除或修改本项目中的署名、联系方式及 GitHub 链接信息，包括但不限于 README 和 LICENSE 文件中的作者信息。
- 未经作者书面同意，任何未经授权的商业用途或移除署名及联系信息的举动均视为违反本许可证。

详情请查看 LICENSE 文件。
