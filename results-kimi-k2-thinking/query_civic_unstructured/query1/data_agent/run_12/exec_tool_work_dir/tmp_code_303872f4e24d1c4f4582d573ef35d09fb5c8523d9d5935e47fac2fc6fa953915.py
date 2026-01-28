code = """import json

# Load the data
with open('var_functions.query_db:0', 'r') as f:
    funding_data = json.load(f)
with open('var_functions.query_db:1', 'r') as f:
    civic_data = json.load(f)

# Create funding lookup for amounts > 50000
funding_over_50k = {}
for item in funding_data:
    amt = int(item['Amount'])
    if amt > 50000:
        funding_over_50k[item['Project_Name']] = amt

# Find capital projects in design status
design_projects = set()

for doc in civic_data:
    text = doc.get('text', '')
    if 'Capital Improvement Projects (Design)' in text:
        section_start = text.index('Capital Improvement Projects (Design)') + len('Capital Improvement Projects (Design)')
        section = text[section_start:]
        
        # Find where section ends
        end_pos = float('inf')
        for marker in ['Capital Improvement Projects (Construction)', 'Capital Improvement Projects (Not Started)', 'Disaster Recovery Projects']:
            marker_pos = section.find(marker)
            if marker_pos > 0 and marker_pos < end_pos:
                end_pos = marker_pos
        
        if end_pos != float('inf'):
            section = section[:end_pos]
        
        # Look for project names in this section
        for line in section.split('\n'):
            line = line.strip()
            if not line or len(line) < 5:
                continue
            
            # Skip metadata lines  
            if line.startswith('(') or line.startswith('-') or line.startswith('•'):
                continue
            if any(word in line for word in ['Updates', 'Schedule', 'Complete Design', 'Advertise', 'Begin Construction', 'Capital Improvement', 'Project Description']):
                continue
            
            # Check if this is a funded project
            if line in funding_over_50k:
                design_projects.add(line)

# Generate result
result_str = json.dumps({'count': len(design_projects), 'projects': list(design_projects)})
print('__RESULT__:')
print(result_str)"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:1': 'file_storage/functions.query_db:1.json', 'var_functions.execute_python:24': {'funding_records': 276, 'civic_docs': 5, 'sample_funding': {'Funding_ID': '5', 'Project_Name': 'Birdview Avenue Improvements', 'Funding_Source': 'National Foundation Fund', 'Amount': '79000'}}}

exec(code, env_args)
