code = """import json, re, os

# Load civic documents from the latest query path
civic_path = locals().get('var_functions.query_db:44')
if isinstance(civic_path, str) and os.path.exists(civic_path):
    with open(civic_path) as f:
        civic_docs = json.load(f)
else:
    civic_docs = []

# Load funding records
funding_path = locals().get('var_functions.query_db:24')
if isinstance(funding_path, str) and os.path.exists(funding_path):
    with open(funding_path) as f:
        funding_records = json.load(f)
else:
    funding_records = locals().get('var_functions.query_db:50', [])

print('Loaded', len(civic_docs), 'civic docs and', len(funding_records), 'funding records')

# Extract park projects completed in 2022
park_projects_2022 = {}

for doc in civic_docs:
    text = doc.get('text', '')
    lines = text.split('\n')
    
    for i, line in enumerate(lines):
        line = line.strip()
        # Skip headers and short lines
        if not line or len(line) < 8:
            continue
        
        # Detect project names containing Park
        if 'Park' in line and not line.startswith('Page') and not line.startswith('Agenda'):
            # Skip common headers
            if any(hdr in line for hdr in ['Public Works', 'Commission', 'Capital Improvement', 'Disaster Recovery', 'Prepared by', 'Approved by']):
                continue
            
            # Look for completion in nearby lines
            context_lines = lines[max(0,i):min(len(lines), i+5)]
            context = ' '.join(context_lines)
            
            if 'completed' in context.lower() and '2022' in context:
                # Clean project name
                clean_name = re.sub(r'[^A-Za-z0-9\s\-&]', '', line).strip()
                clean_name = re.sub(r'\s+(Project|Repair|Repairs|Improvements)$', '', clean_name, flags=re.IGNORECASE)
                
                if clean_name and len(clean_name) > 5:
                    park_projects_2022[clean_name] = clean_name

print('Found', len(park_projects_2022), 'park projects completed in 2022')

# Match with funding records
total_funding = 0
matched_projects = []
common_words = {'park','project','repair','improvements','and','the','at','in','of','phase','south','north','east','west'}

for park_name in park_projects_2022:
    park_words = set(re.findall(r'\b\w+\b', park_name.lower())) - common_words
    
    best_match = None
    best_score = 0
    
    for funding in funding_records:
        funding_name = funding.get('Project_Name', '')
        funding_lower = funding_name.lower()
        
        # Clean funding name
        clean_funding = re.sub(r'\s+(Project|Repair|Repairs|Improvements)$', '', funding_lower, flags=re.IGNORECASE)
        funding_words = set(re.findall(r'\b\w+\b', clean_funding)) - common_words
        
        # Calculate match score
        direct_match = park_name.lower() in funding_lower or funding_lower in park_name.lower()
        
        if park_words and funding_words:
            overlap = park_words.intersection(funding_words)
            score = len(overlap) / max(len(park_words), len(funding_words))
            
            if direct_match:
                score = 1.0
            
            if score > best_score and score >= 0.3:
                best_score = score
                best_match = funding
    
    if best_match:
        amount = int(best_match.get('Amount', 0))
        total_funding += amount
        matched_projects.append({
            'park_project': park_name,
            'funding_record': best_match.get('Project_Name'),
            'amount': amount
        })

# Return result in required format
output = {
    'total_park_projects_2022': len(park_projects_2022),
    'matched_funding_records': len(matched_projects),
    'total_funding_dollars': total_funding,
    'matched_projects': matched_projects
}

print('__RESULT__:')
print(json.dumps(output))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.execute_python:10': {'num_documents': 5, 'type': "<class 'list'>", 'data_preview': "[{'_id': '694eef5c4ec675b6b5f5a285', 'filename': 'malibucity_agenda_03222023-2060.txt', 'text': 'Public Works Commission\\nAgenda Report\\n\\nPublic Works\\nCommission Meeting\\n03-22-23\\nItem\\n4.B.\\n\\nTo:\\n\\nChair Dittrich and Members of the Public Works Commission\\n\\nPrepared by:\\n\\nJorge Rubalcava, Senior Civil Engineer\\n\\nApproved by:\\n\\nRob DuBoux, Public Works Director/City Engineer\\n\\nDate prepared: March 15, 2023\\n\\nMeeting date: March 22, 2023\\n\\nSubject:\\n\\nCapital Improvement Projects and "}, 'var_functions.query_db:18': [{'Funding_ID': '1', 'Project_Name': '2021 Annual Street Maintenance', 'Funding_Source': 'Public-Private Partnership (PPP)', 'Amount': '24000'}, {'Funding_ID': '2', 'Project_Name': '2022 Annual Street Maintenance', 'Funding_Source': 'Government Grant', 'Amount': '45000'}, {'Funding_ID': '3', 'Project_Name': '2022 Morning View Resurfacing & Storm Drain Improvements', 'Funding_Source': 'State Development Grant', 'Amount': '38000'}, {'Funding_ID': '4', 'Project_Name': 'Annual Street Maintenance', 'Funding_Source': 'Corporate Sponsorship', 'Amount': '23000'}, {'Funding_ID': '5', 'Project_Name': 'Birdview Avenue Improvements', 'Funding_Source': 'National Foundation Fund', 'Amount': '79000'}], 'var_functions.list_db:20': ['Funding'], 'var_functions.query_db:24': 'file_storage/functions.query_db:24.json', 'var_functions.execute_python:34': {'civic_docs_count': 5, 'funding_records_count': 500}, 'var_functions.query_db:44': 'file_storage/functions.query_db:44.json', 'var_functions.query_db:50': [{'Project_Name': 'Bluffs Park Shade Structure', 'Amount': '21000'}, {'Project_Name': 'Bluffs Park Workout Station', 'Amount': '39000'}, {'Project_Name': 'Legacy Park Benches and Arbors Renovation', 'Amount': '41000'}, {'Project_Name': 'Legacy Park Paver Repair Project', 'Amount': '69000'}, {'Project_Name': 'Malibu Bluffs Park Roof Replacement Project', 'Amount': '44000'}, {'Project_Name': 'Malibu Bluffs Park South Walkway', 'Amount': '91000'}, {'Project_Name': 'Malibu Bluffs Park South Walkway Repairs', 'Amount': '81000'}, {'Project_Name': 'Malibu Park Drainage Improvements', 'Amount': '17000'}, {'Project_Name': 'Malibu Park Resurfacing Project', 'Amount': '14000'}, {'Project_Name': 'Malibu Park Storm Drain Repairs', 'Amount': '50000'}, {'Project_Name': 'Permanent Skate Park', 'Amount': '97000'}, {'Project_Name': 'Trancas Canyon Park Planting and Irrigation Repairs', 'Amount': '78000'}, {'Project_Name': 'Trancas Canyon Park Planting and Irrigation Repairs (CalJPIA/FEMA Project)', 'Amount': '44000'}, {'Project_Name': 'Trancas Canyon Park Planting and Irrigation Repairs (FEMA/CalOES Project)', 'Amount': '92000'}, {'Project_Name': 'Trancas Canyon Park Playground', 'Amount': '24000'}, {'Project_Name': 'Trancas Canyon Park Playground Resurfacing', 'Amount': '65000'}, {'Project_Name': 'Trancas Canyon Park Slope Stabilization Project', 'Amount': '68000'}, {'Project_Name': 'Trancas Canyon Park Slope Stabilization Project (CalJPIA Project)', 'Amount': '43000'}, {'Project_Name': 'Trancas Canyon Park Slope Stabilization Project (CalOES Project)', 'Amount': '32000'}, {'Project_Name': 'Trancas Canyon Park Upper and Lower Slopes Repair', 'Amount': '23000'}]}

exec(code, env_args)
