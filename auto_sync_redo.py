import os
import shutil
import time
import sys
from datetime import datetime



def main():
    folder_name = sys.argv[1]
    starting_time = sys.argv[2]

    create_new_folder(folder_name)
    print(create_new_folder)

    #pass pc date into functions
    #store_directory( extract_pc_time_date() [0])
    
    #count the no of bag files we wanna copy
    filter_file_time_created( store_directory( extract_pc_time_date()[0]) [1], 
                                                extract_pc_time_date()[1],
                                                starting_time,
                                                store_directory( extract_pc_time_date()[0]) [0])

    print(filter_file_time_created( store_directory( extract_pc_time_date()[0]) [1], 
                                                extract_pc_time_date()[1],
                                                starting_time,
                                                store_directory( extract_pc_time_date()[0]) [0]))    

def create_new_folder(f_name):
    try:
        ssd_dir = os.getcwd()
        ssd_dir_ls = os.listdir(ssd_dir)
        ssd_folder_path = os.path.join(ssd_dir + "/", f_name)
        os.makedirs(ssd_folder_path)
        return f_name

    except ImportError:
        print("import error")

    except IndexError:
        print("did you forgot to enter something?")

def store_directory(folder_date):
    bag_directory = r'/home/kitwei/golfcar/ftp/recorded_bags/' + str(folder_date) + r'/default'
    list_bag_directory = os.listdir(bag_directory)

    return bag_directory, list_bag_directory


def extract_pc_time_date():
    currentDateAndTime = datetime.now()
    currentDate = currentDateAndTime.strftime("%d/%m/%Y")
    pc_date_split = currentDate.split("/")
    pc_date_correct_format = pc_date_split[2] + pc_date_split[1] + pc_date_split[0]
    pc_extract_date = int(pc_date_split[0])
    return str(pc_date_correct_format), pc_extract_date


def filter_file_time_created(passindir, passinpcdate, passintimeentered, passindir2):
    no_bag_files = 0

    for filename in passindir:
        ti_c = os.path.getctime(passindir2 + "/" + filename)
        c_ti = time.ctime(ti_c)    #shows when it was created
        x = c_ti.split()
        y = x[3].split(":")
        f = y[0]
        k = x[2]
        if int(k) == int(passinpcdate) and int(f) >= int(passintimeentered):
            no_bag_files += int(1)

    return no_bag_files


def copy_file():
    



def multiply(n):
    return n * n


if __name__ == "__main__":
    main()
