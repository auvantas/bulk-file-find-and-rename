import os
import tkinter as tk
from tkinter import filedialog

def rename_files(directory, search_string):
    """
    Renames files by removing the provided search string from filenames 
    in the given directory and its subdirectories. Prints a message for each file renamed.
    """
    for foldername, subfolders, filenames in os.walk(directory):
        print(f"Entering folder: {foldername}")  # Print folder name
        
        renamed_files_in_folder = False  # Flag to check if any files are renamed in the folder

        # Iterate over each file in the current folder
        for filename in filenames:
            print(f"Checking file: {filename}")  # Debugging print statement
            
            if search_string in filename:
                old_filepath = os.path.join(foldername, filename)
                new_filename = filename.replace(search_string, "")
                new_filepath = os.path.join(foldername, new_filename)

                try:
                    os.rename(old_filepath, new_filepath)
                    print(f"Found: {filename}")
                    print(f"Renamed: {new_filename}")
                    renamed_files_in_folder = True  # Set flag to True as a file is renamed
                except Exception as e:
                    print(f"Failed to rename {filename}. Error: {e}")

        # If no files are renamed in the folder, print "No files found."
        if not renamed_files_in_folder:
            print("No files found.")

def select_directory():
    root = tk.Tk()
    root.withdraw()  # Hide the main window
    folder_selected = filedialog.askdirectory()  # Open folder selection dialog
    return folder_selected

if __name__ == "__main__":
    directory = select_directory()
    
    if directory:  # Check if a directory was selected
        search_string = input("Enter the string to search for in filenames: ")
        rename_files(directory, search_string)
    else:
        print("No directory selected. Exiting...")
