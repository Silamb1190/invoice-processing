from ftplib import FTP

def fetch_pdfs_from_ftp():
    """
    Fetch PDF file names from an FTP server.
    :return: List of PDF file names
    """
    try:
        ftp = FTP('14.97.231.242')  # Replace with your FTP server details
        ftp.login('ADMS', 'h4y4SSnH')  # Replace with your FTP login credentials
        ftp.cwd('/Resource_Brandvault_Input/RPC0058SSE0001/')  # Change to the appropriate directory on the FTP server
        
        # List files in the current directory
        files = ftp.nlst()  # Get a list of file names in the current directory
        
        # Filter to get only PDF files
        pdf_files = [file for file in files if file.endswith('.pdf')]
        
        ftp.quit()  # Close the connection
        return pdf_files
    
    except Exception as e:
        raise ValueError(f"Error fetching PDFs from FTP: {str(e)}")
