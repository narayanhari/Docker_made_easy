# Docker_Made_Easy
This project is created to make life easy with Docker. As Docker command are little hard to remember,  I have created an TUI Application which ask user what to do, and internally it will execute the same thing.


## Tech Stack that used

I have made this on the top of RHEL8, so it required RHEL8 or similar one like centos:8 to run. Also script is written in Python3
Technology used-

 - Docker
 - RHEL8 (RedHat 8)
 - Python 3

## Program Architecture
To start the program run-
**`Python3 docker_main.py`**
This file will show a menu from which you can select where to go.

 1. **docker_images.py:-** This file contains all image related command
 2. **docker_container.py:-** this file contains all container related command
 3. **docker_config.py:-** this file contains docker initial setup configuration commands
 4. **docker_services.py:-** this file contains service related command for docker
 5. **docker_volume.py:-** this file contains all storage related command
 6. **docker_compose.py:-** this file contains setup of docker-compose and other docker-compose commands

