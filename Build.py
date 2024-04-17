import os
import shutil
import PyInstaller.__main__

if __name__ == '__main__':
    if not os.path.isfile('container.py'):
        exec(open('MissingContainer.py').read())

    if os.path.isfile('DumbApp.exe'):
        os.remove('DumbApp.exe')

    PyInstaller.__main__.run([
        'DumbApp.py',
        '--onefile',
        '--noconsole',
        '--distpath',
        '.\\'
    ])

    shutil.rmtree('.\\build')
    os.remove('DumbApp.spec')