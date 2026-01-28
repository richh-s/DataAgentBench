code = """import json
import re

# Read the query results from file
with open('var_functions.query_db:6', 'r') as f:
    mongo_results = json.load(f)

print(f"Found {len(mongo_results)} documents matching Spring 2022")

# Extract project information from the text
projects = []

for doc in mongo_results:
    text = doc['text']
    # Look for project sections
    # Pattern to capture projects with Spring 2022 start dates
    
    # Find project names and their schedules
    # Look for patterns like "Project Name" followed by schedule info
    
    # First, let's identify capital projects sections
    capital_design_pattern = r'Capital Improvement Projects \(Design\)(.*?)(?=Capital Improvement Projects \(Construction\)|Disaster Projects|$)'
    capital_design_match = re.search(capital_design_pattern, text, re.DOTALL)
    
    if capital_design_match:
        capital_section = capital_design_match.group(1)
        # Find individual projects in this section
        # Each project seems to be separated by blank lines or has a specific format
        
        # Look for project names (typically at the start of a line, title case)
        project_blocks = re.split(r'\n\s*\n', capital_section.strip())
        
        for block in project_blocks:
            if 'Spring 2022' in block or '2022-Spring' in block:
                # Extract project name (first line that looks like a title)
                lines = block.strip().split('\n')
                project_name = None
                for line in lines:
                    line = line.strip()
                    # Skip empty lines and common prefixes
                    if line and not line.startswith('(') and not line.startswith('•') and not line.startswith('■'):
                        # Check if it looks like a project name (not a date/schedule line)
                        if 'Complete Design' not in line and 'Begin Construction' not in line and 'Advertise' not in line:
                            project_name = line
                            break
                
                if project_name:
                    # Clean up project name
                    project_name = re.sub(r'^[\d\.A-Z]+\s*', '', project_name)  # Remove leading item numbers
                    project_name = project_name.strip()
                    
                    # Check if this project actually starts in Spring 2022
                    if 'Begin Construction: Spring 2022' in block or 'Begin Construction: Spring/Summer 2022' in block:
                        projects.append({
                            'project_name': project_name,
                            'status': 'design',
                            'type': 'capital',
                            'start_time': 'Spring 2022'
                        })
    
    # Check disaster projects section too
    disaster_pattern = r'Disaster Projects \(Design\)(.*?)(?=$)'
    disaster_match = re.search(disaster_pattern, text, re.DOTALL)
    
    if disaster_match:
        disaster_section = disaster_match.group(1)
        if 'Spring 2022' in disaster_section or '2022-Spring' in disaster_section:
            # Extract disaster projects
            disaster_blocks = re.split(r'\n\s*\n', disaster_section.strip())
            
            for block in disaster_blocks:
                if 'Spring 2022' in block or '2022-Spring' in block:
                    lines = block.strip().split('\n')
                    project_name = None
                    for line in lines:
                        line = line.strip()
                        if line and not line.startswith('(') and not line.startswith('•') and not line.startswith('■'):
                            if 'Complete Design' not in line and 'Begin Construction' not in line:
                                project_name = line
                                break
                    
                    if project_name:
                        project_name = re.sub(r'^[\d\.A-Z]+\s*', '', project_name)
                        project_name = project_name.strip()
                        
                        if 'Begin Construction: Spring 2022' in block or 'Begin Construction: Spring/Summer 2022' in block:
                            projects.append({
                                'project_name': project_name,
                                'status': 'design',
                                'type': 'disaster',
                                'start_time': 'Spring 2022'
                            })

# Remove duplicates and clean up
unique_projects = []
seen_names = set()

for proj in projects:
    # Clean project name further
    name = proj['project_name']
    # Remove common suffixes/patterns
    name = re.sub(r'\(.*?\)$', '', name).strip()
    name = re.sub(r'Project$', '', name).strip()
    
    if name and name not in seen_names:
        seen_names.add(name)
        proj['project_name'] = name
        unique_projects.append(proj)

print(f"Extracted {len(unique_projects)} unique projects starting in Spring 2022")
for proj in unique_projects:
    print(f"- {proj['project_name']} ({proj['type']})")

# Save the results
with open('spring_2022_projects.json', 'w') as f:
    json.dump(unique_projects, f, indent=2)"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json'}

exec(code, env_args)
