code = """import json
import re

civic_file = locals()['var_functions.query_db:0']
funding_file = locals()['var_functions.query_db:5']

with open(civic_file) as f:
    civic_docs = json.load(f)

with open(funding_file) as f:
    funding_data = json.load(f)

# Get all FEMA/emergency projects from funding data
fema_projects = []
for fund in funding_data:
    if 'fema' in fund['Project_Name'].lower():
        fema_projects.append(fund)

# Check civic docs for status info
final_results = []

for fema_project in fema_projects:
    proj_name = fema_project['Project_Name']
    status = 'Not specified'
    
    # Look for project status in civic documents
    for doc in civic_docs:
        doc_text = doc['text']
        if proj_name in doc_text:
            # Try to extract status - look for keywords near the project name
            lines = doc_text.split('\n')
            for i, line in enumerate(lines):
                if proj_name in line:
                    # Check surrounding lines for status
                    context = '\n'.join(lines[max(0,i-3):min(len(lines),i+4)])
                    if 'construction' in context.lower() and 'complete' in context.lower():
                        status = 'completed'
                    elif 'construction' in context.lower():
                        status = 'construction'
                    elif 'design' in context.lower():
                        status = 'design'
                    elif 'not started' in context.lower():
                        status = 'not started'
                    break
    
    final_results.append({
        'Project_Name': proj_name,
        'Funding_Source': fema_project['Funding_Source'],
        'Amount': int(fema_project['Amount']),
        'Status': status
    })

# Sort by amount
def get_amount(item):
    return item['Amount']

final_results.sort(key=get_amount, reverse=True)

print('__RESULT__:')
print(json.dumps(final_results))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.list_db:2': ['Funding'], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.execute_python:8': 'file_storage/functions.execute_python:8.json', 'var_functions.execute_python:34': [{'Project_Name': 'Encinal Canyon Road Drainage Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Private Sponsor', 'Amount': 94000, 'Status': 'Not specified'}, {'Project_Name': 'Trancas Canyon Park Planting and Irrigation Repairs (FEMA/CalOES Project)', 'Funding_Source': 'Infrastructure Bond', 'Amount': 92000, 'Status': 'Not specified'}, {'Project_Name': 'Latigo Canyon Road Roadway/Retaining Wall Improvements (FEMA Project)', 'Funding_Source': 'Municipal Fund', 'Amount': 91000, 'Status': 'Not specified'}, {'Project_Name': 'Outdoor Warningn Sirens - Design (FEMA Project)', 'Funding_Source': 'Technology Innovation Fund', 'Amount': 84000, 'Status': 'Not specified'}, {'Project_Name': 'Outdoor Warning Sirens (FEMA)', 'Funding_Source': 'State Development Grant', 'Amount': 81000, 'Status': 'Not specified'}, {'Project_Name': 'Storm Drain Master Plan (FEMA Project)', 'Funding_Source': 'Environmental Grant', 'Amount': 80000, 'Status': 'Not specified'}, {'Project_Name': 'Latigo Canyon Road Roadway/Retaining Wall Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Community Fund', 'Amount': 78000, 'Status': 'Not specified'}, {'Project_Name': 'Corral Canyon Road Bridge Repairs (FEMA/CalOES Project)', 'Funding_Source': 'Cultural Heritage Grant', 'Amount': 58000, 'Status': 'Not specified'}, {'Project_Name': 'Guardrail Replacement Citywide (FEMA/CalOES Project)', 'Funding_Source': 'Development Bank Loan', 'Amount': 45000, 'Status': 'Not specified'}, {'Project_Name': 'Latigo Canyon Road Culvert Repairs (FEMA/CalOES Project)', 'Funding_Source': 'National Foundation Fund', 'Amount': 44000, 'Status': 'Not specified'}, {'Project_Name': 'Trancas Canyon Park Planting and Irrigation Repairs (CalJPIA/FEMA Project)', 'Funding_Source': 'Infrastructure Bond', 'Amount': 44000, 'Status': 'Not specified'}, {'Project_Name': 'Corral Canyon Culvert Repairs (FEMA Project)', 'Funding_Source': 'Municipal Fund', 'Amount': 43000, 'Status': 'Not specified'}, {'Project_Name': 'Outdoor Warning Sirens - Design (FEMA Project)', 'Funding_Source': 'Local Business Support', 'Amount': 43000, 'Status': 'Not specified'}, {'Project_Name': 'Latigo Canyon Road Culvert Repairs (FEMA Project)', 'Funding_Source': 'Federal Assistance', 'Amount': 36000, 'Status': 'Not specified'}, {'Project_Name': 'Outdoor Warning Sirens (FEMA Project)', 'Funding_Source': 'Environmental Grant', 'Amount': 27000, 'Status': 'Not specified'}, {'Project_Name': 'Corral Canyon Road Bridge Repairs (FEMA Project)', 'Funding_Source': 'Local Business Support', 'Amount': 25000, 'Status': 'Not specified'}, {'Project_Name': 'Guardrail Replacement Citywide (FEMA Project)', 'Funding_Source': 'Impact Investment Fund', 'Amount': 22000, 'Status': 'Not specified'}, {'Project_Name': 'Clover Heights Storm Drain (FEMA Project)', 'Funding_Source': 'Local NGO Fund', 'Amount': 21000, 'Status': 'Not specified'}, {'Project_Name': 'Corral Canyon Culvert Repairs (FEMA/CalOES Project)', 'Funding_Source': 'Taxpayer Contribution', 'Amount': 15000, 'Status': 'Not specified'}, {'Project_Name': 'Birdview Avenue Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Research Institution Funding', 'Amount': 14000, 'Status': 'Not specified'}]}

exec(code, env_args)
