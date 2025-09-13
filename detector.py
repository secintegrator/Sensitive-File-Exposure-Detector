import requests

# === Target input ===
target = input("Enter target URL (e.g., https://example.com): ").strip("/")
if not target.startswith("http"):
    target = "http://" + target

print(f"\n[+] Scanning: {target}\n")

# === List of common sensitive files ===
sensitive_paths = [
    ".env",
    ".git/config",
    "config.php",
    "wp-config.php",
    "backup.zip",
    "db.sql",
    "database.yml",
    "composer.lock",
    "id_rsa",
    ".htaccess",
    ".DS_Store",
    "server-status"
]

# === Check each path ===
for path in sensitive_paths:
    url = f"{target}/{path}"
    try:
        res = requests.get(url, timeout=5)
        if res.status_code == 200 and len(res.text) > 20:
            print(f"[!!] Potential Exposure: {url}")
        elif res.status_code == 403:
            print(f"[+] Forbidden (might exist): {url}")
        else:
            print(f"[-] Not Found: {url}")
    except requests.RequestException:
        print(f"[!] Failed to connect: {url}")
