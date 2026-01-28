code = """import json
import re

# Load the funding data (projects > $50,000)
funding_file = var_functions.query_db:0
with open(funding_file, 'r') as f:
    funding_data = json.load(f)

# Extract just the project names from funding data
funding_project_names = [record['Project_Name'] for record in funding_data]

# Load the civic documents data
civic_file = var_functions.query_db:5
with open(civic_file, 'r') as f:
    civic_docs = json.load(f)

# Parse civic documents to extract project information
capital_design_projects = []

for doc in civic_docs:
    text = doc.get('text', '')
    
    # Look for capital projects with design status
    # Pattern: capital projects in design section
    
    # Find the "Capital Improvement Projects (Design)" section
    pattern = r'Capital Improvement Projects \(Design\)(.*?)(?=Capital Improvement Projects \(Construction\)|Capital Improvement Projects \(Not Started\)|DISASTER RECOVERY PROJECTS|Disaster Recovery Projects|$)'
    design_section_match = re.search(pattern, text, re.DOTALL | re.IGNORECASE)
    
    if design_section_match:
        design_section = design_section_match.group(1)
        
        # Extract project names from this section
        lines = design_section.split('\n')
        for line in lines:
            line = line.strip()
            # Skip empty lines and common headers
            if not line or line.startswith('(') or line.startswith('cid:'):
                continue
            
            # Look for lines that appear to be project names (not status updates)
            skip_words = ['Updates:', 'Schedule:', 'Advertise:', 'Begin', 'Complete', 'Project', 'RECOMMENDED', 'DISCUSSION:', 'To:', 'Prepared', 'Approved', 'Date', 'Meeting', 'Subject:', 'Agenda', 'Item', 'Page', 'Complete Design:', 'Final Design:', 'Estimated Schedule:']
            if any(line.startswith(word) for word in skip_words):
                continue
                
            # Check if it's likely a project name
            if len(line) > 10:
                # Skip status lines
                if any(keyword in line.lower() for keyword in ['updates:', 'schedule:', 'advertise:', 'begin', 'complete:', 'project is', 'staff is', 'city is', 'this project']):
                    continue
                
                # Clean and add project name
                project_name = line.strip()
                if project_name and project_name not in capital_design_projects:
                    capital_design_projects.append(project_name)

# Find matches between design projects and funded projects > $50,000
matched_projects = []

for design_project in capital_design_projects:
    # Clean the design project name for matching (remove parenthetical suffixes)
    clean_design = re.sub(r'\s*\([^)]+\)$', '', design_project).strip()
    
    for funding_project in funding_project_names:
        # Clean the funding project name too
        clean_funding = re.sub(r'\s*\([^)]+\)$', '', funding_project).strip()
        
        # Check for matches
        if (design_project == funding_project or
            clean_design == clean_funding or
            design_project in funding_project or
            funding_project in design_project or
            clean_design in clean_funding or
            clean_funding in clean_design):
            if design_project not in matched_projects:
                matched_projects.append(design_project)

# Print result in required format
result = {
    'count': len(matched_projects),
    'matched_projects': matched_projects
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.list_db:2': ['civic_docs'], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json'}

exec(code, env_args)
