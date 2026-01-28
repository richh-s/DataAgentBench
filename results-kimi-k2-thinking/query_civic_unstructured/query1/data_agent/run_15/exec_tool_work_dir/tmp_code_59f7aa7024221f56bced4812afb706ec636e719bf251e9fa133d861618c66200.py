code = """import json

# Load funding data
funding_path = locals()['var_functions.query_db:38']
with open(funding_path) as f:
    funding_records = json.load(f)

# Load civic documents
civic_path = locals()['var_functions.query_db:40']
with open(civic_path) as f:
    civic_docs = json.load(f)

# Create set of high-funding project names (> $50,000)
high_funding_names = set()
for record in funding_records:
    amount = int(record['Amount'])
    if amount > 50000:
        high_funding_names.add(record['Project_Name'])

# Extract capital projects with design status
design_project_names = []

for doc in civic_docs:
    text = doc.get('text', '')
    
    # Look for design projects section
    marker = 'Capital Improvement Projects (Design)'
    if marker in text:
        start = text.find(marker) + len(marker)
        end = text.find('Capital Improvement Projects (Construction)', start)
        if end == -1:
            end = len(text)
        
        section = text[start:end]
        lines = section.split('\n')
        
        for line in lines:
            line = line.strip()
            # Filter for actual project names
            if len(line) > 15 and not line.startswith('('):
                if 'Updates:' not in line and 'Schedule:' not in line:
                    clean = line.strip()
                    if len(clean) > 15:
                        design_project_names.append(clean)

# Count direct matches
exact_matches = [name for name in design_project_names if name in high_funding_names]

# Try normalized matching for close names
normalized_matches = []
if len(exact_matches) == 0:
    norm_funding = {name.lower().strip() for name in high_funding_names}
    for design_name in design_project_names:
        if design_name.lower().strip() in norm_funding:
            normalized_matches.append(design_name)

# Combine all matches
all_matches = list(set(exact_matches + normalized_matches))

count_result = {
    'high_funding_projects': len(high_funding_names),
    'design_projects': len(design_project_names),
    'matching_projects': len(all_matches)
}

print('__RESULT__:')
print(json.dumps(count_result))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:32': [{'count': '276'}], 'var_functions.query_db:36': [], 'var_functions.query_db:38': 'file_storage/functions.query_db:38.json', 'var_functions.query_db:40': 'file_storage/functions.query_db:40.json'}

exec(code, env_args)
