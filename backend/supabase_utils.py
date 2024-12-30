from supabase import create_client, Client

# Initialize Supabase client
url = "https://enmxioqjkfvsbzwqtwfu.supabase.co"  # Replace with your Supabase URL
key = "process.env.SUPABASE_KEY"  # Replace with your Supabase service key
supabase: Client = create_client(url, key)

def save_data_to_supabase(data):
    """
    Save extracted invoice data to Supabase.
    :param data: The extracted data (list of dictionaries)
    """
    if not data:
        raise ValueError("No data to save to Supabase.")
    
    try:
        table = supabase.table('invoices')  # Replace with your actual table name
        response = table.insert(data).execute()
        if response.status_code != 201:
            raise ValueError(f"Failed to insert data into Supabase: {response}")
    except Exception as e:
        raise ValueError(f"Error saving data to Supabase: {str(e)}")
