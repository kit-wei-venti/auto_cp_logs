from syn_files import create_new_folder, filter_file_time_created, extract_pc_time_date, multiply, store_directory, extract_apm_no
import os


def test_create_new_folder():
    assert create_new_folder("igg")[0] == "igg"
    assert create_new_folder("ma_de")[1] == "/media/kitwei/Extreme SSD/ma_de"


def test_filter_file_time_created():
    #assert filter_file_time_created( os.listdir(r'/home/kitwei/golfcar/ftp/recorded_bags/20221222/default'), "22", "5", r'/home/kitwei/golfcar/ftp/recorded_bags/20221222/default')[0] == 3
    assert filter_file_time_created( store_directory( extract_pc_time_date()[0]) [1], 
                                                extract_pc_time_date()[1],
                                                "6",
                                                store_directory( extract_pc_time_date()[0]) [0]) == 1

def test_extract_pc_time():
    assert extract_pc_time_date()[0] == str(20230108)


def test_multiply():
    assert multiply(3) == 9


def test_dir():
    assert store_directory("20230108")[0] == r'/home/kitwei/golfcar/ftp/recorded_bags/20230108/default'


def test_apm_no():
    assert extract_apm_no(list_bag_directory = os.listdir(r'/home/kitwei/golfcar/ftp/recorded_bags/20230110/default')) == "PSA8374"


