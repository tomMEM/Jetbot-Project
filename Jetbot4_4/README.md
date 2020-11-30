# Collection of hints to use the DOCKER Jetbot4.4
## 1) Modifications of workspace file and copy to docker container /opt/jetbot/
 * Based on the SD image Jetbot4 Docker. 
 * The workspace is linked to the outside of the docker (home/jetbot), so changes there will remain, in case the docker container is restarted from the docker image.
 * After changes of files in /workspace/jetbot/.... :
 * a) Change files (e.g. motor and robot.py) under cd /workspace/jetbot/jetbot in jupyterlab, or copy my two files into this folder
 * b) from a terminal window in Jupyter lab copy the files to docker container in opt/jetbot/jetbot with:
 * cp /workspace/jetbot/jetbot/motor.py /opt/jetbot/jetbot/motor.py
 * c) cp /workspace/jetbot/jetbot/robot.py /opt/jetbot/jetbot/robot.py
 * d) cd /opt/jetbot/
 * e) python3 setup.py install
 * Restart kernel and start e.g. 4Wheels_basic_motion.ipyn from /workspace/jetbot/notebooks/ in jupyter lab. Here you can also change the notebooks as you like, they do not need   to be copied to /opt/jetbot/.

  *In case Docker container gets rebuild the changes remain in /workspace/jetbot/ but not in the docker container, thus modified files need to be copied back to opt/jetbot/...   followed with python3 setup.py install out of cd /opt/jetbot

## 2) jetbot-042_nano-4gb-jp441.zip (at jetbot.org) 
 * model = model.to(device) or model = model.cuda().eval() #.half() are not running #330
 * looks like some user solved it by using image jetbot-041_nano-4gb-jp441.zip

## 3) Issue at jetbot repository: #328
  If you use HDMI-nano and keyboard directly on nano you might get "tegra-i2c 7000c400.i2c: no acknowledge from address 0x3c" as an error message.
  If you use PC SSH terminal over Wifi to nano then this message does not appear.
  You have to activate the i2c protocol in this terminal or HDMI/keyboard to have i2c outside the docker container - now i2c is running only in       the Docker container. More hints for i2c here: https://www.jetsonhacks.com/2019/07/22/jetson-nano-using-i2c/
  
## 4) Issue at jetbot repository: #320
1.	Install Putty or any SSH terminal software on your PC and set for example 192.168.55.1 port 22 in case of jetson-Nano Micro USB to PC USB connection
  * a) The SSH terminal will be necessary for reboot or shutdown of the nano, it can remain open on the PC together with juptyer lab in the browser later (in this case use the WiFi IP e.g. 192.168.?.? port 22).
2.	In the terminal window on the PC, when first time start, use login jetbot, password jetbot and start with sudo nmcli device wifi list, then sudo nmcli device wifi connect e.g.HomeNet password e.g.HomeNet
3.	sudo reboot
4.	in browser: to juptyer lab using MICRO USB to PC USB (192.168. 55.1:8888/lab?) or WIFI address (192.168.?.?:8888/lab?)
In case of modification attempts of the notebooks:
5.	in cd jetbot/jetbot or cd jetbot/notebooks you might try to change scripts. As long only notebooks scripts are changed a rebuild is not required, only in case of jetbot/jetbot files.
6.	To make jetbot/jetbot files permanent rebuild those into a new container using local changes according tread #319, or same container #296 (jetbot issues)
7.	The build of the new container is going to download all libraries again, so it takes space and time, so better just use the approach described under headline 1.
8.	Disable old container (jupyter lab in browser will close) and enable new container with ./enable $HOME (in cd jetbot/docker)

## 5) Other ways to modify files within the docker container without rebuild of docker image
Follow: https://phoenixnap.com/kb/how-to-commit-changes-to-docker-image


