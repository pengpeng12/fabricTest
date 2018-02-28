from fabric.api import *

env.user =  'songpengpeng'
env.hosts = ['192.168.220.133','192.168.220.134']
env.password = '123'


@runs_once
@task
def local_update():
    with lcd("/home/songpengpeng/tusiji"):
         local("git add -A")
         local("git commit -m 'update'")
         local("git pull origin master")
         local("git push origin master")

@task
def remote_update():
    with cd("/home/songpengpeng/tusiji"):
        run("git add -A")
        run("git pull origin master")

@task
def deploy():
    local_update()
    remote_update()
