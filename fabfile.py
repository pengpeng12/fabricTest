from fabric.api import run

def host_type():
    run('uname -s')

def date_test():
    run('date')

def pwd_test():
    run('pwd')

