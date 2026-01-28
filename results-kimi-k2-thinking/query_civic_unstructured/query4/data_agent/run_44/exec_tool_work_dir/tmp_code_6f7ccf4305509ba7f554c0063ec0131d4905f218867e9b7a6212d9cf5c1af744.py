code = """import json

# Load the filtered documents
file_path = locals()['var_functions.query_db:32']
with open(file_path, 'r') as f:
    spring_docs = json.load(f)

print('Total docs with Spring 2022 references: ' + str(len(spring_docs)))

# Extract project names - look for patterns before "Project Schedule" or similar
spring_2022_projects = []

for doc in spring_docs:
    text = doc['text']
    lines = text.split('\n')
    
    # Look for project names followed by schedule info containing Spring 2022
    for i, line in enumerate(lines):
        line = line.strip()
        # Skip empty or very short lines, and lines that start with special chars
        if (line and len(line) > 5 and not line.startswith('(') and 
            not line.startswith('•') and not line.startswith('□') and 
            not line.startswith('-') and not line.startswith('\x95')):
            
            # Look ahead for schedule information
            if i + 1 < len(lines):
                next_block = '\n'.join(lines[i:i+12])
                
                # Check if this block mentions both Spring and 2022
                if ('Spring' in next_block and '2022' in next_block):
                    # Clean up the project name
                    project_name = line.strip('•·□-* ').strip()
                    
                    # Filter out non-project-name lines
                    if (project_name and 'Updates' not in project_name and 
                        'Project Schedule' not in project_name and
                        not project_name.isupper() and  # Skip ALL CAPS lines
                        len(project_name) < 150):
                        spring_2022_projects.append(project_name)

# Remove duplicates
spring_2022_projects = list(set(spring_2022_projects))

print('\nSpring 2022 Projects found: ' + str(len(spring_2022_projects)))
for proj in sorted(spring_2022_projects):
    print('  - ' + proj)

# Save results for funding lookup
print('__RESULT__:')
print(json.dumps({
    'projects': spring_2022_projects,
    'count': len(spring_2022_projects)
}))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:10': [{'Funding_ID': '1', 'Project_Name': '2021 Annual Street Maintenance', 'Funding_Source': 'Public-Private Partnership (PPP)', 'Amount': '24000'}, {'Funding_ID': '2', 'Project_Name': '2022 Annual Street Maintenance', 'Funding_Source': 'Government Grant', 'Amount': '45000'}, {'Funding_ID': '3', 'Project_Name': '2022 Morning View Resurfacing & Storm Drain Improvements', 'Funding_Source': 'State Development Grant', 'Amount': '38000'}, {'Funding_ID': '4', 'Project_Name': 'Annual Street Maintenance', 'Funding_Source': 'Corporate Sponsorship', 'Amount': '23000'}, {'Funding_ID': '5', 'Project_Name': 'Birdview Avenue Improvements', 'Funding_Source': 'National Foundation Fund', 'Amount': '79000'}, {'Funding_ID': '6', 'Project_Name': 'Birdview Avenue Improvements (CalOES Project)', 'Funding_Source': 'International Aid', 'Amount': '85000'}, {'Funding_ID': '7', 'Project_Name': 'Birdview Avenue Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Research Institution Funding', 'Amount': '14000'}, {'Funding_ID': '8', 'Project_Name': 'Bluffs Park Shade Structure', 'Funding_Source': 'Government Grant', 'Amount': '21000'}, {'Funding_ID': '9', 'Project_Name': 'Bluffs Park Workout Station', 'Funding_Source': 'University Research Fund', 'Amount': '39000'}, {'Funding_ID': '10', 'Project_Name': 'Broad Beach Road Water Quality Infrastructure Repairs', 'Funding_Source': 'International Organization Grant', 'Amount': '87000'}], 'var_functions.query_db:18': 'file_storage/functions.query_db:18.json', 'var_functions.execute_python:30': {'doc_count': 5, 'spring_count': 5}, 'var_functions.query_db:32': 'file_storage/functions.query_db:32.json'}

exec(code, env_args)
