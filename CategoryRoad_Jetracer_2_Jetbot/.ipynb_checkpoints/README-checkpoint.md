# How to use
* interactive_regression_category_datacollection_jetracerforjetbot_joystick: for training and testing, either manually or using Joystick
* live_demo_build_trt_jetracer_categoryModel_for_jetbot: convert the stored model to TRT to increase speed of inference
* live_demo_trt_jetracer_categoryModel_for_jetbotl: Can use the model from jebot road following training or jetracer interactive training
* live_demo_trt_jetracer_categoryModel_for_jetbot_with_stop_and_timeseries_Display: extended version of previous one with category behavior and time series display

# General description
* Category can be switched while driving
* Change of category alters driving behavior of bot
* Category might be also helpful to use a trained model for a fast switch of models in case of street light condition changes (e.g. night, day)
* Prediction.value is used in one of the last scripts to change behavior in case a e.g. bottle is on the road (live_demo_trt_jetracer_categoryModel_for_jetbot_with_stop_and_timeseries_Display)

# Road following 
* Training seems to require less images
* Detection of direction is more stable than using jetbot road following training alone
* Speed up to 0.8, while increasing steering gain and kD

# Object following according category
* Object following is more stable and fast
* Requires choice of category e.g. bottle

# Category dependent behavior change
* live_demo_trt_jetracer_categoryModel_for_jetbot_with_stop_and_timeseries_Display.ipynb
* Script includes category dependent change of behavior (e.g. detection of bottle: backward driving for 10 to 20 frames)
* Includes "jupyterplot" (need to be installed or deactivated with #) to display some time series values: it takes some time to initialize, but does not affect much the timing of the camera stream

# Problems: 
* complex behavior change without affecting Camera stream, and reduction of false positive detection of e.g. bottle.
* using probability of  score.widgets for behavior change
* implement threating, or traitlets to have actions outside the camera stream

# Time lag, 
* Sensitive to calculations within the camera stream
* FPS is deceiving, observation of time lag more important to maintain performance and needs to be reduced.

# Jupyterplot
* can be installed for display of time series values




