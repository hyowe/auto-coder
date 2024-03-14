
<p align="center">
  <picture>    
    <img alt="auto-coder" src="https://github.com/allwefantasy/byzer-llm/blob/master/docs/source/assets/logos/logo.jpg" width=55%>
  </picture>
</p>

<h3 align="center">
Auto-Coder (powered by Byzer-LLM)
</h3>

<p align="center">
| <a href="./README.md"><b>English</b></a> | <a href="./README-CN.md"><b>中文</b></a> |

</p>

---

*Latest News* 🔥

- [2024/03] Release Auto-Coder 0.1.4

---



🚀 Attention developers! 🚨 The game-changing Auto-Coder has arrived, and it's about to take your AI programming to a whole new level! 🌟

Fueled by the incredible power of Byzer-LLM, this command-line tool is packed with features that will blow your mind:

📂 Say goodbye to manual context gathering! Auto-Coder intelligently generates code based on the context of your source directory. It's like having a genius assistant that knows exactly what you need!

💡 Two modes, endless possibilities! Generate perfect prompts to paste into web-based large models, or let Auto-Coder work its magic directly with private models via Byzer-LLM. The choice is yours, and the results are always spectacular!

💻 Python? TypeScript? No problem! Auto-Coder supports all the cool kids on the programming block.

🌍 Going global is a breeze! Auto-Coder automatically translates your project files, so your code can conquer the world!

🤖 Copilot mode is here, and it's your new best friend! With its built-in shell/Jupyter engine, Auto-Coder breaks down tasks, sets up environments, creates projects, and even modifies code for you. It's like having a super-smart sidekick that never sleeps!

🧑‍💻 Developers, prepare to have your minds blown! Auto-Coder integrates seamlessly with the hottest AI models like ChatGPT, turbocharging your development process to lightning speeds! 🚀

🌟 Don't wait another second! Experience the raw power of Auto-Coder today and let AI be your ultimate coding companion! https://github.com/allwefantasy/auto-coder 🔥

#AutoCoder #AIProgramming #GameChanger #ByzerLLM #DevTools

## Table of Contents

- [Brand new Installation](#brand-new-installation)
- [Existing Installation](#existing-installation)
- [Usage](#usage)
  - [Basic](#basic)
  - [Advanced](#advanced)
  - [Python Project Only Features](#python-project-only-features)
  - [TypeScript Project](#typescript-project)
  - [Real-Auto](#real-auto)




## Brand new Installation

You can use the script provided by Byzer-LLM to setup the nvidia-driver/cuda environment:

1. [CentOS 8 / Ubuntu 20.04 / Ubuntu 22.04](https://docs.byzer.org/#/byzer-lang/zh-cn/byzer-llm/deploy)

After the nvidia-driver/cuda environment is set up, you can install auto_coder like this:

```shell
pip install -U auto-coder
```

## Existing Installation


```shell
# or https://gitcode.com/allwefantasy11/auto-coder.git
git clone https://github.com/allwefantasy/auto-coder.git
pip install -r requirements.txt
## if you want to use private/open-source models, uncomment this line.
# pip install -U vllm
pip install -U byzerllm
pip install -U auto-coder
```

## Usage 

### Basic 
> Recommend to use 千义通问Max/Qwen-Max-longcontext SaaS model
> You should deploy the model by [Byzer-LLM](https://github.com/allwefantasy/byzer-llm)


The auto-coder provide two ways:

1. Generate context for the query and used in Web of ChatGPT or other AI models.
2. Use the model from Byzer-LLM to generate the result directly.

>> Note: You should make sure the model has a long context length support, e.g. >32k. 

The auto-coder will collect the source code from the source directory, and then generate context into the target file based on the query.

Then you can copy the content of `output.txt` and paste it to Web of ChatGPT or other AI models:

For example:

```shell
auto-coder --source_dir /home/winubuntu/projects/ByzerRawCopilot --target_file /home/winubuntu/projects/ByzerRawCopilot/output.txt --query "如何让这个系统可以通过 auto-coder 命令执行？" 
```

You can also put all arguments into a yaml file:


```yaml
# /home/winubuntu/projects/ByzerRawCopilot/auto-coder.yaml
source_dir: /home/winubuntu/projects/ByzerRawCopilot
target_file: /home/winubuntu/projects/ByzerRawCopilot/output.txt
query: |
  如何让这个系统可以通过 auto-coder 命令执行？
```
  
Then use the following command:

```shell
auto-coder --file /home/winubuntu/projects/ByzerRawCopilot/auto-coder.yaml
``` 

If you want to use the model from Byzer-LLM, you can use the following command:

```shell
auto-coder --source_dir /home/winubuntu/projects/ByzerRawCopilot --target_file /home/winubuntu/projects/ByzerRawCopilot/output.txt --model qianwen_chat --execute --query "重新生成一个 is_likely_useful_file 方法，满足reactjs+typescript 组合的项目。" 
```

In the above command, we provide a model and enable the execute mode, the auto-coder will collect the source code from the source directory, and then generate context for the query, and then use the model to generate the result, then put the result into the target file.

### Advanced

> This feature only works with the model from Byzer-LLM.

Translate the markdown file in the project:

```shell

auto-coder --source_dir /home/winubuntu/projects/ByzerRawCopilot --target_file /home/winubuntu/projects/ByzerRawCopilot/output.txt --project_type "translate/中文/.md/cn" --model_max_length 2000 --model qianwen_chat 
```
When you want to translate some files, you must specify the model parameter. And the project_type is a litle bit complex, it's a combination of the following parameters:

- translate: the project type
- 中文: the target language you want to translate to
- .md: the file extension you want to translate
- cn: the new file suffix created with the translated content. for example, if the original file is README.md, the new file will be README-cn.md

So the final project_type is "translate/中文/.md/cn"

If your model is powerful enough, you can use the following command to do the same task:

```shell
auto-coder --source_dir /home/winubuntu/projects/ByzerRawCopilot --target_file /home/winubuntu/projects/ByzerRawCopilot/output.txt --model qianwen_chat --project_type translate --model_max_length 2000 --query "把项目中的markdown文档翻译成中文"
```

The model will extract "translate/中文/.md/cn" from the query and then do the same thing as the previous command.

Note: The model_max_length is used to control the model's generation length, if the model_max_length is not set, the default value is 1024.
You should change the value based on your esitmating on the length of the translation.


### Python Project Only Features

In order to reduce the context length collected by the auto-coder, if you are dealing with a python project, you can use the following command:


```shell
auto-coder --target_file /home/winubuntu/projects/ByzerRawCopilot/output.txt --script_path /home/winubuntu/projects/ByzerRawCopilot/xxx --package_name byzer_copilot --project_type py-script --query "帮我实现script模块中还没有实现方法"

```

In the above command, we provide a script path and a package name, the script_path is the python file you are working on now, and the package_name 
is you cares about, then the auto-coder only collect the context from the package_name and imported by the script_path file, this will significantly reduce the context length.

When you refer `script module` in `--query`, you means you are talking about script_path file.

After the job is done, you can copy the prompt from the output.txt and paste it to Web of ChatGPT or other AI models.

If you specify the model, the auto-coder will use the model to generate the result, then put the result into the target file.

```shell
auto-coder --target_file /home/winubuntu/projects/ByzerRawCopilot/output.txt --script_path /home/winubuntu/projects/YOUR_PROJECT/xxx.py --package_name xxxx --project_type py-script --model qianwen_chat --execute --query "帮我实现script模块中还没有实现方法" 
```

## TypeScript Project

Just try to set the project_type to ts-script.

## Real-Auto


Here is a example:

```shell
auto-coder --source_dir /home/winubuntu/projects/ByzerRawCopilot --target_file /home/winubuntu/projects/ByzerRawCopilot/output.txt --project_type copilot --model_max_length 2000 --model qianwen_chat  --query "帮我创建一个名字叫t-copilot 的python项目，生成的目录需要符合包装的python项目结构"

```

This project type will automatically create a python project based on the query, and then generate the result based on the query. 

You can check all log in the `output.txt` file.

auto-coder also support python code interpreter,try this:
  
```shell 
auto-coder --source_dir /home/winubuntu/projects/ByzerRawCopilot --target_file /home/winubuntu/projects/ByzerRawCopilot/output.txt --project_type copilot --model_max_length 2000 --model qianwen_chat  --query "用python打印你好，中国" 
```

The content of the output.txt will be:

```text
=================CONVERSATION==================

user: 
根据用户的问题，对问题进行拆解，然后生成执行步骤。

环境信息如下:
操作系统: linux 5.15.0-48-generic  
Python版本: 3.10.11
Conda环境: byzerllm-dev 
支持Bash

用户的问题是：用python打印你好，中国

每次生成一个执行步骤，然后询问我是否继续，当我回复继续，继续生成下一个执行步骤。

assistant: 
{
  "code": "print('你好，中国')",
  "lang": "python",
  "total_steps": 1,
  "cwd": "",
  "env": {},
  "timeout": -1,
  "ignore_error": false
}

是否继续？
user: 继续
=================RESULT==================

Python Code:
print('你好，中国')
Output:
你好，中国
--------------------
```

You ask the auto-coder to modify a python file:

```shell
auto-coder --source_dir /home/winubuntu/projects/ByzerRawCopilot --target_file /home/winubuntu/projects/ByzerRawCopilot/output.txt --project_type copilot/.py --model_max_length 2000 --model qianwen_chat  --query "优化 copilot 里的get_suffix_from_project_type 函数并更新原文件"
``` 

