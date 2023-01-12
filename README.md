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

创建虚拟环境
```shell
git clone https://github.com/budawu/Aeonium.git #获取
python -m venv ll_env #创建一个叫做ll_env的虚拟环境
```
**注意：激活虚拟环境的方式，不同操作系统方法不同。**

在Linux/MacOS:
```shell
source /ll_env/bin/activate
```
在Windows:
```powershell
.\ll_env\Scripts\activate
```
**激活后提示符应该有(ll_env)**
在虚拟环境下执行以下指令：
```shell
pip install -r requirements.txt #下载依赖的包
cd static/hlcss
pygmentize -S monokai -f html -a .codehilite > monokai.css #语法高亮的css
cd ..
cd ..
python manage.py makemigrations aeonium
python manage.py migrate
python manage.py createsuperuser
```
启动服务器：
```
python manage.py runserver
```
## 编辑
进入站点的/admin页面

## TODO LIST
* 支持LaTeX
* 支持评论
* 多种主题
