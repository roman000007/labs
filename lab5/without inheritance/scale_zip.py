import sys
import os
import shutil
import zipfile
from zip_processor import ZipProcessor
from pygame import image
from pygame.transform import scale

class ScaleZip:
        def __init__(self, filename):
            """
            Init class
            (str)->None
            Need path to zip file
            """
            self.processor = ZipProcessor(filename)
            self.processor.process_zip(self)
        def process_files(self):        
            '''Scale each image in the directory to 640x480'''        
            for filename in os.listdir(self.processor.temp_directory):   
                try:
                    im = image.load(self.processor._full_filename(filename))            
                    scaled = scale(im, (640,480))            
                    image.save(scaled, self.processor._full_filename(filename))
                except:
                    pass
if __name__ == "__main__":
    """
    starting in console mode
    """
    ScaleZip("examp.zip")
    
    
 