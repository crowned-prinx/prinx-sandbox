# DICOM Image Converter

This Python script converts DICOM (`.dcm`) images to common image formats (PNG, JPG, JPEG) and saves them in a specified output folder. It is designed to handle bulk conversion of DICOM files and ensures proper validation of input paths and output formats.

## Features

- Converts DICOM images to PNG, JPG, or JPEG formats.
- Validates input and output paths.
- Automatically creates the output folder if it doesn't exist.
- Logs conversion progress (optional).
- Supports recursive searching for DICOM files in the input folder.

## Requirements

- Python 3.x

Install the required packages using:

```bash
pip install -r requirements.txt
```

## Usage

### Function: `convert_dcm`

```python
convert_dcm(input_path: str, output_path: str, format: str = "png", log: bool = False)
```

#### Parameters:

- **`input_path`**: Path to the folder containing `.dcm` files.
- **`output_path`**: Path to the folder where converted images will be saved.
- **`format`**: Desired output image format (`png`, `jpg`, or `jpeg`). Default is `png`.
- **`log`**: If `True`, prints conversion progress. Default is `False`.

#### Example:

```python
from dicom_converter import convert_dcm

input_folder = "/path/to/dicom/folder"
output_folder = "/path/to/output/folder"

# Convert DICOM files to PNG (default format)
convert_dcm(input_folder, output_folder, format="png", log=True)
```

## Example Folder Structure

```
/path/to/dicom/folder/
    image1.dcm
    image2.dcm
    ...

/path/to/output/folder/
    image1.png
    image2.png
    ...
```
