function Set-AeoniumUp($venv_mane,$highlight_theme) {
    python -m venv $venv_mane
    .\$venv_mane\Scripts\activate
    pip install -r requirements.txt #下载依赖的包

    pygmentize -S $highlight_theme -f html -a .codehilite > themes/highlight/highlight.css #语法高亮的css

    python manage.py makemigrations aeonium
    python manage.py migrate
    python manage.py createsuperuser

}
