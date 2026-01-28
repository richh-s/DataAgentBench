code = """import json, os, re

# Load funding data (Amount > $50,000)
key0 = 'var_functions.query_db:0'
with open(locals()[key0], 'r') as f:
    funding_data = json.load(f)

# Load civic documents
key2 = 'var_functions.query_db:2'
with open(locals()[key2], 'r') as f:
    civic_docs = json.load(f)

# Extract all project names from funding data
funding_projects = set()
for record in funding_data:
    project_name = record.get('Project_Name', '')
    if project_name:
        funding_projects.add(project_name)

# Extract capital projects with 'design' status from civic docs
design_capital_projects = []

for doc in civic_docs:
    text = doc.get('text', '')
    
    # Look for capital improvement projects section
    # Pattern: "Capital Improvement Projects (Design)" followed by project listings
    capital_design_pattern = r'Capital Improvement Projects \(Design\)(.*?)(?=(?:Capital Improvement Projects \(Construction\)|Capital Improvement Projects \(Not Started\)|Disaster Recovery Projects|RECOMMENDED ACTION:|\Z))'
    
    matches = re.findall(capital_design_pattern, text, re.DOTALL | re.IGNORECASE)
    
    for match in matches:
        # Extract project names - they typically appear as:
        # 1. A title line with just the project name
        # 2. Followed by updates or schedule sections
        
        # Split by lines and look for project name patterns
        lines = match.split('\n')
        i = 0
        while i < len(lines):
            line = lines[i].strip()
            
            # Skip empty lines and section headers
            if not line or line.startswith('cid:') or line.startswith('Page'):
                i += 1
                continue
                
            # Check if this looks like a project name (not a bullet/update line)
            # Project names are typically descriptive and don't start with certain keywords
            is_update_line = any(line.lower().startswith(word) for word in ['updates:', 'project schedule:', 'complete', 'advertise', 'begin', 'estimated', 'project description:', 'project updates:'])
            is_bullet = line.startswith('(') and 'cid:' in line
            
            if not is_update_line and not is_bullet and len(line) > 10 and not line.isupper():
                # This might be a project name
                project_name = line
                
                # Look ahead to see if this is followed by project updates (confirming it's a project)
                is_confirmed_project = False
                for j in range(i+1, min(i+5, len(lines))):
                    next_line = lines[j].strip().lower()
                    if 'updates:' in next_line or 'project schedule:' in next_line or 'project description:' in next_line:
                        is_confirmed_project = True
                        break
                
                if is_confirmed_project and project_name not in ['Subject:', 'RECOMMENDED ACTION:', 'DISCUSSION:']:
                    design_capital_projects.append(project_name)
            
            i += 1

# Also look for disaster recovery projects with design status
disaster_design_pattern = r'Disaster Recovery Projects \(Design\)(.*?)(?=(?:Disaster Recovery Projects \(Construction\)|Disaster Recovery Projects \(Not Started\)|Capital Improvement Projects|RECOMMENDED ACTION:|\Z))'

for doc in civic_docs:
    text = doc.get('text', '')
    matches = re.findall(disaster_design_pattern, text, re.DOTALL | re.IGNORECASE)
    
    for match in matches:
        lines = match.split('\n')
        i = 0
        while i < len(lines):
            line = lines[i].strip()
            
            if not line or line.startswith('cid:') or line.startswith('Page'):
                i += 1
                continue
                
            is_update_line = any(line.lower().startswith(word) for word in ['updates:', 'project schedule:', 'complete', 'advertise', 'begin', 'estimated', 'project description:', 'project updates:'])
            is_bullet = line.startswith('(') and 'cid:' in line
            
            if not is_update_line and not is_bullet and len(line) > 10 and not line.isupper():
                project_name = line
                
                is_confirmed_project = False
                for j in range(i+1, min(i+5, len(lines))):
                    next_line = lines[j].strip().lower()
                    if 'updates:' in next_line or 'project schedule:' in next_line or 'project description:' in next_line:
                        is_confirmed_project = True
                        break
                
                if is_confirmed_project and project_name not in ['Subject:', 'RECOMMENDED ACTION:', 'DISCUSSION:']:
                    # These are typically disaster projects, but check if they have FEMA suffixes
                    if '(FEMA' in project_name or '(CalOES' in project_name or '(CalJPIA' in project_name:
                        design_capital_projects.append(project_name)
            
            i += 1

# Now find matches between design capital projects and funding projects > $50,000
matched_projects = []
for design_project in design_capital_projects:
    # Direct match
    if design_project in funding_projects:
        matched_projects.append(design_project)
    else:
        # Try to match variations (e.g., with/without FEMA suffixes)
        for funded_project in funding_projects:
            if design_project.startswith(funded_project) or funded_project.startswith(design_project):
                matched_projects.append(design_project)
                break
            # Check if they're the same project with different suffixes
            design_base = re.sub(r'\s*\([^)]*\)\s*$', '', design_project)
            funded_base = re.sub(r'\s*\([^)]*\)\s*$', '', funded_project)
            if design_base == funded_base:
                matched_projects.append(design_project)
                break

# Remove duplicates
matched_projects = list(set(matched_projects))

# Count final matches
count = len(matched_projects)

print('__RESULT__:')
print(json.dumps({
    'count': count,
    'matched_projects': matched_projects,
    'total_design_capital_projects': len(design_capital_projects),
    'total_funded_projects': len(funding_projects)
}))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json'}

exec(code, env_args)
