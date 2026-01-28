code = """import json, re

# Load funding data with amounts > $50k
funding_file_path = var_functions.query_db:0
with open(funding_file_path) as f:
    funding_data = json.load(f)

# Create funding lookup
funding_lookup = set()
for f in funding_data:
    if int(f['Amount']) > 50000:
        funding_lookup.add(f['Project_Name'])

# Load civic documents
civic_file_path = var_functions.query_db:2
with open(civic_file_path) as f:
    civic_docs = json.load(f)

# Extract project names from design sections
extracted_projects = []

for doc in civic_docs:
    text = doc.get('text', '')
    
    # Find design section
    design_marker = 'Capital Improvement Projects (Design)'
    design_pos = text.find(design_marker)
    if design_pos == -1:
        continue
    
    # Get section after marker
    section = text[design_pos + len(design_marker):]
    
    # Limit section to next major heading
    for marker in ['Capital Improvement Projects (Construction)', 'Capital Improvement Projects (Not Started)', 'Disaster Recovery Projects']:
        pos = section.find(marker)
        if pos != -1:
            section = section[:pos]
            break
    
    # Parse potential project names
    parts = section.split('\n\n')
    for part in parts:
        part = part.strip()
        if len(part) >= 10 and 'Updates:' not in part and 'Schedule:' not in part and not part.startswith('('):
            first_line = part.split('\n')[0].strip()
            if len(first_line) > 10 and not first_line.isupper():
                # Clean up common bullets
                clean_name = re.sub(r'^[A-Z]\.\s*', '', first_line)
                clean_name = re.sub(r'^\d+\.\s*', '', clean_name)
                if len(clean_name) > 10:
                    extracted_projects.append(clean_name)

# Match with funding
match_count = 0
for proj in extracted_projects:
    for fund_name in funding_lookup:
        if proj in fund_name or fund_name in proj:
            match_count += 1
            break

print('__RESULT__:')
print(json.dumps(match_count))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:10': [{'count': '276'}]}

exec(code, env_args)
