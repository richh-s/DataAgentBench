code = """import json
import re

# Load funding data
funding_path = locals()['var_functions.query_db:0']
with open(funding_path, 'r') as f:
    funding_data = json.load(f)

# Load civic docs data
civic_docs_path = locals()['var_functions.query_db:2']
with open(civic_docs_path, 'r') as f:
    civic_docs = json.load(f)

# Create funding lookup
funding_lookup = {}
for item in funding_data:
    clean_name = item['Project_Name'].split('(')[0].strip().lower()
    if clean_name not in funding_lookup:
        funding_lookup[clean_name] = []
    funding_lookup[clean_name].append({
        'Project_Name': item['Project_Name'],
        'Funding_Source': item['Funding_Source'],
        'Amount': int(item['Amount'])
    })

# Find all projects with emergency/FEMA keywords
emergency_keywords = ['fema', 'emergency', 'disaster', 'fire', 'caloes', 'caljpia']
results = []

# First, check funding data directly for FEMA/emergency projects
for item in funding_data:
    project_name = item['Project_Name']
    name_lower = project_name.lower()
    if any(keyword in name_lower for keyword in emergency_keywords):
        results.append({
            'Project_Name': project_name,
            'Funding_Source': item['Funding_Source'],
            'Amount': int(item['Amount']),
            'Status': 'Not found in civic documents',
            'Type': 'Unknown'
        })

# Add funding info found by clean name matching
for clean_name, fundings in funding_lookup.items():
    if any(keyword in clean_name for keyword in emergency_keywords):
        for funding in fundings:
            if not any(r['Project_Name'] == funding['Project_Name'] for r in results):
                results.append({
                    'Project_Name': funding['Project_Name'],
                    'Funding_Source': funding['Funding_Source'],
                    'Amount': funding['Amount'],
                    'Status': 'Not found in civic documents',
                    'Type': 'Unknown'
                })

print('Found ' + str(len(results)) + ' emergency/FEMA related projects')
print('__RESULT__:')
print(json.dumps(results))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.execute_python:6': [{'Funding_ID': '7', 'Project_Name': 'Birdview Avenue Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Research Institution Funding', 'Amount': '14000'}, {'Funding_ID': '22', 'Project_Name': 'Clover Heights Storm Drain (FEMA Project)', 'Funding_Source': 'Local NGO Fund', 'Amount': '21000'}, {'Funding_ID': '25', 'Project_Name': 'Corral Canyon Culvert Repairs (FEMA Project)', 'Funding_Source': 'Municipal Fund', 'Amount': '43000'}, {'Funding_ID': '26', 'Project_Name': 'Corral Canyon Culvert Repairs (FEMA/CalOES Project)', 'Funding_Source': 'Taxpayer Contribution', 'Amount': '15000'}, {'Funding_ID': '28', 'Project_Name': 'Corral Canyon Road Bridge Repairs (FEMA Project)', 'Funding_Source': 'Local Business Support', 'Amount': '25000'}, {'Funding_ID': '29', 'Project_Name': 'Corral Canyon Road Bridge Repairs (FEMA/CalOES Project)', 'Funding_Source': 'Cultural Heritage Grant', 'Amount': '58000'}, {'Funding_ID': '35', 'Project_Name': 'Encinal Canyon Road Drainage Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Private Sponsor', 'Amount': '94000'}, {'Funding_ID': '38', 'Project_Name': 'Guardrail Replacement Citywide (FEMA Project)', 'Funding_Source': 'Impact Investment Fund', 'Amount': '22000'}, {'Funding_ID': '39', 'Project_Name': 'Guardrail Replacement Citywide (FEMA/CalOES Project)', 'Funding_Source': 'Development Bank Loan', 'Amount': '45000'}, {'Funding_ID': '43', 'Project_Name': 'Latigo Canyon Road Culvert Repairs (FEMA Project)', 'Funding_Source': 'Federal Assistance', 'Amount': '36000'}]}

exec(code, env_args)
