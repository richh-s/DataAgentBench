code = """import json

# Load funding data
funding_path = locals()['var_functions.query_db:5']
with open(funding_path) as f:
    funding_data = json.load(f)

# Load civic docs
civic_docs_path = locals()['var_functions.query_db:2']
with open(civic_docs_path) as f:
    civic_docs = json.load(f)

# High funding projects
high_funding = set()
for item in funding_data:
    if int(item['Amount']) > 50000:
        high_funding.add(item['Project_Name'])

# Extract design capital projects
design_projects = set()
for doc in civic_docs:
    text = doc.get('text', '')
    design_start = text.find('Capital Improvement Projects (Design)')
    construction_start = text.find('Capital Improvement Projects (Construction)', design_start)
    
    if design_start >= 0:
        if construction_start >= 0:
            design_section = text[design_start:construction_start]
        else:
            design_section = text[design_start:]
        
        lines = design_section.split('\n')
        for line in lines[1:]:  # Skip header
            line = line.strip()
            if line and len(line) > 15 and '(' not in line[:3]:
                if 'Updates:' not in line and 'Schedule:' not in line:
                    design_projects.add(line)

matches = high_funding.intersection(design_projects)

result = {
    'high_funding': len(high_funding),
    'design_projects': len(design_projects),
    'matching': len(matches)
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json'}

exec(code, env_args)
