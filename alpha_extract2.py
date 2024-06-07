import PyPDF2

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

# Extract information for candidates allocated to MTE-RUET
mte_ruet_candidates = []
for line in lines[5:]:  # Skip the header lines
    parts = line.split()
    if len(parts) >= 5 and parts[-1] == 'MTE-RUET':  # Check if allocated to MTE-RUET
        admission_roll = parts[1]
        name = ' '.join(parts[2:-2])  # Join the name parts
        merit = parts[-2]
        department_university = parts[-1]
        mte_ruet_candidates.append((admission_roll, name, merit, department_university))

# Print the extracted information for MTE-RUET candidates
for candidate in mte_ruet_candidates:
    print("Admission Roll:", candidate[0])
    print("Name:", candidate[1])
    print("Merit:", candidate[2])
    print("Department-University:", candidate[3])
    print()
