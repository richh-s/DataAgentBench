code = """import json

# Load funding data - get all projects with amount > 50000
funding_file = locals()['var_functions.query_db:38']
with open(funding_file) as f:
    funding_records = json.load(f)

high_funding_names = set()
for record in funding_records:
    amount = int(record['Amount'])
    if amount > 50000:
        high_funding_names.add(record['Project_Name'])

# Load civic documents
docs_file = locals()['var_functions.query_db:40']
with open(docs_file) as f:
    civic_docs = json.load(f)

# Extract design projects from each document
design_names = []

for doc in civic_docs:
    text = doc.get('text', '')
    
    # Find the design section
    design_marker = 'Capital Improvement Projects (Design)'
    construction_marker = 'Capital Improvement Projects (Construction)'
    
    start_pos = text.find(design_marker)
    if start_pos >= 0:
        end_pos = text.find(construction_marker, start_pos)
        if end_pos < 0:
            end_pos = len(text)
        
        # Get the design section
        section = text[start_pos:end_pos]
        lines = section.split('\n')
        
        # Skip the header line
        for line in lines[1:]:
            line = line.strip()
            # Only keep lines that look like project names
            if len(line) > 15 and not line.startswith('(') and not line.startswith('Page'):
                if 'Updates:' not in line and 'Schedule:' not in line and 'Complete Design:' not in line:
                    # Clean up common markers
                    clean_line = line.replace('(cid:190)', '').replace('(cid:131)', '').strip()
                    if len(clean_line) > 15:
                        design_names.append(clean_line)

# Find matches
matches = []
for design_name in design_names:
    if design_name in high_funding_names:
        matches.append(design_name)

# Try fuzzy matching for close names
for design_name in design_names:
    if design_name not in matches:
        design_lower = design_name.lower()
        for fund_name in high_funding_names:
            fund_lower = fund_name.lower()
            # Check if one is contained in the other
            if design_lower in fund_lower or fund_lower in design_lower:
                if len(design_lower) > 10 or len(fund_lower) > 10:
                    matches.append(design_name)
                    break

# Remove duplicates
unique_matches = list(set(matches))

result = {
    'high_funding_projects': len(high_funding_names),
    'design_projects_found': len(design_names),
    'matching_projects': len(unique_matches)
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:32': [{'count': '276'}], 'var_functions.query_db:36': [], 'var_functions.query_db:38': 'file_storage/functions.query_db:38.json', 'var_functions.query_db:40': 'file_storage/functions.query_db:40.json'}

exec(code, env_args)
