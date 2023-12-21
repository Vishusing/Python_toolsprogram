import os

# Get the desired base directory path from the user
base_dir_path = input("Enter the full path where you want to create the base directory: ")

# No. of folders to be created in base_directory
num_folders = int(input("Enter the number of folders to be created: "))

# No. of files to be created in each folder
num_files_per_folder = int(input("Enter the number of files to be created in each folder: "))

# What is the extension of file
ext = input("Enter the extensions of the file:-")

# Create the base directory if it doesn't exist
if not os.path.exists(base_dir_path):
   os.makedirs(base_dir_path)

# Extract the base directory name from the path
base_dir_name = os.path.basename(base_dir_path)

# Create folders with numbered names within the base directory
for i in range(1, num_folders + 1):
   folder_name = f"folder_{i}"
   folder_path = os.path.join(base_dir_path, folder_name)
   os.makedirs(folder_path)

# Create files with numbered names within each folder
for folder in os.listdir(base_dir_path):
   folder_path = os.path.join(base_dir_path, folder)
   for i in range(1, num_files_per_folder + 1):
       file_name = f"file_{i}.{ext}"
       file_path = os.path.join(folder_path, file_name)
       with open(file_path, "w") as f:
           pass

print(f"Successfully created {num_folders} folders and {num_folders * num_files_per_folder} files in '{base_dir_name}' directory at '{base_dir_path}'.")
