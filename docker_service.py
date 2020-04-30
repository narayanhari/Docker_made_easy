import os
while True:
	print("""
    ----|---------------------------------------------------|----
\t|\t                                            |
\t|\tWelcome to NHM's Docker Service Console     |
\t|\t                                            |
    ----|---------------------------------------------------|----""")
	print("""
	
	Select one option from the menu
		1- Start Docker
		2- Set Docker for Auto start on reboot
		3- Restart Docker
		4- Check Docker Status
		5- Go to previous Menu""")
	x=int(input("Enter your choice  : "))
	if x==1:
		os.system("systemctl start docker")
		print("docker Started")
		input("Enter to Continue")
	elif x==2:
		os.system("setenforce 0")
		os.system("systemctl start docker")
		os.system("systemctl enable docker")
		print("docker enabled for auto start")
		input("Enter to Continue")
	elif x==3:
		os.system("systemctl restart docker")
		print("docker restarted")
		input("Enter to Continue")
	elif x==4:
		os.system("systemctl status docker")
		input("Enter to Continue")
	elif x==5:
		break
	else:
		print("Pls Enter above option only")
		input("Enter to Continue")
	os.system("clear")
