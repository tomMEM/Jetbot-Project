# Installation
* the modified scripts are based on https://github.com/NVIDIA-AI-IOT/jetracer, thus first clone that repository and install as they describe
* place the Jetracer-2-Jetbot script in the Jetracer/roadfollowing directory, otherwise it can not find utilis.py etc.
* to try the Jetbot road following TRT model, copy it from the Jetbot/roadfollowing to Jetracer/roadfollowing
* the Jetracer interactive script requires also JetCam and Clickable installation, as NVIDIA-AI-IOT/jetracer describe.

# Installation of clickable gives sometimes problems
* in case previous trials failed, delete the Clickablewidget directory
* and then:
```
cd #reach home directory
sudo apt-get install nodejs-dev node-gyp libssl1.0-dev
sudo apt-get install npm #likely already installed, but it does no harm
git clone https://github.com/jaybdub/jupyter_clickable_image_widget
cd jupyter_clickable_image_widget
git checkout no_typescript
sudo python3 setup.py build #TB modified, takes a long time >30 min
sudo pip3 install -e .
sudo jupyter labextension install js
sudo jupyter lab build
```
# How to use
* interactive_regression_category_datacollection_jetracerforjetbot_joystick: for training and testing, either manually or using Joystick
* live_demo_build_trt_jetracer_categoryModel_for_jetbot: convert the stored model to TRT to increase speed of inference
* “trt_jetracer_categoryModel_for_jetbot_with_stop” is using probability scores for stop (but still not working nicely because of probability values to low)
* trt_jetracer_categoryModel_for_jetbot_with_collision_avoidance_of_jetbot.ipynb: it combines the Jetracer category road following with Jetbot collision_avoidance trained model "best_model_trt.pth" - if collision_avoidance model is not to aggressive, it stops if object (not specific one) is in the way
* please note: not tested yet with "best_model_resnet18.pth"

# General description
* Category can be switched while driving, can be used for object following in case collision_avoidance model is not detecting it
* goal: Change of category alters driving behavior of bot
* Category might be also helpful to use a trained model for a fast switch of models in case of street light condition changes (e.g. night, day) - a more complex version, for experimenting

# Road following 
* Training seems to require less images
* Detection of direction is more stable than using jetbot road following training alone
* Speed up to 0.8, while increasing steering gain and kD

# Object following according category
* Object following is more stable and fast
* Requires choice of category e.g. bottle

# Category dependent behavior change
* trt_jetracer_categoryModel_for_jetbot_with_collision_avoidance_of_jetbot.ipynb
* Script includes category dependent change of behavior (e.g. detection of bottle: stop for 10 to 20 frames)

# Problems: 
* reduction of false positive detection of e.g. bottle.
* using probability of  score.widgets for behavior change, - does not work
* implement threating, or traitlets to have actions outside the camera stream

# Time lag, 
* Sensitive to calculations within the camera stream
* FPS is deceiving, observation of time lag more important to maintain performance and needs to be reduced.
