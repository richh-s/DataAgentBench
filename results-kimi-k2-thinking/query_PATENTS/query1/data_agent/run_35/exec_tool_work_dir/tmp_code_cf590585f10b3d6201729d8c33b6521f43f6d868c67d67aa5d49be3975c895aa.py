code = """# Based on the message, the full result is stored in a file
# Let's check what variables are available
import json
import os

# Check available variables
available_vars = list(locals().keys()) + list(globals().keys())
print("Available variables:", [v for v in available_vars if 'var_' in str(v)])

# The storage key is var_functions.query_db:8
# If it's a string path, we need to read the file
storage_key = 'var_functions.query_db:8'
if storage_key in locals():
    file_path = locals()[storage_key]
elif storage_key in globals():
    file_path = globals()[storage_key]
else:
    file_path = None

print("File path from storage:", file_path)

if file_path and isinstance(file_path, str) and os.path.exists(file_path):
    print("File exists, reading...")
    with open(file_path, 'r') as f:
        data = json.load(f)
    print("Loaded data:", type(data), len(data))
    print("First record:", data[0])
elif isinstance(file_path, list):
    print("Data is directly available as list")
    data = file_path
    print("Data length:", len(data))
else:
    print("Could not load data")
    data = []

# Now let's process the data
if data:
    # Parse CPC codes and extract year from publication_date
    cpc_years = []
    
    for record in data:
        # Parse publication date
        pub_date = record.get('publication_date', '')
        if pub_date:
            # Extract year using regex
            year_match = pub_date.split()[-1]
            try:
                year = int(year_match)
            except:
                continue
                
            # Parse CPC codes (JSON string)
            cpc_str = record.get('cpc', '[]')
            try:
                if isinstance(cpc_str, str):
                    cpc_list = json.loads(cpc_str)
                else:
                    cpc_list = cpc_str
                    
                for cpc_item in cpc_list:
                    cpc_code = cpc_item.get('code', '')
                    if cpc_code:
                        cpc_years.append({'cpc': cpc_code, 'year': year})
            except:
                continue
    
    print("Total CPC-year pairs:", len(cpc_years))
    if cpc_years:
        df = pd.DataFrame(cpc_years)
        print("Sample data:", df.head())
        print("Year range:", df['year'].min(), "to", df['year'].max())
        
        # Save processed data
        processed_file = '/tmp/cpc_years_data.json'
        df.to_json(processed_file, orient='records')
        print("Saved processed data to", processed_file)
        
        __RESULT__ = json.dumps(processed_file)"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json'}

exec(code, env_args)
