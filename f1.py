from fabric.api import *

env.hosts=['192.168.220.132', '192.168.220.133']
env.passwords = {
    'songpengpeng@192.168.220.132:22':'123456',
    'songpengpeng@192.168.220.133:22':'123456',
}

@runs_once
def input_raw():
    return prompt("please input directory name:", default="/home")

def workask(dirname):
    run('ls -l '+ dirname)

@task
def go():
    print('start...')
    getdirname = input_raw()
    workask(getdirname)
    print('end...')

