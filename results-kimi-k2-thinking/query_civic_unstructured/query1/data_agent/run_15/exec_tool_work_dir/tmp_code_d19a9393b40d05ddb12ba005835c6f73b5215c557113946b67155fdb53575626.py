code = """import json

# Load the funding data
f_path = locals()['var_functions.query_db:64']
with open(f_path) as f:
    funding = json.load(f)

# Load the civic documents  
d_path = locals()['var_functions.query_db:40']
with open(d_path) as f:
    docs = json.load(f)

# Get high funding project names (> $50,000)
high_funding = set()
for r in funding:
    amount = int(r['Amount'])
    if amount > 50000:
        high_funding.add(r['Project_Name'])

# Extract design project names from documents
design = []
for doc in docs:
    text = doc.get('text', '')
    marker = 'Capital Improvement Projects (Design)'
    if marker in text:
        start = text.find(marker) + len(marker)
        end = text.find('Capital Improvement Projects (Construction)', start)
        if end == -1:
            end = len(text)
        section = text[start:end]
        for line in section.split('\n'):
            line = line.strip()
            if len(line) > 15 and not line.startswith('('):
                if 'Updates:' not in line and 'Schedule:' not in line:
                    clean = line.strip()
                    if len(clean) > 15:
                        design.append(clean)

# Find matching projects
design_set = set(design)
exact_matches = high_funding.intersection(design_set)

# Try normalized matching if needed
norm_funding = {name.lower().strip() for name in high_funding}
norm_design = {name.lower().strip() for name in design_set}
all_matches = norm_funding.intersection(norm_design)

result = {
    'high_funding_total': len(high_funding),
    'design_projects_total': len(design_set),
    'matching_count': len(exact_matches),
    'normalized_match_count': len(all_matches)
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:32': [{'count': '276'}], 'var_functions.query_db:36': [], 'var_functions.query_db:38': 'file_storage/functions.query_db:38.json', 'var_functions.query_db:40': 'file_storage/functions.query_db:40.json', 'var_functions.query_db:64': 'file_storage/functions.query_db:64.json'}

exec(code, env_args)
