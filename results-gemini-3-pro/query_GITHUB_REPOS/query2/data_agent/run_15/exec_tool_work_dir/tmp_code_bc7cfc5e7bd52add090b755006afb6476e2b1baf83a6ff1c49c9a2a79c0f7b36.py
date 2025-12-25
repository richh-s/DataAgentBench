code = """import json
import re

# Get the file path from the variable
file_path = locals()['var_function-call-2551927007963219470']

# Load the JSON data
with open(file_path, 'r') as f:
    data = json.load(f)

max_copies = -1
best_id = None
best_sample_repo = None

# Regex to capture the number of copies
pattern = re.compile(r'(?:seen|appearing|duplicated|copied|repeated)\s+(\d+)\s+times')

for item in data:
    desc = item.get('repo_data_description', '')
    match = pattern.search(desc)
    if match:
        copies = int(match.group(1))
        if copies > max_copies:
            max_copies = copies
            best_id = item['id']
            best_sample_repo = item['sample_repo_name']

print("__RESULT__:")
print(json.dumps({'max_copies': max_copies, 'best_id': best_id, 'best_sample_repo': best_sample_repo}))"""

env_args = {'var_function-call-14304438012032230050': 'file_storage/function-call-14304438012032230050.json', 'var_function-call-6739222787129283358': [{'count_star()': '89'}], 'var_function-call-2551927007963219470': 'file_storage/function-call-2551927007963219470.json'}

exec(code, env_args)
