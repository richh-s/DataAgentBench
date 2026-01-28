code = """import json
import os

# Get the file path from the stored variable
file_path = locals()['var_functions.query_db:0']
print('File path:', file_path)

# Check if file exists and read it
if os.path.exists(file_path):
    with open(file_path, 'r') as f:
        data = json.load(f)
    
    print('Number of records:', len(data))
    
    if len(data) > 0:
        # Show first record keys
        first_keys = list(data[0].keys())
        print('Keys:', first_keys)
        
        # Examine Patents_info structure
        print('\nSample Patents_info:')
        print(data[0]['Patents_info'][:300])
        
        # Look for UNIV CALIFORNIA specifically
        california_records = []
        for i, rec in enumerate(data[:1000]):  # Check first 1000 records
            if 'UNIV CALIFORNIA' in rec['Patents_info']:
                california_records.append((i, rec['Patents_info']))
        
        print('\nRecords with UNIV CALIFORNIA (in first 1000):', len(california_records))
        
        if california_records:
            print('\nExample UNIV CALIFORNIA record:')
            print(california_records[0][1])

else:
    print('File not found')"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json'}

exec(code, env_args)
