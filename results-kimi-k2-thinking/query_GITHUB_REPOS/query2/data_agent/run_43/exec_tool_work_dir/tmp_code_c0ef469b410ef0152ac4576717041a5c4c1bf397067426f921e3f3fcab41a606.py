code = """import json
import re

# Read the file from the previous query
file_path = var_functions.query_db_20

# Read the JSON file
with open(file_path, 'r') as f:
    swift_files = json.load(f)

print(f"Processing {len(swift_files)} Swift files")

# Parse copy count from repo_data_description
copy_count_pattern = r'(\d+)\s*(?:times|time)'

parsed_files = []
for file in swift_files:
    description = file.get('repo_data_description', '')
    match = re.search(copy_count_pattern, description)
    if match:
        copy_count = int(match.group(1))
        parsed_files.append({
            'id': file['id'],
            'repo_name': file['sample_repo_name'],
            'path': file['sample_path'],
            'copy_count': copy_count,
            'description': description
        })

# Sort by copy count descending
sorted_files = sorted(parsed_files, key=lambda x: x['copy_count'], reverse=True)

# Get the top 10 files
top_10 = sorted_files[:10]

print('__RESULT__:')
print(json.dumps({
    'top_files': top_10,
    'max_copy_count': top_10[0]['copy_count'] if top_10 else 0,
    'total_files_processed': len(parsed_files)
}, indent=2))"""

env_args = {'var_functions.list_db:0': ['languages', 'repos', 'licenses'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': [{'language_description': 'This repository is mainly written in Swift (16,364 bytes), with additional code in Ruby (7,243 bytes), Shell (94 bytes).'}, {'language_description': 'The codebase includes: Swift (109,540 bytes), Ruby (3,068 bytes), Shell (762 bytes).'}, {'language_description': 'The codebase includes: Swift (18,238 bytes), Ruby (716 bytes), Shell (211 bytes).'}, {'language_description': 'The majority of the code is in Swift (1,723,695 bytes), followed by Shell (17,716 bytes), Ruby (297 bytes).'}, {'language_description': 'While most of the project is built in Swift (585,714 bytes), it also incorporates Ruby (3,447 bytes), Shell (190 bytes).'}, {'language_description': 'The codebase includes: Swift (33,632 bytes), Shell (711 bytes), Ruby (434 bytes).'}, {'language_description': 'The majority of the code is in Swift (747,765 bytes), followed by Ruby (3,949 bytes), Shell (393 bytes).'}, {'language_description': 'While most of the project is built in Swift (419,579 bytes), it also incorporates Ruby (767 bytes), Shell (169 bytes).'}, {'language_description': 'While most of the project is built in Swift (87,439 bytes), it also incorporates Ruby (2,165 bytes), Shell (65 bytes).'}, {'language_description': 'While most of the project is built in Swift (71,711 bytes), it also incorporates Shell (3,156 bytes), Ruby (3,009 bytes).'}], 'var_functions.query_db:11': 'file_storage/functions.query_db:11.json', 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json', 'var_functions.query_db:12': [], 'var_functions.query_db:14': 'file_storage/functions.query_db:14.json', 'var_functions.query_db:20': 'file_storage/functions.query_db:20.json'}

exec(code, env_args)
