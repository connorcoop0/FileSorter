import os
import shutil

# global list of the sorted directory names
directories = ["Documents_Sorted", "Spreadsheets_Sorted", "Images_Sorted", "Audio_Sorted", "Video_Sorted", "Scripts_Sorted", "Archives_Sorted", "Other_Sorted"]

def get_file_path():
    # Loop for file_path input + validation
    while True:
        file_path = input("Please input the exact path of the directory where you would like your files sorted: ")
        if os.path.isfile(file_path):
            print("This is a file not a directory, try again")
        elif os.path.isdir(file_path):
            break
        else:
            print("Invalid path, make sure it looks similair to this:", os.getcwd())
    return file_path

# Gets all file names
def get_dir_files(file_path):
    file_list = []
    for files in os.listdir(file_path):
        file_name, file_extension = os.path.splitext(files)
        if file_extension:
            file_list.append(file_name+file_extension)
    return file_list
            
def create_sorted_directories(file_path):
    for directory in directories:
        try:
            os.mkdir(os.path.join(file_path, directory))
        except FileExistsError:
            print(directory, "Already Exists")

def remove_sorted_directories(file_path):
    for directory in directories:
        try:
            os.rmdir(os.path.join(file_path, directory))
        except OSError:
            print(directory, "Is not Empty!")

# Displays amount of files moved to target directory
def sorting_summary(documents_moved, target_directory):
    if documents_moved > 0:
        print(documents_moved, "files moved to", str(target_directory))

# Main Script

# Get user file path
file_path = get_file_path()

# Loop to validate the input directory
while True:
    # Verify directory based on first 10 files in user selected directory
    print("\nThe directory you selected contains these files")
    files_in_dir = get_dir_files(file_path)
    for file in files_in_dir[:10]:
        print(file)
    path_validation = input("Does this look correct? ('y' or 'n'): ")
    if path_validation in ['y', 'n']:
        if path_validation == 'n':
            file_path = get_file_path()
            continue
        else:
            break
    else:
        print("ERROR: Invalid Input, must be 'y' or 'n'")

print("Creating Sorted Directories")
create_sorted_directories(file_path)

# Initializing variables for summary
documents_moved = 0
spreadsheets_moved = 0
images_moved = 0
audio_moved = 0
videos_moved = 0
scripts_moved = 0
archives_moved = 0
other_moved = 0


# Moving of files
for file in files_in_dir:
    file_name, file_extension = os.path.splitext(file)
    file_extension = file_extension.lower()
    file_full_path = os.path.join(file_path, file)
    if not os.path.isfile(file_full_path):
        continue  # Skip if not a file
    
    if file_extension in [".docx", ".doc", ".pdf", ".rtf", ".txt"]:
        shutil.move(file_full_path, os.path.join(file_path, "Documents_Sorted"))
        documents_moved += 1

    elif file_extension in [".csv", ".xlsx", ".xsl", ".ods"]:
        shutil.move(file_full_path, os.path.join(file_path, "Spreadsheets_Sorted"))
        spreadsheets_moved += 1
        
    elif file_extension in [".jpg", ".jpeg", ".png", ".webp"]:
        shutil.move(file_full_path, os.path.join(file_path, "Images_Sorted"))
        images_moved += 1

    elif file_extension in [".mp3", ".wav", ".aud", ".ogg", ".m4a", ".wma"]:
        shutil.move(file_full_path, os.path.join(file_path, "Audio_Sorted"))
        audio_moved += 1

    elif file_extension in [".mov", ".mp4", ".mkv", ".wmv", ".webm"]:
        shutil.move(file_full_path, os.path.join(file_path, "Video_Sorted"))
        videos_moved += 1

    elif file_extension in [".py", ".c", ".cpp", ".h", ".r"]:
        shutil.copy(file_full_path, os.path.join(file_path, "Scripts_Sorted"))
        scripts_moved += 1

    elif file_extension in [".zip", ".rar", ".tar", ".gz", ".7z"]:
        shutil.move(file_full_path, os.path.join(file_path, "Archives_Sorted"))
        archives_moved += 1

    else:
        shutil.copy(file_full_path, os.path.join(file_path, "Other_Sorted"))
        other_moved += 1

sorting_summary(documents_moved, "Documents_Sorted")
sorting_summary(spreadsheets_moved, "Spreadsheets_Sorted")
sorting_summary(images_moved, "Images_Sorted")
sorting_summary(audio_moved, "Audio_Sorted")
sorting_summary(videos_moved, "Video_Sorted")
sorting_summary(scripts_moved, "Scripts_Sorted")
sorting_summary(archives_moved, "Archives_Sorted")
sorting_summary(other_moved, "Other_Sorted")

print("All files succesfully sorted to relevant folders!")
