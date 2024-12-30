import csv

def save_data_to_csv(data, file_path):
    """
    Save the extracted data to a CSV file.
    :param data: The extracted data (list of dictionaries or a similar structure)
    :param file_path: The path to save the CSV file
    """
    if not data:
        raise ValueError("No data to save to CSV.")
    
    # Get the headers from the keys of the first dictionary in the data
    headers = data[0].keys()
    
    # Write the data to CSV
    with open(file_path, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=headers)
        writer.writeheader()  # Write the header
        writer.writerows(data)  # Write the data rows
