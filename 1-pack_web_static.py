#!/usr/bin/python3
"""Fabric script that generates a .tgz archive"""
from fabric import task
from invoke import run
from datetime import datetime
from os.path import isdir


@task
def do_pack(ctx):
    """Generates a .tgz archive from web_static
        Args:
            ctx:...
    """
    try:
        date = datetime.now().strftime("%Y%m%d%H%M%S")
        if isdir("versions") is False:
            run("mkdir -p versions")
        file_name = "versions/web_static_{}.tgz".format(date)
        run("tar -cvzf {} web_static".format(file_name))
        return file_name
    except Exception as e:
        return None
