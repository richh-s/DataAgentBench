code = """import json

# Access the file path
file_path = globals()['var_functions.query_db:2']
print('File path:', file_path)

# Read the file content
with open(file_path, 'r', encoding='utf-8') as f:
    civic_docs = json.load(f)

print('Total documents loaded:', len(civic_docs))

# Check documents that mention 2022
projects = []
for doc in civic_docs:
    text = doc.get('text', '')
    if '2022' in text:
        # Look for lines containing project names
        lines = text.split('\n')
        for line in lines:
            line = line.strip()
            if line and 'Project' in line:
                # Check if this looks like a project name by checking uppercase ratio
                upper_count = sum(1 for c in line if c.isupper())
                total_alpha = len([c for c in line if c.isalpha()])
                if total_alpha > 0 and upper_count / total_alpha > 0.2:
                    # Check if Spring 2022 appears near this project
                    # By checking nearby lines
                    idx = lines.index(line)
                    start = max(0, idx-5)
                    end = min(len(lines), idx+6)
                    context = ' '.join([l.strip() for l in lines[start:end]])
                    
                    if '2022-Spring' in context or '2022-March' in context or '2022-April' in context or '2022-May' in context:
                        projects.append({
                            'project_name': line[:200],
                            'context': context[:300]
                        })

unique_projects = []
project_names = set()
for proj in projects:
    if proj['project_name'] not in project_names:
        project_names.add(proj['project_name'])
        unique_projects.append(proj)

print('Projects starting in Spring 2022:', len(unique_projects))

result = {
    'spring_2022_count': len(unique_projects),
    'projects': unique_projects
}

print('__RESULT__:')
print(json.dumps(result, default=str))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:46': [{'Funding_ID': '1', 'Project_Name': '2021 Annual Street Maintenance', 'Funding_Source': 'Public-Private Partnership (PPP)', 'Amount': '24000'}, {'Funding_ID': '2', 'Project_Name': '2022 Annual Street Maintenance', 'Funding_Source': 'Government Grant', 'Amount': '45000'}, {'Funding_ID': '3', 'Project_Name': '2022 Morning View Resurfacing & Storm Drain Improvements', 'Funding_Source': 'State Development Grant', 'Amount': '38000'}, {'Funding_ID': '4', 'Project_Name': 'Annual Street Maintenance', 'Funding_Source': 'Corporate Sponsorship', 'Amount': '23000'}, {'Funding_ID': '5', 'Project_Name': 'Birdview Avenue Improvements', 'Funding_Source': 'National Foundation Fund', 'Amount': '79000'}, {'Funding_ID': '6', 'Project_Name': 'Birdview Avenue Improvements (CalOES Project)', 'Funding_Source': 'International Aid', 'Amount': '85000'}, {'Funding_ID': '7', 'Project_Name': 'Birdview Avenue Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Research Institution Funding', 'Amount': '14000'}, {'Funding_ID': '8', 'Project_Name': 'Bluffs Park Shade Structure', 'Funding_Source': 'Government Grant', 'Amount': '21000'}, {'Funding_ID': '9', 'Project_Name': 'Bluffs Park Workout Station', 'Funding_Source': 'University Research Fund', 'Amount': '39000'}, {'Funding_ID': '10', 'Project_Name': 'Broad Beach Road Water Quality Infrastructure Repairs', 'Funding_Source': 'International Organization Grant', 'Amount': '87000'}], 'var_functions.query_db:48': 'file_storage/functions.query_db:48.json', 'var_functions.execute_python:53': {'count': 0, 'projects': []}}

exec(code, env_args)
