# Scripts are for Jetbot to allow road following and object specific actions (Stop, backward drive, time settings)
### * A similar approach can be found in "https://github.com/abuelgasimsaadeldin/Jetbot-Road-Following-and-Collision-Avoidance" 

## General notes:
* A connection of the nano directly to HDMI display and keyboard/mouse requires too many resources and might lead to system crashes or error messages that inflate syslog (check /var/log)
* However, to prevent syslog build-up at the nano (can reach Max SD card space e.g. 35 GiB) deactivate rsyslog service with 

```
    $sudo service rsyslog stop
    $sudo systemctl disable rsyslog.service
    $cd /var/log
    $sudo rm syslog
    $sudo truncate –s 0 *
    $sudo systemctl status rsyslog  
```



* Make sure using $top in the terminal window that sufficient resources are available (about 20-38micros Cp, disk space (df) at least 20% free)
* Only python, jupyter, nvargus should occupy CPU (10-90%)
* Memory build up is also happen at the host computer, thus monitor host computer with Resource monitor (Windows) – mainly because of video stream rendering (some json webpack troubles).
* After a sudo apt-get update, sudo apt-get dist-upgrade and using chrome as a browser the Memory build-up at the PC is less but still obvious

# Installation of the scripts

* The modified scripts are based on https://github.com/NVIDIA-AI-IOT/jetbot, thus first clone that repository and install as they describe
* Place the folder with all files in the Jetracer/roadfollowing directory (it might also work out of Jetbot-Project folder, in case jetracer and jetbot repositories were installed)
* To try the Jetbot road following TRT model, copy it from the Jetbot/roadfollowing to this folder, which can be in Jetbot/roadfollowing/Classification_Stop
* The 1_datacollection... script is used to collect images for the four classes (the first class needs to be background/free) and to train a model, and also to test if objects are recognized
* The model will be saved as "classification_behavior_model.pth"
* Use 2_load_build_2_TRT_classification_model.ipynb to convert into TRT and save as "trt_classification_behavior_model.pth"
* 3_roadfollowing_classification_behavior.ipynb is the live run of the classification and road following

# 3 script
* Since the sliders are creating a time lag, they have been removed. They can be re-activated again by removing the #.
* The thresholds and behaviour need to be adjusted at the last major cell in the two LISTs - the order of the values is according  Categories

# Training of classes
* First take background images (everything that should not be detected as object) - start with 40 images
* Collect for every class with the corresponding background some images e.g. 40
* Train with 5 epoch, evaluate, and live test
* If in live test objects not recognized or wrongly, just take more images, and train, evaluate and test
* Some classes might be easier to train than others
* Since there is no distance check, the objects might be trained in a distance to the camera that should give a block signal
* Finally run the training for about 30 epochs at Max and sudo jetson_clocks settings of the nano - the training still might need some hours
* It is recommended to run robot.stop(), and camera.stop() before to avoid memory build up by the video stream
* At the end of the training session the model needs to be saved manually

# Control of driving and behavior
* The main threshold of detection is controlled by the Manu. Thresh. slider. In case the threshold has been reached the script checks the secondary class threshold.
* The thresholds and pause times of the second to last category can be fine-tuned and adjusted manually by editing the two lists (see below) in the last main cell
* Other sliders can be used to apply a backward drive speed and an angle in case an object has been detected


```
----------------------------------------------------------------------------------------------------------------------------------------
stop_time=[10,100,150,1] ----------------------------pause: number of frames * ~ 0.05 s
second_category_threshold=[0.0,0.4,0.7,0.4]----------threshold per category, less sensitivity at larger values Max 1 
Background/free should be always the first category---------threshold is set by Manu thresh slider, if threshold has been reached the secondary thresholds are used to decide
If one of the secondary classes is not well trained and always above 0.7-1, then set it to 1.1 in the second_category_threshold .e.g. [0.0,0.4,0.7,1.4], 
This class will be not used for decision - further training of the model, including data acquistion might be required to prevent false-positive detection in that particular class. It might be also helpful to collect some images of the background/foreground of the object, without the object into the 1st background/free class.

e.g.
for category bottle: give short time, so it will start to run once bottle is remove
for other category it will wait for some time, even the object has been removed
-------------------------------------------------------------------------------------------------------------------------
```




