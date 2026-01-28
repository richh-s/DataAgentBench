code = """import json

# Load the data
mongo_file = locals()['var_functions.query_db:2']
with open(mongo_file, 'r') as f:
    docs = json.load(f)

funding_file = locals()['var_functions.query_db:48']
with open(funding_file, 'r') as f:
    all_funding = json.load(f)

print('Documents:', len(docs))
print('Funding records:', len(all_funding))

spring_projects = []

# Look for spring 2022 in documents
for doc in docs:
    text = doc.get('text', '')
    text_lower = text.lower()
    
    has_spring = False
    indicators = ['spring 2022', '2022-spring', 'march 2022', 'april 2022', 'may 2022']
    for ind in indicators:
        if ind in text_lower:
            has_spring = True
            break
    
    if has_spring:
        lines = text.split('\n')
        for line in lines:
            line = line.strip()
            if len(line) > 15 and len(line) < 100:
                lower = line.lower()
                skip_words = ['public works', 'agenda', 'item', 'to:', 'prepared by', 'approved by', 'date', 'meeting', 'subject:', 'page']
                should_skip = False
                for word in skip_words:
                    if word in lower:
                        should_skip = True
                        break
                if should_skip:
                    continue
                
                if any(c.isupper() for c in line):
                    spring_projects.append(line)

unique_projects = list(set(spring_projects))
print('Projects found:', len(unique_projects))

import re

def normalize_name(name):
    n = name.lower().strip()
    n = re.sub(r'\s+', ' ', n)
    n = re.sub(r'\([^)]*\)', '', n)
    return n.strip()

funding_index = {}
for fund in all_funding:
    key = normalize_name(fund['Project_Name'])
    funding_index[key] = fund

matches = []
for proj in unique_projects:
    key = normalize_name(proj)
    if key in funding_index:
        matches.append({'name': proj, 'fund': funding_index[key]})
    else:
        for fund_key, fund in funding_index.items():
            if key in fund_key or fund_key in key:
                matches.append({'name': proj, 'fund': fund})
                break

total = sum(int(m['fund']['Amount']) for m in matches)

result = {
    'spring_2022_projects': len(matches),
    'total_funding': total,
    'details': [{'name': m['name'], 'amount': int(m['fund']['Amount'])} for m in matches]
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.execute_python:16': {'key': 'var_functions.query_db:2', 'type': "<class 'str'>", 'length': 38}, 'var_functions.execute_python:18': {'total_docs': 5, 'sample_keys': ['_id', 'filename', 'text'], 'doc_preview': 'Public Works Commission\nAgenda Report\n\nPublic Works\nCommission Meeting\n03-22-23\nItem\n4.B.\n\nTo:\n\nChair Dittrich and Members of the Public Works Commission\n\nPrepared by:\n\nJorge Rubalcava, Senior Civil Engineer\n\nApproved by:\n\nRob DuBoux, Public Works Director/City Engineer\n\nDate prepared: March 15, 202'}, 'var_functions.query_db:20': [{'Funding_ID': '1', 'Project_Name': '2021 Annual Street Maintenance', 'Funding_Source': 'Public-Private Partnership (PPP)', 'Amount': '24000'}, {'Funding_ID': '2', 'Project_Name': '2022 Annual Street Maintenance', 'Funding_Source': 'Government Grant', 'Amount': '45000'}, {'Funding_ID': '3', 'Project_Name': '2022 Morning View Resurfacing & Storm Drain Improvements', 'Funding_Source': 'State Development Grant', 'Amount': '38000'}, {'Funding_ID': '4', 'Project_Name': 'Annual Street Maintenance', 'Funding_Source': 'Corporate Sponsorship', 'Amount': '23000'}, {'Funding_ID': '5', 'Project_Name': 'Birdview Avenue Improvements', 'Funding_Source': 'National Foundation Fund', 'Amount': '79000'}, {'Funding_ID': '6', 'Project_Name': 'Birdview Avenue Improvements (CalOES Project)', 'Funding_Source': 'International Aid', 'Amount': '85000'}, {'Funding_ID': '7', 'Project_Name': 'Birdview Avenue Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Research Institution Funding', 'Amount': '14000'}, {'Funding_ID': '8', 'Project_Name': 'Bluffs Park Shade Structure', 'Funding_Source': 'Government Grant', 'Amount': '21000'}, {'Funding_ID': '9', 'Project_Name': 'Bluffs Park Workout Station', 'Funding_Source': 'University Research Fund', 'Amount': '39000'}, {'Funding_ID': '10', 'Project_Name': 'Broad Beach Road Water Quality Infrastructure Repairs', 'Funding_Source': 'International Organization Grant', 'Amount': '87000'}], 'var_functions.execute_python:36': {'doc_count': 5}, 'var_functions.execute_python:38': {'spring_2022_docs': 4, 'total_docs': 5}, 'var_functions.execute_python:42': {'spring_2022_projects_count': 0, 'total_funding': 0}, 'var_functions.execute_python:44': {'funding_records': 10, 'sample': [{'Funding_ID': '1', 'Project_Name': '2021 Annual Street Maintenance', 'Funding_Source': 'Public-Private Partnership (PPP)', 'Amount': '24000'}, {'Funding_ID': '2', 'Project_Name': '2022 Annual Street Maintenance', 'Funding_Source': 'Government Grant', 'Amount': '45000'}, {'Funding_ID': '3', 'Project_Name': '2022 Morning View Resurfacing & Storm Drain Improvements', 'Funding_Source': 'State Development Grant', 'Amount': '38000'}]}, 'var_functions.query_db:46': [{'Funding_ID': '2', 'Project_Name': '2022 Annual Street Maintenance', 'Funding_Source': 'Government Grant', 'Amount': '45000'}, {'Funding_ID': '3', 'Project_Name': '2022 Morning View Resurfacing & Storm Drain Improvements', 'Funding_Source': 'State Development Grant', 'Amount': '38000'}], 'var_functions.query_db:48': 'file_storage/functions.query_db:48.json'}

exec(code, env_args)
