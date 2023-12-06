import os

from constants import *

# List all folders in downloads
files_and_folders_in_downloads_folder = os.listdir(path=DOWNLOADS)

# List to hold the different filenames and extensions
# [{"filename": "", "extension": ""}]
file_and_extensions = []

# Check if files are available
for file in files_and_folders_in_downloads_folder:
    # Unpacking the filenames and extensions
    file, ext = os.path.splitext(file)

    # Store in a list as a dictionary
    file_and_extensions.append({"filename": file, "extension": ext})

# List to hold all folders
folders_in_download = []
# List to hold all files
files_in_download = []

# Separating folders from files
for file in file_and_extensions:
    if file["extension"] == "":
        folders_in_download.append(file)
    else:
        files_in_download.append(file)


def separate_video_files():
    for file in files_in_download:
        # Checking file extensions
        if file["extension"] in VIDEO_EXT:
            # Move the files
            os.rename(
                src=f"{DOWNLOADS}/{file['filename']}{file['extension']}",
                dst=f"{VIDEOS}/{file['filename']}{file['extension']}",
            )


def separate_compressed_files():
    for file in files_in_download:
        # Checking file extensions
        if file["extension"] in COMPRESSED_EXT:
            # Move the files
            os.rename(
                src=f"{DOWNLOADS}/{file['filename']}{file['extension']}",
                dst=f"{COMPRESSED}/{file['filename']}{file['extension']}",
            )


def separate_audio_files():
    for file in files_in_download:
        # Checking file extensions
        if file["extension"] in AUDIO_EXT:
            # Move the files
            os.rename(
                src=f"{DOWNLOADS}/{file['filename']}{file['extension']}",
                dst=f"{MUSIC}/{file['filename']}{file['extension']}",
            )


def separate_program_files():
    for file in files_in_download:
        # Checking file extensions
        if file["extension"] in PROGRAMS_EXT:
            # Move the files
            os.rename(
                src=f"{DOWNLOADS}/{file['filename']}{file['extension']}",
                dst=f"{PROGRAMS}/{file['filename']}{file['extension']}",
            )


def separate_folders():
    for file in folders_in_download:
        # No need to check for extension
        # Check for the predefined folders first
        if (
            file["filename"] == "Videos"
            or file["filename"] == "Music"
            or file["filename"] == "Programs"
            or file["filename"] == "Others"
            or file["filename"] == "Compressed"
        ):
            pass
        else:
            os.rename(
                src=f"{DOWNLOADS}/{file['filename']}{file['extension']}",
                dst=f"{OTHERS}/{file['filename']}{file['extension']}",
            )


def separate_other_folders():
    # This is for folders that contain . in their names
    for file in files_in_download:
        # Checking file extensions
        if (
            file["extension"] not in AUDIO_EXT
            and file["extension"] not in PROGRAMS_EXT
            and file["extension"] not in VIDEO_EXT
            and file["extension"] not in COMPRESSED_EXT
        ):
            # Move the files to others
            os.rename(
                src=f"{DOWNLOADS}/{file['filename']}{file['extension']}",
                dst=f"{OTHERS}/{file['filename']}{file['extension']}",
            )


# Make folder for videos
if os.path.isdir(VIDEOS):
    separate_video_files()
else:
    # Make folder
    os.mkdir(VIDEOS)
    separate_video_files()

# Make folder for compressed files
if os.path.isdir(COMPRESSED):
    separate_compressed_files()
else:
    # Make folder
    os.mkdir(COMPRESSED)
    separate_compressed_files()

# Make folder for music files
if os.path.isdir(MUSIC):
    separate_audio_files()
else:
    # Make folder
    os.mkdir(MUSIC)
    separate_audio_files()

# Make folder for program files
if os.path.isdir(PROGRAMS):
    separate_program_files()
else:
    # Make folder
    os.mkdir(PROGRAMS)
    separate_program_files()

# Make folder for others files
if os.path.isdir(OTHERS):
    separate_folders()
    separate_other_folders()
else:
    # Make folder
    os.mkdir(OTHERS)
    separate_folders()
    separate_other_folders()
