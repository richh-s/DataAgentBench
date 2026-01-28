code = """import json
import re

funding_result = locals()['var_functions.query_db:6']
civic_result = locals()['var_functions.query_db:8']

funding_list = funding_result
if isinstance(funding_result, str) and funding_result.endswith('.json'):
    with open(funding_result, 'r') as f:
        funding_list = json.load(f)

civic_list = civic_result
if isinstance(civic_result, str) and civic_result.endswith('.json'):
    with open(civic_result, 'r') as f:
        civic_list = json.load(f)

funding_dict = {}
for item in funding_list:
    funding_dict[item['Project_Name']] = int(item['Amount'])

disaster_2022 = []
for doc in civic_list:
    txt = doc.get('text', '')
    if '(FEMA' in txt or '(CalOES' in txt or '(CalJPIA' in txt:
        if '2022' in txt:
            lines = txt.split('\n')
            for line in lines:
                line = line.strip()
                if line and ('(FEMA' in line or '(CalOES' in line or '(CalJPIA' in line):
                    disaster_2022.append(line)

unique_disaster = list(set(disaster_2022))

total_funding = 0
for project in unique_disaster:
    if project in funding_dict:
        total_funding += funding_dict[project]
    else:
        base_match = re.match(r'^(.+?)\s*\([^)]*\)$', project)
        if base_match:
            base = base_match.group(1)
            for funded_name in funding_dict:
                if funded_name.startswith(base) or base.startswith(funded_name):
                    if abs(len(base) - len(funded_name)) < 30:
                        total_funding += funding_dict[funded_name]
                        break

result = {"total_funding": total_funding}
print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['Funding'], 'var_functions.query_db:2': [{'Funding_ID': '1', 'Project_Name': '2021 Annual Street Maintenance', 'Funding_Source': 'Public-Private Partnership (PPP)', 'Amount': '24000'}, {'Funding_ID': '2', 'Project_Name': '2022 Annual Street Maintenance', 'Funding_Source': 'Government Grant', 'Amount': '45000'}, {'Funding_ID': '3', 'Project_Name': '2022 Morning View Resurfacing & Storm Drain Improvements', 'Funding_Source': 'State Development Grant', 'Amount': '38000'}, {'Funding_ID': '4', 'Project_Name': 'Annual Street Maintenance', 'Funding_Source': 'Corporate Sponsorship', 'Amount': '23000'}, {'Funding_ID': '5', 'Project_Name': 'Birdview Avenue Improvements', 'Funding_Source': 'National Foundation Fund', 'Amount': '79000'}], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json'}

exec(code, env_args)
