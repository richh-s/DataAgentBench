code = """import json, re

# Load data from files
funding_file_path = var_functions.query_db:0
civic_file_path = var_functions.query_db:2

with open(funding_file_path) as f:
    funding_data = json.load(f)

with open(civic_file_path) as f:
    civic_docs = json.load(f)

# Get high funding projects
high_funding = [(f['Project_Name'], int(f['Amount'])) for f in funding_data if int(f['Amount']) > 50000]

# Extract capital projects in design status from civic documents
projects = []

for doc in civic_docs:
    text = doc.get('text', '')
    
    # Find design section
    start = text.find('Capital Improvement Projects (Design)')
    if start == -1:
        continue
    
    design_part = text[start+len('Capital Improvement Projects (Design)'):]
    
    # Find end of design section
    end_markers = ['Capital Improvement Projects (Construction)', 
                   'Capital Improvement Projects (Not Started)', 
                   'Disaster Recovery Projects']
    
    end_pos = len(design_part)
    for marker in end_markers:
        pos = design_part.find(marker)
        if pos != -1 and pos < end_pos:
            end_pos = pos
    
    design_section = design_part[:end_pos]
    
    # Extract project names
    sections = design_section.split('\n\n')
    for section in sections:
        section = section.strip()
        if not section:
            continue
        
        first_line = section.split('\n')[0].strip()
        if len(first_line) >= 10 and not any(x in first_line.upper() for x in ['UPDATES', 'SCHEDULE', 'RECOMMENDED']):
            cleaned = re.sub(r'^[A-Z]\. ', '', first_line)
            if len(cleaned) > 10:
                projects.append(cleaned)

# Normalize function
def normalize(name):
    return re.sub(r'[^a-z0-9]', '', name.lower())

# Match
matched = 0
for proj in projects:
    proj_norm = normalize(proj)
    if len(proj_norm) < 10:
        continue
    
    for fund_name, amount in high_funding:
        fund_norm = normalize(fund_name)
        
        if proj_norm == fund_norm:
            matched += 1
            break
        
        if len(proj_norm) > 15 and proj_norm in fund_norm:
            matched += 1
            break
        
        if len(fund_norm) > 15 and fund_norm in proj_norm:
            matched += 1
            break

print('__RESULT__:')
print(json.dumps(matched))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:10': [{'count': '276'}]}

exec(code, env_args)
