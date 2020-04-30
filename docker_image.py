import os
while True:
	print("""
    ----|-------------------------------------------------|----
\t|\t                                          |
\t|\tWelcome to NHM's Docker Image Console     |
\t|\t                                          |
    ----|-------------------------------------------------|----""")
	print("""
	
	Select one option from the menu
		1- Show all images
		2- Download an image
		3- Remove an image
		4- Go to previous Menu""")
	x=int(input("Enter your choice  : "))
	if x==1:
		os.system("docker images")
		input("Enter to Continue")
	elif x==2:
		image_name=input("Enter image name that you want to download  : ")
		os.system("docker pull {}".format(image_name))
		input("Enter to Continue")
	elif x==3:
		image_name=input("Enter image name that you want to remove  : ")
		os.system("docker image rm {}".format(image_name))
		input("Enter to Continue")
	elif x==4:
		break
	else:
		print("Pls Enter above option only")
		input("Enter to Continue")
	os.system("clear")
