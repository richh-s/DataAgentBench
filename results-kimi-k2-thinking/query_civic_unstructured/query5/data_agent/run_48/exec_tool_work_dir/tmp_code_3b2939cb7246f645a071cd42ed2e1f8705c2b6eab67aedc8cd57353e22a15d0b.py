code = """import json
import re

def extract_disaster_projects_2022(civic_docs):
    """Extract disaster projects that started in 2022"""
    projects = []
    
    for doc in civic_docs:
        text = doc['text']
        lines = text.split('\n')
        
        for i, line in enumerate(lines):
            line = line.strip()
            if not line or len(line) < 10:
                continue
                
            # Check if this line looks like a project name with disaster indicators
            has_disaster = any(k in line for k in ['(FEMA Project)', '(CalOES Project)', '(CalJPIA Project)'])
            has_keywords = any(k in line for k in ['FEMA/', 'CalOES', 'disaster', 'fire recovery'])
            
            if has_disaster or has_keywords:
                project_name = line
                
                # Check if 2022 is mentioned in this line or nearby lines (within 3 lines)
                context_window = ' '.join(lines[max(0, i-1):min(len(lines), i+4)])
                if '2022' in context_window:
                    projects.append({
                        'name': project_name,
                        'start_year': '2022',
                        'source': 'civic_doc'
                    })
    
    return projects

# Load data
civic_file = locals()['var_functions.query_db:5']
with open(civic_file, 'r') as f:
    civic_docs = json.load(f)

# Extract disaster projects from 2022
disaster_projects = extract_disaster_projects_2022(civic_docs)

# Load funding data
funding_file = locals()['var_functions.query_db:22']
with open(funding_file, 'r') as f:
    funding_data = json.load(f)

# Also look for disaster projects by checking funding records for disaster indicators
disaster_funding_projects = []
for fund in funding_data:
    proj_name = fund['Project_Name']
    if any(k in proj_name for k in ['(FEMA Project)', '(CalOES Project)', '(CalJPIA Project)', 'FEMA/', 'CalOES']):
        disaster_funding_projects.append(fund)

print('__RESULT__:')
print(json.dumps({
    'civic_disaster_projects': len(disaster_projects),
    'funding_disaster_projects': len(disaster_funding_projects),
    'civic_projects': disaster_projects,
    'sample_funding': disaster_funding_projects[:5]
}))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': [{'Funding_ID': '1', 'Project_Name': '2021 Annual Street Maintenance', 'Funding_Source': 'Public-Private Partnership (PPP)', 'Amount': '24000'}, {'Funding_ID': '2', 'Project_Name': '2022 Annual Street Maintenance', 'Funding_Source': 'Government Grant', 'Amount': '45000'}, {'Funding_ID': '3', 'Project_Name': '2022 Morning View Resurfacing & Storm Drain Improvements', 'Funding_Source': 'State Development Grant', 'Amount': '38000'}, {'Funding_ID': '4', 'Project_Name': 'Annual Street Maintenance', 'Funding_Source': 'Corporate Sponsorship', 'Amount': '23000'}, {'Funding_ID': '5', 'Project_Name': 'Birdview Avenue Improvements', 'Funding_Source': 'National Foundation Fund', 'Amount': '79000'}, {'Funding_ID': '6', 'Project_Name': 'Birdview Avenue Improvements (CalOES Project)', 'Funding_Source': 'International Aid', 'Amount': '85000'}, {'Funding_ID': '7', 'Project_Name': 'Birdview Avenue Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Research Institution Funding', 'Amount': '14000'}, {'Funding_ID': '8', 'Project_Name': 'Bluffs Park Shade Structure', 'Funding_Source': 'Government Grant', 'Amount': '21000'}, {'Funding_ID': '9', 'Project_Name': 'Bluffs Park Workout Station', 'Funding_Source': 'University Research Fund', 'Amount': '39000'}, {'Funding_ID': '10', 'Project_Name': 'Broad Beach Road Water Quality Infrastructure Repairs', 'Funding_Source': 'International Organization Grant', 'Amount': '87000'}], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.execute_python:12': ['var_functions.query_db:0', 'var_functions.query_db:2', 'var_functions.query_db:5', '__builtins__', 'json'], 'var_functions.execute_python:16': {'funding_type': "<class 'list'>", 'civic_type': "<class 'str'>"}, 'var_functions.execute_python:18': {'funding_count': 10, 'civic_is_file_path': 'yes'}, 'var_functions.execute_python:20': {'civic_docs_count': 5, 'funding_count': 10}, 'var_functions.query_db:22': 'file_storage/functions.query_db:22.json', 'var_functions.execute_python:24': {'funding_records': 500, 'civic_documents': 5}}

exec(code, env_args)
