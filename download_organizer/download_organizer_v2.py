import os

from constants import *

# List to hold the different filenames and extensions
# [{"filename": "", "extension": ""}]
file_and_extensions = []
# List to hold all folders
folders_in_download = []
# List to hold all files
files_in_download = []


def sort_through_the_files():
    # List all folders in downloads
    files_and_folders_in_downloads_folder = os.listdir(path=DOWNLOADS)

    # Check if files are available
    for file in files_and_folders_in_downloads_folder:
        # Unpacking the filenames and extensions
        file, ext = os.path.splitext(file)

        # Store in a list as a dictionary
        file_and_extensions.append({"filename": file, "extension": ext})

    # Separating folders from files
    for file in file_and_extensions:
        if file["extension"] == "":
            folders_in_download.append(file)
        else:
            files_in_download.append(file)


def separate_files(ext, dpath):
    for file in files_in_download:
        # Checking file extensions
        if file["extension"] in ext:
            # Move the files
            os.rename(
                src=f"{DOWNLOADS}/{file['filename']}{file['extension']}",
                dst=f"{dpath}/{file['filename']}{file['extension']}",
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


def make_the_holder_paths(dpath, dext):
    # Make folder for videos
    if os.path.isdir(dpath):
        separate_files(ext=dext, dpath=dpath)
    else:
        # Make folder
        os.mkdir(dpath)
        separate_files(ext=dext, dpath=dpath)


def clean_downloads_folder():
    sort_through_the_files()

    for path_ext in PATH_EXT:
        make_the_holder_paths(dpath=path_ext[0], dext=path_ext[1])

    separate_folders()
    separate_other_folders()


if __name__ == "__main__":
    # Run the program
    clean_downloads_folder()
