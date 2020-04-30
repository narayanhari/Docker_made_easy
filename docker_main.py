import os
while True:
	print("""
    ----|-------------------------------------------|----
\t|\t                                    |
\t|\tWelcome to NHM's Docker Console     |
\t|\t                                    |
    ----|-------------------------------------------|----""")
	print("""
	
	Select one option from the menu
		1- Docker Installation Setup
		2- Docker service Command
		3- Docker Image Commands
		4- Docker Container Commands
		5- Docker Volume Commands
		6- Docker-Compose Commands
		7- Exit""")
	x=int(input("Enter your choice  : "))
	if x==1:
		os.system("clear")
		os.system("python3 docker_config.py")
	elif x==2:
		os.system("clear")
		os.system("python3 docker_service.py")
	elif x==3:
		os.system("clear")
		os.system("python3 docker_image.py")
		input("Enter to Continue")
	elif x==4:
		os.system("clear")
		os.system("python3 docker_container.py")
		input("Enter to Continue")
	elif x==5:
		os.system("clear")
		os.system("python3 docker_volume.py")
		input("Enter to Continue")
	elif x==6:
		os.system("clear")
		os.system("python3 docker_compose.py")
		input("Enter to Continue")
	elif x==7:
		break
	else:
		print("Pls Enter above option only")
		input("Enter to Continue")
	os.system("clear")

