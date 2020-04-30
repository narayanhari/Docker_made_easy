import os
while True:
	print("""
    ----|-----------------------------------------------------|----
\t|\t                                              |
\t|\tWelcome to NHM's Docker Container Console     |
\t|\t                                              |
    ----|-----------------------------------------------------|----""")
	print("""
	
	Select one option from the menu
		1- Show running Containers
		2- Show all Containers
		3- Create a container and attach
		4- Remove a container
		5- Remove all container
		6- Start a container
		7- Attach to an container
		8- Inspect an container
		9- Go to previous Menu""")
	x=int(input("Enter your choice  : "))
	if x==1:
		os.system("docker ps")
		input("Enter to Continue")
	elif x==2:
		os.system("docker ps -a")
		input("Enter to Continue")
	elif x==3:
		cont_name=input("Enter container name that you want to launch  : ")
		image_name=input("Which image you want to use : ")
		vol_name=input("which volume and where you want to attach(volume:path) : ")
		net_name=input("Enter network that you want to assosiate this  : ")
		os.system("docker run -it --name {} --network {} -v {} {}".format(cont_name,net_name,vol_name,image_name))
		input("Enter to Continue")
	elif x==4:
		cont_name=input("Enter container name that you want to remove : ")
		os.system("docker rm {}".format(cont_name))
		input("Enter to Continue")
	elif x==5:
		os.system("docker rm -f $(docker ps -aq)")
		input("Enter to Continue")
	elif x==6:
		cont_name=input("Enter container name that you want to start  : ")
		os.system("docker start {}".format(cont_name))
		input("Enter to Continue")
	elif x==7:
		cont_name=input("Enter container name that you want to attach  : ")
		os.system("docker attach {}".format(cont_name))
		input("Enter to Continue")
	elif x==8:
		cont_name=input("Enter container name that you want to inspect  : ")
		os.system("docker inspect {}".format(cont_name))
		input("Enter to Continue")
	elif x==9:
		break
	else:
		print("Pls Enter above option only")
		input("Enter to Continue")
	os.system("clear")
