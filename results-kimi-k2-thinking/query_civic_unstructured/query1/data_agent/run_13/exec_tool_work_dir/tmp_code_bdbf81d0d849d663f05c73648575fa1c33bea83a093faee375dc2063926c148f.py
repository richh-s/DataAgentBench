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
    design_section_match = re.search(r'Capital Improvement Projects \(Design\)(.*?)(?=Capital Improvement Projects \(Construction\)|Capital Improvement Projects \(Not Started\)|DISASTER RECOVERY PROJECTS|Disaster Recovery Projects|$)', 
                                      text, re.DOTALL | re.IGNORECASE)
    
    if design_section_match:
        design_section = design_section_match.group(1)
        
        # Extract project names from this section
        # Look for project names that are preceded by bullet points or similar
        # Pattern: project names on lines after bullet points or similar markers
        
        # Split by lines and look for project names
        lines = design_section.split('\n')
        for i, line in enumerate(lines):
            line = line.strip()
            # Skip empty lines and common headers
            if not line or line.startswith('(') or line.startswith('cid:'):
                continue
            
            # Look for lines that appear to be project names (not status updates)
            # Project names typically don't start with these keywords
            if not any(line.startswith(word) for word in ['Updates:', 'Schedule:', 'Advertise:', 'Begin', 'Complete', 'Project', 'RECOMMENDED', 'DISCUSSION:', 'To:', 'Prepared', 'Approved', 'Date', 'Meeting', 'Subject:', 'Agenda', 'Item', 'Page']):
                # Check if it's likely a project name (not too short, not a date/status line)
                if len(line) > 10 and not re.match(r'^\d{4}-', line) and not re.match(r'^[A-Z][a-z]+ \d{4}$', line):
                    # Clean up the project name
                    project_name = line.strip()
                    
                    # Skip if it's a status line or update
                    if any(keyword in project_name.lower() for keyword in ['updates:', 'schedule:', 'advertise:', 'begin', 'complete:', 'project is', 'staff is', 'city is', 'this project']):
                        continue
                    
                    # Add if not already in list
                    if project_name and project_name not in capital_design_projects:
                        capital_design_projects.append(project_name)

# Now match with funding projects > $50,000
# We need to do fuzzy matching since names might not match exactly

matched_projects = []

for design_project in capital_design_projects:
    # Direct match
    if design_project in funding_project_names:
        matched_projects.append(design_project)
    else:
        # Try to find partial matches
        for funding_project in funding_project_names:
            # Check if one contains the other
            if (design_project in funding_project or 
                funding_project in design_project or
                # Check for similar names (remove suffixes like (FEMA Project) etc.)
                re.sub(r'\s*\([^)]+\)$', '', design_project) == re.sub(r'\s*\([^)]+\)$', '', funding_project)):
                matched_projects.append(design_project)
                break

# Count unique matches
unique_matches = list(set(matched_projects))

# Print result in required format
print('__RESULT__:')
print(json.dumps({
    'count': len(unique_matches),
    'matched_projects': unique_matches
}))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.list_db:2': ['civic_docs'], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json'}

exec(code, env_args)
