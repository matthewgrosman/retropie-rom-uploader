# Constants needed to establish a connection to Raspberry Pi SSH server.
PORT = 22
HOSTNAME = "someIPaddress"
USERNAME = "someUserName"
PASSWORD = "somePassword"

# Remote path where roms live.
REMOTE_ROMS_PATH = "/home/pi/RetroPie/roms/"

# Path to roms.
LOCAL_ROMS_PATH = "/Users/matthew/Documents/roms/"

# Defines the types of files we identify as a rom.
VALID_ROM_FILE_TYPES = {
    ".a26",  # Atari 2600
    ".a78",  # Atari 7800
    ".md",   # Sega Genesis
    ".nes",  # NES
    ".sfc",  # SNES
    ".z64",  # N64
    ".chd",  # Playstation
    ".7z",   # Compressed file, works for multiple consoles
    ".zip",  # Compressed file, works for multiple consoles
}
