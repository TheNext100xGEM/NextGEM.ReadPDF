import PyPDF2
import requests
import re


# URL of the PDF file on the website
pdf_url = 'https://rehold.io/whitepaper-v2.pdf'  # Replace with the PDF URL

# Download the PDF
response = requests.get(pdf_url)
with open('downloaded.pdf', 'wb') as pdf_file:
    pdf_file.write(response.content)

# Open and extract text from the PDF
with open('downloaded.pdf', 'rb') as pdf_file:
    pdf_reader = PyPDF2.PdfReader(pdf_file)
    
    extracted_text = ''
    for page_num in range(len(pdf_reader.pages)):
        page = pdf_reader.pages[page_num]
        text = page.extract_text()
        text = re.sub(r'\n', ' ', text)  # Remove newlines and replace with spaces
        extracted_text += text

# Print or process the extracted text as needed
print(extracted_text)