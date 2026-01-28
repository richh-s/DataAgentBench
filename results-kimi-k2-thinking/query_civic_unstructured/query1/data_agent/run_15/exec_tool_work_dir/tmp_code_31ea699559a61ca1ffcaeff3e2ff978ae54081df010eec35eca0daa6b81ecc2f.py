code = """import json

# Load funding data
funding_path = locals()['var_functions.query_db:5']
with open(funding_path) as f:
    funding_data = json.load(f)

# Load civic docs
civic_docs_path = locals()['var_functions.query_db:2']
with open(civic_docs_path) as f:
    civic_docs = json.load(f)

# High funding projects set
high_funding = set()
for item in funding_data:
    if int(item['Amount']) > 50000:
        high_funding.add(item['Project_Name'])

# Extract design capital projects
design_projects = set()
for doc in civic_docs:
    text = doc.get('text', '')
    
    # Find design section
    if 'Capital Improvement Projects (Design)' in text:
        start = text.find('Capital Improvement Projects (Design)')
        end = text.find('Capital Improvement Projects (Construction)', start)
        if end == -1:
            end = len(text)
        
        design_section = text[start:end]
        lines = design_section.split('\n')
        
        # Collect project names (skip header)
        for line in lines[1:]:
            line = line.strip()
            if line and len(line) > 15 and not line.startswith('('):
                if 'Updates:' not in line and 'Schedule:' not in line:
                    design_projects.add(line)

# Find intersection
matches = high_funding.intersection(design_projects)

result = {
    'high_funding_total': len(high_funding),
    'design_projects_total': len(design_projects),
    'matching_projects': len(matches)
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json'}

exec(code, env_args)
