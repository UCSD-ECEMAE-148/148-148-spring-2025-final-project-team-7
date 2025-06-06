Overview
- We promised to build an autonomous robot that can detect a predefined open parallel parking spot in real time using camera input, then plan and execute a forward/reverse parking maneuver without human control.
  - Other than telling the car to do forward/reverse parallel parking, the car must move entirely on its own.
  - Use both cameras for object detection (OAK-D for spot detection, rear camera for collision detection
  -  “collision detection” only detects the inner bounds of the designated blue spot when reverse parking
 
Nice to Have:
- LiDAR integration for further collision detection
- Testing our implementation of  collision detection with 2 car chassis
 

Final Slides:
 - https://docs.google.com/presentation/d/13PX9E5gsUsDH-hQndY35sVaeM-fLZfGM4H_qzhaS2d8/edit?slide=id.g3615553ebbd_0_3#slide=id.g3615553ebbd_0_3

Results:
  - Able to park in the spot successfully! Could scale up the functionality of the car, but due to time constraints and part malfunctions, this is as much as we could do.

How to replicated:
 - Install all the libraries, such as opencv-python, pyvesc, dpethai, etc (check files for other files needed)
 - Edit the values in the align_to_spot.py, forward_park.py and parallel_park.py to work for your configuration (also control_values.py)
 - Use camera debug to create an hsv mask to detect the spot using the oakd lite
 - run python3 parallel_park.py
 - All good to go!


Thanks to Profsesor Jack and TA Alex for helping us!
