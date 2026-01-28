code = """import json
import re

# First, load and inspect the documents to understand structure
mongo_file = locals()['var_functions.query_db:2']
with open(mongo_file, 'r') as f:
    docs = json.load(f)

# Load all funding records
funding_file = locals()['var_functions.query_db:48']
with open(funding_file, 'r') as f:
    all_funding = json.load(f)

# Simple approach - just look for documents that mention spring 2022
spring_docs = []
for doc in docs:
    text = doc.get('text', '').lower()
    if 'spring 2022' in text or '2022-spring' in text or 'march 2022' in text or 'april 2022' in text or 'may 2022' in text:
        spring_docs.append(doc)

print('Found', len(spring_docs), 'documents mentioning Spring 2022')

# Look for patterns like "Project Name" followed by schedule info
projects = []
for doc in spring_docs:
    text = doc.get('text', '')
    lines = text.split('\n')
    for i, line in enumerate(lines):
        line = line.strip()
        if len(line) < 10 or len(line) > 80:
            continue
        # Skip section headers
        lower = line.lower()
        if 'public works' in lower or 'agenda' in lower or 'item' in lower or 'prepared' in lower:
            continue
        # Look for capitalized lines (likely project names)
        if any(c.isupper() for c in line):
            # Check if following lines mention spring 2022
            next_text = '\n'.join(lines[i:i+8]).lower()
            if 'spring 2022' in next_text or '2022-spring' in next_text:
                projects.append(line)

unique_projects = list(set(projects))
print('Projects starting in Spring 2022:', len(unique_projects))

# Normalize names for matching
def normalize(name):
    n = name.lower().strip()
    n = re.sub(r'\s+', ' ', n)
    n = re.sub(r'\([^)]*\)', '', n)
    return n.strip()

# Create funding lookup
funding_lookup = {}
for fund in all_funding:
    key = normalize(fund['Project_Name'])
    funding_lookup[key] = fund

# Match projects and calculate funding
matched = []
for proj in unique_projects:
    key = normalize(proj)
    if key in funding_lookup:
        matched.append({'Project': proj, 'Funding': funding_lookup[key]})
    else:
        # Check for partial matches
        for fund_key in funding_lookup:
            if key in fund_key or fund_key in key:
                matched.append({'Project': proj, 'Funding': funding_lookup[fund_key]})
                break

total_funding = sum(int(m['Funding']['Amount']) for m in matched)

final_result = {
    'Spring_2022_Project_Count': len(matched),
    'Total_Funding': total_funding,
    'Projects': [
        {
            'Name': m['Project'],
            'Amount': int(m['Funding']['Amount']),
            'Source': m['Funding']['Funding_Source']
        }
        for m in matched
    ]
}

print('__RESULT__:')
print(json.dumps(final_result))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.execute_python:16': {'key': 'var_functions.query_db:2', 'type': "<class 'str'>", 'length': 38}, 'var_functions.execute_python:18': {'total_docs': 5, 'sample_keys': ['_id', 'filename', 'text'], 'doc_preview': 'Public Works Commission\nAgenda Report\n\nPublic Works\nCommission Meeting\n03-22-23\nItem\n4.B.\n\nTo:\n\nChair Dittrich and Members of the Public Works Commission\n\nPrepared by:\n\nJorge Rubalcava, Senior Civil Engineer\n\nApproved by:\n\nRob DuBoux, Public Works Director/City Engineer\n\nDate prepared: March 15, 202'}, 'var_functions.query_db:20': [{'Funding_ID': '1', 'Project_Name': '2021 Annual Street Maintenance', 'Funding_Source': 'Public-Private Partnership (PPP)', 'Amount': '24000'}, {'Funding_ID': '2', 'Project_Name': '2022 Annual Street Maintenance', 'Funding_Source': 'Government Grant', 'Amount': '45000'}, {'Funding_ID': '3', 'Project_Name': '2022 Morning View Resurfacing & Storm Drain Improvements', 'Funding_Source': 'State Development Grant', 'Amount': '38000'}, {'Funding_ID': '4', 'Project_Name': 'Annual Street Maintenance', 'Funding_Source': 'Corporate Sponsorship', 'Amount': '23000'}, {'Funding_ID': '5', 'Project_Name': 'Birdview Avenue Improvements', 'Funding_Source': 'National Foundation Fund', 'Amount': '79000'}, {'Funding_ID': '6', 'Project_Name': 'Birdview Avenue Improvements (CalOES Project)', 'Funding_Source': 'International Aid', 'Amount': '85000'}, {'Funding_ID': '7', 'Project_Name': 'Birdview Avenue Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Research Institution Funding', 'Amount': '14000'}, {'Funding_ID': '8', 'Project_Name': 'Bluffs Park Shade Structure', 'Funding_Source': 'Government Grant', 'Amount': '21000'}, {'Funding_ID': '9', 'Project_Name': 'Bluffs Park Workout Station', 'Funding_Source': 'University Research Fund', 'Amount': '39000'}, {'Funding_ID': '10', 'Project_Name': 'Broad Beach Road Water Quality Infrastructure Repairs', 'Funding_Source': 'International Organization Grant', 'Amount': '87000'}], 'var_functions.execute_python:36': {'doc_count': 5}, 'var_functions.execute_python:38': {'spring_2022_docs': 4, 'total_docs': 5}, 'var_functions.execute_python:42': {'spring_2022_projects_count': 0, 'total_funding': 0}, 'var_functions.execute_python:44': {'funding_records': 10, 'sample': [{'Funding_ID': '1', 'Project_Name': '2021 Annual Street Maintenance', 'Funding_Source': 'Public-Private Partnership (PPP)', 'Amount': '24000'}, {'Funding_ID': '2', 'Project_Name': '2022 Annual Street Maintenance', 'Funding_Source': 'Government Grant', 'Amount': '45000'}, {'Funding_ID': '3', 'Project_Name': '2022 Morning View Resurfacing & Storm Drain Improvements', 'Funding_Source': 'State Development Grant', 'Amount': '38000'}]}, 'var_functions.query_db:46': [{'Funding_ID': '2', 'Project_Name': '2022 Annual Street Maintenance', 'Funding_Source': 'Government Grant', 'Amount': '45000'}, {'Funding_ID': '3', 'Project_Name': '2022 Morning View Resurfacing & Storm Drain Improvements', 'Funding_Source': 'State Development Grant', 'Amount': '38000'}], 'var_functions.query_db:48': 'file_storage/functions.query_db:48.json'}

exec(code, env_args)
