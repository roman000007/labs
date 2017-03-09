import sys
import os
import shutil
import zipfile
class ZipProcessor:
    def __init__(self, zipname):
        """
        Init class
        (str)->None
        Need path to zip file
        """
        self.zipname = zipname
        self.temp_directory = "unzipped-{}".format(zipname[:-4])
        
    def _full_filename(self, filename):
        """
        (str)->(str)
        Return full path
        """
        return os.path.join(self.temp_directory, filename)
        
    def process_zip(self, other):
        """
        function, which unzip, process and zip files 
        """
        self.unzip_files()
        other.process_files()
        self.zip_files()
        
    def unzip_files(self):
        """
        function, which unzip files
        """
        os.mkdir(self.temp_directory)
        zip = zipfile.ZipFile(self.zipname)
        try:
            zip.extractall(self.temp_directory)
        finally:
            zip.close()
            
    def zip_files(self):
        """
        function, which zip files
        """
        file = zipfile.ZipFile(self.zipname, 'w')
        for filename in os.listdir(self.temp_directory):
            file.write(self._full_filename(filename), filename)
        shutil.rmtree(self.temp_directory)