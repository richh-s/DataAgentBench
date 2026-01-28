code = """import json
funding_path = var_functions.query_db:0
civic_path = var_functions.query_db:2

f_funding = open(funding_path)
funding_data = json.load(f_funding)
f_funding.close()

f_civic = open(civic_path)
civic_docs = json.load(f_civic)
f_civic.close()

# Get projects with funding > $50,000
high_funding = set()
for item in funding_data:
    if int(item['Amount']) > 50000:
        high_funding.add(item['Project_Name'])

# Extract capital projects in design status
design_projects = []
for doc in civic_docs:
    text = doc.get('text', '')
    
    # Find design section
    start = text.find('Capital Improvement Projects (Design)')
    if start == -1:
        continue
    
    # Get section up to next major heading
    section = text[start + 37:]
    markers = ['Capital Improvement Projects (Construction)', 
               'Capital Improvement Projects (Not Started)', 
               'Disaster Recovery Projects']
    
    end_pos = len(section)
    for m in markers:
        pos = section.find(m)
        if pos > 0:
            end_pos = min(end_pos, pos)
    
    section = section[:end_pos]
    
    # Extract project names
    parts = section.split('\n\n')
    for part in parts:
        block = part.strip()
        if len(block) > 10:
            first_line = block.split('\n')[0].strip()
            # Skip non-project lines
            if len(first_line) > 10 and not first_line.isupper():
                clean_name = first_line
                # Remove bullet prefixes
                if clean_name and clean_name[0] in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ' and len(clean_name) > 2 and clean_name[1] == '.':
                    clean_name = clean_name[2:].strip()
                if len(clean_name) > 10 and 'Updates:' not in clean_name:
                    design_projects.append(clean_name)

# Simple string matching without complex regex
matched = 0
for proj in design_projects:
    proj_lower = proj.lower().strip()
    for fund_name in high_funding:
        fund_lower = fund_name.lower().strip()
        # Direct match
        if proj_lower == fund_lower or proj in fund_name or fund_name in proj:
            matched += 1
            break
        # Word matching for multi-word names
        proj_words = proj_lower.split()
        fund_words = fund_lower.split()
        if len(proj_words) >= 3 and len(fund_words) >= 3:
            common = set(proj_words) & set(fund_words)
            if len(common) >= 3:
                matched += 1
                break

print('__RESULT__:')
print(json.dumps(matched))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:10': [{'count': '276'}]}

exec(code, env_args)
