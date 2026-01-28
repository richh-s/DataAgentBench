code = """import json
import re

# Load funding data
f_path = locals()['var_functions.query_db:5']
with open(f_path) as f:
    funding_records = json.load(f)

# Load civic documents
c_path = locals()['var_functions.query_db:2']
with open(c_path) as f:
    civic_docs = json.load(f)

# Step 1: Get all projects with funding > 50000
high_funding = {}
for rec in funding_records:
    amount = int(rec['Amount'])
    if amount > 50000:
        high_funding[rec['Project_Name']] = amount

# Step 2: Extract capital projects in design phase from civic docs
design_projects = []
for doc in civic_docs:
    text = doc.get('text', '')
    
    # Look for design projects section
    design_section = text.split('Capital Improvement Projects (Design)')
    if len(design_section) > 1:
        # Get the section until construction projects start
        section_text = design_section[1].split('Capital Improvement Projects (Construction)')[0]
        
        # Extract project names from lines
        for line in section_text.split('\n'):
            line = line.strip()
            if line and len(line) > 15 and line[0] not in ['(', '-', '•']:
                if 'Updates:' not in line and 'Schedule:' not in line:
                    clean_line = re.sub(r'^(cid:\d+)\s*', '', line)
                    if len(clean_line) > 15:
                        design_projects.append(clean_line)

# Step 3: Find matches (projects that are in both sets)
matches = []
for proj in design_projects:
    if proj in high_funding:
        matches.append({'project': proj, 'funding': high_funding[proj]})

# Output result
result = {
    'total_high_funding': len(high_funding),
    'total_design_projects': len(design_projects),
    'matching_projects_count': len(matches),
    'matching_projects': matches
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json'}

exec(code, env_args)
