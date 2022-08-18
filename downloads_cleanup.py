import os
import collections
from pprint import pprint

EXT_AUDIO = ['mp3', 'wav', 'raw', 'wma', 'mid', 'midi']
EXT_VIDEO = ['mp4', 'mpg', 'mpeg', 'avi', 'mov', 'flv', 'mkv', 'mwv', 'm4v', 'h264']
EXT_IMGS = ['png', 'jpg', 'jpeg', 'gif', 'tiff', 'tif', 'bmp', 'svg', 'psd']
EXT_DOCS = ['txt', 'pdf', 'csv', 'xls', 'xlsx', 'ods', 'doc', 'docx', 'html', 'odt', 'tex', 'ppt', 'pptx', 'log']
EXT_COMPR = ['zip', 'z', '7z', 'rar', 'tar', 'gz', 'rpm', 'pkg', 'deb']
EXT_INSTL = ['dmg', 'exe', 'iso', 'msi']



def move_files(folder, file):
    path_name = os.path.join(DOWNLOADS_PATH, file)
    check_name = os.path.join(BASE_PATH, folder, file)

    dest_name = ""

    num = 0
    while True:
        if num != 0:
            split = check_name.split('.')
            part_1 = split[0] + '_' + str(num)
            dest_name = ".".join([part_1, split[1]])
        if not os.path.isfile(check_name):
            os.rename(path_name, check_name)
            break
        if num > 0 and not os.path.isfile(dest_name):
            os.rename(path_name, dest_name)
            break
        else:
            num += 1
           


# Create directories where we want to store the files
BASE_PATH = 'C:/Users/reeve/Downloads'
DEST_DIRS = ['Music', 'Pictures', 'Videos', 'Documents', 'Applications', 'Compressed', 'Other']

for d in DEST_DIRS:
    dir_path = os.path.join(BASE_PATH, d)
    if not os.path.isdir(dir_path):
        os.mkdir(dir_path)

# Map files from Downloads folder based on their file extension
DOWNLOADS_PATH = 'C:/Users/reeve/Downloads'
files_mapping = collections.defaultdict(list)
files_list = os.listdir(DOWNLOADS_PATH)

files_list.remove('desktop.ini')
files_list.remove('Applications')
files_list.remove('Music')
files_list.remove('Pictures')
files_list.remove('Documents')
files_list.remove('Compressed')
files_list.remove('Other')
files_list.remove('Videos')

for file_name in files_list:
    file_ext = file_name.split('.')[-1]
    files_mapping[file_ext].append(file_name)

#pprint(files_mapping)

# Move all files given a file extension to a target directory
for f_ext, f_list in files_mapping.items():
    if f_ext in EXT_INSTL:
        for file in f_list:
            move_files('Applications', file)

    elif f_ext in EXT_AUDIO:
        for file in f_list:
            move_files('Music', file)

    elif f_ext in EXT_VIDEO:
        for file in f_list:
            move_files('Videos', file)

    elif f_ext in EXT_IMGS:
        for file in f_list:
            move_files('Pictures', file)

    elif f_ext in EXT_DOCS:
        for file in f_list:
            move_files('Documents', file)
    
    elif f_ext in EXT_COMPR:
        for file in f_list:
            move_files('Compressed', file)

    else:
        for file in f_list:
            move_files('Other', file)
          
