from __future__ import print_function

from setuptools import setup
import shlex
import subprocess
import sys


version = '1.0.1'


# release helper
if sys.argv[-1] == 'release':
    commands = [
        'git pull origin master',
        'git tag v{0}'.format(version),
        'git push origin master --tags',
        'python setup.py sdist',
        'twine upload dist/togif-{0}.tar.gz'.format(version),
    ]
    for cmd in commands:
        print('+ {0}'.format(cmd))
        subprocess.check_call(shlex.split(cmd))
    sys.exit(0)


def get_long_description():
    with open('README.md') as f:
        long_description = f.read()

    try:
        import github2pypi

        return github2pypi.replace_url(
            slug='wkentaro/togif', content=long_description
        )
    except Exception:
        return long_description


setup(
    name='togif',
    version=version,
    py_modules=['togif'],
    long_description=get_long_description(),
    long_description_content_type='text/markdown',
    install_requires=['imageio<2.5', 'imageio-ffmpeg', 'imgviz', 'tqdm'],
    author='Kentaro Wada',
    author_email='www.kentaro.wada@gmail.com',
    url='http://github.com/wkentaro/togif',
    entry_points={
        'console_scripts': ['togif=togif:main']
    },
)
