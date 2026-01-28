code = """import json
import re

# Load the data
civic_file = locals()['var_functions.query_db:5']
with open(civic_file, 'r') as f:
    civic_docs = json.load(f)

funding_file = locals()['var_functions.query_db:22']
with open(funding_file, 'r') as f:
    funding_data = json.load(f)

# Extract disaster projects that started in 2022
disaster_projects_2022 = []

for doc in civic_docs:
    text = doc['text']
    lines = text.split('\n')
    
    for i, line in enumerate(lines):
        line = line.strip()
        
        if not line:
            continue
            
        # Check if this is a disaster-related project name
        has_disaster_keywords = any(k in line for k in ['FEMA', 'CalOES', 'CalJPIA'])
        has_project_keywords = any(k in line for k in ['Project', 'Improvements', 'Repairs', 'Replacement'])
        
        if has_disaster_keywords and has_project_keywords and len(line) > 10:
            project_info = {
                'name': line,
                'type': 'disaster'
            }
            
            # Look for date information in surrounding lines (next 5 lines)
            date_found = False
            for j in range(i, min(i+5, len(lines))):
                check_line = lines[j]
                if '2022' in check_line and ('Complete' in check_line or 'Design' in check_line or 'Begin' in check_line):
                    project_info['start_date'] = '2022'
                    date_found = True
                    break
            
            if date_found or '2022' in line:
                project_info['start_date'] = '2022'
                
            if project_info.get('start_date') == '2022':
                disaster_projects_2022.append(project_info)

print('__RESULT__:')
print(json.dumps({
    'disaster_projects_2022': disaster_projects_2022,
    'count': len(disaster_projects_2022)
}))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': [{'Funding_ID': '1', 'Project_Name': '2021 Annual Street Maintenance', 'Funding_Source': 'Public-Private Partnership (PPP)', 'Amount': '24000'}, {'Funding_ID': '2', 'Project_Name': '2022 Annual Street Maintenance', 'Funding_Source': 'Government Grant', 'Amount': '45000'}, {'Funding_ID': '3', 'Project_Name': '2022 Morning View Resurfacing & Storm Drain Improvements', 'Funding_Source': 'State Development Grant', 'Amount': '38000'}, {'Funding_ID': '4', 'Project_Name': 'Annual Street Maintenance', 'Funding_Source': 'Corporate Sponsorship', 'Amount': '23000'}, {'Funding_ID': '5', 'Project_Name': 'Birdview Avenue Improvements', 'Funding_Source': 'National Foundation Fund', 'Amount': '79000'}, {'Funding_ID': '6', 'Project_Name': 'Birdview Avenue Improvements (CalOES Project)', 'Funding_Source': 'International Aid', 'Amount': '85000'}, {'Funding_ID': '7', 'Project_Name': 'Birdview Avenue Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Research Institution Funding', 'Amount': '14000'}, {'Funding_ID': '8', 'Project_Name': 'Bluffs Park Shade Structure', 'Funding_Source': 'Government Grant', 'Amount': '21000'}, {'Funding_ID': '9', 'Project_Name': 'Bluffs Park Workout Station', 'Funding_Source': 'University Research Fund', 'Amount': '39000'}, {'Funding_ID': '10', 'Project_Name': 'Broad Beach Road Water Quality Infrastructure Repairs', 'Funding_Source': 'International Organization Grant', 'Amount': '87000'}], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.execute_python:12': ['var_functions.query_db:0', 'var_functions.query_db:2', 'var_functions.query_db:5', '__builtins__', 'json'], 'var_functions.execute_python:16': {'funding_type': "<class 'list'>", 'civic_type': "<class 'str'>"}, 'var_functions.execute_python:18': {'funding_count': 10, 'civic_is_file_path': 'yes'}, 'var_functions.execute_python:20': {'civic_docs_count': 5, 'funding_count': 10}, 'var_functions.query_db:22': 'file_storage/functions.query_db:22.json', 'var_functions.execute_python:24': {'funding_records': 500, 'civic_documents': 5}}

exec(code, env_args)
