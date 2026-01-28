code = """import json
import re

# Get the civic docs data - it's stored in var_functions.query_db:2
civic_docs_key = 'var_functions.query_db:2'
civic_docs_data = globals().get(civic_docs_key)

if not civic_docs_data:
    # Try reading as file path
    try:
        with open('/tmp/tmp8r9gntdv.json', 'r') as f:
            civic_docs = json.load(f)
    except:
        civic_docs = []
elif isinstance(civic_docs_data, str) and '.json' in civic_docs_data:
    with open(civic_docs_data, 'r') as f:
        civic_docs = json.load(f)
else:
    civic_docs = civic_docs_data

print(f'Documents loaded: {len(civic_docs)}')

# Extract park projects completed in 2022
park_projects_2022 = []

for doc in civic_docs:
    text = doc.get('text', '')
    # Look for patterns like "Construction was completed November 2022" or similar
    
    # Find all project mentions with park and completion in 2022
    # Pattern: project name followed by completion info
    lines = text.split('\n')
    
    for i, line in enumerate(lines):
        line = line.strip()
        if not line:
            continue
            
        # Check if this line mentions a park project completed in 2022
        if ('park' in line.lower() and '2022' in line and 
            'completed' in line.lower()):
            
            # Try to find project name (previous line or this line)
            project_name = 'Unknown Park Project'
            if i > 0:
                prev_line = lines[i-1].strip()
                if prev_line and len(prev_line) > 5 and not prev_line.startswith('('):
                    project_name = prev_line
            
            # Also look for project name in current line if it has a colon or dash
            if ':' in line or '-' in line:
                parts = re.split('[:\-]', line)
                if parts[0] and len(parts[0]) > 10:
                    project_name = parts[0].strip()
            
            park_projects_2022.append({
                'Project_Name': project_name,
                'note': line
            })
        
        # Also check if a park-related project name is followed by completion in next few lines
        if i < len(lines) - 1 and 'park' in line.lower():
            project_name = line
            # Check next 3 lines for completion info
            for j in range(i+1, min(i+4, len(lines))):
                next_line = lines[j].strip()
                if ('2022' in next_line and 'completed' in next_line.lower()):
                    park_projects_2022.append({
                        'Project_Name': project_name,
                        'note': next_line
                    })
                    break

print(f'Found {len(park_projects_2022)} park projects completed in 2022')

# Get funding data
funding_data = globals().get('var_functions.query_db:18')
if isinstance(funding_data, str) and '.json' in funding_data:
    with open(funding_data, 'r') as f:
        funding_records = json.load(f)
else:
    funding_records = funding_data

print(f'Funding records: {len(funding_records)}')

# Try to match park projects with funding records
total_funding = 0
matched_projects = []

for park_project in park_projects_2022:
    park_name = park_project['Project_Name']
    
    # Look for matching funding record
    for funding in funding_records:
        funding_name = funding.get('Project_Name', '')
        
        # Simple matching - check if key words match
        park_words = set(re.findall(r'\b\w+\b', park_name.lower()))
        funding_words = set(re.findall(r'\b\w+\b', funding_name.lower()))
        
        # Check for substantial overlap (ignore common words)
        common_words = {'project', 'park', 'repair', 'improvements', 'road', 'street', 'construction', 'phase', 'and', 'the', 'at'}
        park_key = park_words - common_words
        funding_key = funding_words - common_words
        
        if park_key and funding_key and len(park_key.intersection(funding_key)) > 0:
            amount = int(funding.get('Amount', 0))
            total_funding += amount
            matched_projects.append({
                'project': park_name,
                'funding_project': funding_name,
                'amount': amount
            })
            break

print(f'Matched projects: {len(matched_projects)}')
print(f'Total funding: {total_funding}')

output = {
    'park_projects_2022': len(park_projects_2022),
    'matched_with_funding': len(matched_projects),
    'total_funding': total_funding,
    'details': matched_projects
}

print('__RESULT__:')
print(json.dumps(output))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.execute_python:10': {'num_documents': 5, 'type': "<class 'list'>", 'data_preview': "[{'_id': '694eef5c4ec675b6b5f5a285', 'filename': 'malibucity_agenda_03222023-2060.txt', 'text': 'Public Works Commission\\nAgenda Report\\n\\nPublic Works\\nCommission Meeting\\n03-22-23\\nItem\\n4.B.\\n\\nTo:\\n\\nChair Dittrich and Members of the Public Works Commission\\n\\nPrepared by:\\n\\nJorge Rubalcava, Senior Civil Engineer\\n\\nApproved by:\\n\\nRob DuBoux, Public Works Director/City Engineer\\n\\nDate prepared: March 15, 2023\\n\\nMeeting date: March 22, 2023\\n\\nSubject:\\n\\nCapital Improvement Projects and "}, 'var_functions.query_db:18': [{'Funding_ID': '1', 'Project_Name': '2021 Annual Street Maintenance', 'Funding_Source': 'Public-Private Partnership (PPP)', 'Amount': '24000'}, {'Funding_ID': '2', 'Project_Name': '2022 Annual Street Maintenance', 'Funding_Source': 'Government Grant', 'Amount': '45000'}, {'Funding_ID': '3', 'Project_Name': '2022 Morning View Resurfacing & Storm Drain Improvements', 'Funding_Source': 'State Development Grant', 'Amount': '38000'}, {'Funding_ID': '4', 'Project_Name': 'Annual Street Maintenance', 'Funding_Source': 'Corporate Sponsorship', 'Amount': '23000'}, {'Funding_ID': '5', 'Project_Name': 'Birdview Avenue Improvements', 'Funding_Source': 'National Foundation Fund', 'Amount': '79000'}], 'var_functions.list_db:20': ['Funding']}

exec(code, env_args)
