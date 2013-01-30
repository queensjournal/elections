from fabric.api import run, env, cd

env.dir = '~/election'

def update():
    with cd(env.dir):
        run('git pull origin master')

