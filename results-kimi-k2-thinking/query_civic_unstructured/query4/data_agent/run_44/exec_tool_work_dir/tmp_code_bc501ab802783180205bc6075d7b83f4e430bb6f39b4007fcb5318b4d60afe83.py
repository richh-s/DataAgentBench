code = """import json

# Load the filtered documents
file_path = locals()['var_functions.query_db:32']
with open(file_path, 'r') as f:
    spring_docs = json.load(f)

project_names = []

for doc in spring_docs:
    text = doc['text']
    lines = text.split('\n')
    
    # Look for Project Schedule and extract preceding lines as project names
    for i in range(len(lines)):
        if 'Project Schedule' in lines[i]:
            # Look backwards for the project name (usually 1-3 lines before)
            for j in range(1, 4):
                if i-j >= 0:
                    candidate = lines[i-j].strip()
                    # Filter out metadata
                    if (candidate and len(candidate) > 5 and 
                        not candidate.startswith('(') and not candidate.startswith('•')):
                        project_names.append(candidate)

# Remove duplicates
unique_projects = list(set(project_names))
final_projects = []

for p in unique_projects:
    # Clean and filter
    cleaned = p.replace('•', '').replace('·', '').strip()
    if (len(cleaned) < 150 and not cleaned.isupper() and 
        'Updates' not in cleaned and 'Schedule' not in cleaned and
        'Page' not in cleaned and 'Agenda' not in cleaned and len(cleaned) > 0):
        final_projects.append(cleaned)

final_projects.sort()

print('Spring 2022 projects: ' + str(len(final_projects)))
print('Projects:')
for proj in final_projects:
    print('  ' + proj)

# Save results
print('__RESULT__:')
print(json.dumps({'count': len(final_projects), 'projects': final_projects}))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:10': [{'Funding_ID': '1', 'Project_Name': '2021 Annual Street Maintenance', 'Funding_Source': 'Public-Private Partnership (PPP)', 'Amount': '24000'}, {'Funding_ID': '2', 'Project_Name': '2022 Annual Street Maintenance', 'Funding_Source': 'Government Grant', 'Amount': '45000'}, {'Funding_ID': '3', 'Project_Name': '2022 Morning View Resurfacing & Storm Drain Improvements', 'Funding_Source': 'State Development Grant', 'Amount': '38000'}, {'Funding_ID': '4', 'Project_Name': 'Annual Street Maintenance', 'Funding_Source': 'Corporate Sponsorship', 'Amount': '23000'}, {'Funding_ID': '5', 'Project_Name': 'Birdview Avenue Improvements', 'Funding_Source': 'National Foundation Fund', 'Amount': '79000'}, {'Funding_ID': '6', 'Project_Name': 'Birdview Avenue Improvements (CalOES Project)', 'Funding_Source': 'International Aid', 'Amount': '85000'}, {'Funding_ID': '7', 'Project_Name': 'Birdview Avenue Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Research Institution Funding', 'Amount': '14000'}, {'Funding_ID': '8', 'Project_Name': 'Bluffs Park Shade Structure', 'Funding_Source': 'Government Grant', 'Amount': '21000'}, {'Funding_ID': '9', 'Project_Name': 'Bluffs Park Workout Station', 'Funding_Source': 'University Research Fund', 'Amount': '39000'}, {'Funding_ID': '10', 'Project_Name': 'Broad Beach Road Water Quality Infrastructure Repairs', 'Funding_Source': 'International Organization Grant', 'Amount': '87000'}], 'var_functions.query_db:18': 'file_storage/functions.query_db:18.json', 'var_functions.execute_python:30': {'doc_count': 5, 'spring_count': 5}, 'var_functions.query_db:32': 'file_storage/functions.query_db:32.json'}

exec(code, env_args)
