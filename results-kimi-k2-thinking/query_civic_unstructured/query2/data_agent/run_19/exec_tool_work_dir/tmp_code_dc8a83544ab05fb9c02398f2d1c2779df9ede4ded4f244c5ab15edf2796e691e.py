code = """import json
import re

# Load the data
with open(locals()['var_functions.query_db:0'], 'r') as f:
    funding = json.load(f)

with open(locals()['var_functions.query_db:14'], 'r') as f:
    docs = json.load(f)

# Find park projects completed in 2022
park_funding_total = 0
projects_found = []

# Define what we're looking for
park_terms = ['park', 'bluffs', 'playground', 'recreation']

# Check each civic document for 2022 completions
for doc in docs:
    text = doc.get('text', '')
    if '2022' not in text:
        continue
    
    # Look for completed park projects in this document
    for term in park_terms:
        if term in text.lower():
            # Find specific project mentions
            words = text.split()
            for i, word in enumerate(words):
                if term in word.lower():
                    # Look for completion date nearby
                    for j in range(max(0, i-10), min(len(words), i+10)):
                        if '2022' in words[j]:
                            if 'completed' in text.lower():
                                # Find matching funding record
                                for rec in funding:
                                    pname = rec.get('Project_Name', '')
                                    if term in pname.lower():
                                        park_funding_total += int(rec.get('Amount', 0))
                                        if pname not in projects_found:
                                            projects_found.append(pname)
                                    break

# Check for specific known projects
for doc in docs:
    text = doc.get('text', '').lower()
    
    if 'bluffs park shade structure' in text and '2022' in text and 'completed' in text:
        for rec in funding:
            if 'Bluffs Park Shade Structure' in rec.get('Project_Name', ''):
                park_funding_total += int(rec.get('Amount', 0))
                if rec.get('Project_Name') not in projects_found:
                    projects_found.append(rec.get('Project_Name'))
                break

print('__RESULT__:')
print(json.dumps({'total_park_funding_2022': park_funding_total, 'projects': len(projects_found), 'names': projects_found}))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.list_db:2': ['civic_docs'], 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json', 'var_functions.execute_python:12': {'status': 'inspection_complete'}, 'var_functions.query_db:14': 'file_storage/functions.query_db:14.json', 'var_functions.execute_python:16': {'funding_records': 500, 'civic_docs': 5, 'sample_funding': [{'Funding_ID': '1', 'Project_Name': '2021 Annual Street Maintenance', 'Funding_Source': 'Public-Private Partnership (PPP)', 'Amount': '24000'}, {'Funding_ID': '2', 'Project_Name': '2022 Annual Street Maintenance', 'Funding_Source': 'Government Grant', 'Amount': '45000'}]}}

exec(code, env_args)
