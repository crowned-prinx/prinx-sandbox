import shutil
import logging
import os

# Set up logging
logging.basicConfig(level=logging.ERROR)

def validate_and_prepare_paths(input_path, output_path):
    """
    Validate input and output paths, ensuring the input path is a valid directory
    and the output path exists (creating it if necessary).

    Args:
        input_path (str): Path to the input directory.
        output_path (str): Path to the output directory.

    Returns:
        tuple: (input_path, output_path, is_dir) if both paths are valid, else None. is_dir (bool): True if path a directory else False.
    """
    
    # Validate input_path
    if not isinstance(input_path, str) or not isinstance(output_path, str):
        logging.error("Input and output paths must be strings.")
        return None
    
    if not os.path.exists(input_path):
        logging.error(f"Input path does not exist: {input_path}")
        return None

    if os.path.isdir(input_path):
        is_dir: bool = True
        # Normalize input_path (ensure it ends with a separator)
        input_path = os.path.normpath(input_path) + os.sep
    else:
        is_dir: bool = False
        
    # Normalize output_path (ensure it ends with a separator)
    output_path = os.path.normpath(output_path) + os.sep

    # Validate and create output_path if necessary
    if not os.path.exists(output_path):
        try:
            os.makedirs(output_path, exist_ok=True)  # Create directory and parents if needed
            logging.info(f"Created output directory: {output_path}")
        except OSError as e:
            logging.error(f"Failed to create output directory {output_path}: {e}")
            return None

    return (input_path, output_path, is_dir)


def copy_and_paste(input_path, output_path):
    """
    Copies content in the input path (a folder or a file) and paste in the output path. It replace duplicate files/folders if already exist.

    Args:
        input_path (str): Path to the input directory.
        output_path (str): Path to the output directory.

    Returns:
        tuple: (input_path: str, output_path: str, is_dir: bool = True | False) if both paths are valid, else None.
    """
    validate_result = validate_and_prepare_paths(input_path, output_path)
    if validate_result:
        input_path, output_path, is_dir = validate_result
        try:
            if is_dir:
                shutil.copytree(input_path, output_path, dirs_exist_ok=True)
                print("Operation was successful!")
            else:
                shutil.copy2(input_path, output_path)
                print("Operation was successful!")
        except Exception as e:
            logging.error(f"Something went wrong: {e}")
        except NotADirectoryError as e:
            logging.error(f"The path specified isn't a directory: {e}")
        except IsADirectoryError as e:
            logging.error(f"The path specified is a directory: {e}")