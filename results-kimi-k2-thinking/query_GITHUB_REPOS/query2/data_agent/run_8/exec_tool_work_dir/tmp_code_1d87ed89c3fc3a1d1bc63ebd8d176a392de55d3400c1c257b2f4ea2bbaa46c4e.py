code = """import json
import re

# Load the Swift files data with copy counts
swift_files_path = var_functions.query_db:10

with open(swift_files_path, 'r') as f:
    swift_files = json.load(f)

# Parse copy count from repo_data_description
parsed_files = []
for file in swift_files:
    desc = file['repo_data_description']
    
    # Extract copy count using regex
    copy_match = re.search(r'(duplicated|appearing|appears|copied|repeated)\s+(\d+)\s+times?', desc)
    if copy_match:
        copy_count = int(copy_match.group(2))
        parsed_files.append({
            'id': file['id'],
            'repo_name': file['sample_repo_name'],
            'copy_count': copy_count,
            'description': desc
        })

# Find the file with the maximum copy count
if parsed_files:
    max_copy_file = max(parsed_files, key=lambda x: x['copy_count'])
    print('__RESULT__:')
    print(json.dumps(max_copy_file))
else:
    print('__RESULT__:')
    print(json.dumps({'error': 'No parsed files found'}))"""

env_args = {'var_functions.list_db:0': ['languages', 'repos', 'licenses'], 'var_functions.query_db:2': [{'repo_name': 'juliandunn/rackspacecloud', 'language_description': 'The codebase includes: Ruby (22,438 bytes), Shell (465 bytes).'}, {'repo_name': 'xMarkusSpringerx/coloranalyzer', 'language_description': 'This repository is mainly written in Ruby (1,897 bytes), with additional code in Shell (115 bytes).'}, {'repo_name': 'michaellihs/gitlab', 'language_description': 'The codebase includes: Ruby (162,002 bytes), Shell (168 bytes).'}, {'repo_name': 'vyorkin/xftp', 'language_description': 'The majority of the code is in Ruby (25,709 bytes), followed by Shell (115 bytes).'}, {'repo_name': 'airatshigapov/drophunter', 'language_description': 'The majority of the code is in Ruby (4,198 bytes), followed by Shell (115 bytes).'}], 'var_functions.list_db:5': ['commits', 'contents', 'files'], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json'}

exec(code, env_args)
