import os
import shutil
import time
import sys
import socket
from datetime import datetime


####################################################################################### START OF MAIN FUNCTION ######################################################################################################

def main():
    folder_name = sys.argv[1]
    starting_time = sys.argv[2]

    mainpc_ipaddress = get_mainpc_ip_address("kitwei-strix15")
    extract_apm_no(store_directory( extract_pc_time_date()[0], mainpc_ipaddress) [1] )
    f_name, new_folder_dir, ssd_folder_path_rosbags, ssd_folder_path_can, ssd_folder_path_logs, ssd_folder_path_video, ssd_folder_path_avcs  = create_new_folder(
                                                                                                                                                find_ssd_name_and_dir(),
                                                                                                                                                folder_name, 
                                                                                                                                                extract_apm_no(store_directory( extract_pc_time_date()[0], mainpc_ipaddress) [1] )
                                                                                                                                                )
                            

    print("COPYING IN PROGRESS...\n")
    print("")

    
    bags_copied, no_bags_copied = filter_file_time_created( store_directory( extract_pc_time_date()[0], mainpc_ipaddress) [1], 
                                                extract_pc_time_date()[1],
                                                starting_time,
                                                store_directory( extract_pc_time_date()[0], mainpc_ipaddress) [0], #
                                                ssd_folder_path_rosbags,
                                                extract_pc_time_date()[2]
                                                )
    print(bags_copied)
    print("")

    secondpc_logs_copied, no_secondpc_logs_copied = filter_file_time_created( 
        store_directory( extract_pc_time_date()[0], mainpc_ipaddress) [3], 
                                                extract_pc_time_date()[1],
                                                starting_time,
                                                store_directory( extract_pc_time_date()[0], mainpc_ipaddress) [2], ##
                                                ssd_folder_path_logs,
                                                extract_pc_time_date()[2]
                                                )
    print(secondpc_logs_copied)
    print("")

    video_copied, no_video_copied = filter_file_time_created( store_directory( extract_pc_time_date()[0], mainpc_ipaddress) [5], 
                                                extract_pc_time_date()[1],
                                                starting_time,
                                                store_directory( extract_pc_time_date()[0], mainpc_ipaddress) [4], ###
                                                ssd_folder_path_video,
                                                extract_pc_time_date()[2]
                                                )
    print(video_copied)
    print("")

    mainpc_can_copied, no_mainpc_can_copied = filter_file_time_created( 
        store_directory( extract_pc_time_date()[0], mainpc_ipaddress) [7], 
                                                extract_pc_time_date()[1],
                                                starting_time,
                                                store_directory( extract_pc_time_date()[0], mainpc_ipaddress) [6], ####
                                                ssd_folder_path_can,
                                                extract_pc_time_date()[2]
                                                )
    print(mainpc_can_copied)
    print("")

    secondpc_ftp_logs_copied, no_secondpc_ftp_logs_copied = filter_file_time_created( 
        store_directory( extract_pc_time_date()[0], mainpc_ipaddress) [9], 
                                                extract_pc_time_date()[1],
                                                starting_time,
                                                store_directory( extract_pc_time_date()[0], mainpc_ipaddress) [8], #####
                                                ssd_folder_path_logs,
                                                extract_pc_time_date()[2]
                                                )
    print(secondpc_ftp_logs_copied)
    print("")

    mainpc_logs_copied, no_mainpc_logs_copied = filter_file_time_created( 
        store_directory( extract_pc_time_date()[0], mainpc_ipaddress) [11], 
                                                extract_pc_time_date()[1],
                                                starting_time,
                                                store_directory( extract_pc_time_date()[0], mainpc_ipaddress) [10], ### ###
                                                ssd_folder_path_logs,
                                                extract_pc_time_date()[2]
                                                )
    print(mainpc_logs_copied)
    print("")

    mainpc_ftp_logs_copied, no_mainpc_ftp_logs_copied = filter_file_time_created( 
        store_directory( extract_pc_time_date()[0], mainpc_ipaddress) [13], 
                                                extract_pc_time_date()[1],
                                                starting_time,
                                                store_directory( extract_pc_time_date()[0], mainpc_ipaddress) [12], ### ### #
                                                ssd_folder_path_logs,
                                                extract_pc_time_date()[2]
                                                )
    print(mainpc_ftp_logs_copied)
    print("")

                                                
    mainpc_avcs_copied, no_mainpc_avcs_copied = filter_file_time_created( 
        store_directory( extract_pc_time_date()[0], mainpc_ipaddress) [15], 
                                                extract_pc_time_date()[1],
                                                starting_time,
                                                store_directory( extract_pc_time_date()[0], mainpc_ipaddress) [14],### ### ##
                                                ssd_folder_path_avcs,
                                                extract_pc_time_date()[2]
                                                )
    print(mainpc_avcs_copied)
    print("")

####################################################################################### PRINT TOTAL FILES COPIED ######################################################################################################
    
    print(str(no_bags_copied + no_secondpc_logs_copied + no_video_copied + no_mainpc_can_copied + no_secondpc_ftp_logs_copied + no_mainpc_logs_copied + no_mainpc_ftp_logs_copied + no_mainpc_avcs_copied) + " files copied in total !")


######################################################################################## END OF MAIN FUNCTION #########################################################################################################



def create_new_folder(ssd_directory, f_name, apm_no):
    try:
        # find_ssd_name = r'/media/kitwei'
        # list_find_ssd_name = os.listdir(find_ssd_name)
        # ssd_dir = find_ssd_name + "/" + list_find_ssd_name[0]

        ssd_folder_path = os.path.join(ssd_directory + "/" + f_name)
        os.makedirs(ssd_folder_path)
        new_folder_dir = ssd_directory + "/" + f_name + "/" + apm_no


        ssd_folder_path_rosbags = os.path.join(new_folder_dir + "/", "rosbags" + "/" + "default")
        os.makedirs(ssd_folder_path_rosbags)

        ssd_folder_path_can = os.path.join(new_folder_dir + "/", "can")
        os.makedirs(ssd_folder_path_can)

        ssd_folder_path_logs = os.path.join(new_folder_dir + "/", "logs")
        os.makedirs(ssd_folder_path_logs)

        ssd_folder_path_video = os.path.join(new_folder_dir + "/", "video")
        os.makedirs(ssd_folder_path_video)

        ssd_folder_path_avcs = os.path.join(new_folder_dir + "/", "avcs")
        os.makedirs(ssd_folder_path_avcs)                              
        return f_name, new_folder_dir, ssd_folder_path_rosbags, ssd_folder_path_can, ssd_folder_path_logs, ssd_folder_path_video, ssd_folder_path_avcs

    except ImportError:
        print("import error")

    except IndexError:
        print("did you forgot to enter something?")


def store_directory(folder_date, mainpc_ipaddress):
    bag_directory = r'/home/kitwei/golfcar/ftp/recorded_bags/' + str(folder_date) + r'/default'
    list_bag_directory = os.listdir(bag_directory)

    log_directory = r'/home/kitwei/golfcar/ftp/logs/' + str(folder_date) 
    list_log_directory = os.listdir(log_directory)

    video_directory = r'/home/kitwei/golfcar/ftp/video/' + str(folder_date) 
    list_video_directory = os.listdir(video_directory)

    can_directory = r'/home/kitwei/run/user/1000/gvfs/sftp:host=' + mainpc_ipaddress + r'/home/venti/ftp/can/' + str(folder_date) 
    list_can_directory = os.listdir(can_directory)

    secondpc_ftp_log_directory = r'/home/kitwei/golfcar/ftp'
    list_secondpc_ftp_log_directory = os.listdir(secondpc_ftp_log_directory)

    mainpc_log_directory = r'/home/kitwei/run/user/1000/gvfs/sftp:host=' + mainpc_ipaddress + r'/home/venti/ftp/logs/' + str(folder_date) 
    list_mainpc_log_directory = os.listdir(mainpc_log_directory)

    mainpc_ftp_log_directory = r'/home/kitwei/run/user/1000/gvfs/sftp:host=' + mainpc_ipaddress + r'/home/venti/ftp'
    list_mainpc_ftp_log_directory = os.listdir(mainpc_ftp_log_directory)

    mainpc_avcs_directory = r'/home/kitwei/run/user/1000/gvfs/sftp:host=' + mainpc_ipaddress + r'/home/venti/ftp/avcs/' + str(folder_date) 
    list_mainpc_avcs_directory = os.listdir(mainpc_avcs_directory)

    return bag_directory, list_bag_directory, log_directory, list_log_directory, video_directory, list_video_directory, can_directory, list_can_directory, secondpc_ftp_log_directory, list_secondpc_ftp_log_directory, mainpc_log_directory, list_mainpc_log_directory, mainpc_ftp_log_directory, list_mainpc_ftp_log_directory, mainpc_avcs_directory, list_mainpc_avcs_directory


def extract_pc_time_date():
    currentDateAndTime = datetime.now()
    currentDate = currentDateAndTime.strftime("%d/%m/%Y")
    currentTime = currentDateAndTime.strftime("%H:%M:%S")

    pc_time_split = currentTime.split(":")
    pc_date_split = currentDate.split("/")
    pc_date_correct_format = pc_date_split[2] + pc_date_split[1] + pc_date_split[0]
    pc_extract_date = int(pc_date_split[0])
    return str(pc_date_correct_format), pc_extract_date, pc_time_split[0]


def filter_file_time_created(passindir, passinpcdate, passintimeentered, passindir2, ps_dir, current_hour):
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
            if int(k) == int(passinpcdate) and int(f) >= int(passintimeentered) and int(current_hour) >= int(f):
                no_bag_files += int(1)
                shutil.copy(passindir2 + "/" + filename, ps_dir + "/" + filename)
                filtered_filenames.append(filename)

    return filtered_filenames, int(no_bag_files)


def extract_apm_no(list_bag_directory):
    for filename in list_bag_directory:
        apm_no = filename.split("_")
    return str(apm_no[0])


def get_mainpc_ip_address(hostname):
    IpAddress = socket.gethostbyname(hostname)
    return IpAddress


def find_ssd_name_and_dir():
    find_ssd_name = r'/media/kitwei'
    list_find_ssd_name = os.listdir(find_ssd_name)
    ssd_dir = find_ssd_name + "/" + list_find_ssd_name[0]
    return ssd_dir


def multiply(n):
    return n * n


if __name__ == "__main__":
    main()

