code = """import json
import re

# Read the civic documents from the file
file_path = var_functions.query_db:12
with open(file_path, 'r') as f:
    civic_docs = json.load(f)

print(f"Number of documents: {len(civic_docs)}")

# Extract disaster projects with start dates in 2022
disaster_projects_2022 = []

for doc in civic_docs:
    text = doc.get('text', '')
    
    # Look for disaster recovery projects section
    # Common patterns for project names and dates
    lines = text.split('\n')
    
    current_project = None
    project_type = None
    start_date = None
    
    for line in lines:
        line = line.strip()
        
        # Look for project headers (usually bold or with special characters)
        if line and not line.startswith('(') and not line.startswith('•') and len(line) > 10:
            # Check if it looks like a project name
            if any(keyword in line.lower() for keyword in ['project', 'repair', 'improvement', 'replacement']):
                # Look for disaster indicators
                if any(indicator in line.lower() for indicator in ['fema', 'disaster', 'caloes', 'caljpia', 'recovery']):
                    current_project = line
                    project_type = 'disaster'
                elif current_project:  # Reset if we hit a non-disaster project
                    current_project = None
                    project_type = None
                    start_date = None
        
        # Look for start dates in 2022
        if current_project and project_type == 'disaster':
            if '2022' in line or '2022-' in line or '2022 ' in line:
                # Check if this line contains scheduling info
                if any(schedule_word in line.lower() for schedule_word in ['schedule', 'start', 'begin', 'advertise', 'design']):
                    start_date = line
                    
                    # Record the project
                    disaster_projects_2022.append({
                        'Project_Name': current_project,
                        'type': project_type,
                        'st': line
                    })
                    
                    print(f"Found disaster project: {current_project}")
                    print(f"Date info: {line}")
                    print("---")

print(f"\nTotal disaster projects with 2022 dates: {len(disaster_projects_2022)}")

# Also try a more aggressive pattern matching approach
print("\nTrying pattern matching approach...")

# Pattern to match project names (usually followed by "Project" or similar)
project_pattern = r'([A-Z][^.!?]*?(?:Project|Repair|Improvement|Replacement))'

# Look for FEMA/Disaster projects explicitly
disaster_indicators = ['FEMA', 'CalOES', 'CalJPIA', 'disaster', 'recovery', 'fire']

for doc in civic_docs:
    text = doc.get('text', '')
    
    # Find sections mentioning disaster/FEMA
    for indicator in disaster_indicators:
        if indicator.lower() in text.lower():
            # Look around the indicator for project names
            sections = text.split(indicator)
            for i, section in enumerate(sections[1:], 1):
                # Look backwards for a project name
                prev_section = sections[i-1]
                
                # Find project names in the previous section
                matches = re.findall(project_pattern, prev_section, re.IGNORECASE)
                if matches:
                    project_name = matches[-1]  # Last match is usually closest
                    
                    # Check if this section mentions 2022
                    if '2022' in section[:500]:  # Look in next 500 chars
                        disaster_projects_2022.append({
                            'Project_Name': project_name.strip(),
                            'type': 'disaster',
                            'st': f'2022 (near {indicator})',
                            'source': f'Found near {indicator}'
                        })
                        print(f"Pattern match: {project_name.strip()}")

# Remove duplicates based on project name
unique_projects = {}
for proj in disaster_projects_2022:
    name = proj['Project_Name']
    if name not in unique_projects:
        unique_projects[name] = proj

disaster_projects_unique = list(unique_projects.values())

print(f"\nUnique disaster projects: {len(disaster_projects_unique)}")
for proj in disaster_projects_unique:
    print(f"- {proj['Project_Name']}")

result = disaster_projects_unique
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:4': [], 'var_functions.query_db:6': [{'Funding_ID': '1', 'Project_Name': '2021 Annual Street Maintenance', 'Funding_Source': 'Public-Private Partnership (PPP)', 'Amount': '24000'}, {'Funding_ID': '2', 'Project_Name': '2022 Annual Street Maintenance', 'Funding_Source': 'Government Grant', 'Amount': '45000'}, {'Funding_ID': '3', 'Project_Name': '2022 Morning View Resurfacing & Storm Drain Improvements', 'Funding_Source': 'State Development Grant', 'Amount': '38000'}, {'Funding_ID': '4', 'Project_Name': 'Annual Street Maintenance', 'Funding_Source': 'Corporate Sponsorship', 'Amount': '23000'}, {'Funding_ID': '5', 'Project_Name': 'Birdview Avenue Improvements', 'Funding_Source': 'National Foundation Fund', 'Amount': '79000'}], 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json', 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json'}

exec(code, env_args)
