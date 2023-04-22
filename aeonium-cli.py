import argparse
import os
import platform
import json
plf = platform.system()
def setup(venv,hl):
    if plf == "Windows":
        os.system(f'powershell.exe -Command "& Import-Module "setup.ps1";Set-AeoniumUp({venv},{hl})" ' )

    else:
        os.system(f'setup.sh {venv} {hl}')
    venvdata = {'venv_name':venv}
    json.dump(obj=venvdata,fp=open('data.json','w'))

def sever(port='8000'):
    data = json.load(open('data.json','r'))
    if plf == 'Windows':
        os.system(f'{data["venv_name"]}\\Scripts\\activate & python manage.py runserver {port}')
    else:
        os.system(f'source {data["venv_name"]}/bin/activate & python manage.py runserver {port}')

def main():
    parser = argparse.ArgumentParser()
    group = parser.add_mutually_exclusive_group()

    group.add_argument('setup',nargs=2,dest='arg',required=False)
    group.add_argument('server',nargs=1,dest='port_id',required=False)

    args = parser.parse_args()

    if args.arg:
        setup(args.arg[0],args.arg[1])
    elif args.port_id == []:
        sever()
    elif args.port_id:
        sever(args.port_id)

if __name__ == '__main__':
    main()


