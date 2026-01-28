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
    capital_design_section = re.search(r'Capital Improvement Projects \(Design\)(.*?)(?=Capital Improvement Projects \(Construction\)|Capital Improvement Projects \(Not Started\)|Disaster Recovery Projects|RECOMMENDED ACTION:|$)', text, re.DOTALL | re.IGNORECASE)
    
    if capital_design_section:
        section_text = capital_design_section.group(1)
        # Extract project names
        lines = section_text.split('\n')
        i = 0
        while i < len(lines):
            line = lines[i].strip()
            
            # Skip empty lines and formatting
            if not line or line.startswith('cid:') or line.startswith('Page'):
                i += 1
                continue
                
            # Check if this looks like a project name (not an update line)
            skip_words = ['updates:', 'project schedule:', 'complete design:', 'advertise:', 'begin construction:', 'estimated schedule:', 'project description:', 'project updates:']
            is_update = any(line.lower().startswith(word) for word in skip_words)
            is_bullet = line.startswith('(') and 'cid:' in line
            
            if not is_update and not is_bullet and len(line) > 10 and not line.isupper():
                # Confirm it's a project by checking following lines
                is_project = False
                for j in range(i+1, min(i+4, len(lines))):
                    next_line = lines[j].strip().lower()
                    if 'updates:' in next_line or 'project schedule:' in next_line or 'project description:' in next_line:
                        is_project = True
                        break
                
                if is_project and line not in ['Subject:', 'RECOMMENDED ACTION:', 'DISCUSSION:']:
                    design_capital_projects.append(line)
            
            i += 1

# Also look for disaster recovery projects with design status
disaster_design_section = re.search(r'Disaster Recovery Projects \(Design\)(.*?)(?=Disaster Recovery Projects \(Construction\)|Disaster Recovery Projects \(Not Started\)|Capital Improvement Projects|RECOMMENDED ACTION:|$)', text, re.DOTALL | re.IGNORECASE)

if disaster_design_section:
    section_text = disaster_design_section.group(1)
    lines = section_text.split('\n')
    i = 0
    while i < len(lines):
        line = lines[i].strip()
        
        if not line or line.startswith('cid:') or line.startswith('Page'):
            i += 1
            continue
            
        skip_words = ['updates:', 'project schedule:', 'complete design:', 'advertise:', 'begin construction:', 'estimated schedule:', 'project description:', 'project updates:']
        is_update = any(line.lower().startswith(word) for word in skip_words)
        is_bullet = line.startswith('(') and 'cid:' in line
        
        if not is_update and not is_bullet and len(line) > 10 and not line.isupper():
            is_project = False
            for j in range(i+1, min(i+4, len(lines))):
                next_line = lines[j].strip().lower()
                if 'updates:' in next_line or 'project schedule:' in next_line or 'project description:' in next_line:
                    is_project = True
                    break
            
            if is_project and line not in ['Subject:', 'RECOMMENDED ACTION:', 'DISCUSSION:']:
                design_capital_projects.append(line)
        
        i += 1

# Find matches between design capital projects and funded projects
matched_projects = []
for project in design_capital_projects:
    # Direct match
    if project in funding_projects:
        matched_projects.append(project)
    else:
        # Try to match by comparing base names (without parenthetical suffixes)
        project_base = re.sub(r'\s*\([^)]*\)\s*$', '', project).strip()
        for funded in funding_projects:
            funded_base = re.sub(r'\s*\([^)]*\)\s*$', '', funded).strip()
            if project_base == funded_base:
                matched_projects.append(project)
                break

# Remove duplicates
matched_projects = list(set(matched_projects))

# Determine count
count = len(matched_projects)

print('__RESULT__:')
print(json.dumps(count))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json'}

exec(code, env_args)
