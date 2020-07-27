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


def PortSecurity():
    print ("""
    d8888b.        .d8888. d88888b  .o88b. db    db d8888b. d888888b d888888b db    db 
    88  `8D        88'  YP 88'     d8P  Y8 88    88 88  `8D   `88'   `~~88~~' `8b  d8' 
    88oodD'        `8bo.   88ooooo 8P      88    88 88oobY'    88       88     `8bd8'  
    88~~~   C8888D   `Y8b. 88~~~~~ 8b      88    88 88`8b      88       88       88    
    88             db   8D 88.     Y8b  d8 88b  d88 88 `88.   .88.      88       88    
    88             `8888Y' Y88888P  `Y88P' ~Y8888P' 88   YD Y888888P    YP       YP    
    
    
    
    """)
    Interface = raw_input("Please Enter The Interface For Port Security Configurtion: ")
    print (Fore.RED + "Port Security Configurtion Started")
    print (Fore.RED + "Please With")
    print (Fore.RED + "----------------------------------")
    telnet.write("enable" + "\n")
    telnet.write("conf t" + "\n")
    telnet.write("interface range " + Interface + "\n")
    telnet.write("switchport port-security " + "\n")
    telnet.write("switchport port-security maximum 2" +  "\n")
    telnet.write("end" +  "\n")
    time.sleep(1)
    print (Fore.RED + "End Configurtion")




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

        
        
def StormControlBroatcast():
    print ("""
                                                                             
    .oPYo.   o                       .oPYo.                o               8 
    8        8                       8    8                8               8 
    `Yooo.  o8P oPYo. .oPYo. ooYoYo. 8      .oPYo. odYo.  o8P oPYo. .oPYo. 8 
        `8   8  8  `' 8    8 8' 8  8 8      8    8 8' `8   8  8  `' 8    8 8 
         8   8  8     8    8 8  8  8 8    8 8    8 8   8   8  8     8    8 8 
    `YooP'   8  8     `YooP' 8  8  8 `YooP' `YooP' 8   8   8  8     `YooP' 8 
    :.....:::..:..:::::.....:..:..:..:.....::.....:..::..::..:..:::::.....:..
    :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
    :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
   
    """)
    StromControlInterface = raw_input("Please Enter The Interface For StromControl On BroatCast Traffic: ")
    print (Fore.RED + "Strom Control Configurtion Started")
    print (Fore.RED + "Please With")
    print (Fore.RED + "----------------------------------")
    telnet.write("enable" + "\n")
    telnet.write("conf t" + "\n")
    telnet.write("interface range " + StromControlInterface + "\n")
    telnet.write("storm-control broadcast level " + "\n")
    print ("Storm Control Enabled On BroatCast Traffic")
    
    
    
def StormControlMulticastUnicast():
    GigInterface = raw_input("Please Enter The GigEthernet Interface For Multicast Traffic And Unicast: ")
    if not GigInterface.startswith("gig"):
        print ("[-]Enter The GigEthernet")
        print ("[-]Exited The Script")
        sys.exit()
    telnet.write("enable" + "\n")
    telnet.write("conf t" + "\n")
    telnet.write("interface range " + GigInterface + "\n")
    telnet.write("storm-control multicast level " + "\n")
    telnet.write("storm-control unicast level " + "\n")
    print ("Storm Control Enabled On Multicast Traffic And UnicastTraffic")

        
        
        
def ProtectedPort():
    print ("""
    
     .d8888b. 888       888      8888888b.                888                   888                888 
    d88P  Y88b888   o   888      888   Y88b               888                   888                888 
    Y88b.     888  d8b  888      888    888               888                   888                888 
     "Y888b.  888 d888b 888      888   d88P888d888 .d88b. 888888 .d88b.  .d8888b888888 .d88b.  .d88888 
        "Y88b.888d88888b888      8888888P" 888P"  d88""88b888   d8P  Y8bd88P"   888   d8P  Y8bd88" 888 
          "88888888P Y88888888888888       888    888  888888   88888888888     888   88888888888  888 
    Y88b  d88P8888P   Y8888      888       888    Y88..88PY88b. Y8b.    Y88b.   Y88b. Y8b.    Y88b 888 
     "Y8888P" 888P     Y888      888       888     "Y88P"  "Y888 "Y8888  "Y8888P "Y888 "Y8888  "Y88888 
                                                                                                   
    
    
    
    """)
    InterfaceForProtected = raw_input("Please Enter The Interface For ProtectedPort Configurtion: ")
    
    telnet.write("enable" + "\n")
    telnet.write("conf t" + "\n")
    telnet.write("interface range " + InterfaceForProtected + "\n")
    telnet.write("switchport" + "\n")
    telnet.write("switchport protected " + "\n")
    telnet.write("end" + "\n")
    print ("Enabled Protected Port ")
 


PortSecurity()
DHCPSnooping()
DynamicArpInspection()
StormControlBroatcast()
StormControlMulticastUnicast()
ProtectedPort()



printer ("[+]:Settings Completed")
printer ("[+]:DHCP-Snooping: Yes")
printer ("[+]Dynamic-Arp-Inspection: Yes")
printer ("[+]Port-Security: Yes")
printer ("[+]Strom-Control: Yes")
printer ("[+]ProtectedPort: Yes")
sys.exit()

