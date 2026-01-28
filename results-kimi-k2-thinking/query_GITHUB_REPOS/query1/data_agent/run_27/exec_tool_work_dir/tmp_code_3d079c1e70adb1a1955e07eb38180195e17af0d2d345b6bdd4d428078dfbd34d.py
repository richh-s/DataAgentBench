code = """import json
import os
import glob

# Check all JSON files in /tmp
json_files = glob.glob('/tmp/*.json')
print("Available JSON files:", json_files)

# Try to find the most recent file or load all to see which one has our data
for filepath in json_files:
    try:
        with open(filepath, 'r') as f:
            data = json.load(f)
            if len(data) > 0 and 'repo_name' in data[0] and 'language_description' in data[0]:
                print(f"\nFound language data in {filepath}")
                print(f"Total records: {len(data)}")
                
                # Process the data
                python_repos = []
                non_python_repos = []
                
                for item in data:
                    if 'Python' in item.get('language_description', ''):
                        python_repos.append(item['repo_name'])
                    else:
                        non_python_repos.append(item['repo_name'])
                
                result = {
                    'total_repos': len(data),
                    'python_repos_count': len(python_repos),
                    'non_python_repos_count': len(non_python_repos)
                }
                
                print('__RESULT__:')
                print(json.dumps(result))
                break
    except Exception as e:
        continue
else:
    print("Could not find language data file")
    print('__RESULT__:')
    print(json.dumps({"status": "file_not_found"}))"""

env_args = {'var_functions.list_db:0': ['languages', 'repos', 'licenses'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json'}

exec(code, env_args)
