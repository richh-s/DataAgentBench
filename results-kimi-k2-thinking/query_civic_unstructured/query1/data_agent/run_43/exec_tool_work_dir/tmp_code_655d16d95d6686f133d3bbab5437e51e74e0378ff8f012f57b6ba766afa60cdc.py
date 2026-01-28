code = """import json
import os

# Use the actual file paths
tmp_dir = '/root/tmp'
files = os.listdir(tmp_dir)

# Find the relevant files
funding_file = None
civic_file = None
for f in files:
    if 'query_db_60' in f:
        funding_file = os.path.join(tmp_dir, f)
    elif 'query_db_6' in f and '_60' not in f:
        civic_file = os.path.join(tmp_dir, f)

# Load data
with open(funding_file, 'r') as f:
    funding_records = json.load(f)

with open(civic_file, 'r') as f:
    civic_docs = json.load(f)

# Build funding map (already > 50000)
funding_names = [item['Project_Name'] for item in funding_records]

# Find capital improvement projects in design phase
design_projects = set()
for doc in civic_docs:
    text = doc.get('text', '')
    if 'Capital Improvement Projects' in text and 'Design' in text:
        # Extract project names from this document
        for line in text.split('\n'):
            line = line.strip()
            if line and len(line) > 5:
                # Skip obvious non-project lines
                if 'Page' in line or 'Schedule:' in line or 'Updates:' in line:
                    continue
                if line.startswith('•') or line[0].isupper():
                    clean = line.replace('•', '').strip()
                    if len(clean) > 8:
                        design_projects.add(clean)

# Count matches
count = 0
for design in design_projects:
    d_lower = design.lower()
    for funded in funding_names:
        f_lower = funded.lower()
        # Check if names are similar
        if (d_lower in f_lower or f_lower in d_lower) and abs(len(design) - len(funded)) < 40:
            count += 1
            break

result = {'count': count}
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.list_db:2': ['Funding'], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:60': 'file_storage/functions.query_db:60.json'}

exec(code, env_args)
