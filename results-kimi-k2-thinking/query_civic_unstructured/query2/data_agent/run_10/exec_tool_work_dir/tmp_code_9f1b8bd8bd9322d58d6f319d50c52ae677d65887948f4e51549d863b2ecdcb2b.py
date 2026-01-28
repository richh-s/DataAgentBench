code = """import json
import re
from pathlib import Path

# Load data from file if it's a path
civic_docs_raw = locals().get('var_functions.query_db:2')
funding_raw = locals().get('var_functions.query_db:24')

# Load civic documents
if isinstance(civic_docs_raw, str) and Path(civic_docs_raw).exists():
    with open(civic_docs_raw) as f:
        civic_docs = json.load(f)
else:
    civic_docs = civic_docs_raw

# Load funding records - check if it's already a list or a file path
if isinstance(funding_raw, list):
    funding_records = funding_raw
elif isinstance(funding_raw, str) and Path(funding_raw).exists():
    with open(funding_raw) as f:
        funding_records = json.load(f)
else:
    # Try to read from string or use empty list
    try:
        funding_records = json.loads(funding_raw) if isinstance(funding_raw, str) else []
    except:
        funding_records = []

print('Documents loaded:', len(civic_docs))
print('Funding records loaded:', len(funding_records))

# Extract park projects completed in 2022 from civic documents
park_projects_2022 = []

for doc in civic_docs:
    text = doc.get('text', '')
    lines = text.split('\n')
    
    # Look for patterns indicating completion in 2022 near park project names
    for i in range(len(lines)):
        line = lines[i].strip()
        if not line or len(line) < 5:
            continue
        
        # Check if current or next line mentions completion in 2022
        has_completion_2022 = False
        if '2022' in line and 'completed' in line.lower():
            has_completion_2022 = True
        elif i > 0 and '2022' in lines[i-1] and 'completed' in lines[i-1].lower():
            has_completion_2022 = True
        
        if has_completion_2022:
            # Look for park project name in current or previous lines
            for j in range(max(0, i-3), min(i+1, len(lines))):
                candidate_line = lines[j].strip()
                if ('Park' in candidate_line and 
                    len(candidate_line) > 10 and 
                    not any(header in candidate_line for header in ['Public Works', 'Commission', 'Capital Improvement', 'Disaster Recovery', 'Prepared by', 'Approved by', 'Page', 'Agenda'])):
                    
                    clean_name = re.sub(r'[^A-Za-z0-9\s\-&]', '', candidate_line).strip()
                    if clean_name and len(clean_name) > 5:
                        park_projects_2022.append(clean_name)
                        break

# Remove duplicates
park_projects_2022 = list(set(park_projects_2022))
print('Park projects completed in 2022:', len(park_projects_2022))
print('Projects:', park_projects_2022)

# Now match with funding records
common_words = {'park', 'project', 'repair', 'repairs', 'improvements', 'improvement', 'renovation', 'renovations', 'and', 'the', 'at', 'in', 'of', 'phase', 'south', 'north', 'east', 'west'}

matches = []
total_funding = 0

for park_name in park_projects_2022:
    park_words = set(re.findall(r'\b\w+\b', park_name.lower())) - common_words
    
    best_match = None
    best_score = 0
    
    for funding in funding_records:
        funding_name = funding.get('Project_Name', '').lower()
        funding_words = set(re.findall(r'\b\w+\b', funding_name)) - common_words
        
        # Calculate overlap score
        if park_words and funding_words:
            overlap = park_words.intersection(funding_words)
            score = len(overlap) / max(len(park_words), len(funding_words))
            
            if score > best_score:
                best_score = score
                best_match = funding
    
    # Accept matches with at least 30% similarity
    if best_match and best_score >= 0.3:
        amount = int(best_match.get('Amount', 0))
        total_funding += amount
        matches.append({
            'park_project': park_name,
            'funding_record': best_match.get('Project_Name'),
            'amount': amount,
            'similarity_score': round(best_score, 2)
        })

print('Matched with funding:', len(matches))
print('Total funding:', total_funding)

result = {
    'total_park_projects_2022': len(park_projects_2022),
    'funding_matches_found': len(matches),
    'total_funding_amount': total_funding,
    'matched_projects': matches,
    'all_park_projects': park_projects_2022
}

print('__RESULT__:')
print(json.dumps(result, indent=2))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.execute_python:10': {'num_documents': 5, 'type': "<class 'list'>", 'data_preview': "[{'_id': '694eef5c4ec675b6b5f5a285', 'filename': 'malibucity_agenda_03222023-2060.txt', 'text': 'Public Works Commission\\nAgenda Report\\n\\nPublic Works\\nCommission Meeting\\n03-22-23\\nItem\\n4.B.\\n\\nTo:\\n\\nChair Dittrich and Members of the Public Works Commission\\n\\nPrepared by:\\n\\nJorge Rubalcava, Senior Civil Engineer\\n\\nApproved by:\\n\\nRob DuBoux, Public Works Director/City Engineer\\n\\nDate prepared: March 15, 2023\\n\\nMeeting date: March 22, 2023\\n\\nSubject:\\n\\nCapital Improvement Projects and "}, 'var_functions.query_db:18': [{'Funding_ID': '1', 'Project_Name': '2021 Annual Street Maintenance', 'Funding_Source': 'Public-Private Partnership (PPP)', 'Amount': '24000'}, {'Funding_ID': '2', 'Project_Name': '2022 Annual Street Maintenance', 'Funding_Source': 'Government Grant', 'Amount': '45000'}, {'Funding_ID': '3', 'Project_Name': '2022 Morning View Resurfacing & Storm Drain Improvements', 'Funding_Source': 'State Development Grant', 'Amount': '38000'}, {'Funding_ID': '4', 'Project_Name': 'Annual Street Maintenance', 'Funding_Source': 'Corporate Sponsorship', 'Amount': '23000'}, {'Funding_ID': '5', 'Project_Name': 'Birdview Avenue Improvements', 'Funding_Source': 'National Foundation Fund', 'Amount': '79000'}], 'var_functions.list_db:20': ['Funding'], 'var_functions.query_db:24': 'file_storage/functions.query_db:24.json', 'var_functions.execute_python:34': {'civic_docs_count': 5, 'funding_records_count': 500}}

exec(code, env_args)
