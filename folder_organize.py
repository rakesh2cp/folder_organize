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