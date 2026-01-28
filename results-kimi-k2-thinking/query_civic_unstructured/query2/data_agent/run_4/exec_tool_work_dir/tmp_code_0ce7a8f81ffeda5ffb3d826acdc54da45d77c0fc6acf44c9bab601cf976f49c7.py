code = """import json
import re

# Load data from file paths
civic_path = locals()['var_functions.query_db:2']
funding_path = locals()['var_functions.query_db:6']

with open(civic_path, 'r') as f:
    civic_docs = json.load(f)
with open(funding_path, 'r') as f:
    funding_records = json.load(f)

# Convert funding amounts to integers
for rec in funding_records:
    rec['Amount'] = int(rec['Amount'])

# Extract park-related projects completed in 2022
park_projects_2022 = []

for doc in civic_docs:
    text = doc['text']
    lines = [line.strip() for line in text.split('\n') if line.strip()]
    
    for idx, line in enumerate(lines):
        # Look for completion in 2022
        if ('2022' in line and 'completed' in line.lower()):
            # Search backwards for project name (up to 5 lines)
            for j in range(max(0, idx-5), idx):
                prev_line = lines[j]
                
                # Skip obviously non-project lines
                if len(prev_line) > 100 or '(cid:' in prev_line or prev_line.startswith('Page'):
                    continue
                
                # Check if it's park-related
                park_keywords = ['park', 'playground', 'walkway', 'green street', 'shade', 'bluffs', 'skate park', 'arbors', 'benches', 'workout']
                if any(keyword in prev_line.lower() for keyword in park_keywords):
                    # Clean up project name
                    clean_name = re.sub(r'\(cid:\d+\)', '', prev_line).strip()
                    park_projects_2022.append(clean_name)
                    break

# Match with funding data based on project names
matched_funding = []

for park_name in park_projects_2022:
    park_name_lower = park_name.lower()
    
    for funding_rec in funding_records:
        fund_name = funding_rec['Project_Name']
        fund_name_lower = fund_name.lower()
        
        # Check if names match (one contains the other)
        if (park_name_lower in fund_name_lower or fund_name_lower in park_name_lower):
            matched_funding.append({
                'project_name': park_name,
                'funding_record_name': fund_name,
                'amount': funding_rec['Amount'],
                'funding_source': funding_rec['Funding_Source']
            })
            break

# Calculate total funding
total_funding = sum(f['amount'] for f in matched_funding)

result = {
    'total_funding': total_funding,
    'number_of_projects': len(matched_funding),
    'projects': matched_funding
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.list_db:4': ['Funding'], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.execute_python:12': ['var_functions.list_db:0', 'var_functions.query_db:2', 'var_functions.list_db:4', 'var_functions.query_db:6', '__builtins__', 'json'], 'var_functions.execute_python:14': {'civic_docs_count': 5, 'funding_records_count': 500, 'civic_sample_keys': ['_id', 'filename', 'text'], 'funding_sample': [{'Funding_ID': '1', 'Project_Name': '2021 Annual Street Maintenance', 'Funding_Source': 'Public-Private Partnership (PPP)', 'Amount': '24000'}, {'Funding_ID': '2', 'Project_Name': '2022 Annual Street Maintenance', 'Funding_Source': 'Government Grant', 'Amount': '45000'}, {'Funding_ID': '3', 'Project_Name': '2022 Morning View Resurfacing & Storm Drain Improvements', 'Funding_Source': 'State Development Grant', 'Amount': '38000'}]}, 'var_functions.execute_python:36': {'civic_type': "<class 'str'>", 'funding_type': "<class 'str'>", 'civic_is_file': True, 'funding_is_file': True}}

exec(code, env_args)
