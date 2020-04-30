import os
while True:
	print("""
    ----|--------------------------------------------------|----
\t|\t                                           |
\t|\tWelcome to NHM's Docker Volume Console     |
\t|\t                                           |
    ----|--------------------------------------------------|----""")
	print("""
	
	Select one option from the menu
		1- Show all Storage
		2- create a Storage
		3- Remove a Storage
		4- Inspect an Volume 
		5- Go to previous Menu""")
	x=int(input("Enter your choice  : "))
	if x==1:
		os.system("docker volume ls")
		input("Enter to Continue")
	elif x==2:
		volume_name=input("Enter Storage name that you want to create  : ")
		os.system("docker volume create {}".format(volume_name))
		input("Enter to Continue")
	elif x==3:
		image_name=input("Enter Storage name that you want to remove  : ")
		os.system("docker volume rm {}".format(volume_name))
		input("Enter to Continue")
	elif x==4:
		volume_name=input("Enter Storage name that you want to inspect  : ")
		os.system("docker inspect {}".format(volume_name))
		input("Enter to Continue")
	elif x==5:
		break
	else:
		print("Pls Enter above option only")
		input("Enter to Continue")
	os.system("clear")
