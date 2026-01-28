code = """import os
import json

# Check if the UC patents file exists and what it contains
uc_file = 'var_functions.query_db:8'
print(f"Checking UC file: {uc_file}")
print(f"Exists: {os.path.exists(uc_file)}")

if os.path.exists(uc_file):
    with open(uc_file, 'r') as f:
        content = f.read()
        print(f"File size: {len(content)} characters")
        print(f"Content preview: {content[:200]}")
        
        # Try to parse as JSON
        try:
            uc_data = json.loads(content)
            print(f"JSON parsed successfully. Type: {type(uc_data)}, Length: {len(uc_data) if hasattr(uc_data, '__len__') else 'N/A'}")
            if isinstance(uc_data, list) and uc_data:
                print(f"First item type: {type(uc_data[0])}")
                print(f"First item keys: {list(uc_data[0].keys()) if isinstance(uc_data[0], dict) else 'Not a dict'}")
        except Exception as e:
            print(f"JSON parse error: {e}")
else:
    print("UC file does not exist")

print("\n" + "="*50)

# Check the all patents file
all_file = 'var_functions.query_db:36'
print(f"Checking all patents file: {all_file}")
print(f"Exists: {os.path.exists(all_file)}")

if os.path.exists(all_file):
    with open(all_file, 'r') as f:
        content = f.read()
        print(f"File size: {len(content)} characters")
        print(f"Content preview: {content[:200]}")
        
        # Try to parse as JSON
        try:
            all_data = json.loads(content)
            print(f"JSON parsed successfully. Type: {type(all_data)}, Length: {len(all_data) if hasattr(all_data, '__len__') else 'N/A'}")
        except Exception as e:
            print(f"JSON parse error: {e}")
else:
    print("All patents file does not exist")

print('__RESULT__:')
print(json.dumps('File check completed'))"""

env_args = {'var_functions.list_db:0': ['publicationinfo'], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.list_db:6': ['cpc_definition'], 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.query_db:14': 'file_storage/functions.query_db:14.json', 'var_functions.query_db:22': 'file_storage/functions.query_db:22.json', 'var_functions.query_db:24': [{'symbol': 'A', 'titleFull': 'HUMAN NECESSITIES'}, {'symbol': 'B', 'titleFull': 'PERFORMING OPERATIONS; TRANSPORTING'}, {'symbol': 'C', 'titleFull': 'CHEMISTRY; METALLURGY'}], 'var_functions.execute_python:32': {'uc_patents_count': 169, 'all_patents_count': 20000, 'uc_pub_numbers_count': 59}, 'var_functions.query_db:34': 'file_storage/functions.query_db:34.json', 'var_functions.query_db:36': 'file_storage/functions.query_db:36.json', 'var_functions.execute_python:38': {'uc_patents': 0, 'uc_pub_numbers': 0, 'total_citations': 0, 'unique_assignees': 0, 'sample_assignees': []}}

exec(code, env_args)
