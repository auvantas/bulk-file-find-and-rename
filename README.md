# File Renamer

A simple Python script to rename bulk files by removing a specified search string from filenames in a given directory and its subdirectories in Windows.

## For Example:
There is a string pattern --abcd-- in the files you want to remove;

    file001--abcd--.txt
    file002--abcd--.txt
    file003--abcd--.txt

The script will look the in the selected folder for any files with --abcd-- remove and rename these to;

    file001.txt
    file002.txt
    file003.txt

## Getting Started

### Prerequisites

- Python 3.x

### Installing

1. Clone the repository
```bash
git clone https://github.com/auvantas/bulk-file-find-and-rename/file-renamer.git
```

2. Run the script
```bash
python file_renamer.py
```
Usage
    
  1. Select a directory 
  2. Enter the search string to remove from filenames

## License

This project is licensed under the MIT License - see the [MIT License](https://github.com/auvantas/bulk-file-find-and-rename/blob/main/LICENSE) for details.
