code = """import json
import re

# Load funding data - get file path from storage
funding_file = locals()['var_functions.query_db:96']
civic_file = locals()['var_functions.query_db:40']

with open(funding_file, 'r', encoding='utf-8') as f:
    funding_data = json.load(f)

with open(civic_file, 'r', encoding='utf-8') as f:
    civic_docs = json.load(f)

# Step 1: Build set of high-funding project names (> $50,000)
high_funding = set()
for record in funding_data:
    high_funding.add(record['Project_Name'])

# Step 2: Extract capital projects with 'design' status from civic documents
design_projects = set()

for doc in civic_docs:
    text = doc.get('text', '')
    
    # Find the Capital Improvement Projects (Design) section
    design_start = text.find('Capital Improvement Projects (Design)')
    if design_start == -1:
        continue
    
    # Find where this section ends (next major header)
    construction_start = text.find('Capital Improvement Projects (Construction)', design_start)
    disaster_start = text.find('Disaster Recovery Projects', design_start)
    
    # Determine end of design section
    end_candidates = [pos for pos in [construction_start, disaster_start] if pos > design_start]
    design_end = min(end_candidates) if end_candidates else len(text)
    
    # Extract design section
    design_section = text[design_start:design_end]
    
    # Extract project names from this section
    seen_project = False
    for line in design_section.split('\n'):
        line = line.strip()
        if not line:
            continue
        
        # Skip headers and markers
        if line == 'Capital Improvement Projects (Design)':
            seen_project = True
            continue
        if line.startswith('(') or line.startswith('•') or line.startswith('-'):
            continue
        if 'Updates:' in line or 'Schedule:' in line or 'Page' in line:
            continue
        if re.match(r'^\d+\s+of\s+\d+', line):
            continue
        if re.match(r'^\d{4}\s', line):  # Year markers
            continue
            
        # This looks like a project name
        if len(line) > 10 and seen_project:
            # Clean up common prefixes
            clean_line = re.sub(r'^(cid:\d+)\s*', '', line)
            if len(clean_line) > 10:
                design_projects.add(clean_line)

# Step 3: Count matches (projects in both sets)
# Use exact matching first
exact_matches = high_funding.intersection(design_projects)
match_count = len(exact_matches)

# If no matches found, try normalized matching
if match_count == 0 and design_projects:
    norm_funding = {name.lower().strip() for name in high_funding}
    for project in design_projects:
        if project.lower().strip() in norm_funding:
            match_count += 1

# Build final result
result = {'count': match_count}
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:32': [{'count': '276'}], 'var_functions.query_db:36': [], 'var_functions.query_db:38': 'file_storage/functions.query_db:38.json', 'var_functions.query_db:40': 'file_storage/functions.query_db:40.json', 'var_functions.query_db:64': 'file_storage/functions.query_db:64.json', 'var_functions.list_db:94': ['Funding'], 'var_functions.query_db:96': 'file_storage/functions.query_db:96.json'}

exec(code, env_args)
