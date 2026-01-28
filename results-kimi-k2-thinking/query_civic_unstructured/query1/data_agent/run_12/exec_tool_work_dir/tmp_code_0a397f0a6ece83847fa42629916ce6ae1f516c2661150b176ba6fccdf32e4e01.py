code = """import json

# Get file paths from storage
funding_path = locals()['var_functions.query_db:0']
civic_path = locals()['var_functions.query_db:1']

# Load data
with open(funding_path, 'r') as f:
    funding_data = json.load(f)
with open(civic_path, 'r') as f:
    civic_data = json.load(f)

# Build funding lookup for projects > $50,000
funding_lookup = {}
for item in funding_data:
    amt = int(item['Amount'])
    if amt > 50000:
        funding_lookup[item['Project_Name']] = amt

# Find capital design projects
design_projects = set()

for doc in civic_data:
    text = doc.get('text', '')
    marker = 'Capital Improvement Projects (Design)'
    
    if marker not in text:
        continue
    
    # Extract the design section
    start_idx = text.index(marker) + len(marker)
    design_section = text[start_idx:]
    
    # Find where this section ends
    end_markers = [
        'Capital Improvement Projects (Construction)',
        'Capital Improvement Projects (Not Started)', 
        'Disaster Recovery Projects'
    ]
    
    end_idx = len(design_section)
    for marker_text in end_markers:
        pos = design_section.find(marker_text)
        if pos > 0 and pos < end_idx:
            end_idx = pos
    
    design_section = design_section[:end_idx]
    
    # Look for project names in this section
    lines = design_section.split('\n')
    for line in lines:
        line = line.strip()
        if not line or len(line) < 5:
            continue
        
        # Skip metadata lines
        if line.startswith('(') or line.startswith('-') or line.startswith('•'):
            continue
        
        skip_words = ['Updates', 'Schedule', 'Complete Design', 'Advertise', 'Begin Construction', 'Capital Improvement', 'Project Description']
        skip = False
        for word in skip_words:
            if word in line:
                skip = True
                break
        if skip:
            continue
        
        # Check if this is a funded project
        if line in funding_lookup:
            design_projects.add(line)

# Prepare result
result = {
    'count': len(design_projects),
    'projects': sorted(list(design_projects))
}

print('__RESULT__')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:1': 'file_storage/functions.query_db:1.json', 'var_functions.execute_python:24': {'funding_records': 276, 'civic_docs': 5, 'sample_funding': {'Funding_ID': '5', 'Project_Name': 'Birdview Avenue Improvements', 'Funding_Source': 'National Foundation Fund', 'Amount': '79000'}}}

exec(code, env_args)
