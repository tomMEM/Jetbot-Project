# Jetbot-Project
Jetbot-Project related script

1) data_collection-Jetbot_Joystick.ipynb

Modified collision_avoidance data collection Notebook from Jetbot GitHub to allow driving and steering using gamepad joystick while image acquisition by gamepad buttons.

Contains: 
	a) Joystick coordinate system transformation
  b) Gamma scaling for motor values
  d) display of joystick and left, right engine values
  c) gamepad buttons for image aqcuisition (free, blocked)
  d) graphical buttons of orginal script remain active

Issues: 

  Notebook has not been clean-up (display repetitions).
  Scale range for motors is -0.5 to 0.5.
  Gamma value can be between 1-4
  Gamepad: Xbox USB: joystick (controller.axes: x:0, y:1)
  Image acquisition: button (5: free, 7: blocked)
  Inital speed restriction by …. transform=lambda x: -x/2) in the fourth cell.
  
  Excel file: test different steering strategies
  
  2) object recognition
