code = """import os
import json

# Check what files are actually in the results directory
result_dir = '/var/results/'
files = os.listdir(result_dir)
print("Files in /var/results/:")
for file in sorted(files):
    print(f"  {file}")
    if file.endswith('.json'):
        try:
            with open(os.path.join(result_dir, file), 'r') as f:
                data = json.load(f)
                print(f"    Type: {type(data)}, Length: {len(data) if hasattr(data, '__len__') else 'N/A'}")
                if isinstance(data, list) and len(data) > 0:
                    print(f"    Sample: {type(data[0])}")
        except Exception as e:
            print(f"    Error: {e}")"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.query_db:16': 'file_storage/functions.query_db:16.json'}

exec(code, env_args)
