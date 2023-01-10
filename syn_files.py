import os
import shutil
import time
import sys
from datetime import datetime



def main():
    folder_name = sys.argv[1]
    starting_time = sys.argv[2]
    extract_apm_no(store_directory( extract_pc_time_date()[0]) [1] )
    f_name, new_folder_dir, ssd_folder_path_rosbags, ssd_folder_path_can, ssd_folder_path_logs, ssd_folder_path_video  = create_new_folder(
                                                                                                                        folder_name, 
                                                                                                                        extract_apm_no(store_directory( extract_pc_time_date()[0]) [1] )
                                                                                                                        )
 

    print("COPYING IN PROGRESS...\n")
    
    #create_new_folder(folder_name)
    #print(create_new_folder)

    #pass pc date into functions
    #store_directory( extract_pc_time_date() [0])
    
    #count the no of bag files we wanna copy
    filter_file_time_created( store_directory( extract_pc_time_date()[0]) [1], 
                                                extract_pc_time_date()[1],
                                                starting_time,
                                                store_directory( extract_pc_time_date()[0]) [0],
                                                ssd_folder_path_rosbags
                                                )
    
    print(filter_file_time_created( store_directory( extract_pc_time_date()[0]) [1], 
                                                extract_pc_time_date()[1],
                                                starting_time,
                                                store_directory( extract_pc_time_date()[0]) [0],
                                                ssd_folder_path_rosbags
                                                )
                                                )    
    ###############################################################################################                                            
    filter_file_time_created( store_directory( extract_pc_time_date()[0]) [3], 
                                                extract_pc_time_date()[1],
                                                starting_time,
                                                store_directory( extract_pc_time_date()[0]) [2],
                                                ssd_folder_path_logs
                                                )

    print(filter_file_time_created( store_directory( extract_pc_time_date()[0]) [3], 
                                                extract_pc_time_date()[1],
                                                starting_time,
                                                store_directory( extract_pc_time_date()[0]) [2],
                                                ssd_folder_path_logs
                                                )
                                                )
    ###############################################################################################
    filter_file_time_created( store_directory( extract_pc_time_date()[0]) [5], 
                                                extract_pc_time_date()[1],
                                                starting_time,
                                                store_directory( extract_pc_time_date()[0]) [4],
                                                ssd_folder_path_video
                                                )
    
    print(filter_file_time_created( store_directory( extract_pc_time_date()[0]) [5], 
                                                extract_pc_time_date()[1],
                                                starting_time,
                                                store_directory( extract_pc_time_date()[0]) [4],
                                                ssd_folder_path_video
                                                )
                                                )
    ############################################################################################
    filter_file_time_created( store_directory( extract_pc_time_date()[0]) [7], 
                                                extract_pc_time_date()[1],
                                                starting_time,
                                                store_directory( extract_pc_time_date()[0]) [6],
                                                ssd_folder_path_can
                                                )
    
    print(filter_file_time_created( store_directory( extract_pc_time_date()[0]) [7], 
                                                extract_pc_time_date()[1],
                                                starting_time,
                                                store_directory( extract_pc_time_date()[0]) [6],
                                                ssd_folder_path_can
                                                )
                                                )
    ############################################################################################
    filter_file_time_created( store_directory( extract_pc_time_date()[0]) [9], 
                                                extract_pc_time_date()[1],
                                                starting_time,
                                                store_directory( extract_pc_time_date()[0]) [8],
                                                ssd_folder_path_logs
                                                )
    
    print(filter_file_time_created( store_directory( extract_pc_time_date()[0]) [9], 
                                                extract_pc_time_date()[1],
                                                starting_time,
                                                store_directory( extract_pc_time_date()[0]) [8],
                                                ssd_folder_path_logs
                                                )
                                                )
    ###############################################################################################
    filter_file_time_created( store_directory( extract_pc_time_date()[0]) [11], 
                                                extract_pc_time_date()[1],
                                                starting_time,
                                                store_directory( extract_pc_time_date()[0]) [10],
                                                ssd_folder_path_logs
                                                )

    print(filter_file_time_created( store_directory( extract_pc_time_date()[0]) [11], 
                                                extract_pc_time_date()[1],
                                                starting_time,
                                                store_directory( extract_pc_time_date()[0]) [10],
                                                ssd_folder_path_logs
                                                )
                                                )
    #############################################################################################
    filter_file_time_created( store_directory( extract_pc_time_date()[0]) [13], 
                                                extract_pc_time_date()[1],
                                                starting_time,
                                                store_directory( extract_pc_time_date()[0]) [12],
                                                ssd_folder_path_logs
                                                )

    print(filter_file_time_created( store_directory( extract_pc_time_date()[0]) [13], 
                                                extract_pc_time_date()[1],
                                                starting_time,
                                                store_directory( extract_pc_time_date()[0]) [12],
                                                ssd_folder_path_logs
                                                )
                                                )
    ##############################################################################################
    filter_file_time_created( store_directory( extract_pc_time_date()[0]) [15], 
                                                extract_pc_time_date()[1],
                                                starting_time,
                                                store_directory( extract_pc_time_date()[0]) [14],
                                                ssd_folder_path_logs
                                                )

    print(filter_file_time_created( store_directory( extract_pc_time_date()[0]) [15], 
                                                extract_pc_time_date()[1],
                                                starting_time,
                                                store_directory( extract_pc_time_date()[0]) [14],
                                                ssd_folder_path_logs
                                                )
                                                )

##############################################                               END OF MAIN FUNC                          ##########################################








    
    






def create_new_folder(f_name, apm_no):
    try:
        ssd_dir = os.getcwd()
        ssd_dir_ls = os.listdir(ssd_dir)
        ssd_folder_path = os.path.join(ssd_dir + "/", f_name)
        os.makedirs(ssd_folder_path)
        new_folder_dir = ssd_dir + "/" + f_name + "/" + apm_no

        ssd_folder_path_rosbags = os.path.join(new_folder_dir + "/", "rosbags" + "/" + "default")
        os.makedirs(ssd_folder_path_rosbags)

        ssd_folder_path_can = os.path.join(new_folder_dir + "/", "can")
        os.makedirs(ssd_folder_path_can)

        ssd_folder_path_logs = os.path.join(new_folder_dir + "/", "logs")
        os.makedirs(ssd_folder_path_logs)

        ssd_folder_path_video = os.path.join(new_folder_dir + "/", "video")
        os.makedirs(ssd_folder_path_video)

        return f_name, new_folder_dir, ssd_folder_path_rosbags, ssd_folder_path_can, ssd_folder_path_logs, ssd_folder_path_video

    except ImportError:
        print("import error")

    except IndexError:
        print("did you forgot to enter something?")


def store_directory(folder_date):
    bag_directory = r'/home/kitwei/golfcar/ftp/recorded_bags/' + str(folder_date) + r'/default'
    list_bag_directory = os.listdir(bag_directory)

    log_directory = r'/home/kitwei/golfcar/ftp/logs/' + str(folder_date) 
    list_log_directory = os.listdir(log_directory)

    video_directory = r'/home/kitwei/golfcar/ftp/video/' + str(folder_date) 
    list_video_directory = os.listdir(video_directory)

    can_directory = r'/home/kitwei/run/user/1000/gvfs/sftp:host=192.168.1.10/home/venti/ftp/can/' + str(folder_date) 
    list_can_directory = os.listdir(can_directory)

    secondpc_ftp_log_directory = r'/home/kitwei/golfcar/ftp'
    list_secondpc_ftp_log_directory = os.listdir(secondpc_ftp_log_directory)

    mainpc_log_directory = r'/home/kitwei/run/user/1000/gvfs/sftp:host=192.168.1.10/home/venti/ftp/logs/' + str(folder_date) 
    list_mainpc_log_directory = os.listdir(mainpc_log_directory)

    mainpc_ftp_log_directory = r'/home/kitwei/run/user/1000/gvfs/sftp:host=192.168.1.10/home/venti/ftp'
    list_mainpc_ftp_log_directory = os.listdir(mainpc_ftp_log_directory)

    mainpc_avcs_directory = r'/home/kitwei/run/user/1000/gvfs/sftp:host=192.168.1.10/home/venti/ftp/avcs/' + str(folder_date) 
    list_mainpc_avcs_directory = os.listdir(mainpc_avcs_directory)

    return bag_directory, list_bag_directory, log_directory, list_log_directory, video_directory, list_video_directory, can_directory, list_can_directory, secondpc_ftp_log_directory, list_secondpc_ftp_log_directory, mainpc_log_directory, list_mainpc_log_directory, mainpc_ftp_log_directory, list_mainpc_ftp_log_directory, mainpc_avcs_directory, list_mainpc_avcs_directory


def extract_pc_time_date():
    currentDateAndTime = datetime.now()
    currentDate = currentDateAndTime.strftime("%d/%m/%Y")
    pc_date_split = currentDate.split("/")
    pc_date_correct_format = pc_date_split[2] + pc_date_split[1] + pc_date_split[0]
    pc_extract_date = int(pc_date_split[0])
    return str(pc_date_correct_format), pc_extract_date


def filter_file_time_created(passindir, passinpcdate, passintimeentered, passindir2, ps_dir):
    no_bag_files = 0
    filtered_filenames = []
    for filename in passindir:
        if os.path.isfile(os.path.join(passindir2 + "/", filename)):
            ti_m = os.path.getmtime(passindir2 + "/" + filename)
            m_ti = time.ctime(ti_m)    #shows when it was created
            x = m_ti.split()
            y = x[3].split(":")
            f = y[0]
            k = x[2]
            if int(k) == int(passinpcdate) and int(f) >= int(passintimeentered):
                no_bag_files += int(1)
                shutil.copy(passindir2 + "/" + filename, ps_dir + "/" + filename)
                filtered_filenames.append(filename)

    return filtered_filenames, str(no_bag_files) + "files"


def extract_apm_no(list_bag_directory):
    for filename in list_bag_directory:
        apm_no = filename.split("_")
    return str(apm_no[0])


def multiply(n):
    return n * n


if __name__ == "__main__":
    main()
