code = """import json
import re

# Load funding data
with open(var_functions.query_db:0, 'r') as f:
    funding_data = json.load(f)

# Load civic documents data
with open(var_functions.query_db:1, 'r') as f:
    civic_docs_data = json.load(f)

# Create a dictionary of funding data for easy lookup
funding_dict = {item['Project_Name']: int(item['Amount']) for item in funding_data}

# Parse civic documents to extract project information
projects = []

for doc in civic_docs_data:
    text = doc.get('text', '')
    
    # Look for capital projects with design status
    # Pattern to find sections with capital projects in design phase
    design_section_pattern = r'Capital Improvement Projects \(Design\)(.*?)\n\n'
    design_sections = re.findall(design_section_pattern, text, re.DOTALL)
    
    if design_sections:
        design_text = design_sections[0]
        
        # Extract project names - they typically appear as:
        # Project Name
        # (cid:190) Updates:
        project_pattern = r'([A-Z][^\n]+?)\n\s*\(cid:190\) Updates:'
        project_names = re.findall(project_pattern, design_text)
        
        for project_name in project_names:
            project_name = project_name.strip()
            # Check if this project has funding > 50000
            if project_name in funding_dict and funding_dict[project_name] > 50000:
                projects.append({
                    'Project_Name': project_name,
                    'type': 'capital',
                    'status': 'design',
                    'Amount': funding_dict[project_name]
                })

# Also need to check for projects that might have variations in name
# Let's also look for projects in the text and match them to funding
for doc in civic_docs_data:
    text = doc.get('text', '')
    
    # Look for design status indicators
    if "design" in text.lower() or "Design" in text:
        # Check each funded project to see if it's mentioned in this doc
        for project_name, amount in funding_dict.items():
            if amount > 50000 and project_name in text:
                # Check if it's a capital project
                if "Capital Improvement" in text:
                    # Check if status is design (look for context)
                    # This is a heuristic - if project name appears near "design" or in design section
                    projects.append({
                        'Project_Name': project_name,
                        'type': 'capital',
                        'status': 'design',
                        'Amount': amount
                    })

# Remove duplicates
duplicates_removed = []
seen_projects = set()
for proj in projects:
    if proj['Project_Name'] not in seen_projects:
        duplicates_removed.append(proj)
        seen_projects.add(proj['Project_Name'])

# Count the projects
count = len(duplicates_removed)

# For debugging, let's also see which projects we found
found_projects = [proj['Project_Name'] for proj in duplicates_removed]

result_str = json.dumps({
    'count': count,
    'projects': found_projects
})

print('__RESULT__:')
print(result_str)"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:1': 'file_storage/functions.query_db:1.json'}

exec(code, env_args)
