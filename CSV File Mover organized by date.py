# This python 3.X program moves csv files from one folder to another and also organize the files by date, but this date is in the file name at a specific index

    
import glob
import os
import shutil

src_folder = r"C:\Users\Administrator\Desktop\File_move_source"
dst_folder = r"C:\Users\Administrator\Desktop\File move destionarion\\"

# Search files with .txt extension in source directory
pattern = "\*.xlsx"
files = glob.glob(src_folder + pattern)


# move the files with txt extension
for file in files:
    # extract file name form file path
    file_name = os.path.basename(file)
    shutil.move(file, dst_folder + file_name)
    print('Moved:', file)

#sort destination folder
def sorted_date_key(x):
    return(x[21:28])

#print(files2)
sorted(os.listdir("C:\\Users\\Administrator\\Desktop\\File move destionarion\\"), key = sorted_date_key)  