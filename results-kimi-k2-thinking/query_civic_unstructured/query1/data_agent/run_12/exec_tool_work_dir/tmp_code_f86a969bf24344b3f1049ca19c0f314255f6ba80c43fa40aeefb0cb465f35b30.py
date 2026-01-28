code = """import json
import re

# Load data from files
with open('var_functions.query_db:0', 'r') as f:
    funding_data = json.load(f)
with open('var_functions.query_db:1', 'r') as f:
    civic_data = json.load(f)

# Map project names to funding amounts (filtering > $50,000)
funding_map = {}
for item in funding_data:
    amount = int(item['Amount'])
    if amount > 50000:
        funding_map[item['Project_Name']] = amount

# Find capital projects in design status
design_projects = set()

for doc in civic_data:
    text = doc.get('text', '')
    if not text:
        continue
    
    # Find the design section for capital improvement projects
    design_marker = 'Capital Improvement Projects (Design)'
    if design_marker in text:
        start = text.index(design_marker) + len(design_marker)
        section = text[start:]
        
        # Determine section end
        end = float('inf')
        for marker in ['Capital Improvement Projects (Construction)', 
                      'Capital Improvement Projects (Not Started)', 
                      'Disaster Recovery Projects']:
            pos = section.find(marker)
            if pos > 0 and pos < end:
                end = pos
        
        if end != float('inf'):
            section = section[:int(end)]
        
        # Extract lines that might be project names
        for line_num, line in enumerate(section.split('\n')):
            line = line.strip()
            if not line or len(line) < 5:
                continue
            
            # Skip metadata/markers
            if line.startswith('(') or line.startswith('-') or line.startswith('•'):
                continue
            if any(x in line for x in ['Updates', 'Schedule', 'Complete Design', 'Advertise', 'Begin Construction', 'Project Description', 'Capital Improvement']):
                continue
            
            # Check if this is a funded project > $50K
            if line in funding_map:
                design_projects.add(line)

# Prepare results
result_data = {
    'count': len(design_projects),
    'projects': sorted(list(design_projects))
}

print('__RESULT__:')
print(json.dumps(result_data))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:1': 'file_storage/functions.query_db:1.json', 'var_functions.execute_python:24': {'funding_records': 276, 'civic_docs': 5, 'sample_funding': {'Funding_ID': '5', 'Project_Name': 'Birdview Avenue Improvements', 'Funding_Source': 'National Foundation Fund', 'Amount': '79000'}}}

exec(code, env_args)
