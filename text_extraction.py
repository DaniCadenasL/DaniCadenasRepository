from PyPDF2 import PdfReader

def pdf_to_text(pdf_path):
    """
    Converts a PDF file to text.
    
    Args:
        pdf_path (str): The path to the PDF file.
    
    Returns:
        str: The extracted text from the PDF file.
    """
    reader = PdfReader(pdf_path) # open the PDF file
    text = "" # Initialize an empty string to store the extracted text
    for page_num in range(len(reader.pages)): # Iterate through each page of the PDF
        page = reader.pages[page_num] # Get the current page
        text += page.extract_text() or "" # Extract text from the page and add it to the total text -- or "" ensures that if page.extract_text() returns None, an empty string is used instead, avoiding concatenation issues.
    return text # Return the complete extracted text
