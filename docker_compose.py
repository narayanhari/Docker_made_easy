import os
while True:
	print("""
    ----|----------------------------------------------------------|----
\t|\t                                                   |
\t|\tWelcome to NHM's Docker Docker-compose Console     |
\t|\t                                                   |
    ----|----------------------------------------------------------|----""")
	print("""
	
	Select one option from the menu
		1- Download and install Docker-compose
		2- Create Workspace 
		3- Go to Workspace
		4- Configure Docker-compose file
		5- Run Docker-compose
		6- Go to previous Menu""")
	x=int(input("Enter your choice  : "))
	if x==1:
		os.system('curl -L "https://github.com/docker/compose/releases/download/1.25.5/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose')
		os.system("chmod +x /usr/local/bin/docker-compose")
		input("Enter to Continue")
	elif x==2:
		dir_name=input("Enter directory name of Workspace  : ")
		os.system("mkdir {}".format(dir_name))
		input("Enter to Continue")
	elif x==3:
		dir_name=input("Enter path of Workspace  : ")
		os.chdir(dir_name)
		input("Enter to Continue")
	elif x==4:
		os.system("gedit docker-compose.yml")
		input("Enter to Continue")
	elif x==5:
		os.system("docker-compose up -d")
	elif x==6:
		break
	else:
		print("Pls Enter above option only")
		input("Enter to Continue")
	os.system("clear")

