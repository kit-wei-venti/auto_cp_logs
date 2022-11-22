import os
import shutil




keyword1 = ".bag"
keyword2 = ".mp4"
#list_file = " "
total_files = 0
files_copied = 0

create_folder = input("Name of folder to create: \n")

directory_ssd = os.getcwd()
#print(directory_ssd)
list_directory_ssd = os.listdir(directory_ssd)

bag_directory = r'/home/kitwei/ftp/recorded_bags'
list_bag_directory = os.listdir(bag_directory)
#print(list_bag_directory)

path = os.path.join(directory_ssd + "/", create_folder)
os.makedirs(path)




for filename in list_bag_directory:
    if filename.endswith('.bag'):   
        total_files = total_files + 1



for filename in list_bag_directory:
    if filename.endswith('.bag'):
        full_directory = path + "/" + filename
        #print(full_directory)

        bag_directory_full = bag_directory + "/" + filename
        #print(bag_directory_full)

        shutil.copy(bag_directory_full, full_directory)
        files_copied = files_copied + 1
        print(str(files_copied) + "/" + str(total_files))




print(os.listdir(path))
print("copy paste done!")