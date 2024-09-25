from PyPDF2 import PdfReader
import os

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

def convert_pdfs_in_folder(input_folder, output_folder):
    """
    Converts all PDF files in a folder to text files and saves them in an output folder.
    
    Args:
        input_folder (str): The path to the folder containing the PDF files.
        output_folder (str): The path to the folder where the text files will be saved.
    """
    # Check if the output folder exists, if not, create it
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
        print(f"The output folder '{output_folder}' has been created.")

    # Check if the input folder exists
    if not os.path.exists(input_folder):
        print(f"The input folder '{input_folder}' does not exist.")
        return # Exits the function early if the input folder is not found.
        
    # Iterate through all files in the input folder
    for filename in os.listdir(input_folder):
        if filename.endswith(".pdf"): # Check if the file is a PDF
            pdf_path = os.path.join(input_folder, filename) # Construct the full path to the PDF file
            text = pdf_to_text(pdf_path)  # Convert the PDF to text
            text_filename = os.path.splitext(filename)[0] + '.txt' # Create the text file name
            text_path = os.path.join(output_folder, text_filename) # Construct the full path to the text file
            with open(text_path, 'w', encoding='utf-8') as text_file: # Open the text file for writing
                text_file.write(text) # Write the extracted text to the text file
            print(f"File '{text_filename}' created in the output folder.") 

# Replace 'pdf/data' with the path to your folder containing the PDF files
pdf_folder = 'data/pdf'
# Replace 'output_folder' with the path to the folder where you want to save the text files
output_folder = 'data/txt'

# Call the function to convert PDF files to text files
convert_pdfs_in_folder(pdf_folder, output_folder)
