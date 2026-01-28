code = """import json
import re

# Step 1: Load funding data for projects > $50k
funding_path = var_functions.query_db:0
with open(funding_path) as f:
    funding_data = json.load(f)

# Step 2: Load civic documents
civic_path = var_functions.query_db:2
with open(civic_path) as f:
    civic_docs = json.load(f)

# Step 3: Extract high-funding project names
high_funding = set()
for record in funding_data:
    if int(record['Amount']) > 50000:
        high_funding.add(record['Project_Name'])

# Step 4: Extract capital design projects from civic documents
design_projects = []

for doc in civic_docs:
    text = doc.get('text', '')
    
    # Find design section
    design_start = text.find('Capital Improvement Projects (Design)')
    if design_start == -1:
        continue
    
    # Get text up to next major section
    design_section = text[design_start:]
    end_markers = ['Capital Improvement Projects (Construction)', 
                   'Capital Improvement Projects (Not Started)', 
                   'Disaster Recovery Projects']
    
    for marker in end_markers:
        end_pos = design_section.find(marker)
        if end_pos > 0:
            design_section = design_section[:end_pos]
            break
    
    # Extract project names
    parts = design_section.split('\n\n')
    for part in parts:
        part = part.strip()
        if len(part) > 10:
            first_line = part.split('\n')[0].strip()
            if len(first_line) > 10 and not first_line.isupper():
                # Remove common bullets
                clean_name = re.sub(r'^[A-Z]\.\s*', '', first_line)
                clean_name = re.sub(r'^\d+\.\s*', '', clean_name)
                if len(clean_name) > 10 and 'Updates:' not in clean_name:
                    design_projects.append(clean_name)

# Step 5: Normalize and match
def normalize(name):
    return re.sub(r'[^a-z0-9]', '', name.lower().strip())

matched_count = 0
for proj in design_projects:
    proj_norm = normalize(proj)
    if len(proj_norm) < 8:
        continue
    
    for fund_name in high_funding:
        fund_norm = normalize(fund_name)
        
        if proj_norm == fund_norm:
            matched_count += 1
            break
        if len(proj_norm) > 12 and proj_norm in fund_norm:
            matched_count += 1
            break
        if len(fund_norm) > 12 and fund_norm in proj_norm:
            matched_count += 1
            break

# Step 6: Output result
print('__RESULT__:')
print(json.dumps(matched_count))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:10': [{'count': '276'}]}

exec(code, env_args)
