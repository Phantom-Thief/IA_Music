import glob
import os

def concatenate(path):
    for i in glob.glob(path +"/*.csv"):
        cmd = 'copy final.csv+'+i+' final.csv'
        os.system(cmd)

concatenate(".")