import os
import zipfile

files = os.listdir()

container = None
for file in files:
    if 'container.zip.' in file:
        with open(file, 'rb') as f:
            if container is None:
                container = f.read()
            else:
                container += f.read()

with open('container.zip', 'wb') as f:
    f.write(container)

with zipfile.ZipFile('container.zip', 'r') as container:
    container.extractall('')

os.remove('container.zip')