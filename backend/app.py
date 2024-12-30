from flask import Flask, jsonify, request, render_template
from backend.extract_pdf import extract_pdf_data
from backend.supabase_utils import save_data_to_supabase
from backend.ftp_utils import fetch_pdfs_from_ftp
from backend.csv_utils import save_data_to_csv  # Ensure this import is correct
import os

# Initialize Flask app
app = Flask(__name__, static_folder='frontend', template_folder='templates')

# Route to serve the index.html page
@app.route('/')
def index():
    return render_template('index.html')  # This looks in the templates folder by default

# Route to handle the extraction of invoice data from the provided PDF
@app.route('/extract-invoice', methods=['POST'])
def extract_invoice():
    try:
        # Get the path of the uploaded PDF from the request
        invoice_pdf_path = request.json.get('pdf_path')
        
        if not invoice_pdf_path:
            return jsonify({"error": "PDF file path not provided"}), 400
        
        # Extract data from the PDF
        extracted_data = extract_pdf_data(invoice_pdf_path)
        
        # Save data to Supabase (or another database)
        save_data_to_supabase(extracted_data)
        
        # Optionally, save data to CSV
        if not os.path.exists('output'):
            os.makedirs('output', exist_ok=True)  # Safe directory creation with exist_ok
        csv_file_path = f"output/{os.path.basename(invoice_pdf_path).replace('.pdf', '.csv')}"
        save_data_to_csv(extracted_data, csv_file_path)

        return jsonify({"status": "success", "extracted_data": extracted_data}), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Route to fetch PDF files from FTP
@app.route('/fetch-pdfs', methods=['GET'])
def fetch_pdfs():
    try:
        # Fetch PDF files from FTP
        pdf_files = fetch_pdfs_from_ftp()
        return jsonify(pdf_files), 200
    except Exception as e:
        return jsonify({"error": f"Failed to fetch PDFs: {str(e)}"}), 500

# Starting the Flask application
if __name__ == '__main__':
    app.run(debug=True)
