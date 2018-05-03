################################################################
# Python Script to Organize a folder on your Computer		   #
# Please change the src_folder the folder name you want		   #
# to Organize.												   #
# It will create and move the files to respective			   #
# folder/directories based on their file type				   #
# e.g. jpeg/jpg/png/gif to images							   #
# zip/tar/gz/bz2 to compress_files etc.						   #
################################################################

# Import Required Libraries
from os import listdir, mkdir, rename
from os.path import isfile, join, exists
# Folder to Organize
src_folder = '/Users/hduser/Downloads/'

# Listing the directory
items_list = listdir(src_folder)

# Mapping respective file types to their respectve folders
extn_to_folder_mapper = {
	'jpeg jpg png gif svg iso JPG': 'images',
	'app dmg pkg':'application',
	'txt xls xlsx pdf doc docx ppt pptx csv':'ppt_pdf_doc_txt',
	'zip tar gz bz2':'compres_file',
	'py pyc R whl sh':'code_files',
	'mp3 mp4 wav':'music_audio',
	'jar':'Jar',
	'json':'Json_Files'
}

# Extracting file extention from the file
def get_file_extn(file_name):
	split_name = file_name.split('.')
	return split_name[-1]

# Creating folders/directories as per the folder mapper dictionary
def create_folder_name(name):
	if not exists(join(src_folder,name)):
		mkdir(join(src_folder,name))

# Moves Files to their respective folder
def move_file_to_folder(file_name,folder_name):
	 old_path = join(src_folder,file_name)
	 new_path = join(src_folder,folder_name,file_name)
	 rename(old_path, new_path)

def map_extn_to_folder(extn,name):
	folder_name = 'others'
	for extn_list, dest_folder in extn_to_folder_mapper.iteritems():
		if extn in extn_list.split(' '):
			folder_name = dest_folder
			break

	create_folder_name(folder_name)
	move_file_to_folder(name, folder_name)
# Main Function
def main():
	for item_name in items_list:
		if isfile(join(src_folder, item_name)):
			split_name = item_name.split('.')
			extn = get_file_extn(item_name)
			map_extn_to_folder(extn, item_name)
			#print "file name" , item_name
			#print "split file name", split_name

main()

#import math, time
#
## Set listing start location
##start_path = "C:\\Users\\1578413\\Downloads\\"
#start_path = "C:\\Users\\1578413\\Desktop\\"
#dir_count = 0
#file_count = 0
#
## Traverse directory tree
#for (path, dirs, files) in os.walk(start_path):
#    #print('Directory: {:s}'.format(path))
#    dir_count += 1
#    # Repeat for each file in directory
#    for file in files:
#        fstat = os.stat(os.path.join(path, file))
#
#        # Convert file size to MB, KB or Bytes
#        if (fstat.st_size > 1024 * 1024):
#            fsize = math.ceil(fstat.st_size / (1024 * 1024))
#            unit = "MB"
#            print(path, '\t{:15.15s}{:8d} {:2s} {:18s}'.format(file, fsize, unit, mtime))
#        elif (fstat.st_size > 1024):
#            fsize = math.ceil(fstat.st_size / 1024)
#            unit = "KB"
#        else:
#            fsize = fstat.st_size
#            unit = "B"
#
#        mtime = time.strftime("%X %x", time.gmtime(fstat.st_mtime))
#
#        # Print file attributes
#        #if (fsize > 2 * 1024 * 1024):
#        #print('\t{:15.15s}{:8d} {:2s} {:18s}'.format(file, fsize, unit, mtime))
#        file_count += 1
## Print total files and directory count
#print('\nFound {} files in {} directories.'.format(file_count, dir_count))
