code = """import json

# Load the spring 2022 documents
file_path = locals()['var_functions.query_db:32']
with open(file_path, 'r') as f:
    spring_docs = json.load(f)

# Process to find projects
project_count = 0
project_list = []

for doc in spring_docs:
    text = doc['text']
    lines = text.split('\n')
    
    # Look for project names (lines before 'Project Schedule')
    for i in range(len(lines)):
        line = lines[i].strip()
        if line and len(line) > 5:
            # Check if next line or nearby lines mention 'Project Schedule'
            has_schedule = False
            for j in range(1, 4):
                if i+j < len(lines) and 'Project Schedule' in lines[i+j]:
                    has_schedule = True
                    break
            
            if has_schedule:
                # Clean up the project name
                clean_name = line.replace('•', '').replace('·', '').strip()
                # Apply filters
                if (len(clean_name) < 150 and not clean_name.isupper() and 
                    'Updates' not in clean_name and 
                    'Schedule' not in clean_name and len(clean_name) > 0):
                    project_list.append(clean_name)
                    project_count += 1

# Remove duplicates
unique_projects = list(set(project_list))

print('Total Spring 2022 projects: ' + str(len(unique_projects)))

# Prepare JSON output
output = {'count': len(unique_projects), 'projects': unique_projects}
final_output = json.dumps(output)
print('__RESULT__:')
print(final_output)"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:10': [{'Funding_ID': '1', 'Project_Name': '2021 Annual Street Maintenance', 'Funding_Source': 'Public-Private Partnership (PPP)', 'Amount': '24000'}, {'Funding_ID': '2', 'Project_Name': '2022 Annual Street Maintenance', 'Funding_Source': 'Government Grant', 'Amount': '45000'}, {'Funding_ID': '3', 'Project_Name': '2022 Morning View Resurfacing & Storm Drain Improvements', 'Funding_Source': 'State Development Grant', 'Amount': '38000'}, {'Funding_ID': '4', 'Project_Name': 'Annual Street Maintenance', 'Funding_Source': 'Corporate Sponsorship', 'Amount': '23000'}, {'Funding_ID': '5', 'Project_Name': 'Birdview Avenue Improvements', 'Funding_Source': 'National Foundation Fund', 'Amount': '79000'}, {'Funding_ID': '6', 'Project_Name': 'Birdview Avenue Improvements (CalOES Project)', 'Funding_Source': 'International Aid', 'Amount': '85000'}, {'Funding_ID': '7', 'Project_Name': 'Birdview Avenue Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Research Institution Funding', 'Amount': '14000'}, {'Funding_ID': '8', 'Project_Name': 'Bluffs Park Shade Structure', 'Funding_Source': 'Government Grant', 'Amount': '21000'}, {'Funding_ID': '9', 'Project_Name': 'Bluffs Park Workout Station', 'Funding_Source': 'University Research Fund', 'Amount': '39000'}, {'Funding_ID': '10', 'Project_Name': 'Broad Beach Road Water Quality Infrastructure Repairs', 'Funding_Source': 'International Organization Grant', 'Amount': '87000'}], 'var_functions.query_db:18': 'file_storage/functions.query_db:18.json', 'var_functions.execute_python:30': {'doc_count': 5, 'spring_count': 5}, 'var_functions.query_db:32': 'file_storage/functions.query_db:32.json'}

exec(code, env_args)
