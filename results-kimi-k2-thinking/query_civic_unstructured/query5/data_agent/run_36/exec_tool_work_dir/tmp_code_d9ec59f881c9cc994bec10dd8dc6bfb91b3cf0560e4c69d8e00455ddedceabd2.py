code = """import json
import re

# Load funding data
funding_path = locals()['var_functions.query_db:6']
with open(funding_path, 'r') as f:
    funding_data = json.load(f)

# Load civic documents  
civic_docs_path = locals()['var_functions.query_db:30']
with open(civic_docs_path, 'r') as f:
    civic_docs_data = json.load(f)

# Build funding lookup table
funding_lookup = {}
for record in funding_data:
    project_name = record['Project_Name']
    amount = int(record['Amount'])
    funding_lookup[project_name] = amount

# Find all disaster projects in funding data
disaster_funding_projects = []
for record in funding_data:
    project_name = record['Project_Name']
    if any(keyword in project_name.lower() for keyword in ['fema', 'caloes', 'caljpia', 'fire']):
        disaster_funding_projects.append(project_name)

# Extract projects from civic docs and find those starting in 2022
projects_in_docs = []

for doc in civic_docs_data:
    text = doc.get('text', '')
    lines = text.split('\n')
    
    for line in lines:
        line = line.strip()
        if len(line) < 5:
            continue
            
        # Skip headers and detail lines
        skip_indicators = ['Page', 'Agenda Item', 'Public Works', 'Commission Meeting', 'Chair', 'Prepared by:', 'Date prepared:', 'Meeting date:', 'Subject:', 'RECOMMENDED', 'DISCUSSION:', 'Complete:', 'Advertise:', 'Begin:', 'Updates:', 'Project Schedule:', 'Project Description:']
        if any(indicator in line for indicator in skip_indicators):
            continue
            
        if '2022' in line and not line.startswith('(') and not line.startswith('•'):
            projects_in_docs.append(line)

# Filter for disaster projects that mention 2022
disaster_projects_2022 = []
for project_name in set(projects_in_docs):
    if any(keyword in project_name.lower() for keyword in ['fema', 'caloes', 'caljpia', 'fire', 'disaster', 'recovery']):
        # Try to find funding
        if project_name in funding_lookup:
            amount = funding_lookup[project_name]
            disaster_projects_2022.append({
                'name': project_name,
                'amount': amount
            })
        else:
            # Try base name without FEMA suffixes
            base_name = project_name.split('(FEMA')[0].strip()
            if base_name in funding_lookup:
                amount = funding_lookup[base_name]
                disaster_projects_2022.append({
                    'name': project_name,
                    'amount': amount
                })

# Calculate total funding
total_funding_amount = sum(p['amount'] for p in disaster_projects_2022)

result = {
    'total_disaster_projects_found': len(disaster_funding_projects),
    'disaster_projects_2022_in_docs': len(disaster_projects_2022),
    'total_funding_for_2022_disaster_projects': total_funding_amount,
    'projects': disaster_projects_2022
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.execute_python:10': {'total_records': 500, 'sample_records': [{'Funding_ID': '1', 'Project_Name': '2021 Annual Street Maintenance', 'Funding_Source': 'Public-Private Partnership (PPP)', 'Amount': '24000'}, {'Funding_ID': '2', 'Project_Name': '2022 Annual Street Maintenance', 'Funding_Source': 'Government Grant', 'Amount': '45000'}, {'Funding_ID': '3', 'Project_Name': '2022 Morning View Resurfacing & Storm Drain Improvements', 'Funding_Source': 'State Development Grant', 'Amount': '38000'}]}, 'var_functions.execute_python:12': {'civic_docs_count': 5, 'first_doc_preview': 'Public Works Commission\nAgenda Report\n\nPublic Works\nCommission Meeting\n03-22-23\nItem\n4.B.\n\nTo:\n\nChair Dittrich and Members of the Public Works Commission\n\nPrepared by:\n\nJorge Rubalcava, Senior Civil Engineer\n\nApproved by:\n\nRob DuBoux, Public Works Director/City Engineer\n\nDate prepared: March 15, 2023\n\nMeeting date: March 22, 2023\n\nSubject:\n\nCapital Improvement Projects and Disaster Recovery Projects Status\nReport\n\nRECOMMENDED ACTION: Receive and file report on the status of the City’s current an'}, 'var_functions.execute_python:22': {'total_funding_records': 500, 'total_funding_amount': 28094000, 'disaster_projects_count': 27, 'disaster_projects': [['Birdview Avenue Improvements (CalOES Project)', 85000], ['Birdview Avenue Improvements (FEMA/CalOES Project)', 14000], ['Broad Beach Road Water Quality Infrastructure Repairs (CalJPIA Project)', 81000], ['Clover Heights Storm Drain (FEMA Project)', 21000], ['Corral Canyon Culvert Repairs (FEMA Project)', 43000], ['Corral Canyon Culvert Repairs (FEMA/CalOES Project)', 15000], ['Corral Canyon Road Bridge Repairs (FEMA Project)', 25000], ['Corral Canyon Road Bridge Repairs (FEMA/CalOES Project)', 58000], ['Encinal Canyon Road Drainage Improvements (CalOES Project)', 18000], ['Encinal Canyon Road Drainage Improvements (FEMA/CalOES Project)', 94000], ['Guardrail Replacement Citywide (FEMA Project)', 22000], ['Guardrail Replacement Citywide (FEMA/CalOES Project)', 45000], ['Latigo Canyon Road Culvert Repairs (FEMA Project)', 36000], ['Latigo Canyon Road Culvert Repairs (FEMA/CalOES Project)', 44000], ['Latigo Canyon Road Roadway/Retaining Wall Improvements (FEMA Project)', 91000], ['Latigo Canyon Road Roadway/Retaining Wall Improvements (FEMA/CalOES Project)', 78000], ['Malibu Road Slope Repairs (CalOES Project)', 37000], ['Outdoor Warning Sirens (FEMA Project)', 27000], ['Outdoor Warning Sirens (FEMA)', 81000], ['Outdoor Warning Sirens - Design (FEMA Project)', 43000]]}, 'var_functions.query_db:30': 'file_storage/functions.query_db:30.json'}

exec(code, env_args)
