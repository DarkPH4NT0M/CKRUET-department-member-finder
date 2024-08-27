import PyPDF2
import re
import sys
import os
import argparse



# Checking flags
parser = argparse.ArgumentParser(description="Script to extract and display department allocation results from a CKRUET department allocation PDF.")
parser.add_argument("pathToFile", nargs="?", help="Path/To/PDF File.pdf")
parser.add_argument("-f", "--file", help="Path/To/PDF File.pdf")
parser.add_argument("-a", "--all", action="store_true", help="Display all department allocation.")
parser.add_argument("-A", "--saveall", action="store_true", help="Save all department allocations to current directory.")
parser.add_argument("-d", "--dept", help="Department-University name")
args = parser.parse_args()


def find_pdf_file():
    file = args.file or args.pathToFile
    if file and file.endswith(".pdf") and os.path.exists(file):
        return file

    else:
        print("No argument passed. Searching for .pdf file in current directory")
        for file in os.listdir():
            if file.endswith(".pdf"):
                return file
    return None

def dept_search(dept_uni=""):
    # Option 1: Extract a specific DEPT-UNI list
    if dept_uni == "":
        if args.dept:
            dept_uni = args.dept
        else:
            dept_uni = input("Which DEPT-UNI list you need? Example: MTE-RUET\n> ")

    dept_uni = dept_uni.upper()

    print(f"Extracting members list of {dept_uni}")

    # Extract information for candidates allocated to dept_uni
    dept_uni_candidates = []
    for line in lines[5:]:  # Skip the header lines
        parts = re.split(r'\s+', line)
        if len(parts) >= 5 and parts[-1] == dept_uni:  # Check if allocated to DEPT-UNI
            admission_roll = parts[1]
            name = ' '.join(parts[2:-2])  # Join the name parts
            merit = parts[-2]
            department_university = parts[-1]
            dept_uni_candidates.append((admission_roll, name, merit, department_university))

    # Print the extracted information for DEPT-UNI candidates
    position = 1
    for candidate in dept_uni_candidates:
        print("Admission Roll:", candidate[0])
        print("Name:", candidate[1])
        print("Merit:", candidate[2])
        print("Department-University:", candidate[3])
        print(f"Position in Department: {position}")
        position += 1
        print()

    if position > 1 :
        # Process the lines to extract members info and write to the output file
        print(f"{position-1} members found for {dept_uni}!")
        output_file_path = f"{dept_uni}.txt"
        position = 1
        with open(output_file_path, 'w') as output_file:
            for candidate in dept_uni_candidates:
                output_file.write(f"Admission Roll: {candidate[0]}\n")
                output_file.write(f"Name: {candidate[1]}\n")
                output_file.write(f"Merit: {candidate[2]}\n")
                output_file.write(f"Department-University: {candidate[3]}\n")
                output_file.write(f"Position in Department: {position}\n")
                output_file.write("\n")
                position += 1

        print(f"Members list created as {output_file_path}")
    else:
        print(f"No member found for {dept_uni}")


def full_search():
    # Option 2: Display department-wise full allocation
    print("Displaying department-wise full allocation")

    dept_merit_ranges = {}
    for line in lines[5:]:  # Skip the header lines
        parts = re.split(r'\s+', line)
        # Check if the last part is an uppercase DEPT-UNI code
        if len(parts) >= 5 and parts[-1].isupper() and parts[-2].isdigit():
            merit = parts[-2]
            department_university = parts[-1]

            if department_university not in dept_merit_ranges:
                dept_merit_ranges[department_university] = [merit, merit]  # Initialize with first merit as both first and last
            else:
                # Update the last merit as the current merit
                dept_merit_ranges[department_university][1] = merit

    # Prepare output for both console display and file writing
    output_lines = []
    target_dept_uni = "MTE-RUET"  # DEPT-UNI to be printed in yellow

    for dept, (first_merit, last_merit) in dept_merit_ranges.items():
        if args.saveall:
            dept_search(dept)

        line = f"{dept} : {first_merit} - {last_merit}"
        if dept == target_dept_uni:
            # Print the target DEPT-UNI in yellow
            print(f"\033[93m{line}\033[0m")
        else:
            print(line)
        output_lines.append(line)

    # Write the department-wise allocation to a file
    output_file_path = "Department wise full allocation.txt"
    with open(output_file_path, 'w') as output_file:
        for line in output_lines:
            output_file.write(line + "\n")
        output_file.write("Code Courtesy: Ragib Rownak [MTE-RUET'23]")
    print(f"Department-wise allocation saved as {output_file_path} \n")
    print("\033[92mCode Courtesy: Ragib Rownak [MTE-RUET'23]\033[0m \n")






if __name__ == "__main__":
    # Find the PDF file in the current directory
    pdf_path = find_pdf_file()
    print(f"Working with {pdf_path}...")


    if not pdf_path:
        sys.exit("Error: No PDF file found in the current directory.")

    try:
        # Open the PDF file
        with open(pdf_path, 'rb') as pdf_file:
            # Create a PDF reader object
            pdf_reader = PyPDF2.PdfReader(pdf_file)

            # Extract text from each page
            text = ''
            for page_num in range(len(pdf_reader.pages)):
                page = pdf_reader.pages[page_num]
                page_text = page.extract_text()

                # Check if the page contains the required headers (indicating a relevant page)
                if re.search(r'Application No|Admission Roll|Name|Merit', page_text):
                    text += page_text
                else:
                    print(f"Skipping irrelevant page: {page_num + 1}")

    except KeyboardInterrupt as e:
        sys.exit("Keyboard Interrupted. Exiting...")
    except Exception as e:
        sys.exit(f"An error occurred: {str(e)}")

    # Split the text by newline to get each line separately
    lines = text.split('\n')


    if args.dept:
        dept_search()

    elif args.all or args.saveall:
        full_search()

    else:
        # Prompt the user to choose an option
        print("Choose an option:")
        print("1. Extract a specific DEPT-UNI list")
        print("2. Display department-wise full allocation")
        choice = input("Enter your choice (1 or 2): ")

        if choice == '1':
            dept_search()

        elif choice == '2':
            full_search()

        else:
            print("Invalid choice. Please run the script again and enter 1 or 2.")
