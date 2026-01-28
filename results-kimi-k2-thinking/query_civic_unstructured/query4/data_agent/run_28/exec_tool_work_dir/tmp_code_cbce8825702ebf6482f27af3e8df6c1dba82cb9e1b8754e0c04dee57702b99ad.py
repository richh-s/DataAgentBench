code = """import json
import re

# Load MongoDB documents
mongo_file = locals()['var_functions.query_db:2']
with open(mongo_file, 'r') as f:
    docs = json.load(f)

# Load funding records  
funding_file = locals()['var_functions.query_db:48']
with open(funding_file, 'r') as f:
    funding_records = json.load(f)

print('Loaded', len(docs), 'documents and', len(funding_records), 'funding records')

# Patterns for Spring 2022 dates
date_patterns = [r'(?:spring\s*2022|2022\s*spring)', r'(?:march\s*2022|2022\s*march)', r'(?:april\s*2022|2022\s*april)', r'(?:may\s*2022|2022\s*may)', r'2022-0[3-5]']
date_regex = re.compile('|'.join(date_patterns), re.IGNORECASE)

projects_with_spring_2022 = []

for doc in docs:
    text = doc.get('text', '')
    lines = text.split('\n')
    
    for i, line in enumerate(lines):
        line = line.strip()
        if not line:
            continue
        
        # Skip headers
        skip_patterns = ['public works', 'agenda', 'item', 'to:', 'prepared by', 'approved by', 'date prepared', 'meeting date', 'subject:', 'recommended action', 'discussion:', 'updates:', 'project schedule', 'page']
        
        if any(pattern in line.lower() for pattern in skip_patterns):
            continue
        
        # Look for project-like lines
        if 10 < len(line) < 100 and any(c.isupper() for c in line):
            # Check following lines for Spring 2022 dates
            subsequent = '\n'.join(lines[i:i+15])
            if date_regex.search(subsequent):
                projects_with_spring_2022.append(line.strip())

unique_projects = list(set(projects_with_spring_2022))
print('Found', len(unique_projects), 'projects starting in Spring 2022')

# Normalize names for matching
def normalize(name):
    name = name.lower().strip()
    name = re.sub(r'\s+', ' ', name)
    name = re.sub(r'\s*\(fema[^)]*\)\s*', '', name)
    name = re.sub(r'\s*\(caloes[^)]*\)\s*', '', name)
    name = re.sub(r'\s*\(caljpia[^)]*\)\s*', '', name)
    return name

# Create funding lookup
funding_lookup = {}
for record in funding_records:
    norm_name = normalize(record['Project_Name'])
    funding_lookup[norm_name] = record

# Match projects to funding
matched = []
for proj in unique_projects:
    norm_proj = normalize(proj)
    
    if norm_proj in funding_lookup:
        matched.append({'project': proj, 'funding': funding_lookup[norm_proj]})
    else:
        # Fuzzy match
        for fund_name, record in funding_lookup.items():
            if norm_proj in fund_name or fund_name in norm_proj:
                matched.append({'project': proj, 'funding': record})
                break

print('Matched', len(matched), 'projects with funding')

# Calculate totals
total_funding = sum(int(m['funding']['Amount']) for m in matched)

result = {
    'spring_2022_project_count': len(matched),
    'total_funding': total_funding,
    'projects': [{'name': m['project'], 'amount': int(m['funding']['Amount']), 'source': m['funding']['Funding_Source']} for m in matched]
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.execute_python:16': {'key': 'var_functions.query_db:2', 'type': "<class 'str'>", 'length': 38}, 'var_functions.execute_python:18': {'total_docs': 5, 'sample_keys': ['_id', 'filename', 'text'], 'doc_preview': 'Public Works Commission\nAgenda Report\n\nPublic Works\nCommission Meeting\n03-22-23\nItem\n4.B.\n\nTo:\n\nChair Dittrich and Members of the Public Works Commission\n\nPrepared by:\n\nJorge Rubalcava, Senior Civil Engineer\n\nApproved by:\n\nRob DuBoux, Public Works Director/City Engineer\n\nDate prepared: March 15, 202'}, 'var_functions.query_db:20': [{'Funding_ID': '1', 'Project_Name': '2021 Annual Street Maintenance', 'Funding_Source': 'Public-Private Partnership (PPP)', 'Amount': '24000'}, {'Funding_ID': '2', 'Project_Name': '2022 Annual Street Maintenance', 'Funding_Source': 'Government Grant', 'Amount': '45000'}, {'Funding_ID': '3', 'Project_Name': '2022 Morning View Resurfacing & Storm Drain Improvements', 'Funding_Source': 'State Development Grant', 'Amount': '38000'}, {'Funding_ID': '4', 'Project_Name': 'Annual Street Maintenance', 'Funding_Source': 'Corporate Sponsorship', 'Amount': '23000'}, {'Funding_ID': '5', 'Project_Name': 'Birdview Avenue Improvements', 'Funding_Source': 'National Foundation Fund', 'Amount': '79000'}, {'Funding_ID': '6', 'Project_Name': 'Birdview Avenue Improvements (CalOES Project)', 'Funding_Source': 'International Aid', 'Amount': '85000'}, {'Funding_ID': '7', 'Project_Name': 'Birdview Avenue Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Research Institution Funding', 'Amount': '14000'}, {'Funding_ID': '8', 'Project_Name': 'Bluffs Park Shade Structure', 'Funding_Source': 'Government Grant', 'Amount': '21000'}, {'Funding_ID': '9', 'Project_Name': 'Bluffs Park Workout Station', 'Funding_Source': 'University Research Fund', 'Amount': '39000'}, {'Funding_ID': '10', 'Project_Name': 'Broad Beach Road Water Quality Infrastructure Repairs', 'Funding_Source': 'International Organization Grant', 'Amount': '87000'}], 'var_functions.execute_python:36': {'doc_count': 5}, 'var_functions.execute_python:38': {'spring_2022_docs': 4, 'total_docs': 5}, 'var_functions.execute_python:42': {'spring_2022_projects_count': 0, 'total_funding': 0}, 'var_functions.execute_python:44': {'funding_records': 10, 'sample': [{'Funding_ID': '1', 'Project_Name': '2021 Annual Street Maintenance', 'Funding_Source': 'Public-Private Partnership (PPP)', 'Amount': '24000'}, {'Funding_ID': '2', 'Project_Name': '2022 Annual Street Maintenance', 'Funding_Source': 'Government Grant', 'Amount': '45000'}, {'Funding_ID': '3', 'Project_Name': '2022 Morning View Resurfacing & Storm Drain Improvements', 'Funding_Source': 'State Development Grant', 'Amount': '38000'}]}, 'var_functions.query_db:46': [{'Funding_ID': '2', 'Project_Name': '2022 Annual Street Maintenance', 'Funding_Source': 'Government Grant', 'Amount': '45000'}, {'Funding_ID': '3', 'Project_Name': '2022 Morning View Resurfacing & Storm Drain Improvements', 'Funding_Source': 'State Development Grant', 'Amount': '38000'}], 'var_functions.query_db:48': 'file_storage/functions.query_db:48.json'}

exec(code, env_args)
