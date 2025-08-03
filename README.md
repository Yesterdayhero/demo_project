# NetEaseMusicVIPDecoder

批量转换网易云音乐下载的 `.ncm` 格式文件为常见的音频格式（如 MP3），适合自用备份与本地播放。

---

## 安装与使用说明

本项目基于开源工具 [`ncmdump`](https://github.com/nondanee/ncmdump) 实现网易云音乐 `.ncm` 格式的会员加密音乐文件解码。

### 📦 安装 ncmdump 工具（推荐使用 pip）

你需要先安装 [Python](https://www.python.org/downloads/) 和 `ncmdump` 工具：

在cmd控制台或者python终端输入指令： pip install ncmdump
（如果还未安装pip，请自行查阅资料安装）

## 🚀使用方法

1. 修改 decoder.py 中的路径为你本地 .ncm 文件夹路径
2. 打开终端（或 Git Bash、cmd,）。

3. 进入你的项目文件夹，例如：cd D:\MyGitProjects\demo_project

4. 运行解码脚本，输入指令：python ncm_decoder.py
转换后的文件将保存在桌面

## 📁文件结构
demo_project/
├── README.md
├── ncm_decoder.py
├── .gitignore


## ❓常见问题

1. 找不到 ncmdump 命令？
确保你已用 pip install ncmdump 安装。
确保 Python 和 Scripts 路径已加入系统 PATH。

2. 脚本没有反应？
检查 .ncm 文件目录是否正确

# ⚠️声明：
仅供技术交流使用，请勿用于商业用途或非法传播



