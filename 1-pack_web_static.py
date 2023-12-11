#!/usr/bin/python3
"""Fabric script that generates a
tgz archive from the contents of the web_static
folder of the AirBnB Clone repo
"""
from datetime import datetime
from fabric import task
from invoke import run
from os.path import isdir


@task
def do_pack(ctx):
    """generates a tgz achive"""
    try:
        date = datetime.now().strftime("%Y%m%d%H%M%S")
        if isdir("versions") is False:
            run("mkdir versions")
        file_name = "versions/web_static_{}.tgz".format(date)
        run("tar -cvzf {} web_static".format(file_name))
        return file_name
    except Exception as e:
        return None
