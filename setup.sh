#!/bin/sh
python -m venv $1
.\$1\Scripts\activate
pip install -r requirements.txt #下载依赖的包

pygmentize -S $2 -f html -a .codehilite > themes/origin/css/highlight.css #语法高亮的css

python manage.py makemigrations aeonium
python manage.py migrate
python manage.py createsuperuser
