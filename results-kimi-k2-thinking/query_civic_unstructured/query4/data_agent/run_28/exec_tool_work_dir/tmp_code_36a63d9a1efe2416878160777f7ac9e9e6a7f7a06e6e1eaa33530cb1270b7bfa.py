code = """import json
import re

mongo_file = locals()['var_functions.query_db:2']
with open(mongo_file, 'r') as f:
    docs = json.load(f)

funding_file = locals()['var_functions.query_db:48']
with open(funding_file, 'r') as f:
    funding = json.load(f)

print('Docs:', len(docs), 'Funding:', len(funding))

spring_pattern = re.compile(r'(spring|march|april|may).{0,5}2022', re.I)
projects = []

for doc in docs:
    text = doc.get('text', '')
    if spring_pattern.search(text.lower()):
        lines = text.split('\n')
        for i,line in enumerate(lines):
            line=line.strip()
            if len(line)>15 and len(line)<100 and any(c.isupper() for c in line):
                if 'public works' not in line.lower() and 'agenda' not in line.lower():
                    next_text = '\n'.join(lines[i:i+15])
                    if spring_pattern.search(next_text.lower()):
                        projects.append(line)

unique = list(set(projects))
print('Found', len(unique), 'projects')

def normalize(n):
    n=n.lower().strip()
    n=re.sub(r'\s+',' ',n)
    n=re.sub(r'\(fema[^)]*\)','',n)
    n=re.sub(r'\(caloes[^)]*\)','',n)
    n=re.sub(r'\(caljpia[^)]*\)','',n)
    return n.strip()

funding_lookup = {normalize(f['Project_Name']):f for f in funding}

matched = []
for proj in unique:
    norm = normalize(proj)
    if norm in funding_lookup:
        matched.append({'name':proj,'fund':funding_lookup[norm]})
    else:
        for fund_norm, fund in funding_lookup.items():
            if norm in fund_norm or fund_norm in norm:
                matched.append({'name':proj,'fund':fund})
                break

total = sum(int(m['fund']['Amount']) for m in matched)

out = {
    'spring_2022_count': len(matched),
    'total_funding': total,
    'projects': [{'name':m['name'],'amount':int(m['fund']['Amount'])} for m in matched]
}

print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.execute_python:16': {'key': 'var_functions.query_db:2', 'type': "<class 'str'>", 'length': 38}, 'var_functions.execute_python:18': {'total_docs': 5, 'sample_keys': ['_id', 'filename', 'text'], 'doc_preview': 'Public Works Commission\nAgenda Report\n\nPublic Works\nCommission Meeting\n03-22-23\nItem\n4.B.\n\nTo:\n\nChair Dittrich and Members of the Public Works Commission\n\nPrepared by:\n\nJorge Rubalcava, Senior Civil Engineer\n\nApproved by:\n\nRob DuBoux, Public Works Director/City Engineer\n\nDate prepared: March 15, 202'}, 'var_functions.query_db:20': [{'Funding_ID': '1', 'Project_Name': '2021 Annual Street Maintenance', 'Funding_Source': 'Public-Private Partnership (PPP)', 'Amount': '24000'}, {'Funding_ID': '2', 'Project_Name': '2022 Annual Street Maintenance', 'Funding_Source': 'Government Grant', 'Amount': '45000'}, {'Funding_ID': '3', 'Project_Name': '2022 Morning View Resurfacing & Storm Drain Improvements', 'Funding_Source': 'State Development Grant', 'Amount': '38000'}, {'Funding_ID': '4', 'Project_Name': 'Annual Street Maintenance', 'Funding_Source': 'Corporate Sponsorship', 'Amount': '23000'}, {'Funding_ID': '5', 'Project_Name': 'Birdview Avenue Improvements', 'Funding_Source': 'National Foundation Fund', 'Amount': '79000'}, {'Funding_ID': '6', 'Project_Name': 'Birdview Avenue Improvements (CalOES Project)', 'Funding_Source': 'International Aid', 'Amount': '85000'}, {'Funding_ID': '7', 'Project_Name': 'Birdview Avenue Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Research Institution Funding', 'Amount': '14000'}, {'Funding_ID': '8', 'Project_Name': 'Bluffs Park Shade Structure', 'Funding_Source': 'Government Grant', 'Amount': '21000'}, {'Funding_ID': '9', 'Project_Name': 'Bluffs Park Workout Station', 'Funding_Source': 'University Research Fund', 'Amount': '39000'}, {'Funding_ID': '10', 'Project_Name': 'Broad Beach Road Water Quality Infrastructure Repairs', 'Funding_Source': 'International Organization Grant', 'Amount': '87000'}], 'var_functions.execute_python:36': {'doc_count': 5}, 'var_functions.execute_python:38': {'spring_2022_docs': 4, 'total_docs': 5}, 'var_functions.execute_python:42': {'spring_2022_projects_count': 0, 'total_funding': 0}, 'var_functions.execute_python:44': {'funding_records': 10, 'sample': [{'Funding_ID': '1', 'Project_Name': '2021 Annual Street Maintenance', 'Funding_Source': 'Public-Private Partnership (PPP)', 'Amount': '24000'}, {'Funding_ID': '2', 'Project_Name': '2022 Annual Street Maintenance', 'Funding_Source': 'Government Grant', 'Amount': '45000'}, {'Funding_ID': '3', 'Project_Name': '2022 Morning View Resurfacing & Storm Drain Improvements', 'Funding_Source': 'State Development Grant', 'Amount': '38000'}]}, 'var_functions.query_db:46': [{'Funding_ID': '2', 'Project_Name': '2022 Annual Street Maintenance', 'Funding_Source': 'Government Grant', 'Amount': '45000'}, {'Funding_ID': '3', 'Project_Name': '2022 Morning View Resurfacing & Storm Drain Improvements', 'Funding_Source': 'State Development Grant', 'Amount': '38000'}], 'var_functions.query_db:48': 'file_storage/functions.query_db:48.json'}

exec(code, env_args)
