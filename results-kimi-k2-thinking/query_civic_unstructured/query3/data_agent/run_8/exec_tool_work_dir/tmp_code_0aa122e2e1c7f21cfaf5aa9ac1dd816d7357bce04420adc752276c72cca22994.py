code = """import json
import re

# Read the data
with open('file_storage/functions.query_db:5.json', 'r') as f:
    funding_data = json.load(f)

with open('file_storage/functions.query_db:8.json', 'r') as f:
    civic_docs = json.load(f)

# Filter for FEMA/emergency related funding
fema_funding = []
for row in funding_data:
    project_name = row.get('Project_Name', '').lower()
    if 'fema' in project_name or 'emergency' in project_name or 'warning' in project_name or 'caloes' in project_name:
        fema_funding.append(row)

# Extract project statuses from civic documents
project_status = {}
for doc in civic_docs:
    text = doc.get('text', '')
    lines = text.split('\n')
    
    current_project = None
    for i, line in enumerate(lines):
        line = line.strip()
        if not line:
            continue
            
        # Skip headers
        if 'Page ' in line or 'Agenda Item' in line:
            continue
            
        # Look for project names that match our funding projects
        for funding_project in fema_funding:
            fund_name = funding_project['Project_Name']
            if fund_name.lower() in line.lower() or line.lower() in fund_name.lower():
                current_project = fund_name
                break
        
        # Extract status if we found a project
        if current_project:
            lower_line = line.lower()
            # Check status indicators in this line or next few lines
            if current_project not in project_status:
                if 'construction was completed' in lower_line or 'completed' in lower_line:
                    project_status[current_project] = 'completed'
                elif 'staff is working' in lower_line or 'complete design' in lower_line:
                    project_status[current_project] = 'design'
                elif 'preliminary' in lower_line or 'not started' in lower_line:
                    project_status[current_project] = 'not started'
                elif 'under construction' in lower_line:
                    project_status[current_project] = 'construction'

# Create final results
results = []
for funding_row in fema_funding:
    project_name = funding_row['Project_Name']
    status = project_status.get(project_name, 'unknown')
    
    results.append({
        'Project_Name': project_name,
        'Funding_Source': funding_row['Funding_Source'],
        'Amount': float(funding_row['Amount']),
        'Status': status
    })

print('__RESULT__:')
print(json.dumps(results))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.list_db:2': ['Funding'], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.execute_python:12': {'funding_storage_key': 'var_functions.query_db:5', 'civic_docs_storage_key': 'var_functions.query_db:8'}, 'var_functions.execute_python:20': ['var_functions.list_db:0', 'var_functions.list_db:2', 'var_functions.query_db:5', 'var_functions.query_db:6', 'var_functions.query_db:8', 'var_functions.execute_python:12', '__builtins__', 'json', 're'], 'var_functions.execute_python:26': ['var_functions.list_db:0', 'var_functions.list_db:2', 'var_functions.query_db:5', 'var_functions.query_db:6', 'var_functions.query_db:8', 'var_functions.execute_python:12', 'var_functions.execute_python:20'], 'var_functions.execute_python:30': {'funding_path': 'file_storage/functions.query_db:5.json', 'civic_path': 'file_storage/functions.query_db:8.json', 'funding_type': "<class 'list'>", 'civic_type': "<class 'list'>"}, 'var_functions.execute_python:32': {'fema_funding_count': 23, 'civic_docs_count': 5, 'sample_funding': [{'Funding_ID': '7', 'Project_Name': 'Birdview Avenue Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Research Institution Funding', 'Amount': '14000'}, {'Funding_ID': '22', 'Project_Name': 'Clover Heights Storm Drain (FEMA Project)', 'Funding_Source': 'Local NGO Fund', 'Amount': '21000'}, {'Funding_ID': '25', 'Project_Name': 'Corral Canyon Culvert Repairs (FEMA Project)', 'Funding_Source': 'Municipal Fund', 'Amount': '43000'}, {'Funding_ID': '26', 'Project_Name': 'Corral Canyon Culvert Repairs (FEMA/CalOES Project)', 'Funding_Source': 'Taxpayer Contribution', 'Amount': '15000'}, {'Funding_ID': '28', 'Project_Name': 'Corral Canyon Road Bridge Repairs (FEMA Project)', 'Funding_Source': 'Local Business Support', 'Amount': '25000'}, {'Funding_ID': '29', 'Project_Name': 'Corral Canyon Road Bridge Repairs (FEMA/CalOES Project)', 'Funding_Source': 'Cultural Heritage Grant', 'Amount': '58000'}, {'Funding_ID': '35', 'Project_Name': 'Encinal Canyon Road Drainage Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Private Sponsor', 'Amount': '94000'}, {'Funding_ID': '38', 'Project_Name': 'Guardrail Replacement Citywide (FEMA Project)', 'Funding_Source': 'Impact Investment Fund', 'Amount': '22000'}, {'Funding_ID': '39', 'Project_Name': 'Guardrail Replacement Citywide (FEMA/CalOES Project)', 'Funding_Source': 'Development Bank Loan', 'Amount': '45000'}, {'Funding_ID': '43', 'Project_Name': 'Latigo Canyon Road Culvert Repairs (FEMA Project)', 'Funding_Source': 'Federal Assistance', 'Amount': '36000'}, {'Funding_ID': '44', 'Project_Name': 'Latigo Canyon Road Culvert Repairs (FEMA/CalOES Project)', 'Funding_Source': 'National Foundation Fund', 'Amount': '44000'}, {'Funding_ID': '47', 'Project_Name': 'Latigo Canyon Road Roadway/Retaining Wall Improvements (FEMA Project)', 'Funding_Source': 'Municipal Fund', 'Amount': '91000'}, {'Funding_ID': '48', 'Project_Name': 'Latigo Canyon Road Roadway/Retaining Wall Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Community Fund', 'Amount': '78000'}, {'Funding_ID': '64', 'Project_Name': 'Outdoor Warning Signs', 'Funding_Source': 'Urban Renewal Fund', 'Amount': '92000'}, {'Funding_ID': '65', 'Project_Name': 'Outdoor Warning Sirens', 'Funding_Source': 'Social Impact Investment', 'Amount': '28000'}]}}

exec(code, env_args)
