code = """import json

# Load documents with Spring 2022 references
file_path = locals()['var_functions.query_db:32']
with open(file_path, 'r') as f:
    spring_docs = json.load(f)

print('Total Spring 2022 documents: ' + str(len(spring_docs)))

# Extract project information more systematically
spring_2022_projects = []

for doc in spring_docs:
    text = doc['text']
    lines = text.split('\n')
    
    # Look for patterns indicating project names
    for i in range(len(lines)):
        line = lines[i].strip()
        if not line or len(line) < 5:
            continue
        
        # Skip metadata lines
        if line.startswith('(') or line.startswith('•') or line.startswith('□'):
            continue
        if line in ['Capital Improvement Projects (Design)', 
                   'Capital Improvement Projects (Construction)',
                   'Capital Improvement Projects (Not Started)',
                   'Disaster Projects (Design)',
                   'Disaster Projects (Construction)',
                   'Disaster Projects (Not Started)']:
            continue
            
        # Look ahead for Spring 2022 in schedule
        if i + 8 < len(lines):
            upcoming = ' '.join(lines[i:i+8])
            if 'Spring' in upcoming and '2022' in upcoming:
                clean_name = line
                spring_2022_projects.append(clean_name)

# Remove duplicates and clean up
unique_projects = list(set(spring_2022_projects))
# Filter out obvious non-project lines
filtered_projects = []
for p in unique_projects:
    if (len(p) < 150 and not p.isupper() and 
        'Updates' not in p and 'Schedule' not in p and
        'Page' not in p and 'Agenda' not in p):
        filtered_projects.append(p)

sorted_projects = sorted(filtered_projects)

print('\nFiltered Spring 2022 projects: ' + str(len(sorted_projects)))

# Show the projects for verification
for proj in sorted_projects:
    print('  ' + proj)

# Store the project list
result = {'count': len(sorted_projects), 'projects': sorted_projects}
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:10': [{'Funding_ID': '1', 'Project_Name': '2021 Annual Street Maintenance', 'Funding_Source': 'Public-Private Partnership (PPP)', 'Amount': '24000'}, {'Funding_ID': '2', 'Project_Name': '2022 Annual Street Maintenance', 'Funding_Source': 'Government Grant', 'Amount': '45000'}, {'Funding_ID': '3', 'Project_Name': '2022 Morning View Resurfacing & Storm Drain Improvements', 'Funding_Source': 'State Development Grant', 'Amount': '38000'}, {'Funding_ID': '4', 'Project_Name': 'Annual Street Maintenance', 'Funding_Source': 'Corporate Sponsorship', 'Amount': '23000'}, {'Funding_ID': '5', 'Project_Name': 'Birdview Avenue Improvements', 'Funding_Source': 'National Foundation Fund', 'Amount': '79000'}, {'Funding_ID': '6', 'Project_Name': 'Birdview Avenue Improvements (CalOES Project)', 'Funding_Source': 'International Aid', 'Amount': '85000'}, {'Funding_ID': '7', 'Project_Name': 'Birdview Avenue Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Research Institution Funding', 'Amount': '14000'}, {'Funding_ID': '8', 'Project_Name': 'Bluffs Park Shade Structure', 'Funding_Source': 'Government Grant', 'Amount': '21000'}, {'Funding_ID': '9', 'Project_Name': 'Bluffs Park Workout Station', 'Funding_Source': 'University Research Fund', 'Amount': '39000'}, {'Funding_ID': '10', 'Project_Name': 'Broad Beach Road Water Quality Infrastructure Repairs', 'Funding_Source': 'International Organization Grant', 'Amount': '87000'}], 'var_functions.query_db:18': 'file_storage/functions.query_db:18.json', 'var_functions.execute_python:30': {'doc_count': 5, 'spring_count': 5}, 'var_functions.query_db:32': 'file_storage/functions.query_db:32.json'}

exec(code, env_args)
