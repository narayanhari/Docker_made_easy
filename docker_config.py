import os
while True:
	print("""
    ----|--------------------------------------------------|----
\t|\t                                           |
\t|\tWelcome to NHM's Docker Config Console     |
\t|\t                                           |
    ----|--------------------------------------------------|----""")
	print("""
	
	Select one option from the menu
		1- Check if Docker-ce installed in system or not
		2- Check if Docker-ce is in yum repo
		3- to check all available yum repo
		4- to create/edit yum repo
		5- to install docker
		6- Go to previous Menu""")
	x=int(input("Enter your choice  : "))
	if x==1:
		os.system("rpm -q docker-ce")
		input("Enter to Continue")
	elif x==2:
		os.system("yum list docker-ce")
		input("Enter to Continue")
	elif x==3:
		os.system("ls /etc/yum.repos.d")
		input("Enter to Continue")
	elif x==4:
		os.chdir("/etc/yum.repos.d")
		file_name=input("Enter Docker file name  : ")
		os.system("gedit {}.repo".format(file_name))
		input("Enter to Continue")
	elif x==5:
		os.system("yum install docker-ce --nobest -y")
	elif x==6:
		break
	else:
		print("Pls Enter above option only")
		input("Enter to Continue")
	os.system("clear")

