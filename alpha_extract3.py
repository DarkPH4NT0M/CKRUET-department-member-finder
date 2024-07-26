import PyPDF2
import re

# Path to the PDF file
pdf_path = "alpha.pdf"


# Open the PDF file
with open(pdf_path, 'rb') as pdf_file:
    # Create a PDF reader object
    pdf_reader = PyPDF2.PdfReader(pdf_file)

    # Extract text from each page
    text = ''
    for page_num in range(len(pdf_reader.pages)):
        page = pdf_reader.pages[page_num]
        text += page.extract_text()

# Split the text by newline to get each line separately
lines = text.split('\n')

dept_uni= input("Which DEPT-UNI list you need?\n")
print ("Extracting members list of " + dept_uni)
# Extract information for candidates allocated to dept_uni
dept_uni_candidates = []
for line in lines[5:]:  # Skip the header lines
    parts = line.split()
    if len(parts) >= 5 and parts[-1] == dept_uni:  # Check if allocated to DEPT-UNI
        admission_roll = parts[1]
        name = ' '.join(parts[2:-2])  # Join the name parts
        merit = parts[-2]
        department_university = parts[-1]
        dept_uni_candidates.append((admission_roll, name, merit, department_university))

# Print the extracted information for DEPT-UNI candidates
position= int(1)
for candidate in dept_uni_candidates:
    print("Admission Roll:", candidate[0])
    print("Name:", candidate[1])
    print("Merit:", candidate[2])
    print("Department-University:", candidate[3])
    print(f"Position in Department: {position}")
    position+=1
    print()



# Process the lines to extract members info and write to the output file
output_file_path = f"{dept_uni}.txt"
position = int(1)
with open(output_file_path, 'w') as output_file:
    for candidate in dept_uni_candidates:
        output_file.write(f"Admission Roll:{candidate[0]}\n")
        output_file.write(f"Name:{candidate[1]}\n")
        output_file.write(f"Merit:{candidate[2]}\n")
        output_file.write(f"Department-University:{candidate[3]}\n")
        output_file.write(f"Position in Department: {position}\n")
        output_file.write(f"\n")
        position +=1
        

print(f"Members list created as {dept_uni}.txt")


