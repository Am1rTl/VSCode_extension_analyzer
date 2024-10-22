import hashlib
import os
import vt
import time

analyzers = ["https://www.virustotal.com/gui/home/upload","https://opentip.kaspersky.com/","https://www.filescan.io/scan","https://virusscan.jotti.org/","https://manalyzer.org/"]




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

#print('\n'.join(str(i) for i in analyzers))

print("The paths is:",extensions)
for i in extensions.keys():
    for name in extensions[i]:
        print(f"zip -r '{name}.zip' '{i+"/"+name}'")
        os.system(f"zip -r '{name}.zip' '{i+"/"+name}'")

os.system("zip -r all.zip *.zip")

asd = """import requests

url = "https://www.virustotal.com/api/v3/files"


# files = { "file": ("flag", open("/home/amir/.vscode/extensions/blackboxapp.blackbox-1.4.15/out/extension.js", "rb"), "application/octet-stream") }
files = { "file": ("flag", open("all.zip", "rb"), "application/octet-stream") }

headers = {
    "accept": "application/json",
    "x-apikey": "a4e48932eb137e5cdae5919ddd48da57346469abec023330b249069c8de73567"
}

print("Start upload files")

response = requests.post(url, files=files, headers=headers)

print(response.text)

#data = {
#    "data": {
#        "type": "analysis",
#        "id": "ZDVlYzg5Y2Y0ODRhMWZjNWZiOWY3ODBmYTkwNjNkMWU6MTcyNzQzNDAyMw==",
#        "links": {
#            "self": "https://www.virustotal.com/api/v3/analyses/ZDVlYzg5Y2Y0ODRhMWZjNWZiOWY3ODBmYTkwNjNkMWU6MTcyNzQzNDAyMw=="
#        }
#    }
#}
data = eval(response.text)

url = data["data"]["links"]['self']
print(url)

print("Sleep some time for getting response")

time.sleep(180)

headers = {
    "accept": "application/json",
    "x-apikey": "a4e48932eb137e5cdae5919ddd48da57346469abec023330b249069c8de73567"
}
response = requests.get(url, headers=headers)
print("RESPONS ANALYSE")
print(response.text)
with open("report", 'w') as f:
    f.write(str(response.text))"""


client = vt.Client("a4e48932eb137e5cdae5919ddd48da57346469abec023330b249069c8de73567")
with open("all.zip", "rb") as f:
    analysis = client.scan_file(f, wait_for_completion=True)

print(analysis)

with open("report", 'w') as f:
    f.write(str(analysis))

with open("all.zip", "rb") as f:
    hash = hashlib.sha1(f.read()).hexdigest()
file = client.get_object(f"/files/{hash}")