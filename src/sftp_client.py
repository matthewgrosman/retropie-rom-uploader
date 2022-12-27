import os
import pysftp
import constants


class SftpClient:
    """
    The SftpClient class handles all interactions with the SFTP protocol between your local machine and the
    Raspberry Pi SSH server. This includes establishing a connection, transferring files from local machine
    to the Raspberry Pi, and closing the connection.
    """
    def __init__(self) -> None:
        """
        Constructor for the SftpClient class. Initializes an object that will hold a connection to the Raspberry Pi
        SSH client.

        :return: None.
        """
        self.connection = None

    def get_connection(self) -> None:
        """
        Establishes a connection to the Raspberry Pi's SSH server.

        :return: None.
        """
        print(f"Attempting to connect to {constants.USERNAME}@{constants.HOSTNAME} ...")

        self.connection = pysftp.Connection(
            host=constants.HOSTNAME,
            username=constants.USERNAME,
            password=constants.PASSWORD,
            port=constants.PORT,
        )

        print("Connection established!\n")

    def close_connection(self) -> None:
        """
        Closes a connection to the Raspberry Pi's SSH server.

        :return: None.
        """
        self.connection.close()

    def upload_roms(self, roms: list[str]) -> None:
        """
        Uploads retrieved roms to Raspberry Pi via SFTP.

        :param roms:    List containing the filepaths of all retrieved roms
        :return:        None.
        """
        print("Uploading roms from local machine:")

        for i, rom in enumerate(roms):
            # Builds remote filepath. The filepath is of the format: {pathToPiRomDirectory}/{consoleSubdirectory}/{rom}
            split_rom_path = os.path.split(rom)
            remote_rom_subdirectory = os.path.basename(split_rom_path[0])
            rom_filename = split_rom_path[1]
            full_remote_filepath = constants.REMOTE_ROMS_PATH + remote_rom_subdirectory + f"/{rom_filename}"

            if not self.connection.exists(full_remote_filepath):
                print(f"Uploading {rom} ...")
                self.connection.put(rom, full_remote_filepath)
            else:
                print(f"Rom {rom} already exists on your Retropie, skipping upload.")

        print("All roms uploaded successfully!\n")
