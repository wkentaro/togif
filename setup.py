from __future__ import print_function

from setuptools import setup
import shlex
import subprocess


def git_hash():
    cmd = 'git log -1 --format="%h"'
    try:
        hash_ = subprocess.check_output(shlex.split(cmd)).decode().strip()
    except subprocess.CalledProcessError:
        hash_ = None
    return hash_


version = '0.1.0.post0'

hash_ = git_hash()
if hash_ is not None:
    version = '%s.%s' % (version, hash_)


setup(
    name='togif',
    version=version,
    py_modules=['togif'],
    install_requires=['imageio', 'imageio-ffmpeg', 'imgviz', 'tqdm'],
    author='Kentaro Wada',
    author_email='www.kentaro.wada@gmail.com',
    url='http://github.com/wkentaro/togif',
    entry_points={
        'console_scripts': ['togif=togif:main']
    },
)
