code = """import json

# Load funding data
with open(locals()['var_functions.query_db:64']) as f:
    funding = json.load(f)

# Load civic documents
with open(locals()['var_functions.query_db:40']) as f:
    docs = json.load(f)

print('DEBUG: Funding records:', len(funding))
print('DEBUG: Civic docs:', len(docs))

# High funding projects (>50000)
high_funding = set()
for r in funding:
    if int(r['Amount']) > 50000:
        high_funding.add(r['Project_Name'])

print('DEBUG: High funding projects:', len(high_funding))

# Extract design projects from civic docs
design = []
for d in docs:
    text = d.get('text', '')
    
    # Find design section
    start = text.find('Capital Improvement Projects (Design)')
    if start < 0:
        continue
    
    end = text.find('Capital Improvement Projects (Construction)', start)
    if end < 0:
        end = len(text)
    
    section = text[start:end]
    for line in section.splitlines():
        line = line.strip()
        # Skip empty lines and markers
        if len(line) < 15 or line.startswith('('):
            continue
        if 'Updates:' in line or 'Schedule:' in line:
            continue
        
        # Clean and add likely project names
        if 15 <= len(line) <= 200:
            clean_line = line.split('(cid')[0].strip()
            if clean_line:
                design.append(clean_line)

print('DEBUG: Design projects found:', len(design))

# Find matches (exact name match)
design_set = set(design)
exact_matches = high_funding.intersection(design_set)

print('DEBUG: Exact matches:', len(exact_matches))

# If no exact matches, try fuzzy matching
if len(exact_matches) == 0:
    norm_funding = {name.lower().strip() for name in high_funding}
    fuzzy_matches = 0
    for proj in design:
        if proj.lower().strip() in norm_funding:
            fuzzy_matches += 1
    result_count = fuzzy_matches
else:
    result_count = len(exact_matches)

print('__RESULT__:', json.dumps({'count': result_count}))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:32': [{'count': '276'}], 'var_functions.query_db:36': [], 'var_functions.query_db:38': 'file_storage/functions.query_db:38.json', 'var_functions.query_db:40': 'file_storage/functions.query_db:40.json', 'var_functions.query_db:64': 'file_storage/functions.query_db:64.json'}

exec(code, env_args)
