import hashlib
import vt
from http import client


client = vt.Client("a4e48932eb137e5cdae5919ddd48da57346469abec023330b249069c8de73567")

with open("all.zip", "rb") as f:
    hash = hashlib.sha1(f.read()).hexdigest()
file = client.get_object(f"/files/{hash}")

print(file.size)    
print(file.type_tag)
print(file.last_analysis_stats)