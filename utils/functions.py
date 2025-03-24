import numpy as np
import cv2
import os
from pydicom import dcmread
import glob
from enum import Enum, unique
import logging

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

def validate_and_prepare_paths(input_path, output_path):
    """
    Validate input and output paths, ensuring the input path is a valid directory
    and the output path exists (creating it if necessary).

    Args:
        input_path (str): Path to the input directory.
        output_path (str): Path to the output directory.

    Returns:
        tuple: (input_path, output_path) if both paths are valid, else None.
    """
    # Validate input_path
    if not isinstance(input_path, str) or not isinstance(output_path, str):
        logging.error("Input and output paths must be strings.")
        return None

    if not os.path.exists(input_path):
        logging.error(f"Input path does not exist: {input_path}")
        return None

    if not os.path.isdir(input_path):
        logging.error(f"Input path is not a directory: {input_path}")
        return None

    # Normalize input_path (ensure it ends with a separator)
    input_path = os.path.normpath(input_path) + os.sep

    # Validate and create output_path if necessary
    if not os.path.exists(output_path):
        try:
            os.makedirs(output_path, exist_ok=True)  # Create directory and parents if needed
            logging.info(f"Created output directory: {output_path}")
        except OSError as e:
            logging.error(f"Failed to create output directory {output_path}: {e}")
            return None

    return input_path, output_path

def convert_dcm(input_path: str, output_path: str, format: str = "png", log: bool = False):
    ''' Takes two required arguments: (1) An input folder containing .dcm files. (2) The desired output folder.\n
    This function converts all DICOM images in the input folder to the default format (png) and saves them in the output folder specified.
    '''
    validate_results = validate_and_prepare_paths(input_path, output_path)
    format = format.lower()
    
    if validate_results:
        input_path, output_path = validate_results
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

