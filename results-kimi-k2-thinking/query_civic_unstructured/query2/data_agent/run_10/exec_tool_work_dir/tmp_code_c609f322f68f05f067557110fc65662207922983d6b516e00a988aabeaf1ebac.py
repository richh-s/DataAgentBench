code = """import json
import re
import os

# Load civic documents from the file path
civic_file_path = locals().get('var_functions.query_db:44')
if isinstance(civic_file_path, str) and os.path.exists(civic_file_path):
    with open(civic_file_path, 'r') as f:
        civic_docs = json.load(f)
else:
    # Try the other path
    civic_file_path = '/tmp/tmp8r9gntdv.json'
    if os.path.exists(civic_file_path):
        with open(civic_file_path, 'r') as f:
            civic_docs = json.load(f)
    else:
        civic_docs = []

# Load all funding records
funding_file_path = locals().get('var_functions.query_db:24')
if isinstance(funding_file_path, str) and os.path.exists(funding_file_path):
    with open(funding_file_path, 'r') as f:
        funding_records = json.load(f)
else:
    # Fallback to the filtered park funding if full data not available
    funding_records = locals().get('var_functions.query_db:50')

print(f'Loaded {len(civic_docs)} civic documents and {len(funding_records)} funding records')

# Extract park projects completed in 2022
park_projects_2022 = {}

for doc in civic_docs:
    text = doc.get('text', '')
    lines = text.split('\n')
    
    for i, line in enumerate(lines):
        line = line.strip()
        if not line:
            continue
        
        # Look for park project names (lines containing "Park" and not headers)
        if ('Park' in line and 
            len(line) > 8 and 
            not line.startswith('Page') and 
            not line.startswith('Agenda') and
            not any(header in line for header in ['Public Works', 'Commission', 'Capital Improvement', 'Disaster Recovery', 'Prepared by', 'Approved by', 'Date prepared', 'Meeting date'])):
            
            # Look for completion status in nearby lines (within 5 lines)
            start_idx = max(0, i)
            end_idx = min(len(lines), i + 5)
            
            found_2022_completion = False
            for j in range(start_idx, end_idx):
                check_line = lines[j].strip()
                if ('2022' in check_line and 'completed' in check_line.lower()):
                    found_2022_completion = True
                    break
            
            if found_2022_completion:
                # Clean and normalize the project name
                clean_name = re.sub(r'[^A-Za-z0-9\s\-&]', '', line).strip()
                # Remove common suffixes to help with matching
                clean_name = re.sub(r'\s+(Project|Repair|Repairs|Improvements)$', '', clean_name, flags=re.IGNORECASE)
                
                if clean_name and len(clean_name) > 5:
                    park_projects_2022[clean_name] = {'original': line, 'clean': clean_name}

print(f'Found {len(park_projects_2022)} park projects completed in 2022')
print('Projects:', list(park_projects_2022.keys()))

# Match with funding records
matched_projects = []
total_funding = 0

common_words = {'park', 'project', 'repair', 'repairs', 'improvements', 'improvement', 'renovation', 'renovations', 'and', 'the', 'at', 'in', 'of', 'phase', 'south', 'north', 'east', 'west', 'bluffs', 'malibu', 'canyon', 'trancas'}

for park_name, park_info in park_projects_2022.items():
    park_words = set(re.findall(r'\b\w+\b', park_name.lower())) - common_words
    
    best_match = None
    best_score = 0
    best_funding_name = None
    
    for funding in funding_records:
        funding_name = funding.get('Project_Name', '')
        funding_lower = funding_name.lower()
        
        # Clean funding name similarly
        clean_funding = re.sub(r'\s+(Project|Repair|Repairs|Improvements)$', '', funding_lower, flags=re.IGNORECASE)
        funding_words = set(re.findall(r'\b\w+\b', clean_funding)) - common_words
        
        # Check for direct match or strong similarity
        direct_match = False
        if park_name.lower() in funding_lower or funding_lower in park_name.lower():
            direct_match = True
        
        # Calculate overlap score
        if park_words and funding_words:
            overlap = park_words.intersection(funding_words)
            score = len(overlap) / max(len(park_words), len(funding_words))
            
            # Boost score for direct matches
            if direct_match:
                score = 1.0
            
            if score > best_score and score >= 0.3:
                best_score = score
                best_match = funding
                best_funding_name = funding_name
    
    if best_match:
        amount = int(best_match.get('Amount', 0))
        total_funding += amount
        matched_projects.append({
            'park_project': park_name,
            'funding_record': best_funding_name,
            'amount': amount,
            'match_score': round(best_score, 2)
        })

print(f'Matched {len(matched_projects)} projects with funding')

result = {
    'total_park_projects_2022': len(park_projects_2022),
    'funding_matches': len(matched_projects),
    'total_funding_dollars': total_funding,
    'matched_projects': matched_projects
}

print('__RESULT__:')
print(json.dumps(result, indent=2))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.execute_python:10': {'num_documents': 5, 'type': "<class 'list'>", 'data_preview': "[{'_id': '694eef5c4ec675b6b5f5a285', 'filename': 'malibucity_agenda_03222023-2060.txt', 'text': 'Public Works Commission\\nAgenda Report\\n\\nPublic Works\\nCommission Meeting\\n03-22-23\\nItem\\n4.B.\\n\\nTo:\\n\\nChair Dittrich and Members of the Public Works Commission\\n\\nPrepared by:\\n\\nJorge Rubalcava, Senior Civil Engineer\\n\\nApproved by:\\n\\nRob DuBoux, Public Works Director/City Engineer\\n\\nDate prepared: March 15, 2023\\n\\nMeeting date: March 22, 2023\\n\\nSubject:\\n\\nCapital Improvement Projects and "}, 'var_functions.query_db:18': [{'Funding_ID': '1', 'Project_Name': '2021 Annual Street Maintenance', 'Funding_Source': 'Public-Private Partnership (PPP)', 'Amount': '24000'}, {'Funding_ID': '2', 'Project_Name': '2022 Annual Street Maintenance', 'Funding_Source': 'Government Grant', 'Amount': '45000'}, {'Funding_ID': '3', 'Project_Name': '2022 Morning View Resurfacing & Storm Drain Improvements', 'Funding_Source': 'State Development Grant', 'Amount': '38000'}, {'Funding_ID': '4', 'Project_Name': 'Annual Street Maintenance', 'Funding_Source': 'Corporate Sponsorship', 'Amount': '23000'}, {'Funding_ID': '5', 'Project_Name': 'Birdview Avenue Improvements', 'Funding_Source': 'National Foundation Fund', 'Amount': '79000'}], 'var_functions.list_db:20': ['Funding'], 'var_functions.query_db:24': 'file_storage/functions.query_db:24.json', 'var_functions.execute_python:34': {'civic_docs_count': 5, 'funding_records_count': 500}, 'var_functions.query_db:44': 'file_storage/functions.query_db:44.json', 'var_functions.query_db:50': [{'Project_Name': 'Bluffs Park Shade Structure', 'Amount': '21000'}, {'Project_Name': 'Bluffs Park Workout Station', 'Amount': '39000'}, {'Project_Name': 'Legacy Park Benches and Arbors Renovation', 'Amount': '41000'}, {'Project_Name': 'Legacy Park Paver Repair Project', 'Amount': '69000'}, {'Project_Name': 'Malibu Bluffs Park Roof Replacement Project', 'Amount': '44000'}, {'Project_Name': 'Malibu Bluffs Park South Walkway', 'Amount': '91000'}, {'Project_Name': 'Malibu Bluffs Park South Walkway Repairs', 'Amount': '81000'}, {'Project_Name': 'Malibu Park Drainage Improvements', 'Amount': '17000'}, {'Project_Name': 'Malibu Park Resurfacing Project', 'Amount': '14000'}, {'Project_Name': 'Malibu Park Storm Drain Repairs', 'Amount': '50000'}, {'Project_Name': 'Permanent Skate Park', 'Amount': '97000'}, {'Project_Name': 'Trancas Canyon Park Planting and Irrigation Repairs', 'Amount': '78000'}, {'Project_Name': 'Trancas Canyon Park Planting and Irrigation Repairs (CalJPIA/FEMA Project)', 'Amount': '44000'}, {'Project_Name': 'Trancas Canyon Park Planting and Irrigation Repairs (FEMA/CalOES Project)', 'Amount': '92000'}, {'Project_Name': 'Trancas Canyon Park Playground', 'Amount': '24000'}, {'Project_Name': 'Trancas Canyon Park Playground Resurfacing', 'Amount': '65000'}, {'Project_Name': 'Trancas Canyon Park Slope Stabilization Project', 'Amount': '68000'}, {'Project_Name': 'Trancas Canyon Park Slope Stabilization Project (CalJPIA Project)', 'Amount': '43000'}, {'Project_Name': 'Trancas Canyon Park Slope Stabilization Project (CalOES Project)', 'Amount': '32000'}, {'Project_Name': 'Trancas Canyon Park Upper and Lower Slopes Repair', 'Amount': '23000'}]}

exec(code, env_args)
