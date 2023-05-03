#!usr/bin/env bash
python -m venv ll_env
source ll_env/bin/activate
pip install -r requirements.txt #下载依赖的包

pygmentize -S monokai -f html -a .codehilite > themes/highlight/highlight.css #语法高亮的css

python cli/secret_key.py
python manage.py makemigrations aeonium
python manage.py migrate
python manage.py createsuperuser
