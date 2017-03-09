import sys
import os
import shutil
import zipfile
from processor import ZipProcessor
class ZipReplace(ZipProcessor):
    def __init__(self, filename, search_string,replace_string):
        """
        Init class
        (str, str, str)->None
        Need path to zip file, string to search and string to replace
        """
        self.search_string = search_string
        self.replace_string = replace_string
        super().__init__(filename)
        

    def process_files(self):
        """
        function, which replace content
        """
        for filename in os.listdir(self.temp_directory):
            with open(self._full_filename(filename)) as file:
                contents = file.read()
                contents = contents.replace(self.search_string, self.replace_string)
            with open(self._full_filename(filename), "w") as file:
                file.write(contents)
               
                



if __name__ == "__main__":
    """
    starting in console mode
    """
    ZipReplace("examp.zip", "mistake", "changed").process_zip()
    
    
 