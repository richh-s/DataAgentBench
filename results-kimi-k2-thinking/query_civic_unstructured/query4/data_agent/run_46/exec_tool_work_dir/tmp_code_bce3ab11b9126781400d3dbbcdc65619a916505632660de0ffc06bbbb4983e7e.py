code = """import json
import re

# Load data from storage
civic_docs_file = locals()['var_functions.query_db:2']
funding_file = locals()['var_functions.query_db:5']

with open(civic_docs_file, 'r') as f:
    civic_docs = json.load(f)

with open(funding_file, 'r') as f:
    funding_data = json.load(f)

print(f'Loaded {len(civic_docs)} civic documents and {len(funding_data)} funding records')

# Debug: print structure of first document
first_doc = civic_docs[0]
print('First doc keys:', list(first_doc.keys()))
print('First doc filename:', first_doc.get('filename'))
print('First 500 chars of text:', first_doc.get('text', '')[:500])

# Build simple funding map
funding_map = {}
for f in funding_data:
    name = f['Project_Name']
    amount = int(f['Amount'])
    funding_map[name] = funding_map.get(name, 0) + amount

print('Sample funding entries:', list(funding_map.items())[:5])

# Look for Spring 2022 in the text
spring_mentions = 0
spring_contexts = []

for doc in civic_docs:
    text = doc.get('text', '').lower()
    if '2022' in text and 'spring' in text:
        spring_mentions += 1
        # Get context
        lines = doc.get('text', '').split('\n')
        for i, line in enumerate(lines):
            low_line = line.lower()
            if '2022' in low_line and 'spring' in low_line:
                # Get surrounding context
                start = max(0, i-2)
                end = min(len(lines), i+3)
                context = '\n'.join(lines[start:end])
                spring_contexts.append(context)

print(f'Documents mentioning Spring 2022: {spring_mentions}')
print(f'Found {len(spring_contexts)} Spring 2022 contexts')

if spring_contexts:
    print('First context:')
    print(spring_contexts[0][:500])

result = {
    'docs_loaded': len(civic_docs),
    'funding_loaded': len(funding_data),
    'spring_mentions': spring_mentions,
    'contexts_found': len(spring_contexts)
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:8': [{'Funding_ID': '1', 'Project_Name': '2021 Annual Street Maintenance', 'Funding_Source': 'Public-Private Partnership (PPP)', 'Amount': '24000'}, {'Funding_ID': '2', 'Project_Name': '2022 Annual Street Maintenance', 'Funding_Source': 'Government Grant', 'Amount': '45000'}, {'Funding_ID': '3', 'Project_Name': '2022 Morning View Resurfacing & Storm Drain Improvements', 'Funding_Source': 'State Development Grant', 'Amount': '38000'}, {'Funding_ID': '4', 'Project_Name': 'Annual Street Maintenance', 'Funding_Source': 'Corporate Sponsorship', 'Amount': '23000'}, {'Funding_ID': '5', 'Project_Name': 'Birdview Avenue Improvements', 'Funding_Source': 'National Foundation Fund', 'Amount': '79000'}], 'var_functions.execute_python:14': {'civic_count': 5, 'funding_count': 500}, 'var_functions.execute_python:20': {'civic_file': 'var_functions.query_db:2', 'funding_file': 'var_functions.query_db:5'}, 'var_functions.execute_python:22': {'civic_path': 'file_storage/functions.query_db:2.json', 'funding_path': 'file_storage/functions.query_db:5.json', 'civic_exists': True, 'funding_exists': True}, 'var_functions.execute_python:36': {'project_count': 0, 'total_funding': 0}}

exec(code, env_args)
