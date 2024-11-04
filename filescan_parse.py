import json
import time
import requests

def get_report_by_url(url):
    response = requests.get(f"https://www.filescan.io/api/scan/{flow_id}/report")
    
    if response.text == "Internal Server Error":
        return None
    else:
        report = json.loads(response.text)
        return report
    


with open("reports/filescan_reports", 'r')  as f:
    data = f.read()
f.close()

hash_reports = eval(data)

for name in hash_reports.keys():
    print(hash_reports[name])

    for flow_id in hash_reports[name]:
        report = get_report_by_url(f"https://www.filescan.io/api/scan/{flow_id}/report")

        if report != None:
            while report['state'] != 'finished':
                time.sleep(10)
                report = get_report_by_url(f"https://www.filescan.io/api/scan/{flow_id}/report")
            
            verdict = report["sourceArchive"]["verdict"]

            print(verdict)



resp = requests.get(f"https://www.filescan.io/api/reports/{report_id}/files")
