code = """import json, re

# Load funding data - projects with > $50k
funding_file_path = var_functions.query_db:0
with open(funding_file_path) as f:
    funding_data = json.load(f)

# Build list of high-funding projects for easy lookup
high_funding_names = []
for f in funding_data:
    if int(f['Amount']) > 50000:
        high_funding_names.append(f['Project_Name'])

# Load civic documents
civic_file_path = var_functions.query_db:2
with open(civic_file_path) as f:
    civic_docs = json.load(f)

# Extract design projects by scanning for keywords
project_names = []

for doc in civic_docs:
    text = doc.get('text', '')
    
    # Find the design section boundaries
    design_start = text.find('Capital Improvement Projects (Design)')
    construction_start = text.find('Capital Improvement Projects (Construction)', design_start)
    
    if design_start == -1:
        continue
    
    start_pos = design_start + 38  # Length of "Capital Improvement Projects (Design)"
    end_pos = construction_start if construction_start != -1 else len(text)
    
    design_section = text[start_pos:end_pos]
    
    # Split and find likely project names
    for para in design_section.split('\n\n'):
        para = para.strip()
        if len(para) >= 15 and not para.startswith('(') and 'Updates:' not in para:
            # First line is likely a project name
            lines = para.split('\n')
            if lines:
                name = lines[0].strip()
                if len(name) >= 10 and not name.isupper() and 'Schedule' not in name:
                    cleaned = re.sub(r'^[A-Z]\.\s*', '', name)
                    cleaned = re.sub(r'^\d+\.\s*', '', cleaned)
                    if len(cleaned) > 10:
                        project_names.append(cleaned)

# Count matches with high funding
matched = 0
for proj in project_names:
    proj_lower = proj.lower()
    for fund_name in high_funding_names:
        fund_lower = fund_name.lower()
        if proj_lower == fund_lower or proj in fund_name or fund_name in proj:
            matched += 1
            break

print('__RESULT__:')
print(json.dumps(matched))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:10': [{'count': '276'}]}

exec(code, env_args)
