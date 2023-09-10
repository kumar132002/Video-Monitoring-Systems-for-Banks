# Video-Monitoring-Systems-for-Banks
The system identifies any tampering of cameras, count of the people in the bank, entering the bank &amp; exiting the bank and feedback of customers/client.The proposed system should run on top of the existing CCTV footage.
The final basic UI developed using Tkinter is as follows


![image](https://github.com/kumar132002/Video-Monitoring-Systems-for-Banks/assets/105906512/e82fc3c8-5910-45f3-aa01-3b8fef0af252)

When each of the button is clicked the corresponding detection is shown.
The feedback analysis is based on the Facial Emotion Recognition for the 3 classes happy,sad and neutral.
Tampering of cameras is found using BackgroundSeperatorMOG2() of CV2 library
Count of People identifies the people as object and tracks the coordinates to be moven front or back,for POC the video in mp4 format is linked for further use can be linked with Live feed.

Pull the repository ,Install the dependencies and run the app.py for running the Video Monitoring System for Banks.
