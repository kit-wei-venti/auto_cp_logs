import os
import time
from datetime import datetime


 
# Path to the file/directory
#path = "/home/kitwei/golfcar/ftp/recorded_bags/PSA8374_2022-11-24-10-46-39_1.bag"


starting_time = input("Enter starting time: ")
bag_directory = r'/home/kitwei/golfcar/ftp/recorded_bags'
list_bag_directory = os.listdir(bag_directory)


for filename in list_bag_directory:
    if filename.endswith('.bag'):
         

        # Both the variables would contain time
        # elapsed since EPOCH in float
        ti_c = os.path.getctime(bag_directory + "/" + filename)
        ti_m = os.path.getmtime(bag_directory + "/" + filename)
        
        # Converting the time in seconds to a timestamp
        c_ti = time.ctime(ti_c)    #shows when it was created
        m_ti = time.ctime(ti_m)    #shows when it was modified
        
        x = c_ti.split(" ")
        y = x[3].split(":")
        f = y[0]
        #a = int(starting_time)
        a = int(starting_time)
        #print(list(map(int,y)))
        #if a == b:
            #print("test")
        if a == int(f):
            print(f)
            print(c_ti)
