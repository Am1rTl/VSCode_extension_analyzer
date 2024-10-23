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
for user in users:
    for ext_name in extensions[f"/home/{user}/.vscode/extensions"]:
        os.makedirs(os.path.join(temp_dir, user, ext_name), exist_ok=True)
        ext_files = subprocess.run(['find', f'/home/{user}/.vscode/extensions/{ext_name}', '-type', 'f'], capture_output=True, text=True).stdout.splitlines()
        for  file in ext_files:
            rash = file.split('.')[-1:][0]
            print(rash)
            
            try:
                if len(rash) < 5:
                    with open(os.path.join(temp_dir, user, ext_name, "file."+rash), 'a') as f:
                        with open(file, 'rb') as e:
                            f.write(str(e.read())[2:-1]+"\n")
                else:
                    raise  Exception("File name too long")
            except:
                with open(os.path.join(temp_dir, user, ext_name, "file.txt"), 'a') as f:
                    with open(file, 'rb') as e:
                        f.write(str(e.read())[2:-1]+"\n")


print(temp_dir)