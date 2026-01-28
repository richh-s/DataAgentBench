code = """import json
import re

# Load data
funding_file = var_functions.query_db:28
with open(funding_file, 'r') as f:
    funding_data = json.load(f)

civic_file = var_functions.query_db:5
with open(civic_file, 'r') as f:
    civic_docs = json.load(f)

# Find disaster projects
projects = {}
for item in funding_data:
    name = item['Project_Name']
    if 'FEMA' in name.upper() or 'CALOES' in name.upper() or 'CALJPIA' in name.upper():
        projects[name] = {
            'amount': int(item['Amount']),
            'id': item['Funding_ID'],
            'started_2022': False
        }

# Map base names to full names
name_map = {}
for name in projects.keys():
    base = name.replace(' (FEMA Project)', '').replace(' (CalOES Project)', '').replace(' (FEMA/CalOES Project)', '').replace(' (CalJPIA Project)', '').replace(' (CalJPIA/FEMA Project)', '')
    name_map[base] = name
    name_map[name] = name

# Check civic docs for 2022 dates
for doc in civic_docs:
    text = doc.get('text', '')
    if '2022' not in text:
        continue
    lines = text.split('\n')
    for i in range(len(lines)):
        line = lines[i]
        for base_name, full_name in name_map.items():
            if base_name in line or full_name in line:
                # Check nearby lines for 2022 dates
                start = max(0, i-2)
                end = min(len(lines), i+5)
                for j in range(start, end):
                    date_line = lines[j]
                    if '2022' in date_line:
                        indicators = ['Complete', 'Schedule', 'Advertise', 'Begin', 'Construction', 'Design']
                        if any(ind in date_line for ind in indicators):
                            projects[full_name]['started_2022'] = True

# Projects with 2022 in name
for name in projects.keys():
    if '2022' in name:
        projects[name]['started_2022'] = True

# Calculate total funding
total_funding = 0
for name, info in projects.items():
    if info['started_2022']:
        total_funding += info['amount']

disaster_count = len([p for p in projects.values() if p['started_2022']])

result = {
    'total_funding': total_funding,
    'project_count': disaster_count
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.execute_python:8': {'total_disaster_projects_in_funding': 20, 'sample_disaster_projects': [{'Project_Name': 'Birdview Avenue Improvements (FEMA/CalOES Project)', 'Funding_ID': '7', 'Funding_Source': 'Research Institution Funding', 'Amount': 14000}, {'Project_Name': 'Clover Heights Storm Drain (FEMA Project)', 'Funding_ID': '22', 'Funding_Source': 'Local NGO Fund', 'Amount': 21000}, {'Project_Name': 'Corral Canyon Culvert Repairs (FEMA Project)', 'Funding_ID': '25', 'Funding_Source': 'Municipal Fund', 'Amount': 43000}, {'Project_Name': 'Corral Canyon Culvert Repairs (FEMA/CalOES Project)', 'Funding_ID': '26', 'Funding_Source': 'Taxpayer Contribution', 'Amount': 15000}, {'Project_Name': 'Corral Canyon Road Bridge Repairs (FEMA Project)', 'Funding_ID': '28', 'Funding_Source': 'Local Business Support', 'Amount': 25000}, {'Project_Name': 'Corral Canyon Road Bridge Repairs (FEMA/CalOES Project)', 'Funding_ID': '29', 'Funding_Source': 'Cultural Heritage Grant', 'Amount': 58000}, {'Project_Name': 'Encinal Canyon Road Drainage Improvements (FEMA/CalOES Project)', 'Funding_ID': '35', 'Funding_Source': 'Private Sponsor', 'Amount': 94000}, {'Project_Name': 'Guardrail Replacement Citywide (FEMA Project)', 'Funding_ID': '38', 'Funding_Source': 'Impact Investment Fund', 'Amount': 22000}, {'Project_Name': 'Guardrail Replacement Citywide (FEMA/CalOES Project)', 'Funding_ID': '39', 'Funding_Source': 'Development Bank Loan', 'Amount': 45000}, {'Project_Name': 'Latigo Canyon Road Culvert Repairs (FEMA Project)', 'Funding_ID': '43', 'Funding_Source': 'Federal Assistance', 'Amount': 36000}]}, 'var_functions.query_db:14': 'file_storage/functions.query_db:14.json', 'var_functions.query_db:16': 'file_storage/functions.query_db:16.json', 'var_functions.query_db:28': 'file_storage/functions.query_db:28.json'}

exec(code, env_args)
