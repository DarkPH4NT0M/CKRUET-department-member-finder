# CKRUET Department Allocation Extractor

This script extracts and displays department allocation results from the CKRUET department allocation PDF. It provides options to search for specific department lists, display full department-wise allocation, and save the results to text files.

## Features

- **Extract a Specific Department-University List**: Retrieve and display the list of candidates for a specific department and university.
- **Display Department-Wise Full Allocation**: Show the full allocation for all departments and universities.
- **Save All Allocations**: Save each department's allocation to a text file.

## Requirements

- Python 3.x
- PyPDF2 library

You can install the required library using:

```bash
pip install PyPDF2
```

## Usage

### Command-Line Arguments

- `pathToFile` (optional): Path to the PDF file. If not provided, the script will search for a PDF file in the current directory.
- `-f` or `--file`: Path to the PDF file.
- `-a` or `--all`: Display all department allocations.
- `-A` or `--saveall`: Save all department allocations to text files in the current directory.
- `-d` or `--dept`: Department-University name. If specified, the script will extract and display the list for this department.

### Examples

**1. Extracting a specific Department-University list:**

```bash
python alpha_extract.py -d MTE-RUET
```

**2. Displaying department-wise full allocation:**

```bash
python alpha_extract.py -a
```

**3. Displaying and saving all department allocations:**

```bash
python alpha_extract.py -A
```

**4. Providing a PDF file path:**

```bash
python alpha_extract.py -f path/to/your/pdf_file.pdf
```

**5. Combining options:**

```bash
python alpha_extract.py -f path/to/your/pdf_file.pdf -A
```

## How It Works

1. **Finding the PDF File**: The script first checks if a PDF file path is provided via command-line arguments. If not, it searches the current directory for a PDF file.
2. **Extracting Text**: It extracts text from each relevant page of the PDF.
3. **Processing Data**: Depending on the provided options, it either extracts a specific department list, displays full department allocations, or saves allocations to text files.

## Notes

- Ensure that you have downloaded the correct allocation pdf from [the official website](https://admissionckruet.ac.bd/notice.php).
- If the script doesn't find any PDF file or encounters an error, it will display an appropriate message and exit.


## Contact

For any questions or issues, please open a GitHub issue!