import PyPDF2

def extract_pdf_data(pdf_path):
    """
    Extract text from a PDF file.
    :param pdf_path: Path to the PDF file
    :return: Extracted text or structured data (modify this according to your needs)
    """
    extracted_data = []
    
    try:
        # Open the PDF file
        with open(pdf_path, 'rb') as file:
            pdf_reader = PyPDF2.PdfReader(file)
            text = ""
            
            # Loop through all pages and extract text
            for page_num in range(len(pdf_reader.pages)):
                page = pdf_reader.pages[page_num]
                text += page.extract_text()
                
            # Example: Parse the text (you may need more sophisticated parsing logic)
            extracted_data = parse_pdf_text(text)
            
    except Exception as e:
        raise ValueError(f"Error extracting PDF data: {str(e)}")
    
    return extracted_data

def parse_pdf_text(text):
    """
    Example function to parse the extracted text into structured data.
    Modify this based on the PDF format you are dealing with.
    :param text: Raw extracted text
    :return: Structured data (e.g., list of dictionaries)
    """
    # Dummy implementation, replace with actual parsing logic
    return [{"field1": "value1", "field2": "value2"}]  # Replace with actual parsing
