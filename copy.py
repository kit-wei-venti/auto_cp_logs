import os
import shutil




keyword = ".pdf"
list_file = " "

directory = os.getcwd()
list_file = os.listdir(directory)

for filename in list_file:
    if keyword in filename:
        print(filename)
        full_directory = directory + "/" + filename
        #print(full_directory)

        #adding the r converts the normal string to a raw string
        destination_dir = r'D:\cppycode'
        destination_dir_cpfile = destination_dir + "/" + filename
        #print(destination_dir_cpfile)
        shutil.copy(full_directory, destination_dir_cpfile)

        print(os.listdir(destination_dir))
        
        #os.listdir returns everyth in a file










