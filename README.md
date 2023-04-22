# Aeonium
![](https://img.shields.io/badge/Python_3.11-blue?style=for-the-badge&logo=python&logoColor=white)   ![](https://img.shields.io/badge/powered_by_django-darkgreen?style=for-the-badge&logo=django&logoColor=white)
![](https://img.shields.io/badge/markdown_supported-black?style=for-the-badge&logo=markdown&logoColor=white)

## 什么是Aeonium
Aeonium是一个极简的博客系统，基于Django。
* 支持Markdown
* 在线编辑器
* 易于配置——甚至可以轻松地自己修改源代码
* 在线编辑静态页面
* 支持Gitalk

## 快速开始
环境：Python 3.11（或其他Django4支持的版本）
    **警告：Aeonium CLI暂时无法正常使用**
```sh
python aeonium-cli.py setup [虚拟环境名称] [语法高亮主题]
```
## 启动服务器
```sh
python aeonium-cli.py sever [port]
```
## 编辑
进入站点的/admin页面

## 配置
打开[config.yml](config.yml)进行配置
在[detail.html](themes/origin/templates/detail.html)和[pages.html](themes/origin/templates/pages.html)进行Gitalk配置
## TODO LIST
* 支持LaTeX


