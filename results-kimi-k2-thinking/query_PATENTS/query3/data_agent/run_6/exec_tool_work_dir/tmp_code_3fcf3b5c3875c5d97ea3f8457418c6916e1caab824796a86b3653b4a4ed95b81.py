code = """import json
import os

file_path = locals()['var_functions.query_db:0']
print('File path:', file_path)

if os.path.exists(file_path):
    with open(file_path, 'r') as f:
        data = json.load(f)
    
    print('Number of records:', len(data))
    
    if len(data) > 0:
        first_keys = list(data[0].keys())
        print('Keys:', first_keys)
        
        print('\nSample Patents_info (first 300 chars):')
        print(data[0]['Patents_info'][:300])
        
        calif_count = 0
        for rec in data:
            if 'CALIFORNIA' in rec['Patents_info']:
                calif_count += 1
        
        print('\nRecords mentioning CALIFORNIA:', calif_count)
        
        unif_count = 0
        for rec in data:
            if 'UNIV' in rec['Patents_info']:
                unif_count += 1
        
        print('Records mentioning UNIV:', unif_count)

else:
    print('File not found')"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json'}

exec(code, env_args)
