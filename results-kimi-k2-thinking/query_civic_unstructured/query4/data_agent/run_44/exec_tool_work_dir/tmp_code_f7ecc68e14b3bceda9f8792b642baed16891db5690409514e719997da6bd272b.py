code = """import json

# Load data
file_path = locals()['var_functions.query_db:18']
with open(file_path, 'r') as f:
    civic_docs = json.load(f)

print('Total documents: ' + str(len(civic_docs)))

# Extract projects using simple parsing
spring_2022_projects = []

for doc in civic_docs:
    text = doc['text']
    if 'Spring' in text and '2022' in text:
        lines = text.split('\n')
        for line in lines:
            clean_line = line.strip('•·□-* ')
            if clean_line and len(clean_line) > 5:
                spring_2022_projects.append(clean_line)

# Remove duplicates
spring_2022_projects = list(set(spring_2022_projects))

print('Spring 2022 projects: ' + str(len(spring_2022_projects)))

print('__RESULT__:')
result = json.dumps({'count': len(spring_2022_projects), 'projects': spring_2022_projects[:20]})
print(result)"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:10': [{'Funding_ID': '1', 'Project_Name': '2021 Annual Street Maintenance', 'Funding_Source': 'Public-Private Partnership (PPP)', 'Amount': '24000'}, {'Funding_ID': '2', 'Project_Name': '2022 Annual Street Maintenance', 'Funding_Source': 'Government Grant', 'Amount': '45000'}, {'Funding_ID': '3', 'Project_Name': '2022 Morning View Resurfacing & Storm Drain Improvements', 'Funding_Source': 'State Development Grant', 'Amount': '38000'}, {'Funding_ID': '4', 'Project_Name': 'Annual Street Maintenance', 'Funding_Source': 'Corporate Sponsorship', 'Amount': '23000'}, {'Funding_ID': '5', 'Project_Name': 'Birdview Avenue Improvements', 'Funding_Source': 'National Foundation Fund', 'Amount': '79000'}, {'Funding_ID': '6', 'Project_Name': 'Birdview Avenue Improvements (CalOES Project)', 'Funding_Source': 'International Aid', 'Amount': '85000'}, {'Funding_ID': '7', 'Project_Name': 'Birdview Avenue Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Research Institution Funding', 'Amount': '14000'}, {'Funding_ID': '8', 'Project_Name': 'Bluffs Park Shade Structure', 'Funding_Source': 'Government Grant', 'Amount': '21000'}, {'Funding_ID': '9', 'Project_Name': 'Bluffs Park Workout Station', 'Funding_Source': 'University Research Fund', 'Amount': '39000'}, {'Funding_ID': '10', 'Project_Name': 'Broad Beach Road Water Quality Infrastructure Repairs', 'Funding_Source': 'International Organization Grant', 'Amount': '87000'}], 'var_functions.query_db:18': 'file_storage/functions.query_db:18.json'}

exec(code, env_args)
