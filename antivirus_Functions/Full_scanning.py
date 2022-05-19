import pyautogui as p
import os
import time
from antivirus_Functions import *
from antivirus_Functions.token.Fullscan import *


class FullScanning:
    def Full_Scannings(Type_of_Scan):
        confirmation = p.confirm('Sure to start all app scanning ??', buttons=['Start', 'Cancel'])
        print('App Scan '+confirmation+'ing')
        time.sleep(3)
        fULLsCANNER(confirmation)