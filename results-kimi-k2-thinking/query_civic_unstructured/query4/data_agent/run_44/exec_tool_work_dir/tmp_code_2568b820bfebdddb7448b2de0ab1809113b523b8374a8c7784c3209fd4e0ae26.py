code = """import json
import re

# Read the full result from the file
file_path = locals()['var_functions.query_db:0']
with open(file_path, 'r') as f:
    civic_docs = json.load(f)

print('Total documents: ' + str(len(civic_docs)))

# Function to extract projects from text
def extract_projects_from_text(text):
    projects = []
    lines = text.split('\n')
    
    for i, line in enumerate(lines):
        line = line.strip()
        # Look for project names (lines that look like titles)
        if line and len(line) > 5 and not line.startswith('(') and not line.startswith('•') and not line.startswith('·'):
            # Check if next lines contain schedule info
            if i + 1 < len(lines):
                next_lines = '\n'.join(lines[i+1:i+4])
                if 'Project Schedule' in next_lines or 'Schedule' in next_lines:
                    # Look for date patterns
                    date_patterns = [
                        r'(Spring|Fall|Summer|Winter)\s*2022',
                        r'2022-(Spring|Fall|Summer|Winter)',
                        r'2022-(Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)'
                    ]
                    
                    for pattern in date_patterns:
                        matches = re.findall(pattern, next_lines, re.IGNORECASE)
                        if matches:
                            projects.append({
                                'name': line,
                                'dates': matches
                            })
                            break
    
    return projects

all_projects = []
for doc in civic_docs:
    projects = extract_projects_from_text(doc['text'])
    all_projects.extend(projects)

print('Total projects found: ' + str(len(all_projects)))

# Find projects that started in Spring 2022
spring_2022_projects = []
for p in all_projects:
    # Check if any date indicates Spring 2022
    for date_tuple in p['dates']:
        date_str = ' '.join(date_tuple)
        if '2022' in date_str and 'Spring' in date_str:
            spring_2022_projects.append(p['name'])
            break

print('Spring 2022 projects found: ' + str(len(spring_2022_projects)))
for name in spring_2022_projects[:10]:
    print('  ' + name)

# Save results for next step
print('__RESULT__:')
result = json.dumps({
    'spring_2022_project_names': spring_2022_projects,
    'total_spring_2022': len(spring_2022_projects)
})
print(result)"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:10': [{'Funding_ID': '1', 'Project_Name': '2021 Annual Street Maintenance', 'Funding_Source': 'Public-Private Partnership (PPP)', 'Amount': '24000'}, {'Funding_ID': '2', 'Project_Name': '2022 Annual Street Maintenance', 'Funding_Source': 'Government Grant', 'Amount': '45000'}, {'Funding_ID': '3', 'Project_Name': '2022 Morning View Resurfacing & Storm Drain Improvements', 'Funding_Source': 'State Development Grant', 'Amount': '38000'}, {'Funding_ID': '4', 'Project_Name': 'Annual Street Maintenance', 'Funding_Source': 'Corporate Sponsorship', 'Amount': '23000'}, {'Funding_ID': '5', 'Project_Name': 'Birdview Avenue Improvements', 'Funding_Source': 'National Foundation Fund', 'Amount': '79000'}, {'Funding_ID': '6', 'Project_Name': 'Birdview Avenue Improvements (CalOES Project)', 'Funding_Source': 'International Aid', 'Amount': '85000'}, {'Funding_ID': '7', 'Project_Name': 'Birdview Avenue Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Research Institution Funding', 'Amount': '14000'}, {'Funding_ID': '8', 'Project_Name': 'Bluffs Park Shade Structure', 'Funding_Source': 'Government Grant', 'Amount': '21000'}, {'Funding_ID': '9', 'Project_Name': 'Bluffs Park Workout Station', 'Funding_Source': 'University Research Fund', 'Amount': '39000'}, {'Funding_ID': '10', 'Project_Name': 'Broad Beach Road Water Quality Infrastructure Repairs', 'Funding_Source': 'International Organization Grant', 'Amount': '87000'}]}

exec(code, env_args)
