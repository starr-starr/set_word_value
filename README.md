# 前情概要
- 如果你是一个`懒人`，并且你读的是`计算机相关专业`，那一定有很多实验报告，即使是嫖同伴的，每次也得点进去修改基础信息，非常的不友好
- 因为周围同学写的实验报告都是 .doc，因此未区分 .doc 和 .docx，即要求转换的文件必须为 .doc 后缀
- 因为大多数实验报告都是第二行为个人信息，因此这块替换后的个人信息就在第二行，如果格式不同可以自己魔改一下
# 项目信息
- python 版本 3.11 
# 使用方式
> 为了使每个项目有每个项目的包管理因此这里使用虚拟环境（venv），不过似乎早已被废弃？？！<br>
> 事先声明，本地需有 python 环境
- clone 项目到本地，在当前目录打开终端
- python -m venv venv 创建虚拟环境：
- .\venv\Scripts\activate 激活虚拟环境
- pip install -r requirements.txt 安装所有依赖
- 手动配置 config 目录下的 config.json 文件来自定义个人信息( Json 文件中的空格为不同项之间的间距，可自己调整)
- 运行 `python main.py` 后输入嫖来的实验报告的存放路径
- 静待文件存放目录下同名的 .docx 后缀的文件产出即可
# 注意事项
- 该脚本会将该目录下的所有 .doc 文件进行转换
- 输入文件路径直接从文件资源管理器顶部复制即可(如 C:\Users\xxx\Desktop)<br> 
# [同文](https://juejin.cn/post/7347165355585847333)
