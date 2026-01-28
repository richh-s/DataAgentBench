code = """import json

funding_path = var_functions.query_db:0
civic_path = var_functions.query_db:1

with open(funding_path, 'r') as f:
    funding = json.load(f)

with open(civic_path, 'r') as f:
    docs = json.load(f)

# Map project names to amounts for projects > $50K
funding_map = {}
for item in funding:
    amount = int(item['Amount'])
    if amount > 50000:
        funding_map[item['Project_Name']] = amount

# Find projects in design phase from capital improvement projects
design_projects = set()

for doc in docs:
    text = doc.get('text', '')
    
    # Look for capital projects in design phase
    if 'Capital Improvement Projects (Design)' in text:
        start_pos = text.index('Capital Improvement Projects (Design)')
        section = text[start_pos:]
        
        # Find end of section
        end_pos = float('inf')
        for marker in ['Capital Improvement Projects (Construction)', 'Capital Improvement Projects (Not Started)', 'Disaster Recovery Projects']:
            pos = section.find(marker)
            if 0 < pos < end_pos:
                end_pos = pos
        
        if end_pos != float('inf'):
            section = section[:end_pos]
        
        # Extract lines
        for line in section.split('\n'):
            line = line.strip()
            if not line or len(line) < 5:
                continue
            if line.startswith('(') or line.startswith('-') or line.startswith('•'):
                continue
            if 'Updates' in line or 'Schedule' in line or 'Capital Improvement' in line:
                continue
            if line in funding_map:
                design_projects.add(line)

result = json.dumps({'count': len(design_projects), 'projects': sorted(list(design_projects))})
print('__RESULT__:')
print(result)"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:1': 'file_storage/functions.query_db:1.json'}

exec(code, env_args)
