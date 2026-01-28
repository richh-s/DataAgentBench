code = """import json
import re

# Access data files
civic_docs_file = locals()['var_functions.query_db:16']
funding_file = locals()['var_functions.query_db:17']

# Load the data
with open(civic_docs_file, 'r') as f:
    civic_docs = json.load(f)
with open(funding_file, 'r') as f:
    funding = json.load(f)

# Find Spring 2022 references
spring_2022_refs = []
pattern = re.compile(r'2022[-\s](spring|march|april|may)', re.IGNORECASE)

for doc in civic_docs:
    text = doc.get('text', '')
    matches = pattern.findall(text.lower())
    if matches:
        spring_2022_refs.append({
            'doc_id': doc.get('_id'),
            'filename': doc.get('filename'),
            'match_count': len(matches)
        })

# Count projects in funding database
project_names = [item['Project_Name'] for item in funding]

print('__RESULT__:')
print(json.dumps({
    'docs_with_spring_2022': len(spring_2022_refs),
    'total_funding_records': len(funding),
    'sample_refs': spring_2022_refs[:3]
}))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.list_db:1': ['Funding'], 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json', 'var_functions.query_db:5': [{'Funding_ID': '1', 'Project_Name': '2021 Annual Street Maintenance', 'Funding_Source': 'Public-Private Partnership (PPP)', 'Amount': '24000'}, {'Funding_ID': '2', 'Project_Name': '2022 Annual Street Maintenance', 'Funding_Source': 'Government Grant', 'Amount': '45000'}, {'Funding_ID': '3', 'Project_Name': '2022 Morning View Resurfacing & Storm Drain Improvements', 'Funding_Source': 'State Development Grant', 'Amount': '38000'}, {'Funding_ID': '4', 'Project_Name': 'Annual Street Maintenance', 'Funding_Source': 'Corporate Sponsorship', 'Amount': '23000'}, {'Funding_ID': '5', 'Project_Name': 'Birdview Avenue Improvements', 'Funding_Source': 'National Foundation Fund', 'Amount': '79000'}], 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json', 'var_functions.query_db:11': 'file_storage/functions.query_db:11.json', 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json', 'var_functions.query_db:14': 'file_storage/functions.query_db:14.json', 'var_functions.query_db:16': 'file_storage/functions.query_db:16.json', 'var_functions.query_db:17': 'file_storage/functions.query_db:17.json', 'var_functions.execute_python:22': {'civic_docs_count': 5, 'funding_count': 500, 'sample_civic_doc_filename': 'malibucity_agenda_03222023-2060.txt', 'total_funding_available': 28094000}}

exec(code, env_args)
