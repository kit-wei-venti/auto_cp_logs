import os
import shutil




keyword = ".bag"
list_file = " "
count = 0

directory = os.getcwd()
list_file = os.listdir(directory)

for filename in list_file:
    if keyword in filename:
        
        count = count +1
        full_directory = directory + "/" + filename
        
        for (i = 1; i < count; i++)
            
        """
        #adding the r converts the normal string to a raw string
        destination_dir = r'/media/kitwei/Extreme SSD/test_paste'     #change this according to ur thumbdrive directory
        destination_dir_cpfile = destination_dir + "/" + filename
        #print(destination_dir_cpfile)
        shutil.copy(full_directory, destination_dir_cpfile)

        print(os.listdir(destination_dir))
        
        #os.listdir returns everyth in a file
5               """



print(count)





