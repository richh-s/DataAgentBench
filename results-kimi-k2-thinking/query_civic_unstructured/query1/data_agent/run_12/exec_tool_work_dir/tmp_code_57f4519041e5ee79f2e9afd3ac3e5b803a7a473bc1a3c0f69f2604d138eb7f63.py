code = """import json

# Load funding data using locals()
funding_file = locals()['var_functions.query_db:0']
civic_file = locals()['var_functions.query_db:1']

with open(funding_file, 'r') as f:
    funding_data = json.load(f)
with open(civic_file, 'r') as f:
    civic_data = json.load(f)

# Create lookup for projects > $50K
funding_map = {}
for item in funding_data:
    amt = int(item['Amount'])
    if amt > 50000:
        funding_map[item['Project_Name']] = amt

# Find capital projects in design status
design_projects = set()

for doc in civic_data:
    txt = doc.get('text', '')
    if not txt:
        continue
    
    # Find the design section
    m_start = txt.find('Capital Improvement Projects (Design)')
    if m_start < 0:
        continue
    
    start = m_start + len('Capital Improvement Projects (Design)')
    section = txt[start:]
    
    # Find section end
    end_markers = [
        'Capital Improvement Projects (Construction)',
        'Capital Improvement Projects (Not Started)',
        'Disaster Recovery Projects'
    ]
    
    end = len(section)
    for marker in end_markers:
        pos = section.find(marker)
        if pos > 0 and pos < end:
            end = pos
    
    section = section[:end]
    
    # Look for project names
    for line in section.splitlines():
        line = line.strip()
        if len(line) < 5:
            continue
        
        # Skip metadata
        if line.startswith('(') or line.startswith('-'):
            continue
        if 'Updates' in line or 'Schedule' in line:
            continue
        
        # Check if funded
        if line in funding_map:
            design_projects.add(line)

result_data = {
    'count': len(design_projects),
    'projects': sorted(list(design_projects))
}

print('__RESULT__:')
print(json.dumps(result_data))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:1': 'file_storage/functions.query_db:1.json', 'var_functions.execute_python:24': {'funding_records': 276, 'civic_docs': 5, 'sample_funding': {'Funding_ID': '5', 'Project_Name': 'Birdview Avenue Improvements', 'Funding_Source': 'National Foundation Fund', 'Amount': '79000'}}}

exec(code, env_args)
