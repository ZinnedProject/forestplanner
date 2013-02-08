from fabric.api import *

dev_server = 'vagrant@127.0.0.1:2222'
prod_server = []

vars = {
    'app_dir': '/usr/local/apps/land_owner_tools/lot',
    'venv': '/usr/local/venv/lot'
}


env.forward_agent = True
env.key_filename = '~/.vagrant.d/insecure_private_key'


def dev():
    """ Use development server settings """
    env.hosts = [dev_server]


def prod():
    """ Use production server settings """
    env.hosts = [prod_server]


def all():
    """ Use all servers """
    env.hosts = [dev_server, prod_server]


def install_requirements():
    run('cd %(app_dir)s && %(venv)s/bin/pip install -r ../requirements.txt' % vars())


def install_django():
    run('cd %(app_dir)s && %(venv)s/bin/python manage.py syncdb && %(venv)s/bin/python manage.py migrate && %(venv)s/bin/python manage.py install_media' % vars())
    run('cd %(app_dir)s && %(venv)s/bin/python manage.py enable_sharing --all' % vars())
    run('cd %(app_dir)s && %(venv)s/bin/python manage.py install_cleangeometry' % vars())


def install_media():
    run('cd %(app_dir)s && %(venv)s/bin/python manage.py install_media' % vars())


def run_server():
    run('cd %(app_dir)s && %(venv)s/bin/python manage.py runserver 0.0.0.0:8000' % vars())


# def update():
#     run('cd %(app_dir)s && git fetch && git merge origin/master' % vars())
