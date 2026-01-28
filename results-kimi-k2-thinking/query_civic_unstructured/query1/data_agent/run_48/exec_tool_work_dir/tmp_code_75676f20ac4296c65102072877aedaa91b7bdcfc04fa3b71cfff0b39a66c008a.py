code = """import json, re

# Load data
funding_file_path = var_functions.query_db:0
civic_file_path = var_functions.query_db:2

with open(funding_file_path) as f:
    funding_data = json.load(f)

with open(civic_file_path) as f:
    civic_docs = json.load(f)

# Get high funding projects
high_funding = {}
for f in funding_data:
    amount = int(f['Amount'])
    if amount > 50000:
        high_funding[f['Project_Name']] = amount

# Extract design projects
design_projects = []

for doc in civic_docs:
    text = doc.get('text', '')
    
    # Find design section
    start = text.find('Capital Improvement Projects (Design)')
    if start == -1:
        continue
    
    design_text = text[start+len('Capital Improvement Projects (Design)'):]
    
    # Find end
    end_pos = len(design_text)
    for marker in ['Capital Improvement Projects (Construction)', 
                   'Capital Improvement Projects (Not Started)', 
                   'Disaster Recovery Projects']:
        pos = design_text.find(marker)
        if pos != -1:
            end_pos = min(end_pos, pos)
    
    design_section = design_text[:end_pos]
    
    # Extract lines that look like project names
    for line in design_section.split('\n'):
        line = line.strip()
        if len(line) >= 10 and not any(x in line for x in ['Updates:', 'Schedule', 'cid:', 'RECOMMENDED', 'DISCUSSION']):
            if line[0].isalpha() and not line.isupper():
                clean_line = re.sub(r'^[A-Z]\. ', '', line)
                clean_line = re.sub(r'^\d+\. ', '', clean_line)
                if len(clean_line) > 10:
                    design_projects.append(clean_line)

# Match by name
matched_count = 0
matched_projects = []

for proj in design_projects:
    # Direct match
    if proj in high_funding:
        matched_count += 1
        matched_projects.append(proj)
        continue
    
    # Partial match
    proj_words = set(proj.lower().split())
    for fund_name in high_funding.keys():
        fund_words = set(fund_name.lower().split())
        if len(proj_words) >= 3 and len(proj_words.intersection(fund_words)) >= 3:
            matched_count += 1
            matched_projects.append(proj)
            break

print('__RESULT__:')
print(json.dumps(matched_count))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:10': [{'count': '276'}]}

exec(code, env_args)
