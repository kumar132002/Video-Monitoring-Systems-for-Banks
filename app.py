from easygui import *
import os
from PIL import Image, ImageTk
from itertools import count
import tkinter as tk
import string
#import selecting
# obtain audio from the microphone

#func()
while 1:
  image   = "bank.png"
  msg="                             VIDEO MONITORING SYSTEM FOR BANKS"
  choices = ["Tampering Detection","Count the people","Sentiment Analysis"]
  reply   = buttonbox(msg,image=image,choices=choices)
  if reply ==choices[0]:
        from tampering_camera import cap
  if reply == choices[2]: 
        from feedback_recognition import cap
  if reply==choices[1]:
       from count_of_people import cap
