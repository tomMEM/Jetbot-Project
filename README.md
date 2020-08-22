# _Jetbot-Project_
*Jetbot-Project related script*

* Sources: (https://github.com/NVIDIA-AI-IOT/jetbot)


## Contents
* [1) data_collection-Jetbot_Joystick.ipynb](#script)
* [2) Object recognition: live_demo-steering_tweak.ipynb](#recognition)
* [3) Adjustments](#adjusts)

## 1) data_collection-Jetbot_Joystick.ipynb

* Modified collision_avoidance data collection Notebook from Jetbot GitHub to allow driving and steering using gamepad joystick while image acquisition by gamepad buttons
* Excel file: test and display two different coordinate transformation strategies
* transfer a notebook copy to Notebooks/collision_avoidance/ of the Jetbot SD image installation

### a) Script contains: 
   * Joystick coordinate system transformation: based on user Pedro Werneck (https://electronics.stackexchange.com/questions/19669/algorithm-for-mixing-2-axis-analog-input-to-control-a-differential-motor-drive)
   * Gamma scaling for motor values
   * display of joystick,  left and right engine values
   * gamepad buttons for image aqcuisition (free, blocked)
   * graphical buttons of orginal script remain active

### b) Issues:
   * Scale range for motors is -0.5 to 0.5
   * Gamma value can be between 1-4
   * Gamepad: Xbox USB: joystick (controller.axes: x:0, y:1)
   * Image acquisition: button (5: free, 7: blocked)
   * Inital speed restriction by …. transform=lambda x: -x/2) in the fourth cell 
 
 ## 2) Object recognition: live_demo-steering_tweak.ipyn
 ### Goal: reduce time lag
 ### Tweak driving towards an Object
	*Steering(x, y) has been also incorporated into live_demo-steering_tweak.ipynb to tweak steering sensitivity.
	*The first value that needs to be adjusted is the torque of right and left motor to allow the bot going straight (offset value for left e.g. 0.04).
	*Then reduce the center_x value (no widefiled camera) e.g. center_x/4 and use a gamma value to further reduce turning strength. The y-value is fixed by speed_widget.value. The values dependent upon motors, speed and camera - takes some trial and error to tweak. Needs a formula.
	*In case the object is not detected for a some frames, then the bot stops and is waiting for a successful detection (e.g. wait for 8 frames).
	*Once object is reached or not detected for >8 frames the bot stops.
	*Collision_avoidance is not active in this script
	
## 3) Adjustments
* High CPU usage by jetpot_stats.service if jetbot OLED display is not installed or used
** Solution:
```
#check if jetbot_stats.service is in the folder 
$ cd /etc/systemd/system/
$ ls
#stop service
$ systemctl stop jetbot_stats #start service in case: systemctl start jebot_stats
#remove from starting at boot up
$ systemctl disable jetbot_stats
#delete the file
$ rm /etc/systemd/system/jetbot_stats.service

#if the service is required again then follow using "SD card from scratch" point 10.
```
