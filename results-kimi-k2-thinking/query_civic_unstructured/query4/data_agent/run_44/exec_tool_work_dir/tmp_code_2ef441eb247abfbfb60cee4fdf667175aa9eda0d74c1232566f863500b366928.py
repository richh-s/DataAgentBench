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
    # Look for project names and schedules
    # Pattern for project names (typically on their own line or followed by updates)
    lines = text.split('\n')
    
    current_project = None
    for i, line in enumerate(lines):
        line = line.strip()
        # Look for project names (lines that look like titles, often followed by project schedule)
        if line and not line.startswith('(') and not line.startswith('•') and not line.startswith('·') and not line.startswith('□'):
            # Check if next lines contain schedule info
            if i + 1 < len(lines):
                next_lines = '\n'.join(lines[i+1:i+4])
                if 'Project Schedule' in next_lines or 'Schedule' in next_lines or 'Complete Design' in next_lines:
                    current_project = line
                    # Look for date patterns
                    date_patterns = [
                        r'(?:Spring|Fall|Summer|Winter)\s*(?:20)?22',
                        r'20(?:20|21|22|23|24|25)\s*(?:Spring|Fall|Summer|Winter)',
                        r'202[0-5]-(?:Spring|Fall|Summer|Winter)',
                        r'(?:Spring|Fall|Summer|Winter)-202[0-5]',
                        r'202[0-5]-(?:Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)',
                        r'202[0-5]-(?:0[1-9]|1[0-2])'
                    ]
                    
                    for pattern in date_patterns:
                        matches = re.findall(pattern, next_lines, re.IGNORECASE)
                        if matches:
                            projects.append({
                                'name': current_project,
                                'dates': matches,
                                'text_snippet': next_lines[:200]
                            })
                            break
    
    return projects

all_projects = []
for doc in civic_docs:
    projects = extract_projects_from_text(doc['text'])
    all_projects.extend(projects)

print('Total projects found: ' + str(len(all_projects)))
print('First few projects:')
for p in all_projects[:5]:
    print('  ' + str(p))

# Find projects that started in Spring 2022
spring_2022_projects = []
for p in all_projects:
    # Check if any date indicates Spring 2022
    for date in p['dates']:
        if ('2022' in date or '22' in date) and 'Spring' in date:
            spring_2022_projects.append(p['name'])
            break

print('\nSpring 2022 projects found: ' + str(len(spring_2022_projects)))
print(spring_2022_projects[:10])

# Save results for next step
print('__RESULT__:')
print(json.dumps({'spring_2022_project_names': spring_2022_projects, 'all_projects': all_projects}))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:10': [{'Funding_ID': '1', 'Project_Name': '2021 Annual Street Maintenance', 'Funding_Source': 'Public-Private Partnership (PPP)', 'Amount': '24000'}, {'Funding_ID': '2', 'Project_Name': '2022 Annual Street Maintenance', 'Funding_Source': 'Government Grant', 'Amount': '45000'}, {'Funding_ID': '3', 'Project_Name': '2022 Morning View Resurfacing & Storm Drain Improvements', 'Funding_Source': 'State Development Grant', 'Amount': '38000'}, {'Funding_ID': '4', 'Project_Name': 'Annual Street Maintenance', 'Funding_Source': 'Corporate Sponsorship', 'Amount': '23000'}, {'Funding_ID': '5', 'Project_Name': 'Birdview Avenue Improvements', 'Funding_Source': 'National Foundation Fund', 'Amount': '79000'}, {'Funding_ID': '6', 'Project_Name': 'Birdview Avenue Improvements (CalOES Project)', 'Funding_Source': 'International Aid', 'Amount': '85000'}, {'Funding_ID': '7', 'Project_Name': 'Birdview Avenue Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Research Institution Funding', 'Amount': '14000'}, {'Funding_ID': '8', 'Project_Name': 'Bluffs Park Shade Structure', 'Funding_Source': 'Government Grant', 'Amount': '21000'}, {'Funding_ID': '9', 'Project_Name': 'Bluffs Park Workout Station', 'Funding_Source': 'University Research Fund', 'Amount': '39000'}, {'Funding_ID': '10', 'Project_Name': 'Broad Beach Road Water Quality Infrastructure Repairs', 'Funding_Source': 'International Organization Grant', 'Amount': '87000'}]}

exec(code, env_args)
