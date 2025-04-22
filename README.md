# PyWinGUIBuilder

![Python](https://img.shields.io/badge/Python-3.10+-blue) ![PySimpleGUI](https://img.shields.io/badge/PySimpleGUI-4.60.5+-red) ![pyinstaller](https://img.shields.io/badge/pyinstaller-5.13.0+-pink) ![HM NIS Edit](https://img.shields.io/badge/HM_NIS_Edit-2.0.3+-green) ![License](https://img.shields.io/badge/License-MIT-yellow) ![Stars](https://img.shields.io/github/stars/iniwap/PyWinGUIBuilder?label=收藏)

**中文**：  
一个基于 **Python** 和 **PySimpleGUI** 的开源工具，快速打造 Windows GUI 软件（EXE），一键生成安装程序，让开发者专注于 UI 设计和业务逻辑。

还在为自己开发了个Python项目，面向的用户不是技术不懂Python，没有各种库的运行环境而烦恼？本工具可以一键打包成安装软件，彻底解决此类痛点。  

**English**:  
An open-source tool based on **Python** and **PySimpleGUI**, enabling rapid development of Windows GUI software (EXE) with one-click installer generation, allowing developers to focus on UI design and business logic.  

## 项目简介 / Project Introduction

**中文**：  
**PyWinGUIBuilder** 是一个简单强大的工具，帮助开发者快速创建 Windows GUI 应用程序。基于 **PySimpleGUI** 提供直观的 UI 框架，集成一键生成 EXE 和安装程序的功能，适合初学者和快速原型开发。  
🌟**欢迎 Fork 和 Star！** 适合 Python 开发者、Windows 软件开发者和 PySimpleGUI 爱好者。

**English**:  
**PyWinGUIBuilder** is a simple yet powerful tool that helps developers quickly create Windows GUI applications. Built on **PySimpleGUI** for an intuitive UI framework, it integrates one-click EXE and installer generation, ideal for beginners and rapid prototyping.  
🌟**Welcome to Fork and Star!** Perfect for Python developers, Windows app creators, and PySimpleGUI enthusiasts.

![界面预览 / Interface Preview](image/demo.png)

## 目录 / Table of Contents

- [功能特性 / Features](#功能特性--features)  
- [快速开始 / Quick Start](#快速开始--quick-start)  
- [使用方法 / Usage](#使用方法--usage)  
- [常见问题 / FAQ](#常见问题--faq)  
- [许可证 / License](#许可证--license)

## 功能特性 / Features

**中文**：  
- **基础 UI 模板**：提供 PySimpleGUI 实现的简单 UI 框架，易于扩展。  
- **一键生成 EXE**：集成 PyInstaller，自动打包 Python 代码为 Windows EXE 文件。  
- **安装程序生成**：支持生成标准 Windows 安装程序（Setup.exe）。  
- **跨平台开发**：在 Windows 系统上运行，支持 Python 3.10+。  
- **高度可定制**：用户可自由修改 UI 布局和业务逻辑。

**English**:  
- **Basic UI Template**: Provides a simple UI framework built with PySimpleGUI, easy to extend.  
- **One-Click EXE Generation**: Integrates PyInstaller to automatically package Python code into a Windows EXE file.  
- **Installer Creation**: Supports generating standard Windows installers (Setup.exe).  
- **Cross-Platform Development**: Runs on Windows systems, supports Python 3.10+.  
- **Highly Customizable**: Users can freely modify UI layouts and business logic.

## 快速开始 / Quick Start

### 环境要求 / Requirements

**中文**：  
- HM NIS Edit 2.0.3 或更高版本  
- Python 3.10 或更高版本  
- PyInstaller 5.13.0  
- Windows 10/11  
- 推荐使用虚拟环境

**English**:  
- HM NIS Edit 2.0.3 or higher  
- Python 3.10 or higher  
- PyInstaller 5.13.0  
- Windows 10/11  
- Virtual environment recommended

### 安装步骤 / Installation Steps

**中文 / English**：  
1. 克隆仓库 / Clone：  
   ```bash  
   git clone https://github.com/iniwap/PyWinGUIBuilder
   ```
2. 安装依赖 / Install dependencies：
   ```bash
   pip install --upgrade pyinstaller
   pip install PySimpleGUI-4.60.5-py3-none-any.whl
   pip install -r requirements.txt
   ```
3. 运行示例 / Run example：
   ```bash
   cd PyWinGUIBuilder
   python .\main.py -d
   ```
4. 修改代码 / Modify Code：
   本项目只提供最基本的 UI 及逻辑演示，修改 `MainGUI.py` 体验，后续扩展请根据自身需求，分离 UI、业务逻辑（⚠️代码使用到的库均需在main.py导入）。
   
   This project provides only a basic UI and logic demo. Modify `MainGUI.py` to explore, and extend further based on your needs by separating UI and business logic（⚠️All libraries used in the code need to be imported in main.py）.

## 使用方法 / Usage

### 制作安装程序（EXE） / Create Installer (EXE)

**中文**：  
- 修改 `tools\make_exe\make_exe.bat` 中的 `HM NIS Edit` 为你实际安装的路径。  
- 双击 `make_exe.bat`，即可自动生成 `GUI_Setup.exe` 在当前目录下。

**English**:  
- Modify the `HM NIS Edit` path in `tools\make_exe\make_exe.bat` to your actual installation path.  
- Double-click `make_exe.bat` to automatically generate `GUI_Setup.exe` in the current directory.

### 个性化定制 / Customization

**中文**：  
- 双击 `gui.nsi`，使用 `HM NIS Edit` 打开，可修改软件名、版本号、发行商、网址等。  
- 可修改 `make_exe.bat` 中的加密密码、添加更多数据文件。  
- 自定义图标，修改 `scripts\UI` 目录下的 `icon.ico` 即可，其他资源文件同理。

**English**:  
- Double-click `gui.nsi` to open it with `HM NIS Edit`, where you can modify the software name, version number, publisher, website, etc.  
- You can modify the encryption password in `make_exe.bat` or add more data files.  
- Customize the icon by replacing `icon.ico` in the `scripts\UI` directory; other resource files can be handled similarly.

## 常见问题 / FAQ

**中文**：  
**Q**：生成的 EXE 运行报错怎么办？  
**A**：检查出错原因并分析（多是资源问题），尝试重新打包安装、运行。  
**Q**：支持 macOS 或 Linux 吗？  
**A**：当前仅支持 Windows，未来可能扩展。

**English**:  
**Q**: What should I do if the generated EXE fails to run?  
**A**: Check the error cause (often resource-related) and try repackaging, installing, or running again.  
**Q**: Does it support macOS or Linux?  
**A**: Currently supports only Windows; future expansions may be considered.

## 许可证 / License

本项目采用 [MIT License](https://opensource.org/licenses/MIT) 许可证，允许商业用途，但需遵守以下附加条款：  
This project is licensed under the [MIT License](https://opensource.org/licenses/MIT), allowing commercial use, but subject to the following additional terms:

### Additional Terms / 附加条款:

English:
- Commercial use requires explicit authorization from the author. If you intend to use this project for commercial purposes, please contact the author iniwap.
  - Contact: Email [iniwaper@gmail.com] or GitHub [https://github.com/iniwap].
- You must not remove or modify the attribution, contact information, or GitHub link provided in this project, including but not limited to the author information in the README and LICENSE files.
- Any unauthorized commercial use or removal of attribution and contact information without the author's written consent will be considered a violation of this license.

中文：
- 商业用途需获得作者的明确授权。如需将本项目用于商业目的，请联系作者 iniwap。
  - 联系方式：邮箱[iniwaper@gmail.com] 或 GitHub[https://github.com/iniwap]。
- 不得移除或修改本项目中的署名、联系方式及 GitHub 链接信息，包括但不限于 README 和 LICENSE 文件中的作者信息。
- 未经作者同意，任何未经授权的商业用途或移除署名及联系信息的举动均视为违反本许可证。

详情请查看 LICENSE 文件。
