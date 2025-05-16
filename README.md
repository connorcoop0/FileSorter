# File Organizer

A Python script to organize files in a directory by file type.

## What It Does

This tool sorts files into categorized folders based on their extensions. For example:

- Documents (`.pdf`, `.docx`, `.txt`) → `Documents_Sorted`
- Images (`.jpg`, `.png`) → `Images_Sorted`
- Audio files (`.mp3`, `.wav`) → `Audio_Sorted`
- Everything else → `Other_Sorted`

Useful for cleaning up cluttered directories like Downloads or Desktop.

## Features

- Sorts files into folders by type  
- Automatically creates folders if they don't exist  
- Skips over directories  
- Copies scripts and unknown file types instead of moving them  
- Prints a summary of how many files were moved to each folder  

## How to Use

1. Clone or download the script.  
2. Run the script with Python:

   ```bash
   python file_organizer.py
   ```

3. When prompted, enter the full path to the folder you want to organize.  
4. Confirm the preview of files; the script will then sort them.

## Requirements

- Python 3.x  
- No external libraries required (uses only `os` and `shutil`).

## Notes

- Files are moved unless otherwise specified (scripts and unknowns are copied).  
- Intended for local file organization only.
