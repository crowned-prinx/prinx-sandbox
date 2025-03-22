import tarfile
import os
import logging

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
    output_path = os.path.normpath(output_path) + os.sep

    # Validate and create output_path if necessary
    if not os.path.exists(output_path):
        try:
            os.makedirs(output_path, exist_ok=True)  # Create directory and parents if needed
            logging.info(f"Created output directory: {output_path}")
        except OSError as e:
            logging.error(f"Failed to create output directory {output_path}: {e}")
            return None

    return input_path, output_path

def compress(input_path: str, output_path: str, filename: str):
    """
    Compress all files/folders specified in the input path
    and saves the compressed file as a (.tar.gz) file in the output path.

    Args:
        input_path (str): Path to the input directory.
        output_path (str): Path to the output directory.
        filename (str): Name of the compressed output file.
    """
    
    validate_results = validate_and_prepare_paths(input_path, output_path)
    if validate_results:
        input_path, output_path = validate_results
        try:
            with tarfile.open(f'{output_path}{filename}.tar.gz', mode="w:gz") as tf:
                for doc in os.listdir(input_path):
                    tf.add(os.path.join(input_path, doc), arcname=doc)
                print(f"Archive created successfully and saved to {output_path}")
        except FileNotFoundError as e:
            print(f"File or directory not found: {e}")
        except Exception as e:
            print(f"An error occurred: {e}")