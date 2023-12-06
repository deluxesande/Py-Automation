HOST = "deluxe"

## Default paths
# Downloads folder path
# Should be based on you os
DOWNLOADS = f"/home/{HOST}/Downloads"
VIDEOS = f"/home/{HOST}/Downloads/Videos"
COMPRESSED = f"/home/{HOST}/Downloads/Compressed"
MUSIC = f"/home/{HOST}/Downloads/Music"
PROGRAMS = f"/home/{HOST}/Downloads/Programs"
OTHERS = f"/home/{HOST}/Downloads/Others"

# Extensions
AUDIO_EXT = [".mp3", ".wav"]
VIDEO_EXT = [".mp4"]
COMPRESSED_EXT = [".zip", ".rar", ".gz"]
PROGRAMS_EXT = [".flatpak", ".deb", ".snap", ".exe"]

# List for path and ext
PATH_EXT = [
    (VIDEOS, VIDEO_EXT),
    (MUSIC, AUDIO_EXT),
    (PROGRAMS, PROGRAMS_EXT),
]
