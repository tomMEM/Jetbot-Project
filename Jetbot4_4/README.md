# Collection of hints to use the DOCKER Jetbot4.4

## 1) Issue at jetbot repository: #328
  If you use HDMI-nano and keyboard directly on nano you might get "tegra-i2c 7000c400.i2c: no acknowledge from address 0x3c" as an error message.
  If you use PC SSH terminal over Wifi to nano then this message does not appear.
  You have to activate the i2c protocol in this terminal or HDMI/keyboard to have i2c outside the docker container - now i2c is running only in       the Docker container. More hints for i2c here: https://www.jetsonhacks.com/2019/07/22/jetson-nano-using-i2c/
  
## 2) Issue at jetbot repository: #320
1.	Install Putty or any SSH terminal software on your PC and set for example 192.168.55.1 port 22 in case of jetson-Nano Micro USB to PC USB connection
  * a) The SSH terminal will be necessary for reboot or shutdown of the nano, it can remain open on the PC together with juptyer lab in the browser later (in this case use the WiFi IP e.g. 192.168.?.? port 22).
2.	In the terminal window on the PC, when first time start, use login jetbot, password jetbot and start with sudo nmcli device wifi list, then sudo nmcli device wifi connect e.g.HomeNet password e.g.HomeNet
3.	sudo reboot
4.	in browser: to juptyer lab using MICRO USB to PC USB (192.168. 55.1:8888/lab?) or WIFI address (192.168.?.?:8888/lab?)
In case of modification attempts of the notebooks:
5.	in cd jetbot/jetbot or cd jetbot/notebooks you might try to change scripts.
6.	To activate these changes rebuild those into a new container using local changes according tread #319, or same container #296 (jetbot issues)
7.	The build of the new container is going to download all libraries again, so it takes space and time.
8.	Disable old container (jupyter lab in browser will close) and enable new container with ./enable $HOME (in cd jetbot/docker)

## 3) Other ways to modify files within the docker container without rebuild of docker image
Follow: https://phoenixnap.com/kb/how-to-commit-changes-to-docker-image
for example: the Jetbot container is active and running
then (not tested yet):
in a SSH terminal try:  
1. sudo docker images  #get ImageID
2. docker exec -it e.g.ImageID /bin/bash
* modify some docker container files
* Commit Changes to Image
3. exit
4. sudo docker ps -a 
5. sudo docker commit [CONTAINER_ID] [new_image_name] 
* Example: sudo docker commit deddd39fa163 ubuntu-nmap 
6. sudo docker images  
7. run the new image as a docker container

