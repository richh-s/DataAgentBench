code = """import json

# Load funding data
funding_path = var_functions.query_db:0
f1 = open(funding_path)
funding_data = json.load(f1)
f1.close()

# Load civic documents
civic_path = var_functions.query_db:2
f2 = open(civic_path)
civic_docs = json.load(f2)
f2.close()

# Get projects with funding > $50,000
high_funding_names = []
for record in funding_data:
    if int(record['Amount']) > 50000:
        high_funding_names.append(record['Project_Name'])

# Extract capital design project names from civic documents
design_project_names = []

for doc in civic_docs:
    text = doc.get('text', '')
    
    # Find design section
    design_start = text.find('Capital Improvement Projects (Design)')
    if design_start == -1:
        continue
    
    # Skip header text
    content_after = text[design_start + 37:]
    
    # Cut at next major section
    design_content = content_after
    construction_marker = 'Capital Improvement Projects (Construction)'
    not_started_marker = 'Capital Improvement Projects (Not Started)'
    disaster_marker = 'Disaster Recovery Projects'
    
    for marker in [construction_marker, not_started_marker, disaster_marker]:
        marker_pos = design_content.find(marker)
        if marker_pos > 0:
            design_content = design_content[:marker_pos]
            break
    
    # Split into blocks and extract names
    blocks = design_content.split('\n\n')
    for block in blocks:
        block = block.strip()
        if len(block) > 10:
            lines = block.split('\n')
            if lines:
                first_line = lines[0].strip()
                if len(first_line) > 10 and not first_line.isupper():
                    design_project_names.append(first_line)

# Simple matching
matched = 0
for proj in design_project_names:
    pj = proj.lower()
    for fund in high_funding_names:
        fd = fund.lower()
        if pj == fd or proj in fund or fund in proj:
            matched += 1
            break

result = matched
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:10': [{'count': '276'}], 'var_functions.query_db:56': [{'count': '276'}]}

exec(code, env_args)
