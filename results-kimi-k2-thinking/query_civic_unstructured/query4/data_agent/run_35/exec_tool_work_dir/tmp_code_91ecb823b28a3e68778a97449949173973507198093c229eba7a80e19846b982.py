code = """import json
import re

with open('file_storage/functions.query_db:6.json', 'r') as f:
    funding = json.load(f)

with open('file_storage/functions.query_db:10.json', 'r') as f:
    docs = json.load(f)

# Find all 2022-Spring and Spring 2022 references
spring_2022_refs = []

for doc in docs:
    text = doc['text']
    # Find all occurrences
    for i, line in enumerate(text.split('\\n')):
        if '2022' in line and ('Spring' in line or 'spring' in line):
            spring_2022_refs.append({'line': line.strip()[:100], 'file': doc['filename']})

print('__RESULT__:')
print(json.dumps({'refs': spring_2022_refs, 'count': len(spring_2022_refs)}))"""

env_args = {'var_functions.query_db:0': [{'Funding_ID': '1', 'Project_Name': '2021 Annual Street Maintenance', 'Funding_Source': 'Public-Private Partnership (PPP)', 'Amount': '24000'}, {'Funding_ID': '2', 'Project_Name': '2022 Annual Street Maintenance', 'Funding_Source': 'Government Grant', 'Amount': '45000'}, {'Funding_ID': '3', 'Project_Name': '2022 Morning View Resurfacing & Storm Drain Improvements', 'Funding_Source': 'State Development Grant', 'Amount': '38000'}, {'Funding_ID': '4', 'Project_Name': 'Annual Street Maintenance', 'Funding_Source': 'Corporate Sponsorship', 'Amount': '23000'}, {'Funding_ID': '5', 'Project_Name': 'Birdview Avenue Improvements', 'Funding_Source': 'National Foundation Fund', 'Amount': '79000'}], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json', 'var_functions.list_db:12': ['civic_docs'], 'var_functions.execute_python:16': {'funding_result_type': "<class 'str'>", 'funding_result_preview': 'file_storage/functions.query_db:6.json', 'civic_result_type': "<class 'str'>", 'civic_result_preview': 'file_storage/functions.query_db:10.json'}, 'var_functions.execute_python:18': {'funding_records': 500, 'civic_docs_count': 5, 'sample_funding': [{'Funding_ID': '1', 'Project_Name': '2021 Annual Street Maintenance', 'Funding_Source': 'Public-Private Partnership (PPP)', 'Amount': 24000}, {'Funding_ID': '2', 'Project_Name': '2022 Annual Street Maintenance', 'Funding_Source': 'Government Grant', 'Amount': 45000}, {'Funding_ID': '3', 'Project_Name': '2022 Morning View Resurfacing & Storm Drain Improvements', 'Funding_Source': 'State Development Grant', 'Amount': 38000}, {'Funding_ID': '4', 'Project_Name': 'Annual Street Maintenance', 'Funding_Source': 'Corporate Sponsorship', 'Amount': 23000}, {'Funding_ID': '5', 'Project_Name': 'Birdview Avenue Improvements', 'Funding_Source': 'National Foundation Fund', 'Amount': 79000}], 'funding_columns': ['Funding_ID', 'Project_Name', 'Funding_Source', 'Amount']}, 'var_functions.execute_python:22': {'funding_records': 500, 'civic_docs_count': 5, 'total_funding_amount': 28094000, 'sample_project_names': ['2021 Annual Street Maintenance', '2022 Annual Street Maintenance', '2022 Morning View Resurfacing & Storm Drain Improvements', 'Annual Street Maintenance', 'Birdview Avenue Improvements']}}

exec(code, env_args)
