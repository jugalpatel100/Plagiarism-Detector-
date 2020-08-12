import os

def getSystemDrives():
    ''' Searches for all the drives in the system '''

    drives = [chr(x) + ":\\" for x in range(65, 90) if os.path.exists(chr(x) + ':')]
    drives_dict = dict()

    i=1
    for drive in drives:
        drives_dict[i] = drive
        i+=1

    return drives_dict


def createNumberedDirectories(dir):
    ''' Creates a dictionary of files/subdirectories indexed by numbers for easier selection'''
    numbered_dirs = dict()
    num = 1
    #lists all the files and sub-directories in a given directory
    for l in os.listdir(dir):
        numbered_dirs[num] = l
        num+=1
    
    return numbered_dirs

def listDirectories(dir_dict, main_dir_full_path):
    ''' Prints all the files/subdirectories in the given main directory'''

    for num, f in dir_dict.items():
        type = ""
        if os.path.isfile(os.path.join(main_dir_full_path, f)):
            type = " (F)"
        else:
            type = " (D)"
        print(str(num) + ". " + f + " " + type)


def fileSelector():
    ''' Repeatedly prompts for input to select a file from the system '''
    drives = getSystemDrives()

    for num, drive in drives.items():
        print(str(num) + ". " + drive)

    selection = int(input('Select a drive: '))

    curr_folder = ""

    for num, drive in drives.items():
        if selection == num:
            curr_folder = drive
            break
    
    while(os.path.isdir(curr_folder)):
        dir_dict = createNumberedDirectories(curr_folder)
        listDirectories(dir_dict, curr_folder)

        selection = int(input('Select a file to upload or directory to open: '))

        for num, f in dir_dict.items():
            if selection == num:
                curr_folder = os.path.join(curr_folder, f)
                break
        
        if os.path.isdir(curr_folder):
            print("\nOpening " + curr_folder + "\n")
        else:
            print("\nSelected " + curr_folder + "\n")