code = """import json
import re

# Load the full datasets
with open('/tmp/tmpquery_db_32.json', 'r') as f:
    funding_data = json.load(f)

with open('/tmp/tmpquery_db_33.json', 'r') as f:
    civic_docs = json.load(f)

print(f"Loaded {len(funding_data)} funding records and {len(civic_docs)} civic documents")

# Identify disaster-related projects that started in 2022
disaster_indicators = ['(FEMA Project)', '(CalOES Project)', '(CalJPIA Project)', 'FEMA/CalOES', 'FEMA', 'CalOES', 'CalJPIA']
projects_2022 = []

# Extract projects from civic docs
for doc in civic_docs:
    text = doc.get('text', '')
    filename = doc.get('filename', '')
    
    lines = text.split('\n')
    for i, line in enumerate(lines):
        line = line.strip()
        if not line or len(line) < 10:
            continue
            
        # Check context for disaster indicators
        context_window = 5
        start_idx = max(0, i - context_window)
        end_idx = min(len(lines), i + context_window + 1)
        context = '\n'.join(lines[start_idx:end_idx])
        
        # Check if disaster-related
        has_disaster = any(indicator.lower() in context.lower() for indicator in disaster_indicators)
        
        # Check if line looks like a project name
        project_keywords = ['Project', 'Improvements', 'Repairs', 'Replacement', 'Drainage', 'Bridge', 'Culvert', 'Resurfacing']
        looks_like_project = any(keyword in line for keyword in project_keywords)
        
        if has_disaster and looks_like_project:
            # Check for 2022 date in context
            if '2022' in context:
                project_name = line
                if project_name.endswith(':'):
                    project_name = project_name[:-1]
                
                # Find date
                st = '2022'
                date_patterns = [r'2022-\w+', r'2022-\d{1,2}', r'\b\w+\s+2022\b']
                for pattern in date_patterns:
                    matches = re.findall(pattern, context)
                    if matches:
                        st = matches[0]
                        break
                
                project_name = project_name.strip()
                if project_name and not any(p['name'] == project_name for p in projects_2022):
                    projects_2022.append({
                        'name': project_name,
                        'start_date': st,
                        'filename': filename
                    })

# Also check for projects starting with 2022 in name
for doc in civic_docs:
    text = doc.get('text', '')
    lines = text.split('\n')
    for line in lines:
        line = line.strip()
        if line.startswith('2022') and any(word in line for word in ['Project', 'Improvements', 'Repairs']):
            if 'storm' in line.lower() or 'drain' in line.lower() or 'fema' in line.lower():
                project_name = line
                if project_name.endswith(':'):
                    project_name = project_name[:-1]
                
                if project_name and not any(p['name'] == project_name for p in projects_2022):
                    projects_2022.append({
                        'name': project_name,
                        'start_date': '2022',
                        'filename': doc.get('filename', '')
                    })

print(f"\nFound {len(projects_2022)} disaster projects from 2022:")
for p in projects_2022[:10]:
    print(f"- {p['name']}")

# Match with funding
def clean_name(name):
    return name.lower().replace('(', '').replace(')', '').replace('-', ' ').strip()

matched_funding = []
for project in projects_2022:
    project_name_clean = clean_name(project['name'])
    
    for funding in funding_data:
        funding_name = funding.get('Project_Name', '')
        funding_name_clean = clean_name(funding_name)
        
        # Check for match
        if (project['name'] == funding_name or 
            funding_name.startswith(project['name']) or
            project_name_clean in funding_name_clean):
            matched_funding.append({
                'project': project['name'],
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
    'details': matched_funding[:20]  # first 20
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.query_db:9': 'file_storage/functions.query_db:9.json', 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json', 'var_functions.query_db:13': 'file_storage/functions.query_db:13.json', 'var_functions.query_db:22': 'file_storage/functions.query_db:22.json', 'var_functions.query_db:23': 'file_storage/functions.query_db:23.json', 'var_functions.query_db:20': 'file_storage/functions.query_db:20.json', 'var_functions.query_db:21': 'file_storage/functions.query_db:21.json', 'var_functions.query_db:26': [{'Project_Name': '2021 Annual Street Maintenance', 'Amount': '24000'}, {'Project_Name': '2022 Annual Street Maintenance', 'Amount': '45000'}, {'Project_Name': '2022 Morning View Resurfacing & Storm Drain Improvements', 'Amount': '38000'}, {'Project_Name': 'Annual Street Maintenance', 'Amount': '23000'}, {'Project_Name': 'Birdview Avenue Improvements', 'Amount': '79000'}], 'var_functions.query_db:27': 'file_storage/functions.query_db:27.json', 'var_functions.query_db:32': 'file_storage/functions.query_db:32.json', 'var_functions.query_db:33': 'file_storage/functions.query_db:33.json', 'var_functions.query_db:36': 'file_storage/functions.query_db:36.json', 'var_functions.query_db:37': 'file_storage/functions.query_db:37.json', 'var_functions.query_db:42': 'file_storage/functions.query_db:42.json', 'var_functions.query_db:43': 'file_storage/functions.query_db:43.json'}

exec(code, env_args)
