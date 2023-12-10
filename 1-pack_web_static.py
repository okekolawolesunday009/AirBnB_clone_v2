#!/usr/bin/ python3
""" using fabric 101
"""
from datetime import datetime
from fabric.api import local
from os.path import isdir


def do_pack():
    """generates a tgz achive"""
    try:
        date = datetime.now().strftime("%Y%m%d%H%M%S")
        if isdir("version") is False:
            local("mkdir versions")
        file_name = "versions/web_static_{}.tgz".format(date)
        local("tar -cvzf {} web_static".format(file_name))
        return file_name
    except:
        return None
