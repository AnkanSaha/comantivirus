import os
import pyautogui as p
from antivirus_Functions.App_scanning import *
from antivirus_Functions.Full_scanning import *

# scanning 
def antivirus(authenticationresult):
    if authenticationresult == 'Authentication failed':
                print(authenticationresult)
    elif authenticationresult == 'Confirmed':
        print('Scanning Starting after few steps')
        scan_Type = p.confirm('Choose Scanning Type', buttons=['App Scanning', 'Full scanning'])
    if scan_Type == 'App Scanning':
            print(scan_Type)
            AppScanning.App_scanning(scan_Type)
    if scan_Type == 'Full scanning':
        FullScanning.Full_Scannings(scan_Type)