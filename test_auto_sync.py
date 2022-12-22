from auto_sync_redo import create_new_folder, filter_file_time_created, extract_pc_time_date, multiply, store_directory
import os

def test_create_new_folder():
    assert create_new_folder("sppo123") == "sppo123"
    


def test_filter_file_time_created():
    #assert filter_file_time_created( os.listdir(r'/home/kitwei/golfcar/ftp/recorded_bags/20221222/default'), "22", "5", r'/home/kitwei/golfcar/ftp/recorded_bags/20221222/default')[0] == 3
    assert filter_file_time_created( store_directory( extract_pc_time_date()[0]) [1], 
                                                extract_pc_time_date()[1],
                                                "6",
                                                store_directory( extract_pc_time_date()[0]) [0]) == 3

def test_extract_pc_time():
    assert extract_pc_time_date()[0] == str(20221222)


def test_multiply():
    assert multiply(3) == 9


def test_dir():
    assert store_directory("20221222")[0] == r'/home/kitwei/golfcar/ftp/recorded_bags/20221222/default'