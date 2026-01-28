code = """import json
import re

# Load funding data
with open('file_storage/functions.query_db:5.json', 'r') as f:
    funding_data = json.load(f)

# Load civic documents
with open('file_storage/functions.query_db:8.json', 'r') as f:
    civic_docs = json.load(f)

# Get all FEMA/emergency/warning projects from funding
fema_projects = []
for row in funding_data:
    project_name = row.get('Project_Name', '')
    lower_name = project_name.lower()
    if 'fema' in lower_name or 'emergency' in lower_name or 'warning' in lower_name or 'caloes' in lower_name:
        fema_projects.append(row)

# Extract statuses from civic docs
status_dict = {}
for doc in civic_docs:
    text = doc.get('text', '')
    # Simple pattern matching for status
    if text:
        # Look for completed projects
        if 'completed' in text.lower():
            # Extract project name in this doc
            for fp in fema_projects:
                name = fp.get('Project_Name', '')
                if name in text:
                    status_dict[name] = 'completed'
        
        # Look for design phase
        if 'design' in text.lower() and 'complete design' in text.lower():
            for fp in fema_projects:
                name = fp.get('Project_Name', '')
                if name in text:
                    status_dict[name] = 'design'

# Create results with basic status detection
results = []
sample_output = []

for project in fema_projects:
    project_name = project.get('Project_Name', '')
    funding_source = project.get('Funding_Source', '')
    amount = float(project.get('Amount', 0))
    
    # Determine status
    status = 'unknown'
    if project_name in status_dict:
        status = status_dict[project_name]
    else:
        # Try to infer from project name
        lower_name = project_name.lower()
        if any(x in lower_name for x in ['design', 'planning']):
            status = 'design'
        elif any(x in lower_name for x in ['construction', 'repair']):
            status = 'construction'
    
    results.append({
        'Project_Name': project_name,
        'Funding_Source': funding_source,
        'Amount': amount,
        'Status': status
    })

print('__RESULT__:')
print(json.dumps(results))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.list_db:2': ['Funding'], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.execute_python:12': {'funding_storage_key': 'var_functions.query_db:5', 'civic_docs_storage_key': 'var_functions.query_db:8'}, 'var_functions.execute_python:20': ['var_functions.list_db:0', 'var_functions.list_db:2', 'var_functions.query_db:5', 'var_functions.query_db:6', 'var_functions.query_db:8', 'var_functions.execute_python:12', '__builtins__', 'json', 're'], 'var_functions.execute_python:26': ['var_functions.list_db:0', 'var_functions.list_db:2', 'var_functions.query_db:5', 'var_functions.query_db:6', 'var_functions.query_db:8', 'var_functions.execute_python:12', 'var_functions.execute_python:20'], 'var_functions.execute_python:30': {'funding_path': 'file_storage/functions.query_db:5.json', 'civic_path': 'file_storage/functions.query_db:8.json', 'funding_type': "<class 'list'>", 'civic_type': "<class 'list'>"}, 'var_functions.execute_python:32': {'fema_funding_count': 23, 'civic_docs_count': 5, 'sample_funding': [{'Funding_ID': '7', 'Project_Name': 'Birdview Avenue Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Research Institution Funding', 'Amount': '14000'}, {'Funding_ID': '22', 'Project_Name': 'Clover Heights Storm Drain (FEMA Project)', 'Funding_Source': 'Local NGO Fund', 'Amount': '21000'}, {'Funding_ID': '25', 'Project_Name': 'Corral Canyon Culvert Repairs (FEMA Project)', 'Funding_Source': 'Municipal Fund', 'Amount': '43000'}, {'Funding_ID': '26', 'Project_Name': 'Corral Canyon Culvert Repairs (FEMA/CalOES Project)', 'Funding_Source': 'Taxpayer Contribution', 'Amount': '15000'}, {'Funding_ID': '28', 'Project_Name': 'Corral Canyon Road Bridge Repairs (FEMA Project)', 'Funding_Source': 'Local Business Support', 'Amount': '25000'}, {'Funding_ID': '29', 'Project_Name': 'Corral Canyon Road Bridge Repairs (FEMA/CalOES Project)', 'Funding_Source': 'Cultural Heritage Grant', 'Amount': '58000'}, {'Funding_ID': '35', 'Project_Name': 'Encinal Canyon Road Drainage Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Private Sponsor', 'Amount': '94000'}, {'Funding_ID': '38', 'Project_Name': 'Guardrail Replacement Citywide (FEMA Project)', 'Funding_Source': 'Impact Investment Fund', 'Amount': '22000'}, {'Funding_ID': '39', 'Project_Name': 'Guardrail Replacement Citywide (FEMA/CalOES Project)', 'Funding_Source': 'Development Bank Loan', 'Amount': '45000'}, {'Funding_ID': '43', 'Project_Name': 'Latigo Canyon Road Culvert Repairs (FEMA Project)', 'Funding_Source': 'Federal Assistance', 'Amount': '36000'}, {'Funding_ID': '44', 'Project_Name': 'Latigo Canyon Road Culvert Repairs (FEMA/CalOES Project)', 'Funding_Source': 'National Foundation Fund', 'Amount': '44000'}, {'Funding_ID': '47', 'Project_Name': 'Latigo Canyon Road Roadway/Retaining Wall Improvements (FEMA Project)', 'Funding_Source': 'Municipal Fund', 'Amount': '91000'}, {'Funding_ID': '48', 'Project_Name': 'Latigo Canyon Road Roadway/Retaining Wall Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Community Fund', 'Amount': '78000'}, {'Funding_ID': '64', 'Project_Name': 'Outdoor Warning Signs', 'Funding_Source': 'Urban Renewal Fund', 'Amount': '92000'}, {'Funding_ID': '65', 'Project_Name': 'Outdoor Warning Sirens', 'Funding_Source': 'Social Impact Investment', 'Amount': '28000'}]}, 'var_functions.execute_python:38': {'funding_rows': 500, 'civic_docs': 5}}

exec(code, env_args)
