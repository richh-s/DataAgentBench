code = """import json
import re

# Load the Swift files data
swift_files_path = var_functions.query_db:20

# Read the JSON file
with open(swift_files_path, 'r') as f:
    swift_files = json.load(f)

print('Total Swift files:', len(swift_files))

# Parse copy counts from repo_data_description
copy_count_pattern = r'(\d+)\s*(times|times\.|times\b)'
file_copy_counts = []

for file_info in swift_files:
    description = file_info['repo_data_description']
    
    # Look for patterns like "duplicated X times", "appearing X times", "repeated X times", "copied X times"
    match = re.search(r'(\d+)\s*times', description)
    if match:
        copy_count = int(match.group(1))
        file_copy_counts.append({
            'id': file_info['id'],
            'repo_name': file_info['sample_repo_name'],
            'copy_count': copy_count,
            'description': description
        })

# Sort by copy count in descending order
file_copy_counts.sort(key=lambda x: x['copy_count'], reverse=True)

print('\nTop 20 most copied Swift files:')
for i, file_info in enumerate(file_copy_counts[:20]):
    print(f"{i+1}. {file_info['repo_name']}")
    print(f"   File ID: {file_info['id']}")
    print(f"   Copy count: {file_info['copy_count']}")
    print(f"   Description: {file_info['description'][:100]}...")
    print()

# Find the most frequently copied file
if file_copy_counts:
    most_copied = file_copy_counts[0]
    print('=== MOST COPIED SWIFT FILE ===')
    print(f"File ID: {most_copied['id']}")
    print(f"Repository: {most_copied['repo_name']}")
    print(f"Copy count: {most_copied['copy_count']}")
    print(f"Description: {most_copied['description']}")
    
    # Save result
    result = {
        'repository': most_copied['repo_name'],
        'file_id': most_copied['id'],
        'copy_count': most_copied['copy_count']
    }
else:
    print('No copy count information found')
    result = None

# Print result in required format
print('\n__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['languages', 'repos', 'licenses'], 'var_functions.list_db:1': ['commits', 'contents', 'files'], 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json', 'var_functions.query_db:6': [{'total_rows': '24286'}], 'var_functions.query_db:7': [{'total_rows': '524077'}], 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json', 'var_functions.query_db:18': 'file_storage/functions.query_db:18.json', 'var_functions.query_db:20': 'file_storage/functions.query_db:20.json'}

exec(code, env_args)
