import hashlib
import os
import vt


def find_name_by_hash(d, value):
    for key, val in d.items():
        if val == value:
            return key
    return None  # Return None if the value is not found


client = vt.Client("a4e48932eb137e5cdae5919ddd48da57346469abec023330b249069c8de73567")

with open("all.zip", "rb") as f:
    hash = hashlib.sha1(f.read()).hexdigest()
file = client.get_object(f"/files/{hash}")


analyze  = file.last_analysis_stats

all_checkers = sum(analyze.values())
print("All checkers: ", all_checkers)
print("Malicious: ", analyze['malicious'])
print("Suspicious: ", analyze['suspicious'])
print("Undetected: ", analyze['undetected'])
print()

#client = vt.Client("a4e48932eb137e5cdae5919ddd48da57346469abec023330b249069c8de73567")


zip_hash = {}

hash_analyze = {}
if  analyze['malicious'] > 0:
    zips = [zip for zip in os.listdir() if zip.endswith(".zip") and zip != "all.zip"]


    for zip in zips:
        with open(zip, "rb") as f:
            hash = hashlib.sha1(f.read()).hexdigest()
        zip_hash[zip] = hash

    for i in zip_hash.values():
        hash_analyze[i] = client.get_object(f"/files/{i}").last_analysis_stats


#zip_hash = {'kiranshah.chatgpt-helper-4.1.0.zip': '3c1a8efea640f52b08f4fb086b799c6f3d523f5b', 'ms-python.vscode-pylance-2024.10.1.zip': 'cfad8a0ca08fbc9b564a92731163925741719b89', 'mustaphakhairanghliss.hawksecv2-0.1.7.zip': '790b168c207b684866bb9fcf719c776e039dc80d', 'blackboxapp.blackbox-1.4.29.zip': 'e635c86d5e961cdfbbb6b01dba93397ce360eec0', 'ms-python.debugpy-2024.12.0-linux-x64.zip': 'e4657646904046ec11a5cd969438e9341d83a563', 'ms-python.python-2024.16.1-linux-x64.zip': '513c472ac48e4444a7f421552252e37f81e284a7', 'NetWorm.zip': '5fe1427e9230be860be004ecaa18f1892fdfed5e'}
#hash_analyze = {'3c1a8efea640f52b08f4fb086b799c6f3d523f5b': {'malicious': 0, 'suspicious': 0, 'undetected': 66, 'harmless': 0, 'timeout': 0, 'confirmed-timeout': 0, 'failure': 0, 'type-unsupported': 11}, 'cfad8a0ca08fbc9b564a92731163925741719b89': {'malicious': 0, 'suspicious': 0, 'undetected': 59, 'harmless': 0, 'timeout': 6, 'confirmed-timeout': 0, 'failure': 1, 'type-unsupported': 10}, '790b168c207b684866bb9fcf719c776e039dc80d': {'malicious': 0, 'suspicious': 0, 'undetected': 66, 'harmless': 0, 'timeout': 0, 'confirmed-timeout': 0, 'failure': 0, 'type-unsupported': 11}, 'e635c86d5e961cdfbbb6b01dba93397ce360eec0': {'malicious': 0, 'suspicious': 0, 'undetected': 54, 'harmless': 0, 'timeout': 12, 'confirmed-timeout': 0, 'failure': 0, 'type-unsupported': 8}, 'e4657646904046ec11a5cd969438e9341d83a563': {'malicious': 0, 'suspicious': 0, 'undetected': 67, 'harmless': 0, 'timeout': 0, 'confirmed-timeout': 0, 'failure': 0, 'type-unsupported': 10}, '513c472ac48e4444a7f421552252e37f81e284a7': {'malicious': 0, 'suspicious': 0, 'undetected': 66, 'harmless': 0, 'timeout': 0, 'confirmed-timeout': 0, 'failure': 1, 'type-unsupported': 10}, '5fe1427e9230be860be004ecaa18f1892fdfed5e': {'malicious': 4, 'suspicious': 0, 'undetected': 62, 'harmless': 0, 'timeout': 0, 'confirmed-timeout': 0, 'failure': 0, 'type-unsupported': 11}}

count = 0
for i in hash_analyze.keys():
    if hash_analyze[i]['malicious'] != 0 or hash_analyze[i]['suspicious'] != 0:
        extension_name = find_name_by_hash(zip_hash,  i)
        if count == 0:
            print("FOUND MALWARE EXTENSION:\n")
            count += 1
        print(extension_name[:-4])
        if hash_analyze[i]['malicious'] != 0 :
            print(f"    Malicious detects: {hash_analyze[i]['malicious']}")
        if hash_analyze[i]['suspicious'] != 0 :
            print(f"    Malicious detects: {hash_analyze[i]['suspicious']}")
        print('')

        
client.close()



