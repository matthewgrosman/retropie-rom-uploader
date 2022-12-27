from sftp_client import SftpClient
from rom_finder import RomFinder


def upload_roms_to_pi() -> None:
    """
    Entry function to begin uploading roms to Raspberry Pi.

    :return: None.
    """
    # Establish connection to Raspberry Pi SSH server.
    pi_client = SftpClient()
    pi_client.get_connection()

    # Find roms on local machine.
    rom_finder = RomFinder()
    rom_finder.find_roms()

    # Upload roms to Raspberry Pi.
    pi_client.upload_roms(rom_finder.get_retrieved_roms())

    # Close connection to Raspberry Pi SSH server.
    pi_client.close_connection()


if __name__ == '__main__':
    upload_roms_to_pi()
