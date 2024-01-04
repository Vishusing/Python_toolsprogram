import os

def remove_empty_folders(path):
    """Recursively removes empty folders within the specified path."""

    for root, dirs, files in os.walk(path, topdown=False):
        if not any(files) and not any(dirs):
            try:
                os.rmdir(root)
                print(f"Removed empty folder: {root}")
            except OSError as e:
                print(f"Error removing folder {root}: {e}")

# Specify the path to the folder bundle you want to scan
folder_path = input("Enter folder path:-\n")  # Replace with the actual path

remove_empty_folders(folder_path)

print("Empty folders have been removed.")

