# CKRUET result analyzer

This Python script processes a PDF file to either extract department-specific information or display department-wise allocation range. 

## Prerequisites

- **Python 3.x** installed on your machine
- Required Python package: `PyPDF2`

To install the required package, run the following command:
```bash
pip install PyPDF2
```

## How to Use

1. **Create an empty folder.**
2. **Place the result PDF file and the Python script in that folder.**
3. **Run the Python script.**
4. **In the input field, input examples like:** `MTE-RUET`.

## Features

This script provides two options for processing the PDF file:

### 1. Extract a specific DEPT-UNI list
- You can extract the list of candidates allocated to a specific DEPT-UNI, such as `MTE-RUET`.
- The extracted information will be saved in a `.txt` file, and the console will display details like admission roll, name, merit, and position in the department.

### 2. Display department-wise full allocation range
- The script displays the full merit range allocation for each department.
- This information is also saved in a `.txt` file, and you can specify a DEPT-UNI (default: `MTE-RUET`) to be highlighted in the output.

## Example Input for specific department data

```bash
MTE-RUET
```


