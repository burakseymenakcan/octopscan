## OctopScan

OctopScan is a modular, multi-purpose network tool built in Python.

---

## 📦 Features

**Port Scanner**: Scans TCP ports on target IP addresses, showing both open and closed ports.

---

## 🚀 How to Run

1. **Clone or download** the script to your local machine.
2. Make sure you have **Python 3.x** installed.
3. Run the script via terminal:

```bash
python octopscan.py
```

---

## 🛠️ Usage

1. When prompted, select an option:
    ```
    [1] Port Scanner
    [0] Exit
    ```
2. If you choose **Port Scanner**, you'll be asked to enter the **target IP address**.
3. The script will begin scanning TCP ports from **1 to 9999**.
4. Output will look like this:
    ```
    [+] Port 22 is OPEN
    [-] Port 23 is CLOSED
    ...
    ```

---

## ⚠️ Legal Disclaimer

This tool is intended for **educational purposes only**.  
Do **NOT** use it to scan IP addresses that you do not own or have permission to test.  
Unauthorized port scanning may be **illegal** depending on your jurisdiction.

---

## 📌 Notes

- On some systems, a firewall may block outgoing requests.
- You can limit the port range by modifying this line in the code:

```python
for port in range(1, 10000):
```

Change `10000` to a lower number like `1000` for faster results.

---

## 📄 License

This project is licensed under the GNU General Public License v3.0 (GPL-3.0).
