from a0_items import *


###################################################################################################
### plugins - folders & sqlite file 
####################################################################################################
class Plg_folders:

    def create_folder(self, folder_path):

        if not os.path.isdir(folder_path):

            os.makedirs(folder_path)  #if folder not exists, create it
            print(folder_path + ' folder NOT exists, is created')

        else:

            #shutil.rmtree(folder_path)#if folder exists, remove it
            print(folder_path + ' folder exists')

            #create_folder (folder_path)

    ########################################################################################################################
    ########################################################################################################################

    def get_ALL_in_folder(self, folder_path):

        LIST_items_in_folder = os.listdir(folder_path)

        return LIST_items_in_folder

        #print(get_ALL_in_folder (folder_path ='../../data/raw/output_folder/'))

    #print (len(get_ALL_in_folder (folder_path=('../../data/cooked/DB_squ/'))))

    def get_ALL_subfolders_files_in_parent_folder(self, parent_folder_path):

        LIST_file = []
        LIST_folder = []

        for root, dirs, files in os.walk(parent_folder_path, topdown=False):
            for name in files:
                # list files

                LIST_file.append(name)
                print(os.path.join(root, name))

            for name in dirs:  #list folders
                LIST_folder.append(name)
                print(os.path.join(root, name))

        print('Total files =>', len(LIST_file))
        print('Total folders =>', len(LIST_folder))

        return LIST_folder, LIST_file

    #get_ALL_subfolders_files_in_parent_folder (parent_folder_path= '../core_TASK/')

    def remove_ALL_folder_items(self, folder_path):
        LIST_folder_item = os.listdir(folder_path)

        for x in LIST_folder_item:
            ab_path_folder = os.path.abspath(folder_path + x)  # Must convert relative path to absolute path

            shutil.rmtree(ab_path_folder, ignore_errors=False)

            print(ab_path_folder + ' => removed')

    #remove_ALL_folder_items (folder_path)

    def copy_folderA_to_folderB(self, folderA_path, folderB_path):

        #Need to remove all in Folder B before copy Folder A to Folder B
        remove_ALL_folder_items(folder_path=folderB_path)

        #print (os.listdir(folder_TFM_SOURCE))

        for y in LIST_folderA_item:
            try:
                ab_path_folderA = os.path.abspath(folderA_path + y)  # Must convert relative path to absolute path
                ab_path_folderB = os.path.abspath(folderB_path + y)  # Must convert relative path to absolute path

                copytree(ab_path_folderA, ab_path_folderB)
                print(ab_path_folderB + '/' + ' => copied')

            except Error as err:

                print('ERROR MSG => ', err)

        #copy_folderA_to_folderB (folderA_path, folderB_path)
