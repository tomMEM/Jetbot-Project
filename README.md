# _Jetbot-Project_
*Jetbot-Project related script*

* Sources: (https://github.com/NVIDIA-AI-IOT/jetbot), (https://github.com/NVIDIA-AI-IOT/jetracer), nvdli-nano
* Hardware: CSI camera, basic 2 Wheel Tracing Robot car chassis, Power Bank 5V 4A (20000 mAh OpponReno), DC Motor+Stepper Feather Wing, 3D Printed Power Bank holder, 64GB  SanDisk Extreme, nano
* Clone with: git clone https://github.com/tomMEM/Jetbot-Project.git or git clone --depth=1 https://github.com/tomMEM/Jetbot-Project.git
* update: 
```
$cd Jetbot-Project     
$git pull origin master
```
in case of troubles 
```
$git pull origin master --allow-unrelated-histories
```

## Contents
* [1) data_collection-Jetbot_Joystick.ipynb](#1-data_collection-jetbot_joystickipynb)
* [2) Object recognition and driving towards it: live_demo-steering_tweak_with_stop.ipynb](#2-object-recognition-and-driving-towards-it-live_demo-steering_tweakipynb-and-trt_object_following_tweak_object_stopipynb)
* [3) Road following: data_collection_joystick_roadfollowing.ipynb and live_demo_roadfollowing_targetdisp.ipynb](#3road-following-scripts-data_collection_joystick_roadfollowingipynb-and-live_demo_roadfollowing_targetdispipynb)
* [4) Jetbot Road following with Anti-collision](#4-jetbot-road-following-with-anti-collision)
* [5) RoadFollowing Jetracer to Jetbot: data collection while driving with joystick control, build TRT and live run](#5-jetracer-to-jetbot-data-collection-while-driving-with-joystick-control-build-of-trt-and-live-run-speed-gain-fixed)
* [6) Adjustments](#6-adjustments)

## 1) data_collection-Jetbot_Joystick.ipynb

* Modified collision_avoidance data collection Notebook from Jetbot GitHub to allow driving and steering using gamepad joystick while image acquisition by gamepad buttons
* Excel file: test and display two different coordinate transformation strategies
* transfer a notebook copy to Notebooks/collision_avoidance/ of the Jetbot SD image installation

### a) Script contains: 
   * Joystick coordinate system transformation: based on user Pedro Werneck (https://electronics.stackexchange.com/questions/19669/algorithm-for-mixing-2-axis-analog-input-to-control-a-differential-motor-drive)   
   * Code in: def steering(x ,y):
   * Gamma, Speed and motoradjustment sliders for tuning  the bot to drive straight, values can be also used for Object following script
   * Display of joystick's left and right engine values
   * Gamepad buttons for image aqcuisition (free, blocked)
   * Graphical buttons of the orginal script remain active and can be used

### b) Issues:
   * Scale range for motors is -1 to 1
   * Gamma value can be between 0.1-4
   * Gamepad: Xbox USB: joystick (controller.axes: x:0 (left-right), y:1 (forward-backward)
   * Image acquisition: button (5: free, 7: blocked)   *
 
## 2) Object recognition and driving towards it: live_demo-steering_tweak.ipynb and TRT_object_following_tweak_object_stop.ipynb

 * TRT_object_following_tweak_object_stop.ipynb: is using "ssd_mobilenet_v2_coco.engine" for object detection and "best_model_trt.pth" for collision_avoidance
 * The TRT script is a few frames per second faster than "live_demo-objectfollowing_tweak_object_stop.ipynb"
 * The time limit is given by the "ssd_mobilenet_v2_coco.engine"
 * Slider for threshold of object reaching: "object_stop_threshold" : 1 is bottom and 0 is top. When object reaches e.g. 0.9 then stop for few frames (slider is beside)
 * If system cannot detect an object for 100 frames (fixed, no slider), then it switches to search mode using "collision_avoidance"
 * Threshold of collision_avoidance is slider "Manu. bloc. threshold" : start with 0.9 (1.1 no collision_avoidance)
 * Object index is activated by changing (up and down) the list

 
 ### Tweak driving towards an Object:
 	*Collision_avoidance is active in this script, and it is activated in case an object is not recognized within 5-10 seconds, the bot will go into search mode for an object 
 	*Possible at high speed towards an stationary object, following a moving object is limited by the 1 s time lag and loss of Object detection (increase number of non-object frame, e.g. 12)
	*Steering(x, y) has been also incorporated into live_demo-steering_tweak.ipynb to tweak steering sensitivity.
	*The first value that needs to be adjusted is the torque of right and left motor to allow the bot going straight (offset value for left e.g. 0.04).
	*At higher speed levels the difference between two wheels becomes lower, thus the motoradjustment_widget.value should be decreased slightly.
	*The center_x value changes were reduced (e.g. center_x/4 worked for non-wide field camera) 
	*Gamma value (to further reduce turning strength) has to be adjusted by turn_gain_widget.value slider (2) 
	*The y-value is fixed by the speed_widget.value.
	*The values dependent upon motors, speed and camera, thus altering y value while driving requires readjustments of other parameters.
	*In case the object is not detected for a number of frames, then the bot stops and is waiting for a successful detection (e.g. wait for 8 frames).
	*Once object is reached the bot stops. Since the time lag is about 1 sec, the bot might crash in the object at higher speed, use soft objects or water bottles (object 44)	


## 3)	Road Following: Scripts data_collection_joystick_roadfollowing.ipynb and live_demo_roadfollowing_targetdisp.ipynb
 -  #### Camera angle should be adjusted to picture mainly the street without large parts of the "horizon".
 -  #### It seems a large number of images is required, >1000, here I tried about 10000 images which took about 24 hours for the training script on the nano at MAX power
 - #### Need to run the training road in both directions, every 100 to 400 images the environment was altered (door, windows, lights) and new objects were placed near the training course
 - #### The idea is to prevent the network to orientate on certain landmarks except road labels (two blue strips)

  * Joystick control to drive during data_collection_road_following
  * The xy coordinates from the driving Joystick (0,1) are taken to image names, however x and y sliders are still possible to use too
  * The image acquisition is initiated with the gamepad button 5 while driving - it can be several times per second especially during turns
  * The calculated xy coordinates can be observed in the camera display of the live_demo_road_following script
  
  - #### The torch2Trt implementation from the Jetbot team greatly enhanced the performance of road following
  * Speed up to 0.7 units are now possible, less wobbling,  (settings for non standard bot: speed 0.77, speed-gain 0.14, kd 0.31 and 0.0 )   
   
  - #### Power Management
  * To reduce the time lag of camera stream processing in the trt script all four CPUs are required 
  * $sudo jetson_clocks is not sufficient to activate. $ sudo nvpmodel -m 0 for 10 W is required
  * The preinstalled $sudo jtop can also be used to activate jetson clocks and CPUs etc..
  * The time lag of display must be below <100 ms. With two CPUs at Max frequency the time lag is about < 2s which does not allow road following at an interesting speed
  * example(click, then download, then open): ![bot-road following link for open bot08-2.mp4](https://github.com/tomMEM/Jetbot-Project/blob/master/Gif_Demo/bot08-2.mp4)
  
  
## 4) Jetbot Road following with Anti-collision
  * "trt-Jetbot-RoadFollowing_with_CollisionRESNet_TRT.ipynb"
  * It requires two TRT models: one model build with "live_demo_resnet18_build_trt.ipynb " from collision_avoidance folder and another one build with "live_demo_build_trt.ipynb" from the roadfollowing folder of the original jetbot repository
  ### For collision_avoidance Jetbot the steps are:
 	*a) data_collection
 	*b) train with train_model_resnet18.ipynb
 	*c) build with live_demo_resnet18_build_trt.ipynb (all scripts in original jetbot collision_avoidance folder)
 	*d) and finally add the TRT model from c to one of our roadfollowing with collision_avoidance folder and right name to the script
  ### For the steering/roadfollowing Jetbot the steps are:
 	*a) data_collection.ipynb
 	*b) train_model.ipynb
 	*c) to convert to TRT live_demo_build_trt.ipynb
 	*d) add to our road following the model and the name to the script
* The collision-avoidance model can be trained for one object (small bottle) or several as "blocked" with "data_collection-collisionavoidance_Jetbot_Joystick.ipynb"
  * Images of road with strips, and object background needs to be collected into "free"
  * The number of background images ("free") can be high, and object (blocked) much less, if the object is a common one (cup, bottle etc).
  * To have the bot stop at a certain distance, images of the object need to be taken at similar distances to the camera
  * If the object is far away from the camera it might be not detected with a high probability score
  * Data for the Road following model have to be created as usual (e.g. "data_collection_joystick_roadfollowing.ipynb")  
  * The object predication threshold can be adjusted with slider (Manu. threshold), and the time of stop with the slider "Manu. time"
  * More complex behavior could be added, for now it is just a pause for some time
  * The Jetracer-2-Jetbot script is similar, however, categories could be added to switch during road following
  * The folder "Classification_Stop_at_RoadFollowing" allows to define behavior according different objects while on the road, which is more functional
  
## 5) Jetracer to Jetbot: data collection while driving with joystick control, build of TRT and live-run (speed gain fixed)
  * only joystick control of bot and clickable display widget for coordinates
  * allows to train for several categories
  * the original jetracer roadfollowing script had this time lag, thus roadfollowing script for Jetbot has been used and modified to use jetracer script for jetbot
  * in directory CategoryRoad_Jetracer_2_Jetbot, the interactive script is for collecting data for specific category (e.g. apex, bottle), need to indicate first cell
  * the other script is to build the TRT model
  * the live_demo_trt_jetracer_categoryModel_for_jetbotl.ipynb is for the free-run
  * models with and without category can be used and run with the jetbot, in case they were created before with Jetbot roadfollowing scripts
  * once category is detected - some to-do functions or behaviours could be added.
  * these scripts do not support Jetracer car control, but could be added, time lag is much less

## 6) Adjustments
* High CPU usage by jetpot_stats.service before 25.08.2020, if jetbot PIOLED display is not installed or used, the new /NVIDIA-AI-IOT/jebot Repository includes the modified service
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
$ sudo -H rm /etc/systemd/system/jetbot_stats.service

#if the service is required again then follow using "SD card from scratch" point 10.
```
* Camera settings in camera.py:
```gst-inspect-1.0 nvarguscamerasrc```

```return 'nvarguscamerasrc sensor-mode=4 awblock=false maxperf=true wbmode=1 exposuretimerange="37000000 37000000" aeantibanding=0 ispdigitalgainrange="8 8" gainrange="8 8" ! video/x-raw(memory:NVMM), width=%d, height=%d, format=(string)NV12, framerate=(fraction)%d/1 ! nvvidconv ! video/x-raw, width=(int)%d, height=(int)%d, format=(string)BGRx ! videoconvert ! appsink' % (```
* modify camera.py in cd /jetbot/jetbot followed by cd ..  and then sudo python3 setup.py install to transfer the modified camera.py to build
* sync notebooks after jetbot pull from home directory (not jetbot), from user nathanperkins issue 240

```rsync -avz jetbot/notebooks/ ~/Notebooks```

