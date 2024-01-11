#!/usr/bin/python3
"""Automate the build and deployment process of web_static"""
import time
import os.path
from fabric.api import local
from fabric.operations import env, put, run

env.hosts = ["54.160.88.197", "52.91.178.63"]


def do_pack():
    """Generate an tgz archive from web_static folder"""
    try:
        local("mkdir -p versions")
        local(
            "tar -cvzf versions/web_static_{}.tgz web_static/".format(
                time.strftime("%Y%m%d%H%M%S")
            )
        )
        return "versions/web_static_{}.tgz".format(
                time.strftime("%Y%m%d%H%M%S"))
    except Exception as e:
        return None


def do_deploy(archive_path):
    """Distribute the archived file to the specified web server"""
    try:
        file = archive_path.split("/")[-1]
        folder = "/data/web_static/releases/" + file.split(".")[0]
        put(archive_path, "/tmp/")
        sudo("mkdir -p {}".format(folder))
        sudo("tar -xzf /tmp/{} -C {}".format(file, folder))
        sudo("rm /tmp/{}".format(file))
        sudo("mv {}/web_static/* {}/".format(folder, folder))
        sudo("rm -rf {}/web_static".format(folder))
        sudo("rm -rf /data/web_static/current")
        sudo("ln -s {} /data/web_static/current".format(folder))
        print("Deployment done")
        return True
    except Exception as e:
        return False


def deploy():
    """Create and distributes an archive to web servers"""
    try:
        return do_deploy(do_pack())
    except Exception as e:
        return False
