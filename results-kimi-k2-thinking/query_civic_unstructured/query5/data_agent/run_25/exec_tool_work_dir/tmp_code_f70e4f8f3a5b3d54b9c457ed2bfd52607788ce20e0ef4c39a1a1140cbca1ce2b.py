code = """import json
import re

# Load funding data
funding_file = var_functions.query_db:16
if isinstance(funding_file, str):
    with open(funding_file, 'r') as f:
        funding_data = json.load(f)
else:
    funding_data = funding_file

# Load civic documents
civic_file = var_functions.query_db:5
if isinstance(civic_file, str):
    with open(civic_file, 'r') as f:
        civic_docs = json.load(f)
else:
    civic_docs = civic_file

# Find disaster projects from funding data
disaster_keywords = ['FEMA', 'CALOES', 'CALJPIA']
disaster_projects = []

for item in funding_data:
    project_name = item['Project_Name']
    if any(keyword in project_name.upper() for keyword in disaster_keywords):
        disaster_projects.append({
            'name': project_name,
            'amount': int(item['Amount']),
            'id': item['Funding_ID'],
            'started_2022': False
        })

print(f"Found {len(disaster_projects)} disaster projects")

# Check for 2022 start dates in civic documents
all_dates_2022 = []

for doc in civic_docs[:20]:  # Check first 20 docs
    text = doc.get('text', '')
    if '2022' in text:
        print(f"2022 found in {doc.get('filename', 'unknown')}")
        # Extract lines with 2022
        lines = text.split('\n')
        for line in lines:
            if '2022' in line and any(word in line.upper() for word in ['PROJECT', 'COMPLETE', 'SCHEDULE', 'BEGIN', 'DESIGN', 'CONSTRUCTION']):
                all_dates_2022.append(line.strip())

print('__RESULT__:')
print(json.dumps({
    'disaster_projects_count': len(disaster_projects),
    'total_disaster_funding': sum(p['amount'] for p in disaster_projects),
    'sample_dates_2022': all_dates_2022[:10]
}))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.execute_python:8': {'total_disaster_projects_in_funding': 20, 'sample_disaster_projects': [{'Project_Name': 'Birdview Avenue Improvements (FEMA/CalOES Project)', 'Funding_ID': '7', 'Funding_Source': 'Research Institution Funding', 'Amount': 14000}, {'Project_Name': 'Clover Heights Storm Drain (FEMA Project)', 'Funding_ID': '22', 'Funding_Source': 'Local NGO Fund', 'Amount': 21000}, {'Project_Name': 'Corral Canyon Culvert Repairs (FEMA Project)', 'Funding_ID': '25', 'Funding_Source': 'Municipal Fund', 'Amount': 43000}, {'Project_Name': 'Corral Canyon Culvert Repairs (FEMA/CalOES Project)', 'Funding_ID': '26', 'Funding_Source': 'Taxpayer Contribution', 'Amount': 15000}, {'Project_Name': 'Corral Canyon Road Bridge Repairs (FEMA Project)', 'Funding_ID': '28', 'Funding_Source': 'Local Business Support', 'Amount': 25000}, {'Project_Name': 'Corral Canyon Road Bridge Repairs (FEMA/CalOES Project)', 'Funding_ID': '29', 'Funding_Source': 'Cultural Heritage Grant', 'Amount': 58000}, {'Project_Name': 'Encinal Canyon Road Drainage Improvements (FEMA/CalOES Project)', 'Funding_ID': '35', 'Funding_Source': 'Private Sponsor', 'Amount': 94000}, {'Project_Name': 'Guardrail Replacement Citywide (FEMA Project)', 'Funding_ID': '38', 'Funding_Source': 'Impact Investment Fund', 'Amount': 22000}, {'Project_Name': 'Guardrail Replacement Citywide (FEMA/CalOES Project)', 'Funding_ID': '39', 'Funding_Source': 'Development Bank Loan', 'Amount': 45000}, {'Project_Name': 'Latigo Canyon Road Culvert Repairs (FEMA Project)', 'Funding_ID': '43', 'Funding_Source': 'Federal Assistance', 'Amount': 36000}]}, 'var_functions.query_db:14': 'file_storage/functions.query_db:14.json', 'var_functions.query_db:16': 'file_storage/functions.query_db:16.json'}

exec(code, env_args)
