import os
import shutil

# Specify the directory you want to organize
source_dir = 'C:/Users/adity/Downloads'

# File type categories
file_types = {
    'Images': ['.jpg', '.jpeg', '.png', '.gif', '.bmp'],
    'Documents': ['.pdf', '.docx', '.txt', '.xlsx'],
    'Desktop Apps': ['.exe'],
    'Videos': ['.mp4', '.mov', '.avi'],
    'Music': ['.mp3', '.wav'],
    'Archives': ['.zip', '.tar', '.rar']
}

# To store moved files and their original locations for undo
moved_files = {}


# Organize files by extension
def organize_files(source_dir, file_types):
    folder_needed = {folder: False for folder in file_types.keys()}

    # Iterate through files in the source directory
    for filename in os.listdir(source_dir):
        file_path = os.path.join(source_dir, filename)

        if os.path.isfile(file_path):
            # Get the file extension
            _, extension = os.path.splitext(filename)

            # Check the extension and move to the respective folder
            for folder_name, extensions in file_types.items():
                if extension.lower() in extensions:
                    folder_needed[folder_name] = True
                    dest_dir = os.path.join(source_dir, folder_name)

                    if not os.path.exists(dest_dir):
                        os.mkdir(dest_dir)

                    # Move file and track its original location
                    new_path = shutil.move(file_path, dest_dir)
                    moved_files[filename] = file_path  # Store original path
                    print(f'Moved: {filename} to {folder_name}')
                    break


# Undo the file organization
def undo_organization():
    for filename, original_path in moved_files.items():
        current_path = os.path.join(os.path.dirname(original_path), filename)

        if os.path.exists(current_path):
            shutil.move(current_path, original_path)
            print(f'Restored: {filename} to original location')

    print("Undo complete!")


if __name__ == '__main__':
    # Step 1: Organize the files
    organize_files(source_dir, file_types)
    print("File organization complete!")

    # Step 2: Prompt user to undo
    undo_choice = input("Do you want to undo the changes? (yes/no): ").lower()

    if undo_choice == 'yes':
        undo_organization()
    else:
        print("No undo performed. Changes are saved.")
