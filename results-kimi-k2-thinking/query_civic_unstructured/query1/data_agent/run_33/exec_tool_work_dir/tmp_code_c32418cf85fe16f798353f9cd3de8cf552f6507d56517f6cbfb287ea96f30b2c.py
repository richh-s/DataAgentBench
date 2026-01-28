code = """import json
import re

# Read funding data from the file
funding_file = var_functions.query_db:8
with open(funding_file, 'r') as f:
    funding_data = json.load(f)

# Read civic documents data from the file
civic_file = var_functions.query_db:10
with open(civic_file, 'r') as f:
    civic_docs_data = json.load(f)

print(f'Loaded {len(funding_data)} funding records')
print(f'Loaded {len(civic_docs_data)} civic documents')

# Create a list of project names from funding data for quick lookup
funding_project_names = [item['Project_Name'] for item in funding_data]

# Debug: Show first few project names
print('Sample funding project names:', funding_project_names[:5])

# Extract project information from civic documents
projects_info = []

for doc in civic_docs_data:
    text = doc.get('text', '')
    
    # Look for project patterns in the text
    # Projects often appear with their status and type in the agenda reports
    # Common patterns:
    # 1. "Project Name (status)" or 
    # 2. "Project Name - type" or
    # 3. Projects listed under "Capital Improvement Projects (Design)" section
    
    # Look for the "Capital Improvement Projects (Design)" section
    design_section_pattern = r'Capital Improvement Projects \(Design\)(.*?)(?=Capital Improvement Projects \(Construction\)|Capital Improvement Projects \(Not Started\)|DISASTER RECOVERY PROJECTS|$)'
    design_section = re.search(design_section_pattern, text, re.IGNORECASE | re.DOTALL)
    
    if design_section:
        section_text = design_section.group(1)
        
        # Extract project names from this section
        # Projects typically appear as:
        # - Project Name followed by updates and schedule
        # Lines that start with a project name (often Title Case)
        
        # Split into lines and look for project names
        lines = section_text.split('\n')
        for line in lines:
            line = line.strip()
            # Skip empty lines and common headers
            if not line or line.startswith('(') or 'cid:' in line or line == 'Capital Improvement Projects (Design)':
                continue
                
            # Check if this line looks like a project name
            # Project names are typically title case and not too long
            # They may contain words like: Road, Street, Avenue, Park, Bridge, Drain, etc.
            project_keywords = ['road', 'street', 'avenue', 'park', 'bridge', 'drain', 'drainage', 'highway', 'crossing', 'walkway', 'sewer', 'culvert', 'retaining', 'traffic']
            
            words = line.split()
            if len(words) > 1 and len(words) < 15:  # Not too short, not too long
                # Check if it has title case (most words start with capital)
                capitalized_words = sum(1 for w in words if w[0].isupper() if w)
                if capitalized_words / len(words) > 0.5:  # More than half are capitalized
                    # Check if it contains project-related keywords
                    line_lower = line.lower()
                    if any(keyword in line_lower for keyword in project_keywords):
                        # This is likely a project name
                        project_name = line
                        
                        # Check if this project is in our funding list (exact match or partial)
                        for funding_proj in funding_project_names:
                            # Check for exact match or if funding name contains this project name
                            # or if this name contains funding name
                            if (project_name == funding_proj or 
                                funding_proj in project_name or 
                                project_name in funding_proj):
                                projects_info.append({
                                    'Project_Name': funding_proj,
                                    'type': 'capital',
                                    'status': 'design'
                                })
                        
                        # Also check for projects with suffixes like (FEMA Project) etc.
                        base_name = project_name
                        for suffix in [' (FEMA Project)', ' (CalJPIA Project)', ' (CalOES Project)', ' (FEMA/CalOES Project)']:
                            modified_name = base_name + suffix
                            if modified_name in funding_project_names:
                                projects_info.append({
                                    'Project_Name': modified_name,
                                    'type': 'capital',
                                    'status': 'design'
                                })

# Remove duplicates
unique_projects = []
seen_names = set()
for proj in projects_info:
    if proj['Project_Name'] not in seen_names:
        unique_projects.append(proj)
        seen_names.add(proj['Project_Name'])

print(f'Found {len(unique_projects)} unique capital projects with design status')
print('Sample extracted projects:', unique_projects[:10])

# For debugging, let's also check which funding projects might be missed
print('Total funding projects with >$50k:', len(funding_project_names))

# Let's check if there are any other patterns we might have missed
# Look for any project names that appear in both documents more directly
matched_projects = []

for funding_name in funding_project_names:
    # Search for this exact name in all civic documents
    for doc in civic_docs_data:
        if funding_name in doc.get('text', ''):
            # Try to determine type and status from context
            text = doc.get('text', '')
            
            # Look for status indicators near the project name
            context_start = max(0, text.find(funding_name) - 200)
            context_end = min(len(text), text.find(funding_name) + len(funding_name) + 200)
            context = text[context_start:context_end]
            
            # Check if it's in design section
            if 'Capital Improvement Projects (Design)' in text:
                design_section_start = text.find('Capital Improvement Projects (Design)')
                construction_section_start = text.find('Capital Improvement Projects (Construction)')
                project_pos = text.find(funding_name)
                
                if design_section_start < project_pos and (construction_section_start == -1 or project_pos < construction_section_start):
                    # Project is in design section
                    if any(keyword in funding_name.lower() for keyword in ['(fema', '(caljpia', '(caloes']):
                        project_type = 'disaster'
                    else:
                        project_type = 'capital'
                    
                    matched_projects.append({
                        'Project_Name': funding_name,
                        'type': project_type,
                        'status': 'design',
                        'amount': next(item['Amount'] for item in funding_data if item['Project_Name'] == funding_name)
                    })

# Remove duplicates from matched_projects
seen = set()
final_matched = []
for proj in matched_projects:
    if proj['Project_Name'] not in seen:
        final_matched.append(proj)
        seen.add(proj['Project_Name'])

print(f'Found {len(final_matched)} total capital/disaster projects with design status and funding > $50k')

# Count only capital projects (not disaster)
capital_design_count = sum(1 for proj in final_matched if proj['type'] == 'capital')

print('Capital projects with design status and funding > $50k:', capital_design_count)

result = {
    'count': capital_design_count,
    'projects': [proj for proj in final_matched if proj['type'] == 'capital']
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.list_db:5': ['civic_docs'], 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json'}

exec(code, env_args)
