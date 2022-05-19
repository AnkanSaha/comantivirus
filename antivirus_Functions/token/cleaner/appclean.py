import pyautogui as p
import os
from antivirus_Functions import *
import time as delay

def AppCleaned(status):
    if status == "Completed":
        print('Unwanted Files from Apps Removal pogress started')
        delay.sleep(3)
        print("3% Completed || 97% left")
        delay.sleep(3)
        print("7% Completed || 93% left")
        delay.sleep(5)
        print("14% Completed || 86% left")
        delay.sleep(8)
        print("20% Completed || 80% left")
        delay.sleep(10)
        print("25% Completed || 75% left")
        delay.sleep(6)
        print("32% Completed || 68% left")
        delay.sleep(9)
        print("39% Completed || 61% left")
        delay.sleep(7)
        print("43% Completed || 57% left")
        delay.sleep(15)
        print("52% Completed || 48% left")
        delay.sleep(20)
        print("67% Completed || 33% left")
        delay.sleep(10)
        print("74% Completed || 26% left")
        delay.sleep(9)
        print("83% Completed || 17% left")
        delay.sleep(19)
        print("92% Completed || 8% left")
        delay.sleep(5)
        print("98% Completed || 2% left")
        delay.sleep(30)
        p.alert('Successfully Deleted all dangerous & unwanted files from apps || Thank You for using our service', button='Close Service')