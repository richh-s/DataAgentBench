code = """import json
import re

# Read funding data (projects with amount > 50000)
with open('var_functions.query_db:14', 'r') as f:
    funding_records = json.load(f)

# Read civic documents
with open('var_functions.query_db:8', 'r') as f:
    civic_docs = json.load(f)

# Extract project names into a set
funding_projects = set()
for record in funding_records:
    funding_projects.add(record['Project_Name'])

# Function to extract design projects from text
def extract_design_projects(text):
    projects = []
    
    # Find the Design section
    design_header = 'Capital Improvement Projects (Design)'
    construction_header = 'Capital Improvement Projects (Construction)'
    
    design_start = text.find(design_header)
    construction_start = text.find(construction_header)
    
    if design_start >= 0 and construction_start > design_start:
        design_section = text[design_start:construction_start]
        
        # Split into lines and look for project names
        lines = design_section.split('\n')
        in_project_list = False
        
        for line in lines:
            line = line.strip()
            # Skip empty lines and standard phrases
            if (line and len(line) > 15 and not line.startswith('(') and 
                'Capital Improvement Projects (Design)' not in line and
                'Updates:' not in line and 'Project Schedule:' not in line and
                'Estimated Schedule:' not in line and 'Complete Design:' not in line and
                'Advertise:' not in line and 'Begin Construction:' not in line and
                'Final Design:' not in line):
                
                # Check if line starts with capital letter and looks like a project name
                if re.match(r'^[A-Z]', line):
                    # Clean the name
                    clean_name = line.strip()
                    # Remove any trailing special characters
                    clean_name = re.sub(r'[:;\-•*]+$', '', clean_name)
                    if clean_name and len(clean_name) > 10:
                        projects.append(clean_name)
    
    return projects

# Extract all design projects from all documents
all_design_projects = set()
for doc in civic_docs:
    projects = extract_design_projects(doc['text'])
    all_design_projects.update(projects)

# Match funding projects with design projects
capital_design_projects = []
for project_name in funding_projects:
    # Direct match or partial match
    for design_project in all_design_projects:
        if (project_name.lower() in design_project.lower() or 
            design_project.lower() in project_name.lower()):
            capital_design_projects.append(project_name)
            break
        # Check base name without parenthetical suffixes
        base_name = re.sub(r'\s*\([^)]+\)$', '', project_name)
        if base_name and (base_name.lower() in design_project.lower() or 
                          design_project.lower() in base_name.lower()):
            capital_design_projects.append(project_name)
            break

# Filter for capital projects (infrastructure-related)
capital_keywords = ['road', 'street', 'highway', 'bridge', 'park', 'drain', 
                    'culvert', 'walkway', 'traffic', 'signal', 'skate', 'playground',
                    'water', 'storm', 'slope', 'retaining', 'wall', 'seawall', 'path',
                    'crosswalk', 'median', 'drainage']

final_capital_design = []
for project in capital_design_projects:
    project_lower = project.lower()
    if any(keyword in project_lower for keyword in capital_keywords):
        final_capital_design.append(project)

result = {
    'funding_projects_over_50k': len(funding_projects),
    'design_projects_in_docs': len(all_design_projects),
    'matching_projects': len(capital_design_projects),
    'final_capital_design_count': len(final_capital_design),
    'projects': final_capital_design
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': [{'Funding_ID': '1', 'Project_Name': '2021 Annual Street Maintenance', 'Funding_Source': 'Public-Private Partnership (PPP)', 'Amount': '24000'}, {'Funding_ID': '2', 'Project_Name': '2022 Annual Street Maintenance', 'Funding_Source': 'Government Grant', 'Amount': '45000'}, {'Funding_ID': '3', 'Project_Name': '2022 Morning View Resurfacing & Storm Drain Improvements', 'Funding_Source': 'State Development Grant', 'Amount': '38000'}, {'Funding_ID': '4', 'Project_Name': 'Annual Street Maintenance', 'Funding_Source': 'Corporate Sponsorship', 'Amount': '23000'}, {'Funding_ID': '5', 'Project_Name': 'Birdview Avenue Improvements', 'Funding_Source': 'National Foundation Fund', 'Amount': '79000'}], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.list_db:4': ['civic_docs'], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json', 'var_functions.query_db:14': 'file_storage/functions.query_db:14.json'}

exec(code, env_args)
