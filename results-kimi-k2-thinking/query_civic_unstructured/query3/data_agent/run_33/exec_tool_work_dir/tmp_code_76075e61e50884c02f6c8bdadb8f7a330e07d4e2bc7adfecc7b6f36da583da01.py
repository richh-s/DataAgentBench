code = """import json
import re

civic_file = locals()['var_functions.query_db:0']
funding_file = locals()['var_functions.query_db:5']

with open(civic_file, 'r') as f:
    civic_docs = json.load(f)

with open(funding_file, 'r') as f:
    funding_data = json.load(f)

all_results = []
seen_names = set()

# Get projects with FEMA in funding data
for record in funding_data:
    name = record['Project_Name']
    if 'fema' in name.lower():
        item = {
            'Project_Name': name,
            'Funding_Source': record['Funding_Source'],
            'Amount': int(record['Amount']),
            'Status': 'Not in civic docs'
        }
        all_results.append(item)
        seen_names.add(name.lower())

# Check civic docs
for doc in civic_docs:
    doc_text = doc['text']
    lines = doc_text.split('\n')
    
    for line in lines:
        low_line = line.lower()
        if 'emergency' in low_line or 'fema' in low_line:
            clean_line = line.strip()
            if len(clean_line) > 8 and not clean_line.startswith('('):
                low_clean = clean_line.lower()
                if low_clean not in seen_names:
                    # Find matching funding
                    match_funding = None
                    for f in funding_data:
                        f_name = f['Project_Name']
                        if clean_line in f_name or f_name in clean_line:
                            match_funding = f
                            break
                    
                    if match_funding:
                        amount = int(match_funding['Amount'])
                        source = match_funding['Funding_Source']
                    else:
                        amount = 0
                        source = 'Unknown'
                    
                    all_results.append({
                        'Project_Name': clean_line,
                        'Funding_Source': source,
                        'Amount': amount,
                        'Status': 'Referenced in civic docs'
                    })
                    seen_names.add(low_clean)

# Sort by amount
all_results.sort(key=lambda x: x['Amount'], reverse=True)

print('__RESULT__:')
print(json.dumps(all_results))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.list_db:2': ['Funding'], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.execute_python:8': 'file_storage/functions.execute_python:8.json'}

exec(code, env_args)
