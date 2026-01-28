code = """import json
import re

file_path = locals()['var_functions.query_db:18']
with open(file_path, 'r') as f:
    civic_docs = json.load(f)

print('Total documents: ' + str(len(civic_docs)))

spring_2022_projects = []

for doc in civic_docs:
    text = doc['text']
    # Look for Spring 2022 specifically
    if 'Spring' in text and '2022' in text:
        lines = text.split('\n')
        i = 0
        while i < len(lines):
            line = lines[i].strip()
            # Check if line contains a project name
            if line and len(line) > 5 and not line.startswith('(') and not line.startswith('•'):
                # Look ahead for Spring 2022 mention
                next_block = ' '.join(lines[i:i+8])
                if 'Spring' in next_block and '2022' in next_block:
                    # Clean up the project name
                    project_name = line.strip('•·□-* ')
                    if project_name and project_name not in spring_2022_projects:
                        spring_2022_projects.append(project_name)
            i += 1

print('Spring 2022 projects: ' + str(len(spring_2022_projects)))
for p in spring_2022_projects[:15]:
    print('  ' + p[:80])

print('__RESULT__:')
print(json.dumps({'projects': spring_2022_projects, 'count': len(spring_2022_projects)}))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:10': [{'Funding_ID': '1', 'Project_Name': '2021 Annual Street Maintenance', 'Funding_Source': 'Public-Private Partnership (PPP)', 'Amount': '24000'}, {'Funding_ID': '2', 'Project_Name': '2022 Annual Street Maintenance', 'Funding_Source': 'Government Grant', 'Amount': '45000'}, {'Funding_ID': '3', 'Project_Name': '2022 Morning View Resurfacing & Storm Drain Improvements', 'Funding_Source': 'State Development Grant', 'Amount': '38000'}, {'Funding_ID': '4', 'Project_Name': 'Annual Street Maintenance', 'Funding_Source': 'Corporate Sponsorship', 'Amount': '23000'}, {'Funding_ID': '5', 'Project_Name': 'Birdview Avenue Improvements', 'Funding_Source': 'National Foundation Fund', 'Amount': '79000'}, {'Funding_ID': '6', 'Project_Name': 'Birdview Avenue Improvements (CalOES Project)', 'Funding_Source': 'International Aid', 'Amount': '85000'}, {'Funding_ID': '7', 'Project_Name': 'Birdview Avenue Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Research Institution Funding', 'Amount': '14000'}, {'Funding_ID': '8', 'Project_Name': 'Bluffs Park Shade Structure', 'Funding_Source': 'Government Grant', 'Amount': '21000'}, {'Funding_ID': '9', 'Project_Name': 'Bluffs Park Workout Station', 'Funding_Source': 'University Research Fund', 'Amount': '39000'}, {'Funding_ID': '10', 'Project_Name': 'Broad Beach Road Water Quality Infrastructure Repairs', 'Funding_Source': 'International Organization Grant', 'Amount': '87000'}], 'var_functions.query_db:18': 'file_storage/functions.query_db:18.json'}

exec(code, env_args)
