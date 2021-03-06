
# How to run
* It is recommended to run the script using Wi-Fi mode
* Connection directly to HDMI display and keyboard/mouse requires too many resources and it might lead to system crashes or error messages that inflate syslog (check /var/log)
* To prevent syslog build-up (can reach Max SD card space e.g. 35 GiB) deactivate rsyslog service with 

"""
'''
    $sudo service rsyslog stop
    $sudo systemctl disable rsyslog.service
    $cd /var/log
    $sudo rm syslog
    $sudo truncate –s 0 *
    $sudo systemctl status rsyslog  
'''

"""



* Make sure using $top in the terminal window that sufficient resources are available (no zombie processes, about 20-38micros Cup, disk space (df) at least 20% free)
* Only python, jupyter, nvargus should occupy CPU (10-90%)
* Memory build up is also happen at the host computer, thus monitor host computer with Resource monitor (Windows) – mainly because of video stream rendering.
* Edge is sometimes writing into /blob_storage – no idea how to prevent


# Installation

* The modified scripts are based on https://github.com/NVIDIA-AI-IOT/jetracer, thus first clone that repository and install as they describe
* place the folder with all files in the Jetracer/roadfollowing directory (it might also work out of Jetbot-Project folder, in case jetracer and jetbot repositories were installed)
* To try the Jetbot road following TRT model, copy it from the Jetbot/roadfollowing to this folder
* The 1_datacollection... script is used to collect images for the four classes and to train a model, and also to test if objects are recognized
* The model will be saved as "classification_behavior_model.pth"
* use 2_load_build_2_TRT_classification_model.ipynb to convert into TRT and save as "trt_classification_behavior_model.pth"
* 3_roadfollowing_classification_behavior.ipynb is the live run of the classification and road following

# 3 script
* since the sliders are creating a time lag, they have been removed. They can be activated again by removing the #.
* the thresholds and behaviour need to be adjusted at the last major cell in the two LISTs - the order of the values is according  Categories

# Training of classes
* First take background images (everything that should not be detected as object) - start with 40 images
* collect for every class with the corresponding background some images e.g. 40
* train with 5 epoch, evaluate, and live test
* if in live test objects not recognized or wrongly, just take more images, and train, evaluate and test
* Some classes might be easier to train then others
* Because no distance check, train the objects in a distance to the camera that should give a block signal
* It takes some time and might need more than 500 images at the end
* Augmentation could be added later to enhance specificity of the detection

# Control of driving and behavior
* the second to last category can be adjusted by pause time and detection threshold
* it is manually by editing the list in the last main cell
"""
'''
----------------------------------------------------------------------------------------------------------------------------------------
stop_time=[10,100,150,1] ----------------------------pause number of about number of frames * 0.05 s
second_category_threshold=[0.0,0.1,0.1,0.1]----------threshold per category 

for category bottle give short time, so it will start to run once bottle is remove
for other category it will wait for some time, even the object has been removed
-------------------------------------------------------------------------------------------------------------------------
'''
"""
* sliders under block threshold control pause activity - speed (0), turning, 



