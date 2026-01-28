code = """import json
import re

# Load civic documents
civic_docs = locals().get('var_functions.query_db:2')
if isinstance(civic_docs, str) and civic_docs.endswith('.json'):
    with open(civic_docs, 'r') as f:
        civic_docs = json.load(f)

# Load funding data
funding_data = locals().get('var_functions.query_db:24')
if isinstance(funding_data, str) and funding_data.endswith('.json'):
    with open(funding_data, 'r') as f:
        funding_records = json.load(f)
else:
    funding_records = funding_data

print(f'Loaded {len(civic_docs)} civic docs and {len(funding_records)} funding records')

# Extract park projects completed in 2022 from civic docs
park_projects_2022 = []

for doc in civic_docs:
    text = doc.get('text', '')
    lines = text.split('\n')
    
    # Look for patterns indicating park projects completed in 2022
    i = 0
    while i < len(lines):
        line = lines[i].strip()
        
        # Check if line looks like a project name containing "Park" 
        # and not a header
        if ('Park' in line and 
            len(line) > 5 and 
            not line.startswith('Page') and
            not line.startswith('Agenda') and
            not any(header in line for header in ['Public Works', 'Commission', 'Capital Improvement', 'Disaster Recovery'])):
            
            # Look ahead for completion info in 2022
            project_name = line
            completed_2022 = False
            completion_line = ''
            
            # Check next 5 lines
            for j in range(i+1, min(i+6, len(lines))):
                next_line = lines[j].strip()
                if ('2022' in next_line and 
                    'completed' in next_line.lower()):
                    completed_2022 = True
                    completion_line = next_line
                    break
            
            if completed_2022:
                # Clean up project name
                project_name = re.sub(r'^[^A-Za-z]*', '', project_name)  # Remove leading non-letters
                project_name = re.sub(r'[^A-Za-z0-9\s\-&]', '', project_name)  # Remove special chars
                project_name = project_name.strip()
                
                if len(project_name) > 3:
                    park_projects_2022.append({
                        'Project_Name': project_name,
                        'completion_note': completion_line
                    })
        i += 1

# Also search for "completed" + "2022" + "park" anywhere in the document text
for doc in civic_docs:
    text = doc.get('text', '')
    
    # Find all lines mentioning completion in 2022
    lines = text.split('\n')
    for i, line in enumerate(lines):
        if '2022' in line and 'completed' in line.lower():
            # Look for nearby project names mentioning park
            # Check previous few lines
            for j in range(max(0, i-3), i):
                prev_line = lines[j].strip()
                if ('Park' in prev_line and 
                    len(prev_line) > 5 and 
                    not any(header in prev_line for header in ['Page', 'Agenda', 'Public', 'Commission'])):
                    
                    project_name = re.sub(r'[^A-Za-z0-9\s\-&]', '', prev_line).strip()
                    if project_name and len(project_name) > 3:
                        # Avoid duplicates
                        if not any(p['Project_Name'] == project_name for p in park_projects_2022):
                            park_projects_2022.append({
                                'Project_Name': project_name,
                                'completion_note': line
                            })

print(f'Found {len(park_projects_2022)} park projects completed in 2022')

# Match with funding records
total_funding = 0
matched_projects = []

for park_project in park_projects_2022:
    park_name = park_project['Project_Name'].lower()
    
    best_match = None
    best_score = 0
    
    for funding in funding_records:
        funding_name = funding.get('Project_Name', '').lower()
        
        # Calculate similarity score
        park_words = set(re.findall(r'\b\w+\b', park_name))
        funding_words = set(re.findall(r'\b\w+\b', funding_name))
        
        # Remove common words
        common = {'park', 'project', 'repair', 'repairs', 'improvements', 'and', 'the', 'at', 'in', 'of', 'phase', 'road', 'street', 'avenue', 'drive', 'lane', 'way', 'boulevard', 'canyon'}
        park_key = park_words - common
        funding_key = funding_words - common
        
        if park_key and funding_key:
            # Check for exact match of key words
            intersection = park_key.intersection(funding_key)
            score = len(intersection) / max(len(park_key), len(funding_key))
            
            if score > best_score and score >= 0.3:  # At least 30% match
                best_score = score
                best_match = funding
    
    if best_match:
        amount = int(best_match.get('Amount', 0))
        total_funding += amount
        matched_projects.append({
            'project_name': park_project['Project_Name'],
            'funding_name': best_match.get('Project_Name'),
            'amount': amount
        })

result = {
    'total_park_projects_2022': len(park_projects_2022),
    'matched_with_funding': len(matched_projects),
    'total_funding': total_funding,
    'details': {
        'projects': matched_projects,
        'all_park_projects': [p['Project_Name'] for p in park_projects_2022]
    }
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.execute_python:10': {'num_documents': 5, 'type': "<class 'list'>", 'data_preview': "[{'_id': '694eef5c4ec675b6b5f5a285', 'filename': 'malibucity_agenda_03222023-2060.txt', 'text': 'Public Works Commission\\nAgenda Report\\n\\nPublic Works\\nCommission Meeting\\n03-22-23\\nItem\\n4.B.\\n\\nTo:\\n\\nChair Dittrich and Members of the Public Works Commission\\n\\nPrepared by:\\n\\nJorge Rubalcava, Senior Civil Engineer\\n\\nApproved by:\\n\\nRob DuBoux, Public Works Director/City Engineer\\n\\nDate prepared: March 15, 2023\\n\\nMeeting date: March 22, 2023\\n\\nSubject:\\n\\nCapital Improvement Projects and "}, 'var_functions.query_db:18': [{'Funding_ID': '1', 'Project_Name': '2021 Annual Street Maintenance', 'Funding_Source': 'Public-Private Partnership (PPP)', 'Amount': '24000'}, {'Funding_ID': '2', 'Project_Name': '2022 Annual Street Maintenance', 'Funding_Source': 'Government Grant', 'Amount': '45000'}, {'Funding_ID': '3', 'Project_Name': '2022 Morning View Resurfacing & Storm Drain Improvements', 'Funding_Source': 'State Development Grant', 'Amount': '38000'}, {'Funding_ID': '4', 'Project_Name': 'Annual Street Maintenance', 'Funding_Source': 'Corporate Sponsorship', 'Amount': '23000'}, {'Funding_ID': '5', 'Project_Name': 'Birdview Avenue Improvements', 'Funding_Source': 'National Foundation Fund', 'Amount': '79000'}], 'var_functions.list_db:20': ['Funding'], 'var_functions.query_db:24': 'file_storage/functions.query_db:24.json'}

exec(code, env_args)
