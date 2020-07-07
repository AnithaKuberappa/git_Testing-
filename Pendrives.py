import string
from ctypes import windll
import time
import os,sys

def get_drives():
    drives = []
    bitmask = windll.kernel32.GetLogicalDrives()

    for letter in string.ascii_uppercase:
        if bitmask & 1:
            drives.append(letter)
        bitmask >>= 1
    return drives


if __name__ == '__main__':
    before = set(get_drives())
    pause = input("Please insert the USB device, then press ENTER")
    print ('Please wait...')
    time.sleep(5)
    after = set(get_drives())
    drives = after - before
    delta = len(drives)
    print(delta)
    deltalist=["D:\\","E:\\","F:\\"]
       #if delta
       

    # delta=os.listdir(path="E:\\")
    # print(delta)

    # delta=os.listdir('.')
    # delta=os.listdir(path="D:\\")
    # print(delta)
    # delta=os.listdir('.')


    # print(delta)

if (delta):
    for drive in drives:
        print(drive)
    if os.system("cd " + str(drive) + ":"):
        newly_mounted = drive
        print ("There were %d drives added: %s. Newly mounted drive letter is %s" % (delta, drives, newly_mounted))
else:
    print ("Sorry, I couldn't find any newly mounted drives.")



