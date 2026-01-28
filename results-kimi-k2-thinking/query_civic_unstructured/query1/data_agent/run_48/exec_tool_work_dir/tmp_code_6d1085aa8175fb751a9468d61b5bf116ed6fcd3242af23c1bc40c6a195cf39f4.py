code = """import json
import re

# Load funding data
funding_path = var_functions.query_db:0
with open(funding_path) as f:
    funding_records = json.load(f)

# Load civic documents
civic_path = var_functions.query_db:2
with open(civic_path) as f:
    civic_documents = json.load(f)

# Get high funding project names
high_funding_names = []
for record in funding_records:
    if int(record['Amount']) > 50000:
        high_funding_names.append(record['Project_Name'])

# Extract capital design projects from civic documents
extracted_project_names = []

for doc in civic_documents:
    text = doc.get('text', '')
    
    # Find design section
    design_pos = text.find('Capital Improvement Projects (Design)')
    if design_pos == -1:
        continue
    
    # Get text after design marker, up to next major section
    design_section = text[design_pos + 38:]
    
    # Cut at next major section
    for marker in ['Capital Improvement Projects (Construction)', 
                   'Capital Improvement Projects (Not Started)', 
                   'Disaster Recovery Projects']:
        end_pos = design_section.find(marker)
        if end_pos != -1:
            design_section = design_section[:end_pos]
            break
    
    # Extract potential project names
    sections = design_section.split('\n\n')
    for section in sections:
        section = section.strip()
        if section and len(section.split('\n')) > 0:
            first_line = section.split('\n')[0].strip()
            # Skip update/schedule lines
            if ('Updates:' not in first_line and 
                'Schedule:' not in first_line and 
                'cid:' not in first_line and
                len(first_line) > 10 and
                not first_line.isupper()):
                # Clean bullets
                clean_name = re.sub(r'^[A-Z]\.\s*', '', first_line)
                clean_name = re.sub(r'^\d+\.\s*', '', clean_name)
                if len(clean_name) > 10:
                    extracted_project_names.append(clean_name)

# Normalize names for matching
def normalize_name(name):
    return re.sub(r'[^a-z0-9]', '', name.lower().strip())

# Count matches
match_count = 0
for proj in extracted_project_names:
    proj_norm = normalize_name(proj)
    if len(proj_norm) < 8:
        continue
    
    for fund_name in high_funding_names:
        fund_norm = normalize_name(fund_name)
        
        # Exact match
        if proj_norm == fund_norm:
            match_count += 1
            break
        
        # Substring match for longer names
        if len(proj_norm) > 12 and proj_norm in fund_norm:
            match_count += 1
            break
        
        if len(fund_norm) > 12 and fund_norm in proj_norm:
            match_count += 1
            break

print('__RESULT__:')
print(json.dumps(match_count))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:10': [{'count': '276'}]}

exec(code, env_args)
