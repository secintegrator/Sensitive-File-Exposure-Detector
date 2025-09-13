# Sensitive-File-Exposure-Detector
A passive reconnaissance tool that checks whether a target web server exposes sensitive files or directories often left unintentionally
#  Sensitive File Exposure Detector

A unique passive reconnaissance tool that checks if a target web server exposes sensitive files commonly left behind by developers or misconfigured servers.

## Why This Project?

Unlike standard vulnerability scanners, this tool:
- Focuses on **sensitive file exposures**
- Does **not** perform brute-force or heavy scanning
- Aims to uncover **high-risk oversights** in deployments

##  Examples of Files Detected

- `.git/config`
- `.env`
- `wp-config.php`
- `backup.zip`
- `id_rsa`

##  Getting Started

### Requirements

```bash
pip install requests


## 📄 License

This project is licensed under the [MIT License](LICENSE).


**Usage**

python detector.py

Enter a URL like:https://example.com
