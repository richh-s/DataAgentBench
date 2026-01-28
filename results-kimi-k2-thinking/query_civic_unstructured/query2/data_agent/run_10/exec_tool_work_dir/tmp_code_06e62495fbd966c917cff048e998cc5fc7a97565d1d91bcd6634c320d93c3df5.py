code = """import json
import re
import os

# Load civic documents from the filtered 2022 completed projects query
civic_path = locals().get('var_functions.query_db:62')
if isinstance(civic_path, str) and os.path.exists(civic_path):
    civic_file = open(civic_path, 'r')
    civic_docs = json.load(civic_file)
    civic_file.close()
else:
    civic_docs = []

# Load all funding records from the full query
funding_path = locals().get('var_functions.query_db:24')
if isinstance(funding_path, str) and os.path.exists(funding_path):
    funding_file = open(funding_path, 'r')
    funding_records = json.load(funding_file)
    funding_file.close()
else:
    funding_records = locals().get('var_functions.query_db:50', [])

print('Loaded ' + str(len(civic_docs)) + ' documents and ' + str(len(funding_records)) + ' funding records')

# Find all park-related projects completed in 2022
park_projects = []

for doc in civic_docs:
    text = doc.get('text', '')
    # Skip if no park mention
    if 'park' not in text.lower():
        continue
    # Split into lines and look for park projects with 2022 completion
    lines = text.split('\n')
    for i in range(len(lines)):
        line = lines[i].strip()
        if not line or len(line) < 8:
            continue
        # Look for project names containing Park
        if 'Park' in line:
            # Check if this is likely a project name (not a header)
            if line.startswith('Page') or line.startswith('Agenda'):
                continue
            # Check nearby lines for completion in 2022
            context_start = max(0, i - 2)
            context_end = min(len(lines), i + 5)
            found_2022 = False
            for j in range(context_start, context_end):
                if '2022' in lines[j] and 'completed' in lines[j].lower():
                    found_2022 = True
                    break
            if found_2022:
                # Clean the project name for matching
                clean_name = re.sub(r'[^A-Za-z0-9\s\-&]', '', line)
                clean_name = clean_name.strip()
                if len(clean_name) > 5:
                    park_projects.append(clean_name)

# Remove duplicates
park_projects = list(set(park_projects))

# Match with funding records and calculate total
total_funding = 0
for park in park_projects:
    # Simplified matching - look for exact or near-exact matches
    park_lower = park.lower()
    for funding in funding_records:
        funding_name = funding.get('Project_Name', '')
        funding_lower = funding_name.lower()
        # Direct substring match (most reliable)
        if park_lower in funding_lower or funding_lower in park_lower:
            amount = int(funding.get('Amount', 0))
            total_funding += amount
            break

result = {
    'park_projects_2022': len(park_projects),
    'total_funding': total_funding
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.execute_python:10': {'num_documents': 5, 'type': "<class 'list'>", 'data_preview': "[{'_id': '694eef5c4ec675b6b5f5a285', 'filename': 'malibucity_agenda_03222023-2060.txt', 'text': 'Public Works Commission\\nAgenda Report\\n\\nPublic Works\\nCommission Meeting\\n03-22-23\\nItem\\n4.B.\\n\\nTo:\\n\\nChair Dittrich and Members of the Public Works Commission\\n\\nPrepared by:\\n\\nJorge Rubalcava, Senior Civil Engineer\\n\\nApproved by:\\n\\nRob DuBoux, Public Works Director/City Engineer\\n\\nDate prepared: March 15, 2023\\n\\nMeeting date: March 22, 2023\\n\\nSubject:\\n\\nCapital Improvement Projects and "}, 'var_functions.query_db:18': [{'Funding_ID': '1', 'Project_Name': '2021 Annual Street Maintenance', 'Funding_Source': 'Public-Private Partnership (PPP)', 'Amount': '24000'}, {'Funding_ID': '2', 'Project_Name': '2022 Annual Street Maintenance', 'Funding_Source': 'Government Grant', 'Amount': '45000'}, {'Funding_ID': '3', 'Project_Name': '2022 Morning View Resurfacing & Storm Drain Improvements', 'Funding_Source': 'State Development Grant', 'Amount': '38000'}, {'Funding_ID': '4', 'Project_Name': 'Annual Street Maintenance', 'Funding_Source': 'Corporate Sponsorship', 'Amount': '23000'}, {'Funding_ID': '5', 'Project_Name': 'Birdview Avenue Improvements', 'Funding_Source': 'National Foundation Fund', 'Amount': '79000'}], 'var_functions.list_db:20': ['Funding'], 'var_functions.query_db:24': 'file_storage/functions.query_db:24.json', 'var_functions.execute_python:34': {'civic_docs_count': 5, 'funding_records_count': 500}, 'var_functions.query_db:44': 'file_storage/functions.query_db:44.json', 'var_functions.query_db:50': [{'Project_Name': 'Bluffs Park Shade Structure', 'Amount': '21000'}, {'Project_Name': 'Bluffs Park Workout Station', 'Amount': '39000'}, {'Project_Name': 'Legacy Park Benches and Arbors Renovation', 'Amount': '41000'}, {'Project_Name': 'Legacy Park Paver Repair Project', 'Amount': '69000'}, {'Project_Name': 'Malibu Bluffs Park Roof Replacement Project', 'Amount': '44000'}, {'Project_Name': 'Malibu Bluffs Park South Walkway', 'Amount': '91000'}, {'Project_Name': 'Malibu Bluffs Park South Walkway Repairs', 'Amount': '81000'}, {'Project_Name': 'Malibu Park Drainage Improvements', 'Amount': '17000'}, {'Project_Name': 'Malibu Park Resurfacing Project', 'Amount': '14000'}, {'Project_Name': 'Malibu Park Storm Drain Repairs', 'Amount': '50000'}, {'Project_Name': 'Permanent Skate Park', 'Amount': '97000'}, {'Project_Name': 'Trancas Canyon Park Planting and Irrigation Repairs', 'Amount': '78000'}, {'Project_Name': 'Trancas Canyon Park Planting and Irrigation Repairs (CalJPIA/FEMA Project)', 'Amount': '44000'}, {'Project_Name': 'Trancas Canyon Park Planting and Irrigation Repairs (FEMA/CalOES Project)', 'Amount': '92000'}, {'Project_Name': 'Trancas Canyon Park Playground', 'Amount': '24000'}, {'Project_Name': 'Trancas Canyon Park Playground Resurfacing', 'Amount': '65000'}, {'Project_Name': 'Trancas Canyon Park Slope Stabilization Project', 'Amount': '68000'}, {'Project_Name': 'Trancas Canyon Park Slope Stabilization Project (CalJPIA Project)', 'Amount': '43000'}, {'Project_Name': 'Trancas Canyon Park Slope Stabilization Project (CalOES Project)', 'Amount': '32000'}, {'Project_Name': 'Trancas Canyon Park Upper and Lower Slopes Repair', 'Amount': '23000'}], 'var_functions.query_db:60': 'file_storage/functions.query_db:60.json', 'var_functions.query_db:62': 'file_storage/functions.query_db:62.json'}

exec(code, env_args)
