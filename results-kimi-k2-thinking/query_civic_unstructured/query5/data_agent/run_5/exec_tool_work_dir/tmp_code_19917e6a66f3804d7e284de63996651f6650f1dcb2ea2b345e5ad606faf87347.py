code = """import json
import re

# Load data
with open(locals()['var_functions.query_db:6'], 'r') as f:
    funding_records = json.load(f)

with open(locals()['var_functions.query_db:8'], 'r') as f:
    civic_docs = json.load(f)

# Identify disaster-related projects by name patterns in funding data
disaster_suffixes = [
    '(FEMA Project)',
    '(FEMA/CalOES Project)', 
    '(CalOES Project)',
    '(CalJPIA Project)',
    '(FEMA)',
    '(FEMA/CalOES)'
]

disaster_projects = []

for record in funding_records:
    project_name = record['Project_Name']
    amount = int(record['Amount'])
    
    # Check if it's a disaster project by suffix
    is_disaster = any(project_name.endswith(suffix) for suffix in disaster_suffixes)
    
    if is_disaster:
        # Extract base name for date lookup
        base_name = project_name
        for suffix in disaster_suffixes:
            base_name = base_name.replace(suffix, '').strip()
        
        disaster_projects.append({
            'Project_Name': project_name,
            'Base_Name': base_name,
            'Amount': amount,
            'Funding_Source': record['Funding_Source']
        })

print('__RESULT__:')
print(json.dumps({
    'disaster_projects_count': len(disaster_projects),
    'sample_disaster_projects': disaster_projects[:10]
}))"""

env_args = {'var_functions.list_db:0': ['Funding'], 'var_functions.query_db:2': [{'Funding_ID': '1', 'Project_Name': '2021 Annual Street Maintenance', 'Funding_Source': 'Public-Private Partnership (PPP)', 'Amount': '24000'}, {'Funding_ID': '2', 'Project_Name': '2022 Annual Street Maintenance', 'Funding_Source': 'Government Grant', 'Amount': '45000'}, {'Funding_ID': '3', 'Project_Name': '2022 Morning View Resurfacing & Storm Drain Improvements', 'Funding_Source': 'State Development Grant', 'Amount': '38000'}, {'Funding_ID': '4', 'Project_Name': 'Annual Street Maintenance', 'Funding_Source': 'Corporate Sponsorship', 'Amount': '23000'}, {'Funding_ID': '5', 'Project_Name': 'Birdview Avenue Improvements', 'Funding_Source': 'National Foundation Fund', 'Amount': '79000'}, {'Funding_ID': '6', 'Project_Name': 'Birdview Avenue Improvements (CalOES Project)', 'Funding_Source': 'International Aid', 'Amount': '85000'}, {'Funding_ID': '7', 'Project_Name': 'Birdview Avenue Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Research Institution Funding', 'Amount': '14000'}, {'Funding_ID': '8', 'Project_Name': 'Bluffs Park Shade Structure', 'Funding_Source': 'Government Grant', 'Amount': '21000'}, {'Funding_ID': '9', 'Project_Name': 'Bluffs Park Workout Station', 'Funding_Source': 'University Research Fund', 'Amount': '39000'}, {'Funding_ID': '10', 'Project_Name': 'Broad Beach Road Water Quality Infrastructure Repairs', 'Funding_Source': 'International Organization Grant', 'Amount': '87000'}], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.execute_python:12': {'funding_records_count': 500, 'civic_docs_count': 5}, 'var_functions.execute_python:20': {'funding_records_count': 500, 'civic_docs_count': 5, 'first_funding_record': {'Funding_ID': '1', 'Project_Name': '2021 Annual Street Maintenance', 'Funding_Source': 'Public-Private Partnership (PPP)', 'Amount': '24000'}, 'first_civic_doc': {'filename': 'malibucity_agenda_03222023-2060.txt', 'text_length': 9796}}}

exec(code, env_args)
