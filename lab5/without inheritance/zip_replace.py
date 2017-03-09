import sys
import os
import shutil
import zipfile
from zip_processor import ZipProcessor
class ZipReplace:
    def __init__(self, filename, search_string,replace_string):
        """
        Init class
        (str, str, str)->None
        Need path to zip file, string to search and string to replace
        """
        self.processor = ZipProcessor(filename)
        self.search_string = search_string
        self.replace_string = replace_string
        self.processor.process_zip(self)
        

    def process_files(self):
        """
        function, which replace content
        """
        for filename in os.listdir(self.processor.temp_directory):
            with open(self.processor._full_filename(self.processor.zipname)) as file:
                contents = file.read()
                contents = contents.replace(self.search_string, self.replace_string)
            with open(self.processor._full_filename(self.processor.zipname), "w") as file:
                file.write(contents)
               
                



if __name__ == "__main__":
    """
    starting in console mode
    """
    ZipReplace("examp.zip", "mistake", "changed")
    
    
 