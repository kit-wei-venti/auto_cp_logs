import os
import shutil




keyword = ".bag"
list_file = " "
total_files = 0
files_copied = 0

create_folder = input("Name of folder to create: \n")

directory = os.getcwd()
list_file = os.listdir(directory)


#adding the r converts the normal string to a raw string
destination_dir = r'/home/kitwei/Downloads'     #change this according to ur thumbdrive directory
path = os.path.join(destination_dir + "/", create_folder)
os.makedirs(path)

for filename in list_file:
    if keyword in filename:
        total_files = total_files + 1




for filename in list_file:
    if keyword in filename:
        files_copied = files_copied + 1
        full_directory = directory + "/" + filename
        destination_dir_cpfile = path + "/" + filename
        #print(destination_dir_cpfile)
        shutil.copy(full_directory, destination_dir_cpfile)
        print(str(files_copied) + "/" + str(total_files))
        #print(os.listdir(destination_dir))
            
        #os.listdir returns everyth in a file

        #print(count)
        





print(os.listdir(path))
print("copy paste done!")




