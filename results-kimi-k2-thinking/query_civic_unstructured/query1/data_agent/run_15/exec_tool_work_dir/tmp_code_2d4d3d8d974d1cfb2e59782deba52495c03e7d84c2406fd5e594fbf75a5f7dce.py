code = """import json
import re

# Load funding data (projects with > $50,000 funding)
funding_file = locals()['var_functions.query_db:96']
with open(funding_file, 'r', encoding='utf-8') as f:
    funding_records = json.load(f)

# Load civic documents
civic_file = locals()['var_functions.query_db:40']
with open(civic_file, 'r', encoding='utf-8') as f:
    civic_docs = json.load(f)

print('Loaded', len(funding_records), 'funding records')
print('Loaded', len(civic_docs), 'civic documents')

# Step 1: Create set of high-funding project names
high_funding = set()
for record in funding_records:
    high_funding.add(record['Project_Name'])

print('High funding projects:', len(high_funding))

# Step 2: Extract capital projects with design status from civic docs
design_projects = set()

for doc in civic_docs:
    text = doc.get('text', '')
    
    # Find design projects section
    design_start = text.find('Capital Improvement Projects (Design)')
    if design_start == -1:
        continue
    
    # Find section end
    construction_start = text.find('Capital Improvement Projects (Construction)', design_start)
    if construction_start == -1:
        construction_start = len(text)
    
    design_section = text[design_start:construction_start]
    
    # Extract project names from this section
    for line in design_section.split('\n'):
        line = line.strip()
        
        # Skip empty, short, or marker lines
        if not line or len(line) < 10:
            continue
        if line.startswith('(') or line.startswith('•') or line.startswith('-'):
            continue
        if 'Updates:' in line or 'Schedule:' in line or 'Page' in line:
            continue
        
        # Clean and add project name
        clean_line = re.sub(r'^Capital Improvement Projects \(Design\)', '', line)
        clean_line = re.sub(r'^(cid:\d+)\s*', '', clean_line)
        clean_line = clean_line.strip()
        
        if len(clean_line) > 10:
            design_projects.add(clean_line)

print('Design projects found:', len(design_projects))

# Step 3: Count matches
# Try exact matching first
exact_matches = high_funding.intersection(design_projects)
match_count = len(exact_matches)

# If no matches, try normalized (lowercase) matching
if match_count == 0:
    norm_funding = {name.lower().strip() for name in high_funding}
    for project in design_projects:
        if project.lower().strip() in norm_funding:
            match_count += 1

print('Matches:', match_count)
result = {'count': match_count}
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:32': [{'count': '276'}], 'var_functions.query_db:36': [], 'var_functions.query_db:38': 'file_storage/functions.query_db:38.json', 'var_functions.query_db:40': 'file_storage/functions.query_db:40.json', 'var_functions.query_db:64': 'file_storage/functions.query_db:64.json', 'var_functions.list_db:94': ['Funding'], 'var_functions.query_db:96': 'file_storage/functions.query_db:96.json'}

exec(code, env_args)
