code = """import json
import os

# Get the file path from the stored variable
file_path = var_functions.query_db:0
print("File path:", file_path)

# Check if file exists and read it
if os.path.exists(file_path):
    with open(file_path, 'r') as f:
        data = json.load(f)
    
    print("Number of records:", len(data))
    
    if len(data) > 0:
        # Show first record keys
        print("Keys in first record:", list(data[0].keys()))
        
        # Examine Patents_info structure
        print("\nSample Patents_info:")
        print(data[0]['Patents_info'][:200])
        
        # Check if we can find California in our sample
        calif_count = 0
        for rec in data:
            if 'CALIFORNIA' in rec['Patents_info'] or 'California' in rec['Patents_info']:
                calif_count += 1
                if calif_count <= 3:
                    print(f"\nCalifornia record {calif_count}:")
                    print(rec['Patents_info'])
        
        print(f"\nTotal records mentioning California (in sample of {len(data)}): {calif_count}")

else:
    print("File not found")"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json'}

exec(code, env_args)
