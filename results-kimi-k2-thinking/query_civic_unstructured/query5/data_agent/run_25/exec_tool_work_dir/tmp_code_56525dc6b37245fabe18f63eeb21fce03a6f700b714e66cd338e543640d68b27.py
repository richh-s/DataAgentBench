code = """import json
import re

civic_docs = locals()['var_functions.query_db:5']
if isinstance(civic_docs, str):
    with open(civic_docs, 'r') as f:
        civic_docs = json.load(f)

all_projects = []

for doc in civic_docs:
    text = doc.get('text', '')
    filename = doc.get('filename', '')
    
    lines = text.split('\n')
    
    for i, line in enumerate(lines):
        line = line.strip()
        
        if line and not line.startswith('Item') and not line.startswith('To:') and not line.startswith('Prepared by'):
            if '2022' in line or any(keyword in line for keyword in ['Project', 'Repair', 'Improvement', 'Maintenance', 'Replacement']):
                if 'Road' in line or 'Street' in line or 'Park' in line or 'Drain' in line or 'Bridge' in line or 'Culvert' in line:
                    project_name = line
                    
                    project_type = 'disaster' if any(keyword in line.upper() for keyword in ['FEMA', 'CALOES', 'CALJPIA']) else 'capital'
                    
                    status = None
                    if '(Design)' in line:
                        status = 'design'
                    elif '(Construction)' in line:
                        status = 'construction'
                    elif '(Completed)' in line:
                        status = 'completed'
                    
                    all_projects.append({
                        'Project_Name': project_name,
                        'type': project_type,
                        'status': status,
                        'filename': filename
                    })

disaster_2022_names = []
for project in all_projects:
    if project['type'] == 'disaster' and '2022' in project['Project_Name']:
        disaster_2022_names.append(project['Project_Name'])

funding_data = locals()['var_functions.query_db:2']
if isinstance(funding_data, str):
    with open(funding_data, 'r') as f:
        funding_data = json.load(f)

disaster_funding_names = []
for item in funding_data:
    project_name = item['Project_Name']
    if any(keyword in project_name.upper() for keyword in ['FEMA', 'CALOES', 'CalJPIA']):
        disaster_funding_names.append(project_name)

print('__RESULT__:')
print(json.dumps({
    'disaster_projects_in_docs': len([p for p in all_projects if p['type'] == 'disaster']),
    'disaster_2022_name_matches': disaster_2022_names[:10],
    'disaster_in_funding': len(disaster_funding_names),
    'sample_funding_disaster': disaster_funding_names[:5]
}))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.execute_python:8': {'total_disaster_projects_in_funding': 20, 'sample_disaster_projects': [{'Project_Name': 'Birdview Avenue Improvements (FEMA/CalOES Project)', 'Funding_ID': '7', 'Funding_Source': 'Research Institution Funding', 'Amount': 14000}, {'Project_Name': 'Clover Heights Storm Drain (FEMA Project)', 'Funding_ID': '22', 'Funding_Source': 'Local NGO Fund', 'Amount': 21000}, {'Project_Name': 'Corral Canyon Culvert Repairs (FEMA Project)', 'Funding_ID': '25', 'Funding_Source': 'Municipal Fund', 'Amount': 43000}, {'Project_Name': 'Corral Canyon Culvert Repairs (FEMA/CalOES Project)', 'Funding_ID': '26', 'Funding_Source': 'Taxpayer Contribution', 'Amount': 15000}, {'Project_Name': 'Corral Canyon Road Bridge Repairs (FEMA Project)', 'Funding_ID': '28', 'Funding_Source': 'Local Business Support', 'Amount': 25000}, {'Project_Name': 'Corral Canyon Road Bridge Repairs (FEMA/CalOES Project)', 'Funding_ID': '29', 'Funding_Source': 'Cultural Heritage Grant', 'Amount': 58000}, {'Project_Name': 'Encinal Canyon Road Drainage Improvements (FEMA/CalOES Project)', 'Funding_ID': '35', 'Funding_Source': 'Private Sponsor', 'Amount': 94000}, {'Project_Name': 'Guardrail Replacement Citywide (FEMA Project)', 'Funding_ID': '38', 'Funding_Source': 'Impact Investment Fund', 'Amount': 22000}, {'Project_Name': 'Guardrail Replacement Citywide (FEMA/CalOES Project)', 'Funding_ID': '39', 'Funding_Source': 'Development Bank Loan', 'Amount': 45000}, {'Project_Name': 'Latigo Canyon Road Culvert Repairs (FEMA Project)', 'Funding_ID': '43', 'Funding_Source': 'Federal Assistance', 'Amount': 36000}]}}

exec(code, env_args)
