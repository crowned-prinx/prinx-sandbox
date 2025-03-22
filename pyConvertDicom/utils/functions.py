import numpy as np
import cv2
import os
from pydicom import dcmread
import glob
from enum import Enum, unique

@unique # Duplicate values will raise an error
class Format(Enum):
    PNG = "png"
    JPG = "jpg"
    JPEG = "jpeg"

def check_format(format: str):
    format = str(format).lower()
    allowed_format = [ x.value for x in Format]
    if format in allowed_format:
        return True
    else:
        return False
    
def check_path(input_path: str, output_path: str):
    if os.path.exists(input_path):
        if not os.path.isdir(input_path):
            print(f"Error: Make sure the `input_path` is a folder.")
            return False
        input_path = input_path if input_path[-1] == "/" else input_path + "/"
    else:
        print(f"Error: Make sure the `input_path` is valid.")
        return False
       
    if not os.path.exists(output_path):
        try:
            os.mkdir(output_path)
        except Exception as e:
            print(f"Error: {e}: Something went wrong creating {output_path} folder.")
            return False
    return input_path

def convert_dcm(input_path: str, output_path: str, format: str = "png", log: bool = False):
    ''' Takes two required arguments: (1) An input folder containing .dcm files. (2) The desired output folder.\n
    This function converts all DICOM images in the input folder to the default format (png) and saves them in the output folder specified.
    '''
    input_path = check_path(input_path, output_path)
    format = format.lower()
    
    if input_path:
        dcms = [os.path.basename(x) for x in glob.glob(input_path + './*.dcm', recursive=True)]
        image_count = 0
        for i, dcm in enumerate(dcms):
            dc = dcmread(input_path + dcm) # read dicom image
            dc_img = dc.pixel_array # get image array
            
            # Normalize the image to 0–255 and convert to 8-bit
            dc_img = cv2.normalize(dc_img, None, 0, 255, cv2.NORM_MINMAX, dtype=cv2.CV_8U)
            
            # Check file format
            if not check_format(format):
                print(f"Invalid file format. Must be either ['jpg', 'png', 'jpeg']. Your input: {format}.")
                return
            
            image_format = '.' + format
            output_image = output_path + dcm.replace('.dcm', image_format)
            
            cv2.imwrite(output_image, dc_img)
            print(f"Converted {dcm} to {dcm.replace('.dcm', image_format)} and succesfully saved in: {output_path}") if log else None
            image_count += 1
        
        print(f"Converted {image_count} images to {format} and saved in: {output_path}")

