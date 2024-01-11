#!/usr/bin/python3
""" Deletes out-of-date archives """
from fabric.api import *


env.hosts = ["54.160.88.197", "52.91.178.63"]
env.user = "ubuntu"


def do_clean(number=0):
    """ Clean out out-dated archives """

    number = int(number)

    if number == 0:
        number = 2
    else:
        number += 1

    local('cd versions ; ls -t | tail -n +{} | xargs rm -rf'.format(number))
    path = '/data/web_static/releases'
    run('cd {} ; ls -t | tail -n +{} | xargs rm -rf'.format(path, number))
