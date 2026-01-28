code = """import json, re

civic_docs = locals().get('var_functions.query_db:2')
if isinstance(civic_docs, str) and civic_docs.endswith('.json'):
    with open(civic_docs, 'r') as f:
        civic_docs = json.load(f)

funding_data = locals().get('var_functions.query_db:24')
if isinstance(funding_data, str) and funding_data.endswith('.json'):
    with open(funding_data, 'r') as f:
        funding_records = json.load(f)
else:
    funding_records = funding_data

print('Loaded docs:', len(civic_docs), 'funding records:', len(funding_records))

park_projects_2022 = []
for doc in civic_docs:
    text = doc.get('text', '')
    lines = text.split('\n')
    
    for i in range(len(lines)):
        line = lines[i].strip()
        if not line:
            continue
        
        if 'Park' in line and len(line) > 5:
            for j in range(i+1, min(i+6, len(lines))):
                next_line = lines[j].strip()
                if '2022' in next_line and 'completed' in next_line.lower():
                    clean_name = re.sub(r'[^A-Za-z0-9\s\-&]', '', line).strip()
                    if len(clean_name) > 3:
                        park_projects_2022.append({'Project_Name': clean_name, 'note': next_line})
                    break

total_funding = 0
matched_projects = []

for park in park_projects_2022:
    park_name = park['Project_Name'].lower()
    park_words = set(re.findall(r'\b\w+\b', park_name)) - {'park','project','repair','improvements','and','the','at','in','of','phase','road'}
    
    for funding in funding_records:
        funding_name = funding.get('Project_Name','').lower()
        funding_words = set(re.findall(r'\b\w+\b', funding_name)) - {'park','project','repair','improvements','and','the','at','in','of','phase','road'}
        
        if park_words and funding_words:
            intersect = park_words.intersection(funding_words)
            if len(intersect) > 0:
                amount = int(funding.get('Amount',0))
                total_funding += amount
                matched_projects.append({
                    'park_name': park['Project_Name'],
                    'funding_name': funding.get('Project_Name'),
                    'amount': amount
                })
                break

result = {
    'park_projects_2022': len(park_projects_2022),
    'matched_funding_records': len(matched_projects),
    'total_funding_dollars': total_funding,
    'matched_projects': matched_projects
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.execute_python:10': {'num_documents': 5, 'type': "<class 'list'>", 'data_preview': "[{'_id': '694eef5c4ec675b6b5f5a285', 'filename': 'malibucity_agenda_03222023-2060.txt', 'text': 'Public Works Commission\\nAgenda Report\\n\\nPublic Works\\nCommission Meeting\\n03-22-23\\nItem\\n4.B.\\n\\nTo:\\n\\nChair Dittrich and Members of the Public Works Commission\\n\\nPrepared by:\\n\\nJorge Rubalcava, Senior Civil Engineer\\n\\nApproved by:\\n\\nRob DuBoux, Public Works Director/City Engineer\\n\\nDate prepared: March 15, 2023\\n\\nMeeting date: March 22, 2023\\n\\nSubject:\\n\\nCapital Improvement Projects and "}, 'var_functions.query_db:18': [{'Funding_ID': '1', 'Project_Name': '2021 Annual Street Maintenance', 'Funding_Source': 'Public-Private Partnership (PPP)', 'Amount': '24000'}, {'Funding_ID': '2', 'Project_Name': '2022 Annual Street Maintenance', 'Funding_Source': 'Government Grant', 'Amount': '45000'}, {'Funding_ID': '3', 'Project_Name': '2022 Morning View Resurfacing & Storm Drain Improvements', 'Funding_Source': 'State Development Grant', 'Amount': '38000'}, {'Funding_ID': '4', 'Project_Name': 'Annual Street Maintenance', 'Funding_Source': 'Corporate Sponsorship', 'Amount': '23000'}, {'Funding_ID': '5', 'Project_Name': 'Birdview Avenue Improvements', 'Funding_Source': 'National Foundation Fund', 'Amount': '79000'}], 'var_functions.list_db:20': ['Funding'], 'var_functions.query_db:24': 'file_storage/functions.query_db:24.json'}

exec(code, env_args)
