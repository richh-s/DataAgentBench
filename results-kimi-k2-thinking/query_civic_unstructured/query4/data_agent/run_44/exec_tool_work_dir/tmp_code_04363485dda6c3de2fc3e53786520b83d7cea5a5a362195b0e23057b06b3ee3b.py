code = """import json
import re

# Read the full result from the file
file_path = locals()['var_functions.query_db:18']
with open(file_path, 'r') as f:
    civic_docs = json.load(f)

print('Total documents: ' + str(len(civic_docs)))

# Function to extract projects with Spring 2022 start dates
def extract_spring_2022_projects(text):
    projects = []
    lines = text.split('\n')
    
    i = 0
    while i < len(lines):
        line = lines[i].strip()
        
        # Look for project names - they often appear before "Project Schedule" or "Updates"
        if line and len(line) > 5 and not line.startswith('(') and not line.startswith('•'):
            # Check if this is followed by schedule information
            next_block = '\n'.join(lines[i:i+10])
            
            # Look for Spring 2022 in the schedule
            if 'Spring' in next_block and '2022' in next_block:
                # Check for specific patterns
                spring_pattern = r'(?:Begin|Start|Complete)[^:]*:\s*(?:Spring\s*2022|2022\s*Spring)'
                if re.search(spring_pattern, next_block, re.IGNORECASE):
                    # Get the project name (usually the line itself or previous clean line)
                    project_name = line
                    projects.append(project_name)
            
            # Also check for projects that have "2022" in their name
            if '2022' in line and not line.startswith('-') and not line.startswith('('):
                # This might be a project starting in 2022
                project_name = line
                # Check if Spring is mentioned nearby
                if 'Spring' in next_block:
                    projects.append(project_name)
        
        i += 1
    
    return list(set(projects))  # Remove duplicates

all_spring_2022_projects = []
for doc in civic_docs:
    projects = extract_spring_2022_projects(doc['text'])
    all_spring_2022_projects.extend(projects)

# Remove duplicates
all_spring_2022_projects = list(set(all_spring_2022_projects))

print('Spring 2022 projects found: ' + str(len(all_spring_2022_projects)))
print('Projects:')
for p in all_spring_2022_projects:
    print('  ' + p)

# Save results for next step
print('__RESULT__:')
result = json.dumps({
    'spring_2022_projects': all_spring_2022_projects,
    'count': len(all_spring_2022_projects)
})
print(result)"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:10': [{'Funding_ID': '1', 'Project_Name': '2021 Annual Street Maintenance', 'Funding_Source': 'Public-Private Partnership (PPP)', 'Amount': '24000'}, {'Funding_ID': '2', 'Project_Name': '2022 Annual Street Maintenance', 'Funding_Source': 'Government Grant', 'Amount': '45000'}, {'Funding_ID': '3', 'Project_Name': '2022 Morning View Resurfacing & Storm Drain Improvements', 'Funding_Source': 'State Development Grant', 'Amount': '38000'}, {'Funding_ID': '4', 'Project_Name': 'Annual Street Maintenance', 'Funding_Source': 'Corporate Sponsorship', 'Amount': '23000'}, {'Funding_ID': '5', 'Project_Name': 'Birdview Avenue Improvements', 'Funding_Source': 'National Foundation Fund', 'Amount': '79000'}, {'Funding_ID': '6', 'Project_Name': 'Birdview Avenue Improvements (CalOES Project)', 'Funding_Source': 'International Aid', 'Amount': '85000'}, {'Funding_ID': '7', 'Project_Name': 'Birdview Avenue Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Research Institution Funding', 'Amount': '14000'}, {'Funding_ID': '8', 'Project_Name': 'Bluffs Park Shade Structure', 'Funding_Source': 'Government Grant', 'Amount': '21000'}, {'Funding_ID': '9', 'Project_Name': 'Bluffs Park Workout Station', 'Funding_Source': 'University Research Fund', 'Amount': '39000'}, {'Funding_ID': '10', 'Project_Name': 'Broad Beach Road Water Quality Infrastructure Repairs', 'Funding_Source': 'International Organization Grant', 'Amount': '87000'}], 'var_functions.query_db:18': 'file_storage/functions.query_db:18.json'}

exec(code, env_args)
