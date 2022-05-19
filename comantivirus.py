import pyautogui as p
import os
from antivirus_Functions.scan import *

def start():
    f=open('antivirus_Functions/token/key.txt')
    key = f.read()
    # authentications
    keys = p.prompt('Please Enter Authenticaton Keys to use services');
    if keys == key:
            p.alert('You are sucessfully authenticated', button='Start Scannig')
            authenticated = 'Confirmed'
            antivirus(authenticated)
    elif keys != key:
            again = p.alert('Sorry ! You entered a wrong key', button='Again Enter key')
            authenticated = 'Authentication failed'
            if again == 'Again Enter key':
                keys = p.prompt('Please Enter Authenticaton Keys to use services');
            if keys == key:
                p.alert('You are sucessfully authenticated', button='Start Scannig')
                authenticated = 'Confirmed'
                antivirus(authenticated)
            elif keys != key:
                p.alert('Sorry ! You entered a wrong key !! run this code again', button='Exit')
                authenticated = 'Authentication failed'