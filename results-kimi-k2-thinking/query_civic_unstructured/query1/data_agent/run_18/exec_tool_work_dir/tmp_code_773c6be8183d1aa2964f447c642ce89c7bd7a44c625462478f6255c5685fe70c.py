code = """import json
import re

# Load funding data
funding_file = var_functions.query_db:1
if isinstance(funding_file, str) and funding_file.endswith('.json'):
    with open(funding_file, 'r') as f:
        funding_data = json.load(f)
else:
    funding_data = funding_file

# Load civic documents
civic_file = var_functions.query_db:2
if isinstance(civic_file, str) and civic_file.endswith('.json'):
    with open(civic_file, 'r') as f:
        civic_docs = json.load(f)
else:
    civic_docs = civic_file

# Count capital design projects with funding
extracted_projects = []

for doc in civic_docs:
    text = doc.get('text', '')
    
    design_pos = text.find('Capital Improvement Projects (Design)')
    if design_pos < 0:
        continue
        
    section = text[design_pos:]
    end_pos = len(section)
    
    for marker in ['Capital Improvement Projects (Construction)', 'Capital Improvement Projects (Not Started)', 'Disaster Recovery Projects']:
        pos = section.find(marker)
        if pos > 0 and pos < end_pos:
            end_pos = pos
    
    design_section = section[:end_pos]
    
    # Match project patterns
    patterns = [r'([A-Z][^\n]{10,}?(?:Project|Improvements|Repairs|Study|Master Plan))', 
                r'([A-Z][^\n]{10,}?(?:Road|Park|Beach|Highway)[^\n]{5,})']
    
    for pattern in patterns:
        matches = re.findall(pattern, design_section)
        for match in matches:
            if 'Updates' not in match and 'Schedule' not in match:
                clean = re.sub(r'[^A-Za-z0-9\s]', '', match).strip()
                if clean:
                    extracted_projects.append(clean)

# Remove duplicates
extracted_projects = list(set(extracted_projects))

# Get funded project names
funded_names = [f['Project_Name'] for f in funding_data]

# Count matches
matches = 0
for proj in extracted_projects:
    proj_lower = proj.lower()
    proj_words = set(proj_lower.split())
    if len(proj_words) < 2:
        continue
    
    for funded in funded_names:
        funded_lower = funded.lower()
        
        if proj_lower in funded_lower or funded_lower in proj_lower:
            matches += 1
            break
        
        funded_words = set(funded_lower.split())
        if len(proj_words & funded_words) >= 3:
            matches += 1
            break

# Output
print('__RESULT__:')
print(json.dumps(matches))"""

env_args = {'var_functions.list_db:0': ['Funding'], 'var_functions.query_db:1': 'file_storage/functions.query_db:1.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json'}

exec(code, env_args)
