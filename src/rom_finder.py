import os
import constants


class RomFinder:
    """
    The RomFinder class handles finding roms on your local machine.
    """
    def __init__(self) -> None:
        """
        Constructor for the RomFinder class. Initializes a list that holds retrieved roms.

        :return: None.
        """
        self.roms = []

    def find_roms(self) -> None:
        """
        Finds roms on your local machine. A rom must be within the local roms directory path (or in a sub-directory
        within that directory) that is defined in constants.py. Found roms are appended to the self.roms list, which
        holds all the retrieved roms.

        :return: None.
        """
        print("Retrieving roms from local machine ...")

        for root, directories, filenames in os.walk(constants.LOCAL_ROMS_PATH):
            for file in filenames:
                if os.path.splitext(file)[-1] in constants.VALID_ROM_FILE_TYPES:
                    self.roms.append(os.path.join(root, file))

        print(f"Retrieved {len(self.roms)} roms from local machine!\n")

    def get_retrieved_roms(self) -> list[str]:
        """
        Returns the retrieved roms.

        :return: A list containing the filepaths to all retrieved roms.
        """
        return self.roms
