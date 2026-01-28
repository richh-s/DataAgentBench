code = """import json
import re

funding_path = var_functions.query_db:36
civic_docs_path = var_functions.query_db:37

with open(funding_path, 'r') as f:
    funding_data = json.load(f)

with open(civic_docs_path, 'r') as f:
    civic_docs = json.load(f)

print(f"Loaded {len(funding_data)} funding records and {len(civic_docs)} civic documents")

# Identify disaster-related projects that started in 2022
disaster_indicators = ['(FEMA Project)', '(CalOES Project)', '(CalJPIA Project)', 'FEMA/CalOES', 'FEMA', 'CalOES', 'CalJPIA']
projects_2022 = []

for doc in civic_docs:
    text = doc.get('text', '')
    filename = doc.get('filename', '')
    
    lines = text.split('\n')
    for i, line in enumerate(lines):
        line = line.strip()
        if not line:
            continue
            
        # Check if line contains disaster indicators (with context)
        context_window = 5
        start_idx = max(0, i - context_window)
        end_idx = min(len(lines), i + context_window + 1)
        context = '\n'.join(lines[start_idx:end_idx])
        
        has_disaster = any(indicator.lower() in context.lower() for indicator in disaster_indicators)
        
        if has_disaster:
            # Extract project name from line
            if any(word in line for word in ['Project', 'Improvements', 'Repairs', 'Replacement', 'Maintenance', 'Drainage', 'Bridge', 'Culvert']):
                project_name = line
                if project_name.endswith(':'):
                    project_name = project_name[:-1]
                
                # Check for 2022 in context
                if '2022' in context:
                    # Look for specific date patterns
                    date_patterns = [r'2022-\w+', r'2022-\d{1,2}', r'\b\w+\s+2022\b', r'\b2022\s+\w+\b']
                    st = '2022'  # default
                    
                    for pattern in date_patterns:
                        matches = re.findall(pattern, context)
                        if matches:
                            st = matches[0]
                            break
                    
                    # Clean project name
                    project_name = project_name.strip()
                    
                    # Only add if not already exists
                    exists = any(p['name'] == project_name for p in projects_2022)
                    if not exists and project_name:
                        projects_2022.append({
                            'name': project_name,
                            'start_date': st,
                            'filename': filename
                        })

# Also look for projects starting with 2022 in name
for doc in civic_docs:
    text = doc.get('text', '')
    filename = doc.get('filename', '')
    
    lines = text.split('\n')
    for line in lines:
        line = line.strip()
        if line.startswith('2022') and any(word in line for word in ['Project', 'Improvements', 'Repairs', 'Drainage']):
            # Check if disaster-related
            if 'storm' in line.lower() or 'drain' in line.lower() or 'fema' in text.lower():
                project_name = line
                if project_name.endswith(':'):
                    project_name = project_name[:-1]
                
                exists = any(p['name'] == project_name for p in projects_2022)
                if not exists:
                    projects_2022.append({
                        'name': project_name,
                        'start_date': '2022',
                        'filename': filename
                    })

print(f"\nFound {len(projects_2022)} disaster projects from 2022:")
for p in projects_2022:
    print(f"- {p['name']}")

# Match with funding
matched_funding = []
for project in projects_2022:
    project_name = project['name']
    
    for funding in funding_data:
        funding_name = funding.get('Project_Name', '')
        
        # Direct match or project name contained in funding name
        if project_name == funding_name or funding_name.startswith(project_name):
            matched_funding.append({
                'project': project_name,
                'funding_name': funding_name,
                'amount': int(funding.get('Amount', 0))
            })

# Sum funding
total_funding = sum(f['amount'] for f in matched_funding)

print(f"\nFound {len(matched_funding)} funding matches")
print(f"Total funding: ${total_funding:,}")

result = {
    'total_funding_2022': total_funding,
    'project_count': len(projects_2022),
    'funding_matches': len(matched_funding),
    'details': matched_funding
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.query_db:9': 'file_storage/functions.query_db:9.json', 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json', 'var_functions.query_db:13': 'file_storage/functions.query_db:13.json', 'var_functions.query_db:22': 'file_storage/functions.query_db:22.json', 'var_functions.query_db:23': 'file_storage/functions.query_db:23.json', 'var_functions.query_db:20': 'file_storage/functions.query_db:20.json', 'var_functions.query_db:21': 'file_storage/functions.query_db:21.json', 'var_functions.query_db:26': [{'Project_Name': '2021 Annual Street Maintenance', 'Amount': '24000'}, {'Project_Name': '2022 Annual Street Maintenance', 'Amount': '45000'}, {'Project_Name': '2022 Morning View Resurfacing & Storm Drain Improvements', 'Amount': '38000'}, {'Project_Name': 'Annual Street Maintenance', 'Amount': '23000'}, {'Project_Name': 'Birdview Avenue Improvements', 'Amount': '79000'}], 'var_functions.query_db:27': 'file_storage/functions.query_db:27.json', 'var_functions.query_db:32': 'file_storage/functions.query_db:32.json', 'var_functions.query_db:33': 'file_storage/functions.query_db:33.json', 'var_functions.query_db:36': 'file_storage/functions.query_db:36.json', 'var_functions.query_db:37': 'file_storage/functions.query_db:37.json'}

exec(code, env_args)
