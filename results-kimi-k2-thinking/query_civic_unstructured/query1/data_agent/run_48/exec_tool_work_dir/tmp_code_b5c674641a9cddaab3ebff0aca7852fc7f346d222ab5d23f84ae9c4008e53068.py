code = """import json

# Load funding data
f1 = open(var_functions.query_db:0)
funding = json.load(f1)
f1.close()

# Load civic documents
f2 = open(var_functions.query_db:2)
docs = json.load(f2)
f2.close()

# Get projects with funding > $50,000
high_funding_names = []
for r in funding:
    if int(r['Amount']) > 50000:
        high_funding_names.append(r['Project_Name'])

# Extract capital design project names
design_project_names = []

for doc in docs:
    text = doc.get('text', '')
    
    # Find design section
    start = text.find('Capital Improvement Projects (Design)')
    if start == -1:
        continue
    
    # Skip header and get content up to next section
    section = text[start + 37:]
    
    end_pos = len(section)
    for marker in ['Capital Improvement Projects (Construction)', 'Capital Improvement Projects (Not Started)', 'Disaster Recovery Projects']:
        pos = section.find(marker)
        if pos > 0 and pos < end_pos:
            end_pos = pos
    
    section = section[:end_pos]
    
    # Extract project names
    blocks = section.split('\n\n')
    for block in blocks:
        block = block.strip()
        if len(block) > 10:
            first_line = block.split('\n')[0].strip()
            if len(first_line) > 10 and not first_line.isupper():
                design_project_names.append(first_line)

# Match by name overlap
matched = 0
for proj in design_project_names:
    proj_lower = proj.lower()
    for fund in high_funding_names:
        fund_lower = fund.lower()
        if proj_lower == fund_lower or proj in fund or fund in proj:
            matched += 1
            break
        project_words = set(proj_lower.split())
        fund_words = set(fund_lower.split())
        if len(project_words) >= 3 and len(fund_words) >= 3 and len(project_words.intersection(fund_words)) >= 2:
            matched += 1
            break

print('__RESULT__:')
print(json.dumps(matched))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:10': [{'count': '276'}], 'var_functions.query_db:56': [{'count': '276'}]}

exec(code, env_args)
