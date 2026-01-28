code = """import json
import os

# Access the result from the file path stored in the variable
file_path = locals()['var_functions.query_db:0']
print("File path:", file_path)

# Check if file exists and read it
if os.path.exists(file_path):
    with open(file_path, 'r') as f:
        data = json.load(f)
    
    print("Number of records:", len(data))
    
    if len(data) > 0:
        # Examine first record structure
        first_keys = list(data[0].keys())
        print("Keys:", first_keys)
        
        # Sample data
        print("\nSample Patents_info:")
        print(data[0]['Patents_info'][:300])
        
        # Check for California-related patents
        print("\nChecking for California in Patents_info...")
        calif_records = []
        for i, rec in enumerate(data):
            patents_info = rec['Patents_info']
            if 'CALIFORNIA' in patents_info or 'UNIV' in patents_info:
                calif_records.append((i, patents_info[:200]))
                if len(calif_records) <= 3:
                    print(f"\nRecord {i}:")
                    print(patents_info[:200])
        
        print(f"\nTotal records mentioning CALIFORNIA/UNIV: {len(calif_records)}")

else:
    print("File not found")"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json'}

exec(code, env_args)
