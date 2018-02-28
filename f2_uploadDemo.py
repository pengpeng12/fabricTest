from fabric.api import *
env.user = 'songpengpeng'
env.hosts = ['192.168.220.133', '192.168.220.134']
env.password = '123'

@task
@runs_once
def tar_task():
    with lcd('/home/songpengpeng/tusiji'):
         local('tar zcvf demo.tar.gz demo.py')

@task
def put_task():
    run('mkdir -p /home/songpengpeng/testDemo')
    with cd('/home/songpengpeng/testDemo'):
         put('/home/songpengpeng/testDemo/demo.tar.gz')

@task
def check_task():
    lmd5 = local('md5sum /home/songpengpeng/testDemo/demo.tar.gz', capture=True).split(' ')[0]
    rmd5 = run('md5sum /home/songpengpeng/testDemo/demo.tar.gz').split('')[0]
    if lmd5 == rmd5:
        print('OK !')
    else:
        print('ERROR')

@task
def run_task():
    with cd('/home/songpengpeng/testDemo'):
        run('tar zxvf demo.tar.gz')
        run('python demo.py')

@task
def go():
    tar_task()
    put_task()
    check_task()
    run_task()

