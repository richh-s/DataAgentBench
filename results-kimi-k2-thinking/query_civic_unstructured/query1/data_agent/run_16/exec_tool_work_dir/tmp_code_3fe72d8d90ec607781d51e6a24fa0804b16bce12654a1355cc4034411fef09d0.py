code = """import json
import re

# Read funding data (projects with amount > 50000)
with open('var_functions.query_db:14', 'r') as f:
    funding_records = json.load(f)

# Extract project names into a set for easy lookup
funding_projects = set()
for record in funding_records:
    funding_projects.add(record['Project_Name'])

# Read civic documents
with open('var_functions.query_db:8', 'r') as f:
    civic_docs = json.load(f)

# Function to extract project information from civic document text
def extract_projects_from_text(text):
    projects = []
    
    # Look for patterns like "Capital Improvement Projects (Design)" section
    # and extract project names and their status
    
    # Pattern to match project sections
    design_section_pattern = r'Capital Improvement Projects \(Design\)(.*?)(?=Capital Improvement Projects \(Construction\)|Capital Improvement Projects \(Not Started\)|DISASTER RECOVERY PROJECTS|$)'
    
    design_match = re.search(design_section_pattern, text, re.DOTALL | re.IGNORECASE)
    
    if design_match:
        design_section = design_match.group(1)
        
        # Look for project names - typically they appear as bolded or titled items
        # Pattern: project name followed by updates or schedule
        project_patterns = [
            r'\n([A-Z][^\n]+?)(?=\n\s*\(cid:\d+\)|\n\s*Updates:|\n\s*Project Schedule:|\n\s*Estimated Schedule:)',
            r'\n([A-Z][^\n]+?)(?=\n\s*\u2022)',
            r'\n([A-Z][^\n]+?)(?=\n\s*[A-Z][^\n]+?)'
        ]
        
        lines = design_section.split('\n')
        for line in lines:
            line = line.strip()
            # Skip empty lines and common headers
            if (line and not line.startswith('(') and not line.startswith('•') and 
                'Updates:' not in line and 'Project Schedule:' not in line and 
                'Estimated Schedule:' not in line and 'Complete Design:' not in line and
                'Advertise:' not in line and 'Begin Construction:' not in line and
                'Final Design:' not in line and len(line) > 5):
                
                # Check if this looks like a project name (starts with capital letter, not a bullet point)
                if re.match(r'^[A-Z]', line) and not re.match(r'^\d', line):
                    # Clean up the line
                    clean_name = line.strip()
                    # Remove any trailing colons or special characters
                    clean_name = re.sub(r'[:;\-*]+$', '', clean_name)
                    if clean_name and len(clean_name) > 10:  # Assume project names are reasonably long
                        projects.append(clean_name)
    
    return projects

# Extract all design projects from all documents
all_design_projects = set()
for doc in civic_docs:
    projects = extract_projects_from_text(doc['text'])
    all_design_projects.update(projects)

# Now find the intersection: projects that are in both funding_projects and all_design_projects
capital_design_funded = []
for project_name in funding_projects:
    # Check if this project name matches or is similar to any design project
    for design_project in all_design_projects:
        if (project_name in design_project or design_project in project_name or
            project_name.lower() in design_project.lower() or design_project.lower() in project_name.lower()):
            capital_design_funded.append(project_name)
            break
        # Also check for similar names with different suffixes (e.g., FEMA project variants)
        base_name = re.sub(r'\s*\([^)]+\)$', '', project_name)
        if base_name in design_project or design_project in base_name:
            capital_design_funded.append(project_name)
            break

# Also check for projects that contain keywords indicating they're capital projects
capital_keywords = ['road', 'street', 'highway', 'bridge', 'park', 'drain', 'drainage', 
                    'culvert', 'walkway', 'traffic', 'signal', 'skate park', 'playground',
                    'water', 'treatment', 'storm', 'slope', 'retaining wall']

# Filter the results further
final_projects = []
for project in capital_design_funded:
    project_lower = project.lower()
    if any(keyword in project_lower for keyword in capital_keywords) and project in funding_projects:
        final_projects.append(project)

print('__RESULT__:')
print(json.dumps({
    'total_funding_projects': len(funding_projects),
    'design_projects_found': len(all_design_projects),
    'candidate_projects': len(capital_design_funded),
    'final_count': len(final_projects),
    'final_projects': final_projects[:20]  # Show first 20
}))"""

env_args = {'var_functions.query_db:0': [{'Funding_ID': '1', 'Project_Name': '2021 Annual Street Maintenance', 'Funding_Source': 'Public-Private Partnership (PPP)', 'Amount': '24000'}, {'Funding_ID': '2', 'Project_Name': '2022 Annual Street Maintenance', 'Funding_Source': 'Government Grant', 'Amount': '45000'}, {'Funding_ID': '3', 'Project_Name': '2022 Morning View Resurfacing & Storm Drain Improvements', 'Funding_Source': 'State Development Grant', 'Amount': '38000'}, {'Funding_ID': '4', 'Project_Name': 'Annual Street Maintenance', 'Funding_Source': 'Corporate Sponsorship', 'Amount': '23000'}, {'Funding_ID': '5', 'Project_Name': 'Birdview Avenue Improvements', 'Funding_Source': 'National Foundation Fund', 'Amount': '79000'}], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.list_db:4': ['civic_docs'], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json', 'var_functions.query_db:14': 'file_storage/functions.query_db:14.json'}

exec(code, env_args)
