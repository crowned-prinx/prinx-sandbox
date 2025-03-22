# File Compression Utility

Description:
This Python script provides a utility to validate input and output directories, and compress files/folders from the input directory into a `.tar.gz` archive. It includes error handling, logging, and path validation to ensure robustness.

---

## Features

- Validates input and output paths.
- Creates the output directory if it doesn't exist.
- Compresses files/folders from the input directory into a `.tar.gz` archive.
- Logs errors and important information for debugging.

## Requirements

- Python 3.x
- Standard Python libraries: `os`, `tarfile`, `logging`

## Setup

**Clone the repository**:

```bash
git clone https://github.com/crowned-prinx/prinx-sandbox.git
cd pyCompress
```

**Install dependencies**:
No additional dependencies are required as the script uses Python's standard libraries.

**Run the script**:

```bash
python main.py
```

## File Structure

```
project-folder/
├── functions           # Folder
    ├── functions.py    # Script containing other functions
├── main.py             # Main script file
├── README.md           # Documentation
```

## Usage

1. Set the `input_path` variable to the directory containing files/folders to compress.
2. Set the `output_path` variable to the directory where the compressed archive will be saved.
3. Set the `filename` variable to the desired name of the compressed file (without the `.tar.gz` extension).
4. Run the script.

Example:

```python
input_path = "/path/to/input"
output_path = "/path/to/output"
filename = "compressed-v1"

compress(input_path, output_path, filename)
```

## Customization

- Modify the `input_path`, `output_path`, and `filename` variables to suit your needs.
- Adjust logging levels in `logging.basicConfig(level=logging.ERROR)` to control the verbosity of logs.

## Example Interaction

```bash
$ python main.py
Archive created successfully and saved to /path/to/output
```
