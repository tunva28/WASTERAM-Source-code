import time
import colorama
import os
from colorama import Fore, Back, Style
colorama.init()
import sys
import webbrowser as WEB
import winsound
import json

spiner = ["|", "/", "-", "\\"]

version = "indev build 732026 1"
versionSol = "indev build 6320261837"

solnaInstalled = False

name = None

# i use ChatGPT 5% for reduce dev time and aslo trying learing form it

## Python Usless_Program.py ts is how to run it in terminal

## MOVIE URL
BradarURL = "https://youtube.com/shorts/gTyaRoxySrE?si=ps7kEeQ1QtQjylpm"
KimURL = "https://www.youtube.com/watch?v=7maE0J9S-T0"
ABATAURL = "https://www.youtube.com/watch?v=EzQiEOQ8nVA"
Movie1 = "https://youtu.be/JreSPMu_VGY?si=zjh5ss8bQCIwix82"
Movie2 = "https://youtu.be/51LMUSVSZHk?si=y8LdeDgvkVGsht6m"
Movie3 = "https://youtu.be/lB7spjbwaGI?si=9xkE0_5lsO-jp3BY"
Movie4 = "https://youtu.be/BYx2JCCt2Ss?si=YXUzJ_WAVaA2iMw5"
Peak1 = "https://www.youtube.com/watch?v=7fzMxxyklTw"
scream = "https://www.youtube.com/watch?v=ykGB4zu7gTc"
fun = "https://www.youtube.com/watch?v=GtL1huin9EE"
yell = "https://www.youtube.com/watch?v=-5R_sviyV4Y"
peakOSURL = "https://www.youtube.com/watch?v=hmjU-6tkEc8"
burgerURL = "https://www.youtube.com/shorts/SxtsnWjD_UA"
homeroURL = "https://youtu.be/miO75CbTuJ4?si=qK9vzf22AvFpshEC"
hateURL = "https://youtu.be/acAfItR04l4?si=K6IIJ6S59Ygb46xW"

## achievements
achievements = {
    "first_command": {"name": "First Command Bradar", "unlocked": False},
    "helloword": {"name": "Hello WORLD!", "unlocked": False},
    "help": {"name": "HELP!", "unlocked": False},
    "exit": {"name": "goodbye !", "unlocked": False},
    "testing": {"name": "testing testing", "unlocked": False},
    "21": {"name": "YOU STUPID!", "unlocked": False},
    "clear": {"name": "clear!", "unlocked": False},
    "Bradar": {"name": "BRADAR WHAT IS THIS", "unlocked": False},
    "forgot": {"name": "what is this program name again?", "unlocked": False},
    "kim": {"name": "kim jong un approve", "unlocked": False},
    "cd": {"name": "SONIC CD", "unlocked": False},
    "yell": {"name": "YELL", "unlocked": False},
    "burger": {"name": "IM SORRY, DID HE JUST SAY THAT HIS LAST NAME... IS BURGER?", "unlocked": False},
    "homer": {"name": "HOMERO VAS A RECOLTALTE", "unlocked": False},
    "A": {"name": "that one DJ remix thing", "unlocked": False},
    "C": {"name": "useless command bradar", "unlocked": False},
    "R": {"name": "R letter", "unlocked": False},
    "Print": {"name": "Print TEXT", "unlocked": False},
    "load": {"name": "loading for what?", "unlocked": False},
    "scream": {"name": "scream", "unlocked": False},
    "math": {"name": "math!", "unlocked": False},
    "draw": {"name": "IT CAN DRAW TOO?", "unlocked": False},
    "solnaMOSI": {"name": "installed solnaMOS!", "unlocked": False},
    "use solna": {"name": "welcome to Solna MOS", "unlocked": False},
    "hate": {"name": "h a t e", "unlocked": False},
    "cabbit": {"name": "Cabbit", "unlocked": False},
    "show": {"name": "1920", "unlocked": False},
    "Holy": {"name": "Temple OS", "unlocked": False},
}

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
      saveAchment()

def saveAchment():
   with open("achievements.json", "w") as f:
      json.dump(achievements, f)

def loadAcgment():
   global achievements
   try:
      with open("achievements.json", "r") as f:
         achievements = json.load(f)
   except:
      saveAchment()

def intro():
   print(f"{Fore.CYAN}Welcome to")
   print(f"""{Fore.RED}
 █████   ███   █████   █████████    █████████  ███████████ ██████████ ███████████     █████████   ██████   ██████
░░███   ░███  ░░███   ███░░░░░███  ███░░░░░███░█░░░███░░░█░░███░░░░░█░░███░░░░░███   ███░░░░░███ ░░██████ ██████ 
 ░███   ░███   ░███  ░███    ░███ ░███    ░░░ ░   ░███  ░  ░███  █ ░  ░███    ░███  ░███    ░███  ░███░█████░███ 
 ░███   ░███   ░███  ░███████████ ░░█████████     ░███     ░██████    ░██████████   ░███████████  ░███░░███ ░███ 
 ░░███  █████  ███   ░███░░░░░███  ░░░░░░░░███    ░███     ░███░░█    ░███░░░░░███  ░███░░░░░███  ░███ ░░░  ░███ 
  ░░░█████░█████░    ░███    ░███  ███    ░███    ░███     ░███ ░   █ ░███    ░███  ░███    ░███  ░███      ░███ 
    ░░███ ░░███      █████   █████░░█████████     █████    ██████████ █████   █████ █████   █████ █████     █████
     ░░░   ░░░      ░░░░░   ░░░░░  ░░░░░░░░░     ░░░░░    ░░░░░░░░░░ ░░░░░   ░░░░░ ░░░░░   ░░░░░ ░░░░░     ░░░░░ 
                                                                                                                 
         stupid Game
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
   print(f"\nDone {Fore.CYAN}Bradar!")

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
   print("> Bradar")
   print("> kim jong un")
   print("> SONIC CD")
   print("> squidward yell")
   print("> burger")
   print("> homero")
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
   print("> command print")
   print("> command load")
   print("> command scream")
   print("> command plusNum > Only Two Number")
   print("> command minusNum > Only Two Number")
   print("> command draw >show drawing list")
   print("> command progress > achievements list ")
   print("> command install > install thing ")
   print("> command Enter > Enter thing ")
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
   print("-------------------------------")

def solnaMain():

   while True:
      User = input(f"{Fore.LIGHTBLUE_EX}SolnaMOS/{name}>")

      if User == "exit":
         break
      if User == "help":
         print("> exit")

## Main

loadAcgment()

clearT()

intro()
print("say Enter command for list of command bardar")
print(f"{Fore.LIGHTYELLOW_EX}^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")

while True:
     GETSOME = input(f"{Fore.GREEN}hello bradar Plz Enter something bradar=>")
     unlock("first_command")

     if GETSOME == "command" :
        listCMS()
        unlock("help")
     elif GETSOME == "atsp":
        clearT()
        intro()
        unlock("forgot")
     elif GETSOME == "hello":
        print(f"{Fore.LIGHTGREEN_EX}Hello World bradar.")
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
        print("the test is DONE bradar!")
        unlock("testing")
     elif GETSOME == "command print":
        print("print text?")
        inputthing = input("INPUT : Text?-->")
        print(f"{Fore.BLUE}print:{Fore.YELLOW}{inputthing}")
        unlock("Print")
     elif GETSOME == "command C":
        print("wat is ts command bradar delete it.")
        unlock("C")
     elif GETSOME == "what 9+10":
        print("21 bradar")
        unlock("21")
     elif GETSOME == "Bradar":
        loading()
        WEB.open_new_tab(BradarURL)
        unlock("Bradar")
     elif GETSOME == "command A":
        loading()
        WEB.open_new_tab(ABATAURL)
        unlock("A")
     elif GETSOME == "command load":
        loading()
        unlock("load")
     elif GETSOME == "exit":
        unlock("exit")
        break
     elif GETSOME == "kim jong un":
        loading()
        WEB.open_new_tab(KimURL)
        unlock("kim")
     elif GETSOME == "SONIC CD":
        loading()
        WEB.open_new_tab(Peak1)
        unlock("cd")
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
         print("NO LETTER BRADAR")
        
     elif GETSOME == "command minusNum":
        num1 = input("NUM =? >")
        num2 = input("NUM2 =? >")

        if num1.isdigit() and num2.isdigit():
           total = int(num1) - int(num2)
           print(f"{num1}-{num2}={total}")

           unlock("math")
        else:
           print("NO LETER BRADAR")
     elif GETSOME == "command install solnaMOS":
        if solnaInstalled == False:
          loading()
          SolnaMDOS()
          solnaInstalled = True
          unlock("solnaMOSI")
        else:
           print(f"{Fore.RED}alrealy install Bradar")

     elif GETSOME == "command Enter solnaMOS":
        loading()
        unlock("use solna")
        if solnaInstalled == True:
           clearT()
           SolnaMDOS()
           if name == None:
               nameEnter = input("EnterYourName>")
               name = nameEnter
           solnaMain()
        else:
           print(f"{Fore.RED}where is solna")
     elif GETSOME == "command draw":
        commandDrawList()
        unlock("draw")
     elif GETSOME == "command draw cabbit":
        loading()
        cabbit()
        unlock("cabbit")
     else:
        print(f"{Fore.RED}Bradar What is this command Bradar")
        print(f"{Fore.RED}say Enter command for list of command bardar")