import sys
import os
import shutil
import zipfile
from processor import ZipProcessor
from pygame import image
from pygame.transform import scale

class ScaleZip(ZipProcessor):
        def process_files(self):        
            '''Scale each image in the directory to 640x480'''        
            for filename in os.listdir(self.temp_directory):   
                try:
                    im = image.load(self._full_filename(filename))            
                    scaled = scale(im, (640,480))            
                    image.save(scaled, self._full_filename(filename))
                except:
                    pass
if __name__ == "__main__":
    """
    starting in console mode
    """
    ScaleZip("examp.zip").process_zip()
    
    
 