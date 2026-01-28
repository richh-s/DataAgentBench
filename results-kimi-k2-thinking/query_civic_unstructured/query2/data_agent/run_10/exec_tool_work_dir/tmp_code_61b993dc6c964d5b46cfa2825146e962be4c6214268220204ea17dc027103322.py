code = """import json, re, os

# Load data from file paths if needed
civic_docs_path = locals().get('var_functions.query_db:2')
funding_path = locals().get('var_functions.query_db:24')

if isinstance(civic_docs_path, str):
    with open(civic_docs_path, 'r') as f:
        civic_docs = json.load(f)
else:
    civic_docs = civic_docs_path

if isinstance(funding_path, str):
    with open(funding_path, 'r') as f:
        funding_records = json.load(f)
else:
    funding_records = funding_path

print(f'Data loaded: {len(civic_docs)} docs, {len(funding_records)} funding records')

# Extract park projects completed in 2022
park_projects_2022 = []

for doc in civic_docs:
    text = doc.get('text', '')
    lines = text.split('\n')
    
    i = 0
    while i < len(lines):
        line = lines[i].strip()
        # Skip empty lines and obvious headers
        if not line or line.startswith('Page') or line.startswith('Agenda'):
            i += 1
            continue
            
        # Look for project names containing Park (but not headers)
        if 'Park' in line and len(line) > 10:
            is_header = any(h in line for h in ['Public Works', 'Commission', 'Capital Improvement', 'Disaster Recovery', 'Prepared by', 'Approved by', 'Date prepared'])
            if not is_header:
                # Check next few lines for completion in 2022
                for j in range(i+1, min(i+5, len(lines))):
                    next_line = lines[j].strip()
                    if ('2022' in next_line and 'completed' in next_line.lower()):
                        # Clean the project name
                        clean_name = re.sub(r'[^A-Za-z0-9\s\-&]', '', line).strip()
                        park_projects_2022.append(clean_name)
                        break
        i += 1

# Remove duplicates
park_projects_2022 = list(set(park_projects_2022))

# Match with funding records
total_funding = 0
matched_projects = []

for park_name in park_projects_2022:
    park_words = set(re.findall(r'\b\w+\b', park_name.lower()))
    park_words = park_words - {'park', 'project', 'repair', 'repairs', 'improvements', 'and', 'the', 'at', 'in', 'of', 'phase'}
    
    for funding in funding_records:
        funding_name = funding.get('Project_Name', '').lower()
        funding_words = set(re.findall(r'\b\w+\b', funding_name))
        funding_words = funding_words - {'park', 'project', 'repair', 'repairs', 'improvements', 'and', 'the', 'at', 'in', 'of', 'phase'}
        
        # Check for word overlap
        if park_words and funding_words:
            overlap = park_words.intersection(funding_words)
            if len(overlap) > 0:  # At least one key word matches
                amount = int(funding.get('Amount', 0))
                total_funding += amount
                matched_projects.append({
                    'park_project': park_name,
                    'funding_record': funding.get('Project_Name'),
                    'amount': amount
                })
                break

result = {
    'park_projects_2022': len(park_projects_2022),
    'funding_matches': len(matched_projects),
    'total_funding_amount': total_funding,
    'matched_funding_details': matched_projects
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.execute_python:10': {'num_documents': 5, 'type': "<class 'list'>", 'data_preview': "[{'_id': '694eef5c4ec675b6b5f5a285', 'filename': 'malibucity_agenda_03222023-2060.txt', 'text': 'Public Works Commission\\nAgenda Report\\n\\nPublic Works\\nCommission Meeting\\n03-22-23\\nItem\\n4.B.\\n\\nTo:\\n\\nChair Dittrich and Members of the Public Works Commission\\n\\nPrepared by:\\n\\nJorge Rubalcava, Senior Civil Engineer\\n\\nApproved by:\\n\\nRob DuBoux, Public Works Director/City Engineer\\n\\nDate prepared: March 15, 2023\\n\\nMeeting date: March 22, 2023\\n\\nSubject:\\n\\nCapital Improvement Projects and "}, 'var_functions.query_db:18': [{'Funding_ID': '1', 'Project_Name': '2021 Annual Street Maintenance', 'Funding_Source': 'Public-Private Partnership (PPP)', 'Amount': '24000'}, {'Funding_ID': '2', 'Project_Name': '2022 Annual Street Maintenance', 'Funding_Source': 'Government Grant', 'Amount': '45000'}, {'Funding_ID': '3', 'Project_Name': '2022 Morning View Resurfacing & Storm Drain Improvements', 'Funding_Source': 'State Development Grant', 'Amount': '38000'}, {'Funding_ID': '4', 'Project_Name': 'Annual Street Maintenance', 'Funding_Source': 'Corporate Sponsorship', 'Amount': '23000'}, {'Funding_ID': '5', 'Project_Name': 'Birdview Avenue Improvements', 'Funding_Source': 'National Foundation Fund', 'Amount': '79000'}], 'var_functions.list_db:20': ['Funding'], 'var_functions.query_db:24': 'file_storage/functions.query_db:24.json', 'var_functions.execute_python:34': {'civic_docs_count': 5, 'funding_records_count': 500}}

exec(code, env_args)
