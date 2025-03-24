# File Handling Utility

A Python script for validating file paths and copying files or directories from one location to another.

---

## Features

- Validates input and output paths
- Creates output directories if they do not exist
- Copies files or entire directories safely
- Logs errors and important operations

## Requirements

- Python 3.x
- `shutil`, `logging`, and `os` modules (built-in)

## Setup

### Clone the repository:

```bash
git clone https://github.com/crowned-prinx/prinx-sandbox.git
cd pyCopyPaste
```

### Install dependencies:

No external dependencies are required.

## File Structure

```
📂 project-root
│── 📄 utils  # Folder
    │── 📄 functions.py  # utility functions
│── 📄 main.py  # Main script
│── 📄 README.md  # Documentation
```

## Usage

Run the `main.py` with specified input and output paths:

```bash
python main.py
```

Modify the `input_path` and `output_path` variables in the script before running.

## Customization

- Update `input_path` and `output_path` with your desired directories.
- Modify logging levels for more detailed output.

## Example Interaction

```bash
python main.py
Operation was successful!
```

If an error occurs, it logs messages like:

```bash
python main.py
ERROR: Input path does not exist: /invalid/path
```
