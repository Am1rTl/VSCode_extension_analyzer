import hashlib
import os
import vt
from http import client

#"""
client = vt.Client("a4e48932eb137e5cdae5919ddd48da57346469abec023330b249069c8de73567")
"""
with open("all.zip", "rb") as f:
    hash = hashlib.sha1(f.read()).hexdigest()
file = client.get_object(f"/files/{hash}")

print(file.size)    
print(file.type_tag)
print(file.last_analysis_stats)

analyze  = file.last_analysis_stats

all_checkers = sum(analyze.values())
print("All checkers: ", all_checkers)
print("Malicious: ", analyze['malicious'])
print("Suspicious: ", analyze['suspicious'])
print("Undetected: ", analyze['undetected'])
print()
"""
zip_hash = {}
analyze = {'malicious': 2}
hash_analyze = {}
if  analyze['malicious'] > 0:
    zips = [zip for zip in os.listdir() if zip.endswith(".zip") and zip != "all.zip"]

    print(zips)

    for zip in zips:
        with open(zip, "rb") as f:
            hash = hashlib.sha1(f.read()).hexdigest()
        zip_hash[zip] = hash

    for i in zip_hash.values():
        hash_analyze[i] = client.get_object(f"/files/{i}").last_analysis_stats

    print(zip_hash)
    print(hash_analyze)


