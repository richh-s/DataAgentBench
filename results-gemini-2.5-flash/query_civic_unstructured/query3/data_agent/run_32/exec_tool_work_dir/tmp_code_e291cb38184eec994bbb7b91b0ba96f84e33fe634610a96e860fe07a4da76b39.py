code = """import json
import re

# Load the full JSON result from the file
file_path = locals()['var_function-call-12540492671589378295']
with open(file_path, 'r') as f:
    civic_docs = json.load(f)

relevant_lines = set() # Use a set to store unique relevant lines

for doc in civic_docs:
    text = doc['text']
    lines = text.split('\n')
    
    for line in lines:
        stripped_line = line.strip()
        if 'emergency' in stripped_line.lower() or 'fema' in stripped_line.lower():
            relevant_lines.add(stripped_line)

# Convert the set to a list of dictionaries for consistent output format
output_list = [{'line': line} for line in sorted(list(relevant_lines))]

print("__RESULT__:")
print(json.dumps(output_list, ensure_ascii=False))"""

env_args = {'var_function-call-12540492671589378295': 'file_storage/function-call-12540492671589378295.json'}

exec(code, env_args)
