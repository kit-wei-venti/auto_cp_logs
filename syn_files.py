import os
import shutil
import time
from datetime import datetime



keyword1 = ".bag"
keyword2 = ".mp4"
#list_file = " "
no_bag_files = 0
no_txt_files = 0
total_files = 0
files_copied = 0

create_folder = input("Name of folder to create: \n")
starting_time = input("starting time: ")

directory_ssd = os.getcwd()
#print(directory_ssd)
list_directory_ssd = os.listdir(directory_ssd)

bag_directory = r'/home/kitwei/golfcar/ftp/recorded_bags'
list_bag_directory = os.listdir(bag_directory)
#print(list_bag_directory)

chinese_txt_directory = r'/home/kitwei/venti/ftp'                                  #chinese txt files
list_chinese_txt_directory = os.listdir(chinese_txt_directory)

path = os.path.join(directory_ssd + "/", create_folder)
os.makedirs(path)


currentDateAndTime = datetime.now()
currentTime = currentDateAndTime.strftime("%H:%M:%S")
currentDate = currentDateAndTime.strftime("%d/%m/%Y")
pc_date_split = currentDate.split("/")
pc_extract_date = int(pc_date_split[0])

############################################################################################################################################################################################################### FUNCTIONS ######################################################################################################################################################################################################################








############################################################################################################################################################################################################### COUNT FILES ####################################################################################################################################################################################################################

for filename in list_bag_directory:
    if filename.endswith('.bag'):   
             # Both the variables would contain time
        # elapsed since EPOCH in float
        ti_c = os.path.getctime(bag_directory + "/" + filename)
        ti_m = os.path.getmtime(bag_directory + "/" + filename)
        
        # Converting the time in seconds to a timestamp
        c_ti = time.ctime(ti_c)    #shows when it was created
        m_ti = time.ctime(ti_m)    #shows when it was modified
        
        x = c_ti.split()
        y = x[3].split(":")
        f = y[0]
        k = x[2]
        #a = int(starting_time)
        a = int(starting_time)


        #if a == int(f):
        if int(k) == pc_extract_date and int(f) >= a:
            no_bag_files = no_bag_files + 1
            #print(no_bag_files)
            total_files = no_bag_files + no_txt_files

for filename in list_chinese_txt_directory:
    if filename.endswith('txt'):
        ti_c = os.path.getctime(chinese_txt_directory + "/" + filename)
        ti_m = os.path.getmtime(chinese_txt_directory + "/" + filename)
        
        # Converting the time in seconds to a timestamp
        c_ti = time.ctime(ti_c)    #shows when it was created
        m_ti = time.ctime(ti_m)    #shows when it was modified
        
        x = c_ti.split()
        y = x[3].split(":")
        f = y[0]
        k = x[2]
        #a = int(starting_time)
        a = int(starting_time)

        if int(k) == pc_extract_date and int(f) >= a:
            no_txt_files = no_txt_files + 1
            total_files = no_bag_files + no_txt_files
            


####################################################################COUNT FILES#################################################################################





for filename in list_chinese_txt_directory:
    if filename.endswith('.txt'):
        ti_c = os.path.getctime(chinese_txt_directory + "/" + filename)
        ti_m = os.path.getmtime(chinese_txt_directory + "/" + filename)

        c_ti = time.ctime(ti_c)    #shows when it was created
        m_ti = time.ctime(ti_m)    #shows when it was modified
        
        x = c_ti.split()
        y = x[3].split(":")
        f = y[0]
        k = x[2]
        a = int(starting_time)

        if int(k) == pc_extract_date and int(f) >= a:

            full_directory = path + "/" + filename
            chinese_txt_directory_full = chinese_txt_directory + "/" + filename
            shutil.copy(chinese_txt_directory_full, full_directory)
            files_copied = files_copied + 1
            print(str(files_copied) + "/" + str(total_files))


for filename in list_bag_directory:
    if filename.endswith('.bag'):


         # Both the variables would contain time
        # elapsed since EPOCH in float
        ti_c = os.path.getctime(bag_directory + "/" + filename)
        ti_m = os.path.getmtime(bag_directory + "/" + filename)
        
        # Converting the time in seconds to a timestamp
        c_ti = time.ctime(ti_c)    #shows when it was created
        m_ti = time.ctime(ti_m)    #shows when it was modified
        
        x = c_ti.split()
        y = x[3].split(":")
        f = y[0]
        k = x[2]
        a = int(starting_time)


        #if a == int(f):
        if int(k) == pc_extract_date and int(f) >= a:
            #no_bag_files = no_bag_files + 1
            full_directory = path + "/" + filename
            #print(full_directory)

            bag_directory_full = bag_directory + "/" + filename
            #print(bag_directory_full)

            shutil.copy(bag_directory_full, full_directory)
            files_copied = files_copied + 1
            print(str(files_copied) + "/" + str(total_files))

            
            #print("testing")


print(os.listdir(path))
print("copy paste done!")


