code = """import json

# Load the Spring 2022 documents file
file_path = locals()['var_functions.query_db:68']
with open(file_path, 'r') as f:
    spring_docs = json.load(f)

spring_2022_start_projects = []

for doc in spring_docs:
    text = doc['text']
    lines = text.split('\n')
    
    # Look for projects with "Begin Construction: Spring 2022" or similar
    for i in range(len(lines)):
        line = lines[i].strip()
        
        # Check if this line indicates construction starts in Spring 2022
        if 'Begin Construction' in line and 'Spring' in line and '2022' in line:
            # Look back to find the project name (usually 1-3 lines before)
            for j in range(1, 5):
                if i-j >= 0:
                    prev_line = lines[i-j].strip()
                    if (prev_line and len(prev_line) > 5 and 
                        not prev_line.startswith('(') and not prev_line.startswith('•') and
                        'Project Schedule' not in prev_line and 'Updates' not in prev_line):
                        project_name = prev_line
                        if project_name not in spring_2022_start_projects:
                            spring_2022_start_projects.append(project_name)
                        break
        
        # Also check for "Begin Construction" followed by "Spring 2022" on same line
        if 'Begin Construction' in line:
            # Check if Spring 2022 is in upcoming lines
            for k in range(0, 3):
                if i+k < len(lines) and 'Spring' in lines[i+k] and '2022' in lines[i+k]:
                    # Look back for project name
                    for j in range(1, 5):
                        if i-j >= 0:
                            prev_line = lines[i-j].strip()
                            if (prev_line and len(prev_line) > 5 and 
                                not prev_line.startswith('(') and not prev_line.startswith('•') and
                                'Project Schedule' not in prev_line and 'Updates' not in prev_line):
                                project_name = prev_line
                                if project_name not in spring_2022_start_projects:
                                    spring_2022_start_projects.append(project_name)
                                break
                    break

# Clean and filter
spring_2022_start_projects_final = []
for name in spring_2022_start_projects:
    clean_name = name.replace('•', '').replace('·', '').strip()
    if (len(clean_name) < 150 and not clean_name.isupper() and 
        'Page' not in clean_name and 'Agenda' not in clean_name and
        len(clean_name) > 0):
        spring_2022_start_projects_final.append(clean_name)

# Remove duplicates
spring_2022_start_projects_final = list(set(spring_2022_start_projects_final))
spring_2022_start_projects_final.sort()

print('Projects starting Spring 2022 construction:')
for proj in spring_2022_start_projects_final:
    print('  ' + proj)

print('Total: ' + str(len(spring_2022_start_projects_final)))

print('__RESULT__:')
print(json.dumps({
    'projects': spring_2022_start_projects_final,
    'count': len(spring_2022_start_projects_final)
}))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:10': [{'Funding_ID': '1', 'Project_Name': '2021 Annual Street Maintenance', 'Funding_Source': 'Public-Private Partnership (PPP)', 'Amount': '24000'}, {'Funding_ID': '2', 'Project_Name': '2022 Annual Street Maintenance', 'Funding_Source': 'Government Grant', 'Amount': '45000'}, {'Funding_ID': '3', 'Project_Name': '2022 Morning View Resurfacing & Storm Drain Improvements', 'Funding_Source': 'State Development Grant', 'Amount': '38000'}, {'Funding_ID': '4', 'Project_Name': 'Annual Street Maintenance', 'Funding_Source': 'Corporate Sponsorship', 'Amount': '23000'}, {'Funding_ID': '5', 'Project_Name': 'Birdview Avenue Improvements', 'Funding_Source': 'National Foundation Fund', 'Amount': '79000'}, {'Funding_ID': '6', 'Project_Name': 'Birdview Avenue Improvements (CalOES Project)', 'Funding_Source': 'International Aid', 'Amount': '85000'}, {'Funding_ID': '7', 'Project_Name': 'Birdview Avenue Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Research Institution Funding', 'Amount': '14000'}, {'Funding_ID': '8', 'Project_Name': 'Bluffs Park Shade Structure', 'Funding_Source': 'Government Grant', 'Amount': '21000'}, {'Funding_ID': '9', 'Project_Name': 'Bluffs Park Workout Station', 'Funding_Source': 'University Research Fund', 'Amount': '39000'}, {'Funding_ID': '10', 'Project_Name': 'Broad Beach Road Water Quality Infrastructure Repairs', 'Funding_Source': 'International Organization Grant', 'Amount': '87000'}], 'var_functions.query_db:18': 'file_storage/functions.query_db:18.json', 'var_functions.execute_python:30': {'doc_count': 5, 'spring_count': 5}, 'var_functions.query_db:32': 'file_storage/functions.query_db:32.json', 'var_functions.query_db:60': 'file_storage/functions.query_db:60.json', 'var_functions.query_db:64': 'file_storage/functions.query_db:64.json', 'var_functions.query_db:68': 'file_storage/functions.query_db:68.json'}

exec(code, env_args)
