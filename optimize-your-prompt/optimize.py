import openai
from jinja2 import Template
import os
import random

client = openai.OpenAI(api_key="", base_url="")

# 你当前的提示词（可为空）
current_prompt = """"""

# 你想让模型做什么？你想实现什么样的AI产品？你的需求！/你想要优化的地方
target = """"""

# 你能提供的文档，任何你觉得有助于优化提示词的东西（可为空）
docs = """"""

if current_prompt.strip() == "" and target.strip() == "" and docs.strip() == "":
  print("请编辑我，修改current_prompt、target、docs变量后再次运行。")
  exit(1)

# 读取 docs 文件夹下的 .md 文件
def read_md_files(folder_path='docs'):
    """
    读取指定文件夹及其子文件夹中的所有.md文件
    :param folder_path: 要搜索的文件夹路径，默认为'docs'
    :return: 包含文件路径和内容的字典 {文件路径: 文件内容}
    """
    md_files = {}
    # 遍历文件夹及其子文件夹
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            if file.endswith('.md'):
                file_path = os.path.join(root, file)
                try:
                    with open(file_path, 'r', encoding='utf-8') as f:
                        content = f.read()
                    md_files[file_path] = content
                except Exception as e:
                    print(f"读取文件 {file_path} 时出错: {str(e)}")
    return md_files

md_contents = read_md_files()
for path, content in md_contents.items():
  docs = docs + "\n\n" + content

# OptimizeYouPrompt 的系统提示词
system_prompt = Template("""助手是由 CanQi Jin 创建的 OptimizeYouPrompt。
OptimizeYouPrompt 喜欢优化大型语言模型的提示词。
OptimizeYouPrompt 会根据用户提供的当前提示词和优化目标以及有用的文档，对提示词进行优化。
OptimizeYouPrompt 擅长理解用户的真实需求，在参考文档中最佳实践的情况下创造性的更新提示词，实现用户的目的。
为了更好的优化提示词 OptimizeYouPrompt 将深入分析以下用户提供的信息：

1. 当前的提示词，以XML标签<current_prompt>包裹

<current_prompt>
{{current_prompt}}
</current_prompt>

2. 优化目标，以XML标签<target>包裹

<target>
{{target}}
</target>

3. 包含最佳实践的参考文档，以XML标签<docs>包裹

<docs>
{{docs}}
</docs>

OptimizeYouPrompt 非常有信心解决问题，喜欢多次尝试，善于倾听用户的想法，并通过 **逐步思考** 来检查自己的输出尽可能的确保没有遗漏。
OptimizeYouPrompt 现在将与一个人连接！""")

system_prompt = system_prompt.render(
    current_prompt=current_prompt,
    target=target,
    docs=docs
)

messages = [
  {"role": "system", "content": system_prompt}
]

while True:
  # 接收键盘输入，请求OpenAI API
  new_user_message = input("发送给LLM(你的建议)(输入EOF结束)：")

  if new_user_message.strip() == "EOF":
    break

  messages.append({"role": "user", "content": new_user_message})
  
  response = client.chat.completions.create(
    model="openai-large",
    messages=messages,
    temperature=0.7,
    top_p=0.7,
    stream=True,
    extra_query={"private": True},
    seed=random.randint(1,999999999),
  )
  
  # 打印流式响应
  for chunk in response:
      if chunk.choices and chunk.choices[0].delta.content is not None:
          if messages[len(messages)-1]["role"] != "assistant":
            messages.append({"role": "assistant", "content": chunk.choices[0].delta.content})
          messages[len(messages)-1]["content"] = messages[len(messages)-1]["content"] + chunk.choices[0].delta.content
          print(chunk.choices[0].delta.content, end="", flush=True)
