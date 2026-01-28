code = """import json
import re

# Load the full civic docs data
civic_docs_file = var_functions.query_db:5
with open(civic_docs_file, 'r') as f:
    civic_docs = json.load(f)

print('Total civic docs:', len(civic_docs))

# Initialize list to capture potential project names
potential_projects = []

# Iterate over each document and search for pattern
for doc in civic_docs:
    text = doc.get('text', '')
    # Find all occurrences where 'Park' and 'completed' and '2022' appear in the text
    if re.search(r'Park', text) and re.search(r'completed', text, re.IGNORECASE) and re.search(r'2022', text):
        # Split text into lines
        lines = text.splitlines()
        # Heuristic: capture lines that look like project names (maybe title case) containing Park
        for i, line in enumerate(lines):
            stripped = line.strip()
            # If line contains 'Park' and is not empty, and next line maybe contains 'Updates:'
            if re.search(r'Park', stripped, re.IGNORECASE):
                # Look ahead for 'completed' and '2022' in subsequent lines (maybe within 5 lines)
                snippet = '\n'.join(lines[i:i+10])
                if re.search(r'completed', snippet, re.IGNORECASE) and re.search(r'2022', snippet):
                    potential_projects.append(stripped)

# Remove duplicates while preserving order
seen = set()
unique_projects = []
for p in potential_projects:
    if p not in seen:
        seen.add(p)
        unique_projects.append(p)

print('Potential park projects with completed 2022:', unique_projects)
print('Count:', len(unique_projects))

# Save the list for later matching
result = {'potential_projects': unique_projects, 'count': len(unique_projects)}
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': [], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json'}

exec(code, env_args)
