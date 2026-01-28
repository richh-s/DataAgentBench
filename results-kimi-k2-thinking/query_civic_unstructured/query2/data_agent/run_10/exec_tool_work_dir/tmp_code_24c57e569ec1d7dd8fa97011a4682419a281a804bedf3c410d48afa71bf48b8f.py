code = """import json, re, os

# Access the data from storage variables
civic_docs_var = 'var_functions.query_db:44'
funding_docs_var = 'var_functions.query_db:24'

# Load civic documents
civic_path = locals().get(civic_docs_var)
if civic_path and os.path.isfile(civic_path):
    with open(civic_path) as f:
        civic_docs = json.load(f)
else:
    civic_docs = []

# Load funding records
funding_path = locals().get(funding_docs_var)
if funding_path and os.path.isfile(funding_path):
    with open(funding_path) as f:
        funding_records = json.load(f)
else:
    funding_records = locals().get('var_functions.query_db:50', [])

print('Documents loaded:', len(civic_docs), 'Funding records loaded:', len(funding_records))

# Extract park projects completed in 2022
park_projects_2022 = []

for doc in civic_docs:
    text = doc.get('text', '')
    # Check if this document mentions park completion in 2022
    if '2022' in text and 'completed' in text.lower() and 'park' in text.lower():
        lines = text.split('\n')
        for i, line in enumerate(lines):
            line_clean = line.strip()
            # Look for project names containing Park
            if line_clean and 'Park' in line_clean and len(line_clean) > 8:
                # Check if completion in 2022 is mentioned nearby
                context_lines = lines[max(0,i-2):min(len(lines), i+5)]
                context = ' '.join(context_lines)
                if '2022' in context and 'completed' in context.lower():
                    park_projects_2022.append(line_clean)

# Remove duplicates
park_projects_2022 = list(set(park_projects_2022))
print('Park projects completed in 2022:', len(park_projects_2022))
for p in park_projects_2022:
    print(' -', p)

# Match with funding records and calculate total funding
total_funding = 0
matched_projects = []
common_words = {'park', 'project', 'repair', 'repairs', 'improvements', 'improvement', 'and', 'the', 'at', 'in', 'of', 'south', 'north', 'east', 'west'}

for park_project in park_projects_2022:
    # Clean project name for matching
    park_clean = park_project.lower()
    park_clean = re.sub(r'[^a-z0-9\s]', ' ', park_clean)
    park_words = set(park_clean.split()) - common_words
    
    for funding_record in funding_records:
        funding_name = funding_record.get('Project_Name', '')
        funding_clean = funding_name.lower()
        funding_clean = re.sub(r'[^a-z0-9\s]', ' ', funding_clean)
        funding_words = set(funding_clean.split()) - common_words
        
        # Check for overlap in key words
        if park_words and funding_words:
            overlap = park_words.intersection(funding_words)
            if len(overlap) > 1:  # At least 2 matching words (more reliable)
                amount = int(funding_record.get('Amount', 0))
                total_funding += amount
                matched_projects.append({
                    'park_project': park_project,
                    'funding_record': funding_name,
                    'amount': amount
                })
                break

# Output result
result = {
    'total_park_projects_2022': len(park_projects_2022),
    'matched_with_funding': len(matched_projects),
    'total_funding_dollars': total_funding,
    'matched_details': matched_projects
}

print('Total funding for park projects completed in 2022:', total_funding)
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.execute_python:10': {'num_documents': 5, 'type': "<class 'list'>", 'data_preview': "[{'_id': '694eef5c4ec675b6b5f5a285', 'filename': 'malibucity_agenda_03222023-2060.txt', 'text': 'Public Works Commission\\nAgenda Report\\n\\nPublic Works\\nCommission Meeting\\n03-22-23\\nItem\\n4.B.\\n\\nTo:\\n\\nChair Dittrich and Members of the Public Works Commission\\n\\nPrepared by:\\n\\nJorge Rubalcava, Senior Civil Engineer\\n\\nApproved by:\\n\\nRob DuBoux, Public Works Director/City Engineer\\n\\nDate prepared: March 15, 2023\\n\\nMeeting date: March 22, 2023\\n\\nSubject:\\n\\nCapital Improvement Projects and "}, 'var_functions.query_db:18': [{'Funding_ID': '1', 'Project_Name': '2021 Annual Street Maintenance', 'Funding_Source': 'Public-Private Partnership (PPP)', 'Amount': '24000'}, {'Funding_ID': '2', 'Project_Name': '2022 Annual Street Maintenance', 'Funding_Source': 'Government Grant', 'Amount': '45000'}, {'Funding_ID': '3', 'Project_Name': '2022 Morning View Resurfacing & Storm Drain Improvements', 'Funding_Source': 'State Development Grant', 'Amount': '38000'}, {'Funding_ID': '4', 'Project_Name': 'Annual Street Maintenance', 'Funding_Source': 'Corporate Sponsorship', 'Amount': '23000'}, {'Funding_ID': '5', 'Project_Name': 'Birdview Avenue Improvements', 'Funding_Source': 'National Foundation Fund', 'Amount': '79000'}], 'var_functions.list_db:20': ['Funding'], 'var_functions.query_db:24': 'file_storage/functions.query_db:24.json', 'var_functions.execute_python:34': {'civic_docs_count': 5, 'funding_records_count': 500}, 'var_functions.query_db:44': 'file_storage/functions.query_db:44.json', 'var_functions.query_db:50': [{'Project_Name': 'Bluffs Park Shade Structure', 'Amount': '21000'}, {'Project_Name': 'Bluffs Park Workout Station', 'Amount': '39000'}, {'Project_Name': 'Legacy Park Benches and Arbors Renovation', 'Amount': '41000'}, {'Project_Name': 'Legacy Park Paver Repair Project', 'Amount': '69000'}, {'Project_Name': 'Malibu Bluffs Park Roof Replacement Project', 'Amount': '44000'}, {'Project_Name': 'Malibu Bluffs Park South Walkway', 'Amount': '91000'}, {'Project_Name': 'Malibu Bluffs Park South Walkway Repairs', 'Amount': '81000'}, {'Project_Name': 'Malibu Park Drainage Improvements', 'Amount': '17000'}, {'Project_Name': 'Malibu Park Resurfacing Project', 'Amount': '14000'}, {'Project_Name': 'Malibu Park Storm Drain Repairs', 'Amount': '50000'}, {'Project_Name': 'Permanent Skate Park', 'Amount': '97000'}, {'Project_Name': 'Trancas Canyon Park Planting and Irrigation Repairs', 'Amount': '78000'}, {'Project_Name': 'Trancas Canyon Park Planting and Irrigation Repairs (CalJPIA/FEMA Project)', 'Amount': '44000'}, {'Project_Name': 'Trancas Canyon Park Planting and Irrigation Repairs (FEMA/CalOES Project)', 'Amount': '92000'}, {'Project_Name': 'Trancas Canyon Park Playground', 'Amount': '24000'}, {'Project_Name': 'Trancas Canyon Park Playground Resurfacing', 'Amount': '65000'}, {'Project_Name': 'Trancas Canyon Park Slope Stabilization Project', 'Amount': '68000'}, {'Project_Name': 'Trancas Canyon Park Slope Stabilization Project (CalJPIA Project)', 'Amount': '43000'}, {'Project_Name': 'Trancas Canyon Park Slope Stabilization Project (CalOES Project)', 'Amount': '32000'}, {'Project_Name': 'Trancas Canyon Park Upper and Lower Slopes Repair', 'Amount': '23000'}], 'var_functions.query_db:60': 'file_storage/functions.query_db:60.json', 'var_functions.query_db:62': 'file_storage/functions.query_db:62.json', 'var_functions.query_db:76': []}

exec(code, env_args)
