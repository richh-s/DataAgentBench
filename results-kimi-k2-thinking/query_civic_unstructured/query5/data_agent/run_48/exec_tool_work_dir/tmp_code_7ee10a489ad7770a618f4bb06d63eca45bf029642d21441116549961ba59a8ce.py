code = """import json
import re

# Load data
civic_file = locals()['var_functions.query_db:5']
with open(civic_file, 'r') as f:
    civic_docs = json.load(f)

funding_file = locals()['var_functions.query_db:22']
with open(funding_file, 'r') as f:
    funding_data = json.load(f)

# Extract disaster projects that mention 2022
disaster_projects = []
project_names = set()

for doc in civic_docs:
    text = doc['text']
    lines = text.split('\n')
    
    for i in range(len(lines)):
        line = lines[i].strip()
        if not line or len(line) < 10:
            continue
        
        # Check for disaster project indicators
        has_fema = '(FEMA Project)' in line
        has_calore = '(CalOES Project)' in line or 'CalOES' in line
        has_caljpia = '(CalJPIA Project)' in line
        
        if has_fema or has_calore or has_caljpia:
            # Check for 2022 in this line or next 3 lines
            found_2022 = False
            for j in range(i, min(i+4, len(lines))):
                if '2022' in lines[j]:
                    found_2022 = True
                    break
            
            if found_2022:
                project_names.add(line)
                disaster_projects.append(line)

# Now get funding for these projects
total_funding = 0
funded_projects = []

for fund in funding_data:
    proj_name = fund['Project_Name']
    
    # Check if this matches any of our disaster projects
    for disaster_proj in disaster_projects:
        # Try to match base project name (without parentheticals)
        base_disaster = disaster_proj.split('(')[0].strip()
        base_funding = proj_name.split('(')[0].strip()
        
        if base_disaster == base_funding or base_funding in base_disaster:
            amount = int(fund['Amount'])
            total_funding += amount
            funded_projects.append({
                'project': proj_name,
                'amount': amount
            })
            break

result = {
    'total_disaster_projects': len(disaster_projects),
    'total_funding': total_funding,
    'funded_projects': funded_projects
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': [{'Funding_ID': '1', 'Project_Name': '2021 Annual Street Maintenance', 'Funding_Source': 'Public-Private Partnership (PPP)', 'Amount': '24000'}, {'Funding_ID': '2', 'Project_Name': '2022 Annual Street Maintenance', 'Funding_Source': 'Government Grant', 'Amount': '45000'}, {'Funding_ID': '3', 'Project_Name': '2022 Morning View Resurfacing & Storm Drain Improvements', 'Funding_Source': 'State Development Grant', 'Amount': '38000'}, {'Funding_ID': '4', 'Project_Name': 'Annual Street Maintenance', 'Funding_Source': 'Corporate Sponsorship', 'Amount': '23000'}, {'Funding_ID': '5', 'Project_Name': 'Birdview Avenue Improvements', 'Funding_Source': 'National Foundation Fund', 'Amount': '79000'}, {'Funding_ID': '6', 'Project_Name': 'Birdview Avenue Improvements (CalOES Project)', 'Funding_Source': 'International Aid', 'Amount': '85000'}, {'Funding_ID': '7', 'Project_Name': 'Birdview Avenue Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Research Institution Funding', 'Amount': '14000'}, {'Funding_ID': '8', 'Project_Name': 'Bluffs Park Shade Structure', 'Funding_Source': 'Government Grant', 'Amount': '21000'}, {'Funding_ID': '9', 'Project_Name': 'Bluffs Park Workout Station', 'Funding_Source': 'University Research Fund', 'Amount': '39000'}, {'Funding_ID': '10', 'Project_Name': 'Broad Beach Road Water Quality Infrastructure Repairs', 'Funding_Source': 'International Organization Grant', 'Amount': '87000'}], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.execute_python:12': ['var_functions.query_db:0', 'var_functions.query_db:2', 'var_functions.query_db:5', '__builtins__', 'json'], 'var_functions.execute_python:16': {'funding_type': "<class 'list'>", 'civic_type': "<class 'str'>"}, 'var_functions.execute_python:18': {'funding_count': 10, 'civic_is_file_path': 'yes'}, 'var_functions.execute_python:20': {'civic_docs_count': 5, 'funding_count': 10}, 'var_functions.query_db:22': 'file_storage/functions.query_db:22.json', 'var_functions.execute_python:24': {'funding_records': 500, 'civic_documents': 5}}

exec(code, env_args)
