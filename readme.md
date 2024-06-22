# File and Folder Deletion Script

This Python script is designed to search for and delete specified files and folders on your Desktop and Downloads directories. It first lists the found items and then asks for confirmation before deleting them. After the initial deletion, it offers the user the option to specify additional files or folders to delete.

## How It Works

The script performs the following steps:

1. **Define Search Paths**: Sets the Desktop and Downloads directories as the default search paths.
2. **Define Default File and Folder Names**: Specifies a list of default file and folder names to search for.
3. **Search for Files and Folders**: Uses the `os.walk` method to search for the specified files and folders in the search paths.
4. **Display Found Items**: Prints the paths of the found files and folders.
5. **Confirm Deletion**: Asks the user if they want to delete the found files and folders.
6. **Delete Files and Folders**: Deletes the files and folders if the user confirms.
7. **Ask for More Deletions**: Prompts the user to enter additional file and folder names to delete and repeats the search and deletion process.

## Script Execution

### Initial Setup

1. **Import Modules**: The script imports the `os` and `shutil` modules for file and directory operations.
2. **Define Functions**:
    - `find_files(file_names, search_paths)`: Searches for specified file names in the given paths.
    - `find_folders(folder_names, search_paths)`: Searches for specified folder names in the given paths.
    - `delete_files(file_paths)`: Deletes the specified files.
    - `delete_folders(folder_paths)`: Deletes the specified folders.

### Main Execution

1. **Set Search Paths**: The script sets the Desktop and Downloads directories as the search paths.
2. **Specify Default File and Folder Names**: Lists the default file and folder names to be searched and deleted.
3. **Find and Display Items**: Searches for and lists the found files and folders.
4. **User Confirmation**: Asks the user if they want to delete the found items.
5. **Delete Items**: Deletes the items if the user confirms.
6. **Additional Deletions**: Prompts the user to specify additional files and folders to delete and repeats the process.

## How to Use

1. **Run the Script**: Execute the script using a Python interpreter.
    ```sh
    python delete_files_and_folders.py
    ```
2. **Review Found Items**: The script will list the found files and folders.
3. **Confirm Deletion**: Respond to the prompt to confirm whether you want to delete the found items.
4. **Specify Additional Deletions**: If prompted, enter the names of any additional files or folders you want to delete.

## Example Usage

```sh
$ python delete_files_and_folders.py
Found the following files:
/Users/username/Desktop/Join Our Platforms.pdf
/Users/username/Downloads/10k Free Courses.pdf
...
Found the following folders:
/Users/username/Desktop/00-Join LearnWithFaizan For Free Courses
...
Do you want to delete these files and folders? (yes/no): yes
Deleted /Users/username/Desktop/Join Our Platforms.pdf
Deleted /Users/username/Downloads/10k Free Courses.pdf
...
Deleted folder /Users/username/Desktop/00-Join LearnWithFaizan For Free Courses
...
Do you want to delete any more files or folders? (yes/no): yes
Enter the names of files to delete, separated by commas: example.txt, sample.docx
Enter the names of folders to delete, separated by commas: TestFolder, SampleFolder
Found the following files:
/Users/username/Desktop/example.txt
/Users/username/Downloads/sample.docx
...
Found the following folders:
/Users/username/Desktop/TestFolder
/Users/username/Downloads/SampleFolder
...
Do you want to delete these files and folders? (yes/no): yes
Deleted /Users/username/Desktop/example.txt
Deleted /Users/username/Downloads/sample.docx
...
Deleted folder /Users/username/Desktop/TestFolder
Deleted folder /Users/username/Downloads/SampleFolder
...
No more deletions requested.
