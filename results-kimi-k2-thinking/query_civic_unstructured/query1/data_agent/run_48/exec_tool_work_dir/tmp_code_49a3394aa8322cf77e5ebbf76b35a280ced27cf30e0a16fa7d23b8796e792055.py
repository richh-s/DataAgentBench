code = """import json
import re

# Get file paths
funding_file = str(var_functions.query_db:0)
civic_file = str(var_functions.query_db:2)

# Load data
with open(funding_file) as f:
    funding_data = json.load(f)

with open(civic_file) as f:
    civic_docs = json.load(f)

# Filter projects with funding > $50k
high_funding = set()
for item in funding_data:
    if int(item['Amount']) > 50000:
        high_funding.add(item['Project_Name'])

# Extract capital design projects
design_projects = []
for doc in civic_docs:
    text = doc.get('text', '')
    
    # Find design section
    start = text.find('Capital Improvement Projects (Design)')
    if start == -1:
        continue
    
    design_section = text[start + 37:]
    
    # Cut at next major section
    end_pos = len(design_section)
    for marker in ['Capital Improvement Projects (Construction)', 
                   'Capital Improvement Projects (Not Started)', 
                   'Disaster Recovery Projects']:
        pos = design_section.find(marker)
        if pos > 0 and pos < end_pos:
            end_pos = pos
            break
    
    design_section = design_section[:end_pos]
    
    # Extract potential project names
    blocks = design_section.split('\n\n')
    for block in blocks:
        block = block.strip()
        if len(block) > 10:
            first_line = block.split('\n')[0].strip()
            # Filter out non-project lines
            if len(first_line) > 10 and not first_line.isupper() and 'Updates:' not in first_line:
                # Clean bullet prefixes
                clean_name = first_line
                clean_name = re.sub(r'^[A-Z]\.\s*', '', clean_name)
                clean_name = re.sub(r'^\d+\.\s*', '', clean_name)
                if len(clean_name) > 10:
                    design_projects.append(clean_name)

# Normalize and match
normalize_func = lambda name: re.sub(r'[^a-z0-9]', '', name.lower().strip())

matched_count = 0
for proj in design_projects:
    proj_normalized = normalize_func(proj)
    if len(proj_normalized) < 8:
        continue
    
    for fund_name in high_funding:
        fund_normalized = normalize_func(fund_name)
        if proj_normalized == fund_normalized:
            matched_count += 1
            break
        if len(proj_normalized) > 10 and proj_normalized in fund_normalized:
            matched_count += 1
            break
        if len(fund_normalized) > 10 and fund_normalized in proj_normalized:
            matched_count += 1
            break

result = matched_count
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:10': [{'count': '276'}]}

exec(code, env_args)
