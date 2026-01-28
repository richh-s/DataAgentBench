code = """import json, re

# Access data from storage
civic_docs = locals().get('var_functions.query_db:2')
funding_data = locals().get('var_functions.query_db:24')

# Handle file paths
import os
if isinstance(civic_docs, str) and os.path.exists(civic_docs):
    with open(civic_docs) as f:
        civic_docs = json.load(f)

if isinstance(funding_data, str) and os.path.exists(funding_data):
    with open(funding_data) as f:
        funding_records = json.load(f)
else:
    funding_records = funding_data

# Extract park projects completed in 2022
park_projects = []
for doc in civic_docs:
    text = doc.get('text', '')
    if 'park' in text.lower() and 'completed' in text.lower() and '2022' in text:
        lines = text.split('\n')
        for i, line in enumerate(lines):
            line = line.strip()
            if line and 'Park' in line and len(line) > 10:
                context = ' '.join(lines[i:min(i+5, len(lines))])
                if 'completed' in context.lower() and '2022' in context:
                    clean_name = re.sub('[^A-Za-z0-9\s\-&]', '', line).strip()
                    if clean_name and len(clean_name) > 3:
                        park_projects.append(clean_name)

# Remove duplicates
park_projects = list(set(park_projects))

# Match with funding records
matches = []
total_funding = 0
common_words = {'park','project','repair','improvements','and','the','at','in','of','phase'}

for park_name in park_projects:
    park_words = set(re.findall(r'\b\w+\b', park_name.lower())) - common_words
    
    for funding in funding_records:
        funding_name = funding.get('Project_Name', '').lower()
        funding_words = set(re.findall(r'\b\w+\b', funding_name)) - common_words
        
        if park_words and funding_words and len(park_words.intersection(funding_words)) > 0:
            amount = int(funding.get('Amount', 0))
            total_funding += amount
            matches.append({
                'park_project': park_name,
                'funding_record': funding.get('Project_Name'),
                'amount': amount
            })
            break

result = {
    'total_park_projects_2022': len(park_projects),
    'matched_funding_records': len(matches),
    'total_funding_dollars': total_funding
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.execute_python:10': {'num_documents': 5, 'type': "<class 'list'>", 'data_preview': "[{'_id': '694eef5c4ec675b6b5f5a285', 'filename': 'malibucity_agenda_03222023-2060.txt', 'text': 'Public Works Commission\\nAgenda Report\\n\\nPublic Works\\nCommission Meeting\\n03-22-23\\nItem\\n4.B.\\n\\nTo:\\n\\nChair Dittrich and Members of the Public Works Commission\\n\\nPrepared by:\\n\\nJorge Rubalcava, Senior Civil Engineer\\n\\nApproved by:\\n\\nRob DuBoux, Public Works Director/City Engineer\\n\\nDate prepared: March 15, 2023\\n\\nMeeting date: March 22, 2023\\n\\nSubject:\\n\\nCapital Improvement Projects and "}, 'var_functions.query_db:18': [{'Funding_ID': '1', 'Project_Name': '2021 Annual Street Maintenance', 'Funding_Source': 'Public-Private Partnership (PPP)', 'Amount': '24000'}, {'Funding_ID': '2', 'Project_Name': '2022 Annual Street Maintenance', 'Funding_Source': 'Government Grant', 'Amount': '45000'}, {'Funding_ID': '3', 'Project_Name': '2022 Morning View Resurfacing & Storm Drain Improvements', 'Funding_Source': 'State Development Grant', 'Amount': '38000'}, {'Funding_ID': '4', 'Project_Name': 'Annual Street Maintenance', 'Funding_Source': 'Corporate Sponsorship', 'Amount': '23000'}, {'Funding_ID': '5', 'Project_Name': 'Birdview Avenue Improvements', 'Funding_Source': 'National Foundation Fund', 'Amount': '79000'}], 'var_functions.list_db:20': ['Funding'], 'var_functions.query_db:24': 'file_storage/functions.query_db:24.json', 'var_functions.execute_python:34': {'civic_docs_count': 5, 'funding_records_count': 500}}

exec(code, env_args)
