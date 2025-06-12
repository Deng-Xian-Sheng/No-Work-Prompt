## optimize.py

optimize.py 是一个精心设计的工具，它借助 docs 文件夹下的文档，对你的提示词进行优化。

你需要确保执行脚本时，当前目录下存在 docs 文件夹，并且你需要修改 optimize.py 添加你的提示词和优化目标之后才可以运行。

### 快速开始

1. 克隆仓库&创建venv&安装依赖

```bash
git clone https://github.com/Deng-Xian-Sheng/No-Work-Prompt.git && cd No-Work-Prompt/optimize-your-prompt

python3 -m venv venv
source ./venv/activate
pip install openai jinja2
```

2. 编辑 optimize.py 填写你的提示词、优化目标、文档（可选）

例如：
```bash
vim optimize.py
```

3. 运行 optimize.py

```bash
python3 optimize.py
```

## 受益而落地的项目

你可以fork仓库并提交pr，在以下列表中显示你的项目，并链接到 benefit 文件夹中的 xxx.md 上。

在 xxx.md 里面，你可以描述优化提示词的过程，经历的困难，以及如何通过 optimize-your-prompt 工具优化好了你的提示词，最终实现项目落地。

- 这是一个例子[例子](benefit/例子.md)
