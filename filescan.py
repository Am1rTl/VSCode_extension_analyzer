import os
import subprocess

users = os.listdir("/home/")
paths = []

for i in users:
    try:
        os.listdir("/home/"+i+"/.vscode")
        paths.append("/home/"+i+"/.vscode/extensions")
    except:
        continue

print(paths)

extensions = {}
for i in paths:
    extensions[i] = os.listdir(i)

for i in extensions.keys():
    extensions[i].pop(extensions[i].index("extensions.json"))
    extensions[i].pop(extensions[i].index(".obsolete"))

print(extensions) 


temp_dir = subprocess.check_output(['mktemp', '-d']).decode('utf-8').strip()
for i in users:
    for j in extensions[f"/home/{i}/.vscode/extensions"]:
        os.makedirs(os.path.join(temp_dir, i, j), exist_ok=True)
        ext_files = subprocess.run(['find', '/home/user/.vscode/extensions/j', '-type', 'f'])for i in extensions.keys():


print(temp_dir)