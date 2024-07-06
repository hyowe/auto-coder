<p align="center">
  <picture>    
    <img alt="auto-coder" src="./logo/auto-coder.jpeg" width=55%>
  </picture>
</p>

<h3 align="center">
Auto-Coder (powered by Byzer-LLM)
</h3>

<p align="center">
| <a href="./docs/en"><b>English</b></a> | <a href="./docs/zh"><b>中文</b></a> |

</p>

---

*Latest News* 🔥
- [2024/07] Release Auto-Coder 0.1.115
- [2024/06] Release Auto-Coder 0.1.82
- [2024/05] Release Auto-Coder 0.1.73
- [2024/04] Release Auto-Coder 0.1.46
- [2024/03] Release Auto-Coder 0.1.25
- [2024/03] Release Auto-Coder 0.1.24

---

Auto-Coder is a command-line tool with YAML-based configuration that can automatically develop your existing project based on your requirements. 

The programming experience with an auto-coder is similar to upgrading from a carriage driver to a car driver. You need to be patient and learn to use the auto-coder as a professional skill and tool. It usually takes weeks or even months and requires changing many of your driving habits to truly achieve a significant (may 3-5) productivity improvement.

The new way of your development is: 

1. to write a YAML file to describe your requirements, and the auto-coder will generate the code 
and merge the code into your project.
2. check the commits from the auto-coder and review the code in vscode or other IDEs.
3. if the commits are correct, you may still need to manually modify the code if necessary with the help of github copilot or other tools.
4. if the commits are incorrect, you need to revert the commits and modify the YAML file to make the auto-coder generate the correct code.
5. repeat the above steps until you are satisfied with the code generated by the auto-coder.

Many products can improve programming efficiency, but their impact is relatively limited, with improvements not exceeding 30%. This is because they merely assist programmers in writing code faster, without altering the fundamental workflow or job structure.

The impact of Auto-Coder goes far beyond this scope. It is not just a code generation tool; by integrating and automating code generation in a novel way, it could fundamentally change the nature of engineers' work and their collaboration methods. 

For example, the responsibilities of engineers at different levels—from junior to senior—will undergo a transformation. Senior engineers might be responsible for generating code using Auto-Coder, while junior engineers would focus on verification. The content and proportion of development and testing work will also see significant changes (we will need more testing), and even the collaboration model between front-end and back-end will differ.

This change is akin to the impact of the Industrial Revolution on social structure and daily life. Auto-Coder will inevitably significantly alter the interfaces and daily aspects of development, freeing up more human resources through extreme efficiency improvements to explore new areas and create new professions within the industry.


## Installation

```shell
conda create --name autocoder python=3.10.11
conda activate autocoder
pip install -U auto-coder
## if you want to use private/open-source models, uncomment this line.
# pip install -U vllm
ray start --head
```

## Tutorial

1. [Setup auto-coder](./docs/en/000-AutoCoder_Prepare_Journey.md)
2. [AutoCoder_准备旅程](./docs/zh/000-AutoCoder_准备旅程.md)


## Example Project

https://github.com/allwefantasy/auto-coder.example

