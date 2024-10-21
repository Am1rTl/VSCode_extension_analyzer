import requests

url = "https://www.filescan.io/api/scan/file"
cookie = {"cookieyes-consent": "consentid:NnpKMU5MSUs4OFE5UU5jS09URjUyRnE0ZW52TWJYb2Y,consent:no,action:,necessary:yes,functional:no,analytics:no,performance:no,advertisement:no"}
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.6167.160 Safari/537.36",
    "Accept": "application/json, text/plain, */*",
    "Content-Type": "multipart/form-data; boundary=----WebKitFormBoundaryhD1oOp8KHCwGJ8RD"
}

file_path = "path/to/your/file.zip"
file_name = "asd.zip"

files = {
    "file": (file_name, open("/tmp/asd.zip", "rb"), "application/zip"),
    "description": ("", "", ""),
    "tags": ("", "", ""),
    "password": ("", "", ""),
    "save_preset": ("false", "", ""),
    "propagate_tags": ("true", "", ""),
    "is_private": ("false", "", ""),
    "skip_whitelisted": ("true", "", ""),
    "rapid_mode": ("false", "", ""),
    "osint": ("true", "", ""),
    "extended_osint": ("true", "", ""),
    "extracted_files_osint": ("true", "", ""),
    "visualization": ("true", "", ""),
    "files_download": ("true", "", ""),
    "resolve_domains": ("true", "", ""),
    "input_file_yara": ("true", "", ""),
    "extracted_files_yara": ("true", "", ""),
    "whois": ("true", "", ""),
    "ips_meta": ("true", "", ""),
    "images_ocr": ("true", "", "")
}

response = requests.post(url, headers=headers, cookies=cookie, files=files)

print(response.text)