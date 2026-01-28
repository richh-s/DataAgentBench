code = """import json
import re

# Read files
funding_file = locals()['var_functions.query_db:0']
civic_file = locals()['var_functions.query_db:6']

with open(funding_file, 'r') as f:
    funding_data = json.load(f)
with open(civic_file, 'r') as f:
    civic_docs = json.load(f)

# Projects from funding with FEMA/emergency
fema_project_names = []
for record in funding_data:
    name = record.get('Project_Name', '')
    if 'FEMA' in name.upper() or 'EMERGENCY' in name.upper():
        fema_project_names.append(name)

# Extract project status from civic documents
project_status = {}

for doc in civic_docs:
    text = doc.get('text', '')
    # Split by project sections
    sections = re.split(r'\n\s*\n', text)
    
    for section in sections:
        # Look for project names in FEMA list
        for proj_name in fema_project_names:
            # Check if this section mentions the project
            base_name = proj_name.replace(' (FEMA Project)', '').replace(' (FEMA/CalOES Project)', '').replace(' (CalJPIA/FEMA Project)', '').strip()
            if base_name in section:
                # Extract status
                status_match = re.search(r'Updates?:(.*?)(?:\n|$)', section, re.IGNORECASE)
                if status_match:
                    status_text = status_match.group(1).strip()
                    # Clean up status
                    if 'construction was completed' in status_text.lower() or 'completed' in status_text.lower():
                        project_status[proj_name] = 'completed'
                    elif 'under construction' in status_text.lower() or 'construction' in status_text.lower():
                        project_status[proj_name] = 'construction'
                    elif 'design' in status_text.lower():
                        project_status[proj_name] = 'design'
                    elif 'not started' in status_text.lower():
                        project_status[proj_name] = 'not started'
                    else:
                        project_status[proj_name] = status_text[:100]  # Truncate long status

# Combine funding data with status
results = []
for record in funding_data:
    proj_name = record.get('Project_Name', '')
    if 'FEMA' in proj_name.upper() or 'EMERGENCY' in proj_name.upper():
        results.append({
            'Project_Name': proj_name,
            'Funding_Source': record.get('Funding_Source', ''),
            'Amount': int(record.get('Amount', 0)),
            'Status': project_status.get(proj_name, 'Unknown')
        })

print('__RESULT__:')
print(json.dumps(results))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.execute_python:12': {'funding_fema_projects': [{'Funding_ID': '7', 'Project_Name': 'Birdview Avenue Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Research Institution Funding', 'Amount': '14000'}, {'Funding_ID': '22', 'Project_Name': 'Clover Heights Storm Drain (FEMA Project)', 'Funding_Source': 'Local NGO Fund', 'Amount': '21000'}, {'Funding_ID': '25', 'Project_Name': 'Corral Canyon Culvert Repairs (FEMA Project)', 'Funding_Source': 'Municipal Fund', 'Amount': '43000'}, {'Funding_ID': '26', 'Project_Name': 'Corral Canyon Culvert Repairs (FEMA/CalOES Project)', 'Funding_Source': 'Taxpayer Contribution', 'Amount': '15000'}, {'Funding_ID': '28', 'Project_Name': 'Corral Canyon Road Bridge Repairs (FEMA Project)', 'Funding_Source': 'Local Business Support', 'Amount': '25000'}, {'Funding_ID': '29', 'Project_Name': 'Corral Canyon Road Bridge Repairs (FEMA/CalOES Project)', 'Funding_Source': 'Cultural Heritage Grant', 'Amount': '58000'}, {'Funding_ID': '35', 'Project_Name': 'Encinal Canyon Road Drainage Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Private Sponsor', 'Amount': '94000'}, {'Funding_ID': '38', 'Project_Name': 'Guardrail Replacement Citywide (FEMA Project)', 'Funding_Source': 'Impact Investment Fund', 'Amount': '22000'}, {'Funding_ID': '39', 'Project_Name': 'Guardrail Replacement Citywide (FEMA/CalOES Project)', 'Funding_Source': 'Development Bank Loan', 'Amount': '45000'}, {'Funding_ID': '43', 'Project_Name': 'Latigo Canyon Road Culvert Repairs (FEMA Project)', 'Funding_Source': 'Federal Assistance', 'Amount': '36000'}, {'Funding_ID': '44', 'Project_Name': 'Latigo Canyon Road Culvert Repairs (FEMA/CalOES Project)', 'Funding_Source': 'National Foundation Fund', 'Amount': '44000'}, {'Funding_ID': '47', 'Project_Name': 'Latigo Canyon Road Roadway/Retaining Wall Improvements (FEMA Project)', 'Funding_Source': 'Municipal Fund', 'Amount': '91000'}, {'Funding_ID': '48', 'Project_Name': 'Latigo Canyon Road Roadway/Retaining Wall Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Community Fund', 'Amount': '78000'}, {'Funding_ID': '66', 'Project_Name': 'Outdoor Warning Sirens (FEMA Project)', 'Funding_Source': 'Environmental Grant', 'Amount': '27000'}, {'Funding_ID': '67', 'Project_Name': 'Outdoor Warning Sirens (FEMA)', 'Funding_Source': 'State Development Grant', 'Amount': '81000'}, {'Funding_ID': '68', 'Project_Name': 'Outdoor Warning Sirens - Design (FEMA Project)', 'Funding_Source': 'Local Business Support', 'Amount': '43000'}, {'Funding_ID': '69', 'Project_Name': 'Outdoor Warningn Sirens - Design (FEMA Project)', 'Funding_Source': 'Technology Innovation Fund', 'Amount': '84000'}, {'Funding_ID': '82', 'Project_Name': 'Storm Drain Master Plan (FEMA Project)', 'Funding_Source': 'Environmental Grant', 'Amount': '80000'}, {'Funding_ID': '86', 'Project_Name': 'Trancas Canyon Park Planting and Irrigation Repairs (CalJPIA/FEMA Project)', 'Funding_Source': 'Infrastructure Bond', 'Amount': '44000'}, {'Funding_ID': '87', 'Project_Name': 'Trancas Canyon Park Planting and Irrigation Repairs (FEMA/CalOES Project)', 'Funding_Source': 'Infrastructure Bond', 'Amount': '92000'}], 'count': 20}}

exec(code, env_args)
