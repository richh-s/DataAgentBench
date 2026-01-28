code = """import json, re, os

civic_file = locals().get('var_functions.query_db:62', '/tmp/tmp8r9gntdv.json')
funding_file = locals().get('var_functions.query_db:24', '/tmp/tmp8r9gntdv.json')

# Read files
civic_f = open(civic_file)
civic_docs = json.load(civic_f)
civic_f.close()

funding_f = open(funding_file)
funding_records = json.load(funding_f)
funding_f.close()

print('Loaded', len(civic_docs), 'docs,', len(funding_records), 'funding')

# Find park projects completed in 2022
park_projects = []
for doc in civic_docs:
    text = doc.get('text', '')
    if '2022' in text and 'completed' in text.lower() and 'park' in text.lower():
        lines = text.split('\n')
        for i in range(len(lines)):
            line = lines[i].strip()
            if line and 'Park' in line and len(line) > 10:
                # Look nearby for completion mention
                start = max(0, i-2)
                end = min(len(lines), i+5)
                window = ' '.join(lines[start:end])
                if '2022' in window and 'completed' in window.lower():
                    clean = re.sub(r'[^A-Za-z0-9\s\-&]', '', line)
                    clean = re.sub(r'\s+(Project|Repair|Improvements)$', '', clean, flags=re.IGNORECASE)
                    if len(clean.strip()) > 5:
                        park_projects.append(clean.strip())

park_projects = list(set(park_projects))
print('Park projects in 2022:', park_projects)

# Calculate funding
ccommon = {'park','project','repair','improvements','and','the','at','in','of'}
total = 0
for park in park_projects:
    park_words = set(re.findall(r'\b\w+\b', park.lower())) - ccommon
    for funding in funding_records:
        funding_name = funding.get('Project_Name', '')
        funding_clean = re.sub(r'\s+(Project|Repair|Improvements)$', '', funding_name, flags=re.IGNORECASE)
        funding_words = set(re.findall(r'\b\w+\b', funding_clean.lower())) - ccommon
        if park_words and funding_words and len(park_words.intersection(funding_words)) > 0:
            total += int(funding.get('Amount', 0))
            break

result = {'count': len(park_projects), 'total_funding': total}
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.execute_python:10': {'num_documents': 5, 'type': "<class 'list'>", 'data_preview': "[{'_id': '694eef5c4ec675b6b5f5a285', 'filename': 'malibucity_agenda_03222023-2060.txt', 'text': 'Public Works Commission\\nAgenda Report\\n\\nPublic Works\\nCommission Meeting\\n03-22-23\\nItem\\n4.B.\\n\\nTo:\\n\\nChair Dittrich and Members of the Public Works Commission\\n\\nPrepared by:\\n\\nJorge Rubalcava, Senior Civil Engineer\\n\\nApproved by:\\n\\nRob DuBoux, Public Works Director/City Engineer\\n\\nDate prepared: March 15, 2023\\n\\nMeeting date: March 22, 2023\\n\\nSubject:\\n\\nCapital Improvement Projects and "}, 'var_functions.query_db:18': [{'Funding_ID': '1', 'Project_Name': '2021 Annual Street Maintenance', 'Funding_Source': 'Public-Private Partnership (PPP)', 'Amount': '24000'}, {'Funding_ID': '2', 'Project_Name': '2022 Annual Street Maintenance', 'Funding_Source': 'Government Grant', 'Amount': '45000'}, {'Funding_ID': '3', 'Project_Name': '2022 Morning View Resurfacing & Storm Drain Improvements', 'Funding_Source': 'State Development Grant', 'Amount': '38000'}, {'Funding_ID': '4', 'Project_Name': 'Annual Street Maintenance', 'Funding_Source': 'Corporate Sponsorship', 'Amount': '23000'}, {'Funding_ID': '5', 'Project_Name': 'Birdview Avenue Improvements', 'Funding_Source': 'National Foundation Fund', 'Amount': '79000'}], 'var_functions.list_db:20': ['Funding'], 'var_functions.query_db:24': 'file_storage/functions.query_db:24.json', 'var_functions.execute_python:34': {'civic_docs_count': 5, 'funding_records_count': 500}, 'var_functions.query_db:44': 'file_storage/functions.query_db:44.json', 'var_functions.query_db:50': [{'Project_Name': 'Bluffs Park Shade Structure', 'Amount': '21000'}, {'Project_Name': 'Bluffs Park Workout Station', 'Amount': '39000'}, {'Project_Name': 'Legacy Park Benches and Arbors Renovation', 'Amount': '41000'}, {'Project_Name': 'Legacy Park Paver Repair Project', 'Amount': '69000'}, {'Project_Name': 'Malibu Bluffs Park Roof Replacement Project', 'Amount': '44000'}, {'Project_Name': 'Malibu Bluffs Park South Walkway', 'Amount': '91000'}, {'Project_Name': 'Malibu Bluffs Park South Walkway Repairs', 'Amount': '81000'}, {'Project_Name': 'Malibu Park Drainage Improvements', 'Amount': '17000'}, {'Project_Name': 'Malibu Park Resurfacing Project', 'Amount': '14000'}, {'Project_Name': 'Malibu Park Storm Drain Repairs', 'Amount': '50000'}, {'Project_Name': 'Permanent Skate Park', 'Amount': '97000'}, {'Project_Name': 'Trancas Canyon Park Planting and Irrigation Repairs', 'Amount': '78000'}, {'Project_Name': 'Trancas Canyon Park Planting and Irrigation Repairs (CalJPIA/FEMA Project)', 'Amount': '44000'}, {'Project_Name': 'Trancas Canyon Park Planting and Irrigation Repairs (FEMA/CalOES Project)', 'Amount': '92000'}, {'Project_Name': 'Trancas Canyon Park Playground', 'Amount': '24000'}, {'Project_Name': 'Trancas Canyon Park Playground Resurfacing', 'Amount': '65000'}, {'Project_Name': 'Trancas Canyon Park Slope Stabilization Project', 'Amount': '68000'}, {'Project_Name': 'Trancas Canyon Park Slope Stabilization Project (CalJPIA Project)', 'Amount': '43000'}, {'Project_Name': 'Trancas Canyon Park Slope Stabilization Project (CalOES Project)', 'Amount': '32000'}, {'Project_Name': 'Trancas Canyon Park Upper and Lower Slopes Repair', 'Amount': '23000'}], 'var_functions.query_db:60': 'file_storage/functions.query_db:60.json', 'var_functions.query_db:62': 'file_storage/functions.query_db:62.json'}

exec(code, env_args)
