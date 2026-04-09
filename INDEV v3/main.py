
import time
import colorama
import os
from colorama import Fore, Back, Style
colorama.init()
import sys
import webbrowser as WEB
import winsound
import json
import random

spiner = ["|", "/", "-", "\\"]

version = "indev build 942026 1"
versionSol = "indev build 6320261837"

installed_apps = {
    "solna": False,
    "testing": False,
    "minigame": False,
}

play_time = 0
session_start = time.time()

name = None

os.system("title "+ "Wasteram Terminal Simulator™")

# i use ChatGPT 5% for reduce dev time and aslo trying learing form it

## Python Usless_Program.py ts is how to run it in terminal

## MOVIE URL
KimURL = "https://www.youtube.com/watch?v=7maE0J9S-T0"
ABATAURL = "https://www.youtube.com/watch?v=EzQiEOQ8nVA"
Movie1 = "https://youtu.be/JreSPMu_VGY?si=zjh5ss8bQCIwix82"
Movie2 = "https://youtu.be/51LMUSVSZHk?si=y8LdeDgvkVGsht6m"
Movie3 = "https://youtu.be/lB7spjbwaGI?si=9xkE0_5lsO-jp3BY"
Movie4 = "https://youtu.be/BYx2JCCt2Ss?si=YXUzJ_WAVaA2iMw5"
scream = "https://www.youtube.com/watch?v=ykGB4zu7gTc"
fun = "https://www.youtube.com/watch?v=GtL1huin9EE"
yell = "https://www.youtube.com/watch?v=-5R_sviyV4Y"
peakOSURL = "https://www.youtube.com/watch?v=hmjU-6tkEc8"
burgerURL = "https://www.youtube.com/shorts/SxtsnWjD_UA"
homeroURL = "https://youtu.be/miO75CbTuJ4?si=qK9vzf22AvFpshEC"
hateURL = "https://youtu.be/acAfItR04l4?si=K6IIJ6S59Ygb46xW"
Dr = "https://www.youtube.com/watch?v=ApAi53Fuzuo"
Wwebb = "https://github.com/tunva28/WASTERAM-Source-code"

## achievements
achievements = {
    "first_command": {"name": "First Command", "unlocked": False},
    "Error_command": {"name": "Error Command", "unlocked": False},
    "updLogV": {"name": "VIEW THE UPDATELOG", "unlocked": False},
    "helloword": {"name": "Hello WORLD!", "unlocked": False},
    "help": {"name": "HELP!", "unlocked": False},
    "exit": {"name": "goodbye !", "unlocked": False},
    "testing": {"name": "testing testing", "unlocked": False},
    "21": {"name": "YOU STUPID!", "unlocked": False},
    "clear": {"name": "clear!", "unlocked": False},
    "forgot": {"name": "what is this program name again?", "unlocked": False},
    "kim": {"name": "kim jong un approve", "unlocked": False},
    "yell": {"name": "YELL", "unlocked": False},
    "burger": {"name": "IM SORRY, DID HE JUST SAY THAT HIS LAST NAME... IS BURGER?", "unlocked": False},
    "homer": {"name": "HOMERO VAS A RECOLTALTE", "unlocked": False},
    "Dr": {"name": "Doctor pigeon", "unlocked": False},
    "A": {"name": "that one DJ remix thing", "unlocked": False},
    "C": {"name": "useless command", "unlocked": False},
    "R": {"name": "R letter", "unlocked": False},
    "Print": {"name": "Print TEXT", "unlocked": False},
    "load": {"name": "loading for what?", "unlocked": False},
    "scream": {"name": "scream", "unlocked": False},
    "sudo": {"name": "I AM NOT A LINUX TERMINAL", "unlocked": False},
    "math": {"name": "math!", "unlocked": False},
    "randomNum": {"name": "random number!", "unlocked": False},
    "draw": {"name": "IT CAN DRAW TOO?", "unlocked": False},
    "appI": {"name": "installed app!", "unlocked": False},
    "use solna": {"name": "welcome to Solna MOS", "unlocked": False},
    "profile": {"name": "show MY profile NOW!", "unlocked": False},
    "minigameApp": {"name": "game inside game?", "unlocked": False},
    "coinW": {"name": "Coin Winner", "unlocked": False},
    "coinL": {"name": "Coin Loser", "unlocked": False},
    "first command in solna": {"name": "first command in solnaMOS", "unlocked": False},
    "Solna": {"name": "Hello Solna!", "unlocked": False},
    "hate": {"name": "h a t e", "unlocked": False},
    "cabbit": {"name": "Cabbit", "unlocked": False},
    "world": {"name": "Earth!", "unlocked": False},
    "logoW": {"name": "Wasteram Terminal Simulator™", "unlocked": False},
    "show": {"name": "1920", "unlocked": False},
    "Holy": {"name": "Temple OS", "unlocked": False},
    "Wweb": {"name": "Open Wasteram Web! :]", "unlocked": False},
}

import shutil

def center_text(text):
    width = shutil.get_terminal_size().columns
    return "\n".join(line.center(width) for line in text.splitlines())

def true_intro():
    wait = 0.2

    clearT()
    time.sleep(wait)

    logo = f"""{Fore.GREEN}
88  dP  dP""b8 88  dP 88  dP
88odP  dP   `" 88odP  88odP 
88"Yb  Yb      88"Yb  88"Yb 
88  Yb  YboodP 88  Yb 88  Yb

Ku Ca Kheiyn Khod
AKA -Breamm
"""

    print(center_text(logo))

    time.sleep(wait)
    clearT()

    logo = f"""{Fore.LIGHTGREEN_EX}
88  dP  dP""b8 88  dP 88  dP
88odP  dP   `" 88odP  88odP 
88"Yb  Yb      88"Yb  88"Yb 
88  Yb  YboodP 88  Yb 88  Yb

Ku Ca Kheiyn Khod
AKA -Breamm
"""
    print(center_text(logo))
    time.sleep(wait)
    clearT()

    logo = f"""{Fore.WHITE}
88  dP  dP""b8 88  dP 88  dP
88odP  dP   `" 88odP  88odP 
88"Yb  Yb      88"Yb  88"Yb 
88  Yb  YboodP 88  Yb 88  Yb

Ku Ca Kheiyn Khod
AKA -Breamm
"""

    print(center_text(logo))

    notes = [
        (100, 220),
        (500, 120),
        (600, 300),
        (800, 180),
        (1000, 220),
        (1200, 300),
    ]

    for freq, dur in notes:
        winsound.Beep(freq, dur)
        time.sleep(0.05)

    winsound.Beep(1500, 200)
    winsound.Beep(1800, 400)

    time.sleep(wait)
    clearT()

    logo = f"""{Fore.LIGHTGREEN_EX}
88  dP  dP""b8 88  dP 88  dP
88odP  dP   `" 88odP  88odP 
88"Yb  Yb      88"Yb  88"Yb 
88  Yb  YboodP 88  Yb 88  Yb

Ku Ca Kheiyn Khod
AKA -Breamm
"""
    print(center_text(logo))

    time.sleep(wait)
    clearT()
    logo = f"""{Fore.GREEN}
88  dP  dP""b8 88  dP 88  dP
88odP  dP   `" 88odP  88odP 
88"Yb  Yb      88"Yb  88"Yb 
88  Yb  YboodP 88  Yb 88  Yb

Ku Ca Kheiyn Khod
AKA -Breamm
"""

    print(center_text(logo))
    loading()
   
## fuction ZONE
def playAchievementSound():
    winsound.Beep(1200, 200)
    winsound.Beep(1500, 200)
    winsound.Beep(1800, 300)

def achievementPopup(title):
   print(f"""{Fore.YELLOW}
----==######################==----
    +           +                +
+      ACHIEVEMENT UNLOCKED!  +    
  +           +                 +
       {title}                 

----==######################==----

""")

def unlock(key):
   if not achievements[key]["unlocked"]:
      achievements[key]["unlocked"] = True
      playAchievementSound()
      achievementPopup(achievements[key]["name"])
      saveData()

def saveData():
    global play_time

    current_session = int(time.time() - session_start)
    total_time = play_time + current_session
    
    data = {
        "achievements": achievements,
        "apps": installed_apps,
        "name": name,
        "play_time": total_time
    }
    with open("save.json", "w") as f:
        json.dump(data, f)

def loadData():
    global achievements, installed_apps, name, session_start ,play_time
    try:
        with open("save.json", "r") as f:
            data = json.load(f)
            achievements = data.get("achievements", achievements)
            installed_apps = data.get("apps", installed_apps)
            name = data.get("name", name)
            play_time = data.get("play_time", play_time)
    except:
        saveData()

    session_start = time.time()

def intro():
   print(f"{Fore.CYAN}Welcome to")
   print(f"""{Fore.RED}
 █████   ███   █████                                                                    
░░███   ░███  ░░███                     ░███                                                 
 ░███   ░███   ░███   ██████    █████  ███████    ██████  ████████   ██████   █████████████  
 ░░░░   ░░░░   ░░░░  ░░░░░███  ███░░  ░░░███░    ███░░███░░███░░███ ░░░░░███ ░░███░░███░░███ 
 ░░███  █████  ███    ███████ ░░█████   ░███    ░███████  ░███ ░░░   ███████  ░███ ░███ ░███ 
  ░░░░░░░░░░░░░░░    ███░░███  ░░░░███  ░███ ███░███░░░   ░███      ███░░███  ░███ ░███ ░███ 
    ░░███ ░░███    ░░████████ ██████   ░░█████ ░░██████  █████    ░░████████ █████░███ █████
     ░░█    ░███████████████████████████████████████████████████████████████████████████████
     ░░    ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
  ██████████████████████████████████████████████████████████████████████████████████████████  
 ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░                                                                                                                           
         Terminal Game
   """)
   print(f"{Fore.YELLOW}(version:{version})")
   print(f"{Fore.LIGHTGREEN_EX}By -> Breamm aka Tunva <-")
   print()
   print("A Useless Terminal Simulator™")
   print()

def loading():
   for i in range(20):
      sys.stdout.write(f"{Fore.LIGHTGREEN_EX}\rLoading " + spiner[i % len(spiner)])
      sys.stdout.flush()
      time.sleep(0.2)
   print(f"\nDone {Fore.CYAN}!")

def clearT():
   os.system('cls' if os.name == 'nt' else 'clear')

def peakOS():
   print(f"""{Fore.LIGHTYELLOW_EX}
 ███████████                                    ████                 ███████     █████████ 
░█░░░███░░░█                                   ░░███               ███░░░░░███  ███░░░░░███
░   ░███  ░   ██████  █████████████   ████████  ░███   ██████     ███     ░░███░███    ░░░ 
    ░███     ███░░███░░███░░███░░███ ░░███░░███ ░███  ███░░███   ░███      ░███░░█████████ 
    ░███    ░███████  ░███ ░███ ░███  ░███ ░███ ░███ ░███████    ░███      ░███ ░░░░░░░░███
    ░███    ░███░░░   ░███ ░███ ░███  ░███ ░███ ░███ ░███░░░     ░░███     ███  ███    ░███
    █████   ░░██████  █████░███ █████ ░███████  █████░░██████     ░░░███████░  ░░█████████ 
   ░░░░░     ░░░░░░  ░░░░░ ░░░ ░░░░░  ░███░░░  ░░░░░  ░░░░░░        ░░░░░░░     ░░░░░░░░░  
                                      ░███                                                 
                                      █████                                                
                                     ░░░░░                                                 
         {Fore.YELLOW}R.I.P Terry A. Davis
   """)

def SolnaMDOS():
   print(f"{Fore.CYAN}HELLO")
   print(f"""{Fore.WHITE}      ::::::::   ::::::::  :::        ::::    :::     :::             :::   :::    ::::::::   :::::::: 
    :+:    :+: :+:    :+: :+:        :+:+:   :+:   :+: :+:          :+:+: :+:+:  :+:    :+: :+:    :+: 
{Fore.LIGHTCYAN_EX}   +:+        +:+    +:+ +:+        :+:+:+  +:+  +:+   +:+        +:+ +:+:+ +:+ +:+    +:+ +:+         
  +#++:++#++ +#+    +:+ +#+        +#+ +:+ +#+ +#++:++#++:       +#+  +:+  +#+ +#+    +:+ +#++:++#++   
        +#+ +#+    +#+ +#+        +#+  +#+#+# +#+     +#+       +#+       +#+ +#+    +#+        +#+    
#+#    #+# #+#    #+# #+#        #+#   #+#+# #+#     #+#       #+#       #+# #+#    #+# #+#    #+#     
{Fore.BLUE}########   ########  ########## ###    #### ###     ###       ###       ###  ########   ########                                                     
         {Fore.LIGHTBLUE_EX}By Breamm(tunva)
{Fore.RED}██{Fore.GREEN}██{Fore.BLUE}██{Fore.CYAN}██{Fore.MAGENTA}██
{Fore.LIGHTYELLOW_EX}Version:{versionSol}
   """)

def cabbit():
   print(f"""                       
   {Fore.LIGHTWHITE_EX}                                             ****                                           
                                          *+=+======+######                                    
                                     ++++=======-------+*######%                               
                                   *+=-------------=++++#%##***+*+                             
                                  *++++--------======+*+%++##*****#                            
                                 *+++===-----=+++-====**%==+%@*+**#                            
                                +*#+======++==*%#=--==***+++*@+=-=+#                           
                                ++=-=++#*+===--+%+-===++++++=+%@@#*#                           
                               ==---==+*#*##@@@@+:--====++==@#@@#+*%%                          
                              +==-----=++=*+@#@@##::-===++==@@@**-=%#%                         
                              ++=-==--==---*@@@*=@=::=+++*+=@#*+-++*%#                         
                              ++==-===-==--::-++--*@+==----=%#--==+*+#                         
                             =+===---=+===---==---+%#+-::--=#@+=**+=+#@                        
                             *+==-----++============+*=---=+*%#**+= =*%                        
                             *+==-----=+++===-=*#+===**+*#%@%%#*=-  =#@                        
                             **+=----:-++**+++=++*+=---*@@#+#*=--   *%                         
                             #*+=-----:+**##++===++=====%#*#++=                                
                             ##+==-----*#*%#**+*++++++***##%#*+                                
                             %%*+====--%*=====++++=++*#*+*+****                                
                             @%#*+===-##*============++++##*++++                               
                             @@%**+*@@@%*+++=+++==+===++=+++++++                               
                            @@@@%%%@@@@#**+++*++==++==++===+==+++                              
                            @@@@@%%@@@%**++**++=+=++======+++==+=                              
                            @@@@%%@@@@%#####+++++============+===+                             
                           @@@@@@@##%@@%%##**#*++++========+====-=                             
                           @@@@@@@%##%###%##%%#+===+=======+=====+                             
                           @@@@@@@@#**++*#%#%%#=============+==#*+                             
                           @%###%%@%#*+++*#%%%*====--===-=====++++                             
                            @##%%@@ %##+=++++++=--====-=-=-=+++=+                              
                                    %%*++=======---=======+++===+                              
                                     ##*+=+==++++++*%  #++++===+                               
                                     ###*+*+*+#++*+*%                                          
                                      ##**##********                                           
                                      %%#%%%@@#***++                                           
                                       @@@@@@@***+++                                           
                                        @%%#*+++**                                                                                                                                                                 
""")
   
def earth():
   print(f"""                       
   {Fore.LIGHTWHITE_EX}                                             ****                                           
                                         @@@@@@@@%%@@@@@@@@@@                                        
                                  @@@@%%###############%%%%%%%@@@                                   
                              @@@%%#####******############%%%%%%%%%@@@                              
                          @@%%%%##*********************########%%%%%%%%@@                           
                        @@%%##*******+++++++++++++++***#####*######%%%%%@@@@                        
                     @@%##****+++++++++++===+++++=++++**##**#%######%%%@@@%%@@                      
                   @%#**+*+++++==+++++++++++*+==+==+*++*#****##%#####%%%%%%@@%@@@                   
                  %#*****++=========++++***#**+++++=++++**#####%%%#%###%%%%%@@%%@@                  
                %#**+++***+=++++===+===-=++====*****++++++*%%###%%##*##%%%%%%@@%%%@@                
              @%*++++*++++=+**+*++--=====+*+=************#**#######****###%%%%%%%%%@@               
             @#+++**++=+++++==--=+=--=++##+=++=---+#*#%%%#%##%###*#**##**#%@@%%%%@%@%@@             
            %#***#+===++**+==--=+++-:-+##**+-------+###**%%#%%%#*#########%@@@%%@@@@@%@@            
           %####*+++****+**=---=*+++--+=-=--:::-+#*+##%%###*******#***##%%%%@@%%%@@@@%@@@           
          %%##*=*##%####*++==+**#***=-++=--:::-=*##**######*++****###%#%@@@@@@%%%@@@@@@@@@          
         %##*++#%#####*##+==++++++++====++=*+****##++##*###**+==+**###**#%%%@@@%#%@@@@@@@@@         
        %%###*#######+=+#+=--==++*+---+++++==+****##=*%*-++*=--=+*#%%##%%@@%@%%%%#@@@@@@@@@@        
       @%###########*+==+#+=-------:::::---+*****###+*###=--#***+#####%@@@@%%%%%%#@@@@@@@@@@        
       %#########*%%*+--:+#+-----------=****#*+**#######%#**++**%+=+*#%%@@%#*%%%#%@@@@@@@@@@@       
      @####******##+=-----+++++=++####++**+**+++****#####%###*++=---==++*#%%%%*+*%@@@@@@@@@@@       
      %####*++#**#*+=----==-==--=*%#*#+**++***#****#########*+==-::-:--==**++*+#%%@@@@@@@@@@@@      
     @####*=+****#*+=--=---=+===+#%+***++***+*#*******####*+*+=-:----===+#*%*#%%%@@@@@@@@@@%@@      
     %#####*##**+*++=--==----===+##++*==++*++++********+**+=----==++#%##**#**%@@@@@@@%%@@@@@@@      
     %####*####**+-===-=+*+-====++=-:-*+==+-=++++**+++==*=+=--+***#%#====*##%@@@@@@@@@@%@@@@@@@     
     %*#########**===-==++==++=-===-:::-...:-====+++++*##*==+****#%@@%%%%%%@@@@@@@%@%%%%@@@@@@@     
     %#+#####*###****=::-=-=----====++=.:=-:=+-=+=+**#**++++*%@@@%#%@%@%@@@@@@@@@@%%%%%%%@@@@@@     
     %*++##*##*##**##*+-:-:::-==-==:-+=::=+=***++=+++**#%@@@@@@@@@%#%%%@@@@%%%%%@@%%%%%%%@@@@@@     
     %##+#############**-::-==++-=--==**+++++##*+==+++*%@@@@@@@@@@@%@%#%%%%%%%@%%*#%%%%%%@@%%@@     
     %**+**+#####%####+---==+##**+=-:::==+=+++**+===**#%@%@%%%@@@@%####%%%%%#%%#*+*###%%%%%%%@@     
     %#+=++***#%#*%#%##=+**#*%%##+=**=-=+++++****++++*%%%*@@%%##@@@%%%%%%%%%%%%#**+**#%%%@@%@@      
      %*+-:-=+=+#####%%%##**#%%#%#++**+++++++***##*#***#@%%@#+-=*##%%@@%#%%%%%%%*++*%%%%%@%@@@      
      %#*=::::=+#######%%%%%%%%%###*#*++=+*+**#######***+++++:::-=+#%%%%%%%%#%%%###%%%%%%@@@@       
       %#*++=:=+-=*#%#*#%%%%%%#***####*****++*##%%%%%#*++**+---+=-:=+#%%##%#******#####%%@@@@       
       @#**##+*###++*#%#+=#+=**#%==*#%#+*#####%%%%%@@@*+*%%%%%%#+==#%%%%%*+****+*+#####%%%%@        
        #**#***+#####**###*##++#%##+=##*##%%%%#**#%%%%@@@@%%@%%%%+==+=+****+++++*#####%%%%@@        
        @#*######*####%#*+=-+++*%#**%#*##%%%%#+#%#%%%%%@%%%%#*+#%#+*###+=*+=*+=+****#%%%%@@         
         @#+*#****########*++**==-+%+-+*+*+%%%@@@%++++#%@@@@@%%@@%#%*+*++**++=+++++*#%%%%@          
          @#+**#####*####*###***+**=++++*##***++#+==-=+**++=+++++++**++=+=======++*%%%%%@           
           %#+=*########**#########%%%*##*###%%*+++****++++*#+++*+*+*++=========*#%%%%%@            
             #*=*########*+******%%*#**+==*#*=**+=+*=+*%%#%%%##%#%#**===+*+**#%%%%%%%@@             
              %*=+#######*########**##*##%%#++*###*++=+**============-=++*#%%%%%%%%%@@              
               %#+-++#####*#######%#%#*%***####*+++++++***++==-=====+++++*######%%%@                
                 %#==*######*########%%%#***##*#*+++++++++==++==-====++***#####%%@                  
                   %*==**###**********#########*++==+++++++===---======+*****##%@                   
                     %#+==+**#******#***++++++===--===++**++======+++++++***#%@                     
                       @#*=-:-+****#####**++*=======+===+*****+====++++**#%@@                       
                          %#+==++**#*++++++++++++*++++*****+++++=++*###%%@                          
                             %##**+*###**++****#####*****+++=++++*#%%%@                             
                                 @%#******=+++=**+**#**#####**#%%@@                                 
                                      @%%###*********####%%%@@                                                                                                                                                                              
""")

def Solna():
   print(f"""                       
   {Fore.LIGHTWHITE_EX}                                                                                                                                                                                         
                                          Xx++++++++++++xX                                          
                                     Xx+;;::::::::::::::::;;+xX                                     
                                  X+:::::::::::::::::::::::::;xX          XXxX                      
                               x+:::::::::::::::::::::::::;+::+x     xx+:...+                       
                             x;:::::::::::::::::::::::::;:.......;x X;......X                       
                           x;:::::::::::::::::::::::::;:...........:xXx;...+                        
                         X+:::::::::::::::::::::::::;:...............:x x;:x                        
                        x;::::::::::::::::::::::::;;...................;X X                         
                       x:::::::::::::::..::::::::;:.....................:x                          
                     X+::::::::::::::..::.::::::;:........................+                         
                     +;:::::::::::::::....:::::;;..........................x  ;..::;;+xX            
                    x;::::::::::::::::::::::::;;...........................:X X:.....;x             
                    +:::::::::::::::::::::::::;.............................;X X:...+$              
                   X:::::::::...   ...:::::::;:.............::::::::::.......+  x.;x                
                 XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX                 
                  X;:+X;:.  .:::::::::. :X+:;;..........+x;::.........::::.+X+XXX                   
                  X;:+X:   .::::::::::...X+:;;..........+x;:..........:::::+X;+                     
                  X;;+X;;: .;;;;;;;;;;...X+;;;..........+x;:..........:::..+X;+                     
                  X;;+X+;:. :;;;;;;;;:..:X+;;;..........+x;::........::::..+X;+                     
                  X+;+X+;;:...:;;;;:...:;X+;;+..........+x::::::...:::::...+X+x                     
                  Xx;+X+;;;;:.. ..  .:;;+X+;;+:.........+x:..:::::::::.....+X+$  XX                 
                   X++XxxxxxxxxxxxxxxxxxxX+;;+;.........+X+;;;;;;;;;;;;;;;;xXX  x.;x                
                   $x++xxxxxxxxxxxxxxxxxx++++++.........:;;;;;;;;;;;;;;;;;;;xX X:...xX              
                    X+++++++++++++++++++++++++x;...........................;X X:.....;x             
                     x+++++++++++++++++++++++++x:.........................:x  ;..::;;;xX            
                     Xx+++++++++++++++++++++++++x:.......................:x                         
                      $X++++++++++++++++++;;+++++x;.....................+X                          
                        Xx++++++++++++++++;....::::...................:x$ X                         
                   XXXxXXXx++++++xxxxxxxxxxx+;.. ..;x::::::::::::::.:+X x;:x                        
               XXx+:.......;xxxxxxxxxxxxxxxxxxxxxxxxxx+::::::::::::;X x+...+                        
           XXx+;..:+++;;;.....:xxxxxxxxxxxxxxxxxxxxxxxxx+:::::::;+X x;.....:X                       
        XX+:.:;+;;;:.::.:;xxx;..:xxxxXXXXXXXXXXXXxxxxxxxxxx;:+xx    Xxx+:...+                       
     XX+;;;+++;;:...::+Xx;...:x;.:x++xXXx;:........;XXxxxxxxxXX           XXxX                      
    Xx:..........:;+x+;:.;++x:..;+......:;;;::::;++...:xXxxxXXX                                     
    Xx+xxxxxxxxx++;:...:++:..::;x;xx+;++;..:+x+x++:....xXXX                                         
      XXXXXxx+++++++xxXx;.;x:.++.;+xxXxxxxxXx+;...;x:.:X                                            
              XXXXXXXXXx+xx:+Xx+::::::::::.....:xx:...+X                                            
                       XXXxxXxxxx+++++++++xxxxx+;:;x;;X                                             
                          XXxxxxXXXXXXXXXXXXXXxxxxxxxXX                                             
                                                XXXXX                                                                                                                                                                                                                    
""")

def Wasteram():
   print(f"""                       
   {Fore.LIGHTRED_EX}                                                                                                                                                                                         
          ))))))))))        )))))))         )))))))))                                                                                                        
           )))))))))        ))))))))       )))))))))                                                                                                         
            )))))))))      ))))))))))      )))))))))                                                                                                         
            )))))))))      ))))))))))     ))))))))))                                                                                                         
            ))))))))))    )))))))))))     )))))))))                                                                                                          
             )))))))))    ))))))))))))   ))))))))))                                                                                                          
              ))))))))    ))))))))))))   )))))))))                                                                                                           
              )))))))))  ))))))))))))))  )))))))))   ))))        ))))))) )))))))))))) )))))))))) )))))))))         )))       )))        )))                  
               )))))))))))))))) ))))))) )))))))))    )))))     ))))))))) )))))))))))) )))))))))) )))))))))))      )))))     )))))      )))))                 
               )))))))))))))))) )))))))))))))))))   )))))))    ))))          ))))     ))))       ))))    ))))    )))))))    ))))))    ))))))                 
                ))))))))))))))   )))))))))))))))   )))) )))    )))))         ))))     ))))       ))))    ))))   )))) )))    )))))))   ))))))                 
                ))))))))))))))    )))))))))))))    )))  ))))    ))))))))     ))))     ))))))))   ))))))))))))   )))  ))))   )))))))  )))))))                 
                 )))))))))))))    )))))))))))))   )))))))))))      ))))))    ))))     ))))))))   ))))))))))    )))))))))))  ))))))))))))))))                 
                 ))))))))))))      ))))))))))))  ))))))))))))) )     )))))   ))))     ))))       ))))  )))))  ))))))))))))) )))) )))))) ))))                 
                 )))))))))))       )))))))))))  ))))      )))) ))))))))))    ))))     )))))))))) ))))   )))) ))))      )))) ))))  ))))  ))))                 
                  ))))))))))        )))))))))   ))))       )))) )))))))      ))))     )))))))))) ))))    ))))))))       ))))))))   ))   ))))                 
                   ))))))))         ))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))               
                                                                                                                                                             
                   )))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))               
                                                                                                                                                                                                       
""")


def listCMS():
   print(f"{Fore.LIGHTYELLOW_EX}-------------------------------")
   print("==>>here is the command list<<==")
   print()
   print("> atsp > about this useless program?")
   print("> hello")
   print("> clear")
   print("> exit")
   print("> test")
   print("> what 9+10")
   print("> kim jong un")
   print("> squidward yell")
   print("> burger")
   print("> homero")
   print("> pigeon")
   print()
   print("==>>Silent Movie Zone 1920<<==")
   print()
   print("> smo 1")
   print("> smo 2")
   print("> smo 3")
   print("> smo 4")
   print()
   print("==>>command zone<<==")
   print()
   print("> command A")
   print("> command C")
   print("> command R")
   print("> command updLog")
   print("> command print")
   print("> command load")
   print("> command scream")
   print("> command sudo > useless command")
   print("> command randomNum > random number")
   print("> command plusNum > Only Two Number")
   print("> command minusNum > Only Two Number")
   print("> command divNum > Only Two Number")
   print("> command mutiNum > Only Two Number")
   print("> command draw >show drawing list")
   print("> command progress > achievements list ")
   print("> command profile > show player profile")
   print("> command install > install thing ")
   print("> command Enter > Enter thing ")
   print("> command WasteramWeb > open wasteram web")
   print()
   print("==>>Holy command ZONE<<==")
   print()
   print("> ---- --?")
   print("-------------------------------")

def commandDrawList():
   print(f"{Fore.LIGHTYELLOW_EX}----------DRAW-LIST-----------")
   print()
   print("exsample > command draw cabbit")
   print("                        ^^^^^^")
   print()
   print("==>>here is the command list<<==")
   print("> cabbit")
   print("> earth")
   print("> Solna")
   print("> Wasteram")
   print("-------------------------------")

def Updlog():
   print(f"{Fore.LIGHTYELLOW_EX}----------UPDATE-LIST-----------")
   print("==>>here is the update list<<==")
   print("  MORE WASTERAM UPDATE INDEV 3 ")
   print()
   print("> redesign logo")
   print("> remove bardar")
   print("> add new command in draw command")
   print("> add 10 achievement and remove some achievement")
   print("> add update log command")
   print("> add new command and remove some command")
   print("> update install command and Enter command")
   print("> add new command to solnaMOS")
   print("> new save system (save.json)")
   print("> Wasteran + SolnaMOS + Minigame Package!")
   print()
   print("-------------------------------")

def solnaMain():

   while True:
      User = input(f"{Fore.LIGHTBLUE_EX}SolnaMOS/{name}> ")

      unlock("use solna")
      unlock("first command in solna")

      if User == "exit":
         loading()
         print(f"{Fore.LIGHTBLUE_EX}Exiting Solna MOS...")
         break
      if User == "help":
         print("----command list----")
         print("> exit")
         print("> clear")
         print("> help")
         print("> atsmos")
         print("--------------------")
      elif User == "clear":
         clearT()
      elif User == "atsmos":
         clearT()
         SolnaMDOS()
      else:
         print(f"{Fore.RED}Unknown command: {User}")

def formatTime(seconds):
    hours = seconds // 3600
    minutes = (seconds % 3600) // 60
    secs = seconds % 60
    return f"{hours}h {minutes}m {secs}s"

def gameApp():
   print(f"{Fore.CYAN}Welcome to")
   print(f"""{Fore.RED}
 █████   ███   █████                                                                    
░░███   ░███  ░░███                     ░███                                                 
 ░███   ░███   ░███   ██████    █████  ███████    ██████  ████████   ██████   █████████████  
 ░░░░   ░░░░   ░░░░  ░░░░░███  ███░░  ░░░███░    ███░░███░░███░░███ ░░░░░███ ░░███░░███░░███ 
 ░░███  █████  ███    ███████ ░░█████   ░███    ░███████  ░███ ░░░   ███████  ░███ ░███ ░███ 
  ░░░░░░░░░░░░░░░    ███░░███  ░░░░███  ░███ ███░███░░░   ░███      ███░░███  ░███ ░███ ░███ 
    ░░███ ░░███    ░░████████ ██████   ░░█████ ░░██████  █████    ░░████████ █████░███ █████
     ░░█    ░███████████████████████████████████████████████████████████████████████████████
     ░░    ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
  ██████████████████████████████████████████████████████████████████████████████████████████  
 ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░                                                                                                                           
         MINIGAME
   """)

   unlock("minigameApp")

   while True:
      User = input(f"{Fore.CYAN}Wasteram/Terminal/Game> ")

      if User == "exit":
         loading()
         print(f"{Fore.CYAN}Exiting Game...")
         break
      elif User == "help":
         print("----command list----")
         print("> exit")
         print("> clear")
         print("> help")
         print("----game list----")
         print("> coinflip")
         print("--------------------")
      elif User == "clear":
         clearT()
      elif User == "coinflip":
         coin = random.randint(0,1)
         inputU = input("Heads or Tails? > ").lower() 
         if inputU == "heads":
            if coin == 0:
               print(f"{Fore.GREEN}You win! It was Heads.")
               unlock("coinW")
            else:
               print(f"{Fore.RED}You lose! It was Tails.")
               unlock("coinL")
         elif inputU == "tails":
            if coin == 1:
               print(f"{Fore.GREEN}You win! It was Tails.")
               unlock("coinW")
            else:
               print(f"{Fore.RED}You lose! It was Heads.")
               unlock("coinL")
      else:
         print(f"{Fore.RED}Unknown game:")


## Main

true_intro()

loadData()

clearT()

intro()
print("say Enter command for list of command")
print(f"{Fore.LIGHTYELLOW_EX}^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")

while True:
     GETSOME = input(f"{Fore.GREEN}Wasteram/Terminal> ")
     unlock("first_command")

     if GETSOME == "command" :
        listCMS()
        unlock("help")
     elif GETSOME == "atsp":
        clearT()
        intro()
        unlock("forgot")
     elif GETSOME == "hello":
        print(f"{Fore.LIGHTGREEN_EX}Hello World.")
        unlock("helloword")
     elif GETSOME == "clear":
        clearT()
        unlock("clear")
     elif GETSOME == "command progress":
        
        total = len(achievements)
        unlocked = sum(1 for a in achievements if achievements[a]["unlocked"])

        precent = int((unlocked / total)* 100)

        print(f"{Fore.CYAN}Achievement Progress")
        print(f"{unlocked}/{total} unlocked ({precent}%)")

        print(f"{Fore.LIGHTCYAN_EX}--------------------------------")

        for a in achievements:
           status = f"{Fore.GREEN}(OK)" if achievements[a]["unlocked"] else f"{Fore.RED}X"
           print(f"{status} {achievements[a]['name']}")

        print(f"{Fore.LIGHTCYAN_EX}--------------------------------")
     elif GETSOME == "test":
        print(f"{Fore.LIGHTGREEN_EX}test")
        loading()
        print("the test is DONE!")
        unlock("testing")
     elif GETSOME == "command updLog":
        unlock("updLogV")
        Updlog()
     elif GETSOME == "command print":
        print("print text?")
        inputthing = input("INPUT : Text?-->")
        print(f"{Fore.BLUE}print:{Fore.YELLOW}{inputthing}")
        unlock("Print")
     elif GETSOME == "command C":
        print("wat is ts command delete it.")
        unlock("C")
     elif GETSOME == "what 9+10":
        print("21")
        unlock("21")
     elif GETSOME == "command A":
        loading()
        WEB.open_new_tab(ABATAURL)
        unlock("A")
     elif GETSOME == "pigeon":
        loading()
        WEB.open_new_tab(Dr)
        unlock("Dr")
     elif GETSOME == "command load":
        loading()
        unlock("load")
     elif GETSOME == "command sudo":
        print("this is not linux terminal bro")
        unlock("sudo")
     elif GETSOME == "exit":
        unlock("exit")
        break
     elif GETSOME == "kim jong un":
        loading()
        WEB.open_new_tab(KimURL)
        unlock("kim")
     elif GETSOME == "smo 1":
        loading()
        WEB.open_new_tab(Movie1)
        unlock("show")
     elif GETSOME == "smo 2":
        loading()
        WEB.open_new_tab(Movie2)
        unlock("show")
     elif GETSOME == "smo 3":
        loading()
        WEB.open_new_tab(Movie3)
        unlock("show")
     elif GETSOME == "smo 4":
        loading()
        WEB.open_new_tab(Movie4)
        unlock("show")
     elif GETSOME == "command WasteramWeb":
        loading()
        WEB.open_new_tab(Wwebb)
        unlock("Wweb")
     elif GETSOME == "command randomNum":
        num = random.randint(1,100)
        print(f"{Fore.YELLOW}Random Number = {Fore.CYAN}{num}")
        unlock("randomNum")
     elif GETSOME == "command scream":
        loading()
        WEB.open_new_tab(scream)
        unlock("scream")
     elif GETSOME == "command R":
        loading()
        WEB.open_new_tab(fun)
        unlock("R")
     elif GETSOME == "command Hate":
        loading()
        WEB.open_new_tab(hateURL)
        unlock("hate")
     elif GETSOME == "command profile":
         unlock("profile")

         current_session = int(time.time() - session_start)
         total_time = play_time + current_session

         total = len(achievements)
         unlocked = sum(1 for a in achievements if achievements[a]["unlocked"])

         print(f"{Fore.CYAN}------ PROFILE ------")
         print(f"Play Time: {formatTime(total_time)}")
         print(f"Achievements: {unlocked}/{total}")
         print(f"{Fore.CYAN}---------------------")
     elif GETSOME == "squidward yell":
        loading()
        WEB.open_new_tab(yell)
        unlock("yell")
     elif GETSOME == "burger":
        loading()
        WEB.open_new_tab(burgerURL)
        unlock("burger")
     elif GETSOME == "homero":
        loading()
        WEB.open_new_tab(homeroURL)
        unlock("homer")
     elif GETSOME == "Holy OS?":
        loading()
        peakOS()
        WEB.open_new_tab(peakOSURL)
        unlock("Holy")
     elif GETSOME == "command plusNum":
        num1 = input("NUM =? > ")
        num2 = input("NUM2 =? > ")

        if num1.isdigit() and num2.isdigit():
         total = int(num1) + int(num2)
         print(f"{num1}+{num2}={total}")

         unlock("math")
        else:
         print("NO LETTER")
        
     elif GETSOME == "command minusNum":
        num1 = input("NUM =? >")
        num2 = input("NUM2 =? >")

        if num1.isdigit() and num2.isdigit():
           total = int(num1) - int(num2)
           print(f"{num1}-{num2}={total}")

           unlock("math")
        else:
           print("NO LETER")
     elif GETSOME == "command divNum":
        num1 = input("NUM =? >")
        num2 = input("NUM2 =? >")

        if num2 == "0":
           print("Cannot divide by zero.")
        elif num1.isdigit() and num2.isdigit():
           total = int(num1) / int(num2)
           print(f"{num1}/{num2}={total}")

           unlock("math")
        else:
           print("NO LETER")
     elif GETSOME == "command mutiNum":
        num1 = input("NUM =? >")
        num2 = input("NUM2 =? >")

        if num1.isdigit() and num2.isdigit():
           total = int(num1) * int(num2)
           print(f"{num1}x{num2}={total}")

           unlock("math")
        else:
           print("NO LETER")
     elif GETSOME.startswith("command install"):
        parts = GETSOME.split()

        if len(parts) < 3:
             print("Install what?")
        else:
           app = parts[2].lower()
           if app in installed_apps:
              if installed_apps[app]:
                 print("Already installed.")
              else:
                 print(f"Installing {app}...")
                 loading()
                 installed_apps[app] = True
                 saveData()
                 print(f"{app} installed successfully!")
                 unlock("appI")
           else:
              print("Unknown app.")
     elif GETSOME.startswith("command Enter"):
        parts = GETSOME.split()

        if len(parts) < 3:
            print("Enter what?")
        else:
            app = parts[2].lower()

            if app in installed_apps and installed_apps[app]:
               if app == "solna":
                  print(f"{Fore.CYAN}Entering SolnaMOS...")
                  loading()
                  clearT()
                  SolnaMDOS()
                  if name == None:
                     nameEnter = input("EnterYourName>")
                     name = nameEnter
                     saveData()
                  solnaMain()
               elif app == "testing":
                  print("Opening testing (test)")
               elif app == "minigame":
                  print("Opening minigame...")
                  loading()
                  clearT()
                  gameApp()
            else:
               print("You don't have this app installed.")

     elif GETSOME == "command draw":
        commandDrawList()
        unlock("draw")
     elif GETSOME == "command draw cabbit":
        loading()
        cabbit()
        unlock("cabbit")
     elif GETSOME == "command draw earth":
        loading()
        earth()
        unlock("world")
     elif GETSOME == "command draw Solna":
        loading()
        Solna()
        unlock("Solna")
     elif GETSOME == "command draw Wasteram":
        loading()
        Wasteram()
        unlock("logoW")
     else:
        unlock("Error_command")
        print(f"{Fore.RED}What is this command bro")
        print(f"{Fore.RED}say Enter command for list of command")