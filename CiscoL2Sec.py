import telnetlib
import sys
from colorama import Fore
import time
import os


sys.stdout.write("\x1b[8;{rows};{cols}t".format(rows=35, cols=170))

def clean():
        os.system('cls' if os.name=='nt' else 'clear')
clean()


def printer(Print):
    for c in Print + '\n':
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(2. / 100)

print ("""


 .d8888b. d8b                        888      .d8888b.  .d8888b.                  
d88P  Y88bY8P                        888     d88P  Y88bd88P  Y88b                 
888    888                           888            888Y88b.                      
888       888.d8888b  .d8888b .d88b. 888          .d88P "Y888b.   .d88b.  .d8888b 
888       88888K     d88P"   d88""88b888      .od888P"     "Y88b.d8P  Y8bd88P"    
888    888888"Y8888b.888     888  888888     d88P"           "88888888888888      
Y88b  d88P888     X88Y88b.   Y88..88P888     888"      Y88b  d88PY8b.    Y88b.    
 "Y8888P" 888 88888P' "Y8888P "Y88P" 88888888888888888  "Y8888P"  "Y8888  "Y8888P 


""")

print ("Welcome To Cisco Layer 2 Security Script")
print ("This Is The Network Security Automation Script For Spoofing Attack Prevention In Cisco Layer 2 Networks")
print ("Developer: AmirHosein Tangsiri Nezhad")
print ("GitHub:https://github.com/AmirHoseinTangsiriNET")
print ("--------------------------------------------------------------------------------------------------------")

#sys.stdout.write("Enter IP address: ")
#sys.stdout.flush()
HostNameOrIP = "127.0.0.1" #Please Instead The Your Switch IP Address Of the "127.0.0.1"
TelnetPortNumber = input("[+]:Please Enter The Telnet Port Number: ")

telnet = telnetlib.Telnet(HostNameOrIP, TelnetPortNumber)

def DynamicArpInspection():
    
    print ("""
         .oo                    o                              o   o              
        .P 8                    8                              8                  
       .P  8 oPYo. .oPYo.       8 odYo. .oPYo. .oPYo. .oPYo.  o8P o8 .oPYo. odYo. 
      oPooo8 8  `' 8    8 ooooo 8 8' `8 Yb..   8    8 8oooo8   8   8 8    8 8' `8 
     .P    8 8     8    8       8 8   8   'Yb. 8    8 8.       8   8 8    8 8   8 
    .P     8 8     8YooP'       8 8   8 `YooP' 8YooP' `Yooo'   8   8 `YooP' 8   8 
   ..:::::....::::8 ....:::::::....::..:.....:8 ....::.....:::..::..:.....:..::..
    :::::::::::::::8 ::::::::::::::::::::::::::8 :::::::::::::::::::::::::::::::::
    :::::::::::::::..::::::::::::::::::::::::::..:::::::::::::::::::::::::::::::::
    """)
    print (Fore.BLUE + "Dynamic Arp Inspection Configurtion Started")
    print (Fore.BLUE + "Please With")
    
#    telnet.write("enable" + "\n")
#    telnet.write("conf t" + "\n")
    telnet.write("ip arp inspection vlan 1-1000" + "\n")
    telnet.write("ip arp inspection validate src-mac dst-mac ip" + "\n")

def DHCPSnooping():
    print(Fore.RED + """
    '||''|.   '||'  '||'   ..|'''.| '||''|.  '  .|'''.|                                     ||                   
     ||   ||   ||    ||  .|'     '   ||   ||    ||..  '  .. ...     ...     ...   ... ...  ...  .. ...     ... . 
     ||    ||  ||''''||  ||          ||...|'     ''|||.   ||  ||  .|  '|. .|  '|.  ||'  ||  ||   ||  ||   || ||  
     ||    ||  ||    ||  '|.      .  ||        .     '||  ||  ||  ||   || ||   ||  ||    |  ||   ||  ||    |''   
    .||...|'  .||.  .||.  ''|....'  .||.       |'....|'  .||. ||.  '|..|'  '|..|'  ||...'  .||. .||. ||.  '||||. 
                                                                               ||                    .|....' 
                                                                              ''''                       
    """)
    print (Fore.RED + "DHCP Snooping Configurtion Started")
    print (Fore.RED + "Please With")
    print (Fore.RED + "----------------------------------")
    telnet.write("enable" + "\n")
    telnet.write("conf t" + "\n")
    telnet.write("ip dhcp snooping" + "\n")
    telnet.write("ip dhcp snooping vlan 1-1000" + "\n")
    telnet.write("ip dhcp snooping information option" + "\n")
    telnet.write("ip dhcp snooping verify mac-address" +  "\n")
    time.sleep(1)
    print (Fore.RED + "End Configurtion")


DHCPSnooping()
print (Fore.RED + "--------------------------------------")
DynamicArpInspection()

printer ("[+]:Settings Completed")
printer ("[+]:DHCP-Snooping: OK")
printer ("[+]Dynamic-Arp-Inspection: OK")
sys.exit()
