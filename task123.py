import os
import shutil

def organize_files(source_dir, destination_dir):
    if not os.path.exists(destination_dir):
        os.makedirs(destination_dir)

    for filename in os.listdir(source_dir):
        if filename != 'organize_files.py':  # Exclude this script itself
            source_path = os.path.join(source_dir, filename)
            
            if os.path.isfile(source_path):
                file_extension = filename.split('.')[-1].lower()
                destination_path = os.path.join(destination_dir, file_extension)
                
                if not os.path.exists(destination_path):
                    os.makedirs(destination_path)
                
                shutil.move(source_path, os.path.join(destination_path, filename))
                print(f"Moved '{filename}' to '{destination_path}'")

if __name__ == "__main__":
    source_directory = "/path/to/source/directory"  # Replace with the source directory path
    destination_directory = "/path/to/destination/directory"  # Replace with the destination directory path

    organize_files(source_directory, destination_directory)
