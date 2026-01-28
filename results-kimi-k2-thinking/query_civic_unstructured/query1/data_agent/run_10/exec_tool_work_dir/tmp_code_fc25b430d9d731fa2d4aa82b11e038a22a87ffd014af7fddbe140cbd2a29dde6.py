code = """import json
import re

# Load the data
civic_docs_file = var_functions.query_db:2
if isinstance(civic_docs_file, str) and civic_docs_file.endswith('.json'):
    with open(civic_docs_file, 'r') as f:
        civic_docs = json.load(f)
else:
    civic_docs = var_functions.query_db:2

funding_file = var_functions.query_db:5
if isinstance(funding_file, str) and funding_file.endswith('.json'):
    with open(funding_file, 'r') as f:
        funding_data = json.load(f)
else:
    funding_data = var_functions.query_db:5

# Extract funding projects > $50,000
funding_projects = set()
for item in funding_data:
    try:
        amount = int(item['Amount'])
        if amount > 50000:
            funding_projects.add(item['Project_Name'])
    except:
        continue

# Extract capital design projects from civic documents
capital_design_projects = []

for doc in civic_docs:
    text = doc.get('text', '')
    
    # Find the Capital Improvement Projects (Design) section
    design_start = text.find('Capital Improvement Projects (Design)')
    if design_start == -1:
        continue
    
    # Find where this section ends
    construction_start = text.find('Capital Improvement Projects (Construction)', design_start)
    not_started_start = text.find('Capital Improvement Projects (Not Started)', design_start)
    disaster_start = text.find('Disaster Recovery Projects', design_start)
    
    end_positions = [p for p in [construction_start, not_started_start, disaster_start] if p > design_start]
    design_end = min(end_positions) if end_positions else len(text)
    
    design_section = text[design_start:design_end]
    
    # Extract project names from this section
    # Projects appear to be listed with their names on separate lines
    lines = design_section.split('\n')
    
    for i, line in enumerate(lines):
        line = line.strip()
        if not line:
            continue
        
        # Skip headers, footers, and descriptive lines
        skip_patterns = [
            'Page', 'Agenda Item', 'Capital Improvement', 'RECOMMENDED ACTION:',
            'DISCUSSION:', 'To:', 'Prepared by:', 'Approved by:',
            'Date prepared:', 'Meeting date:', 'Subject:', 'Updates:',
            'Project Schedule:', 'Estimated Schedule:', 'Complete Design:',
            'Advertise:', 'Begin Construction:', 'Staff is', 'City is',
            'City has', 'Project is', 'Staff has', 'cid:', '(cid:'
        ]
        
        if any(pattern in line for pattern in skip_patterns):
            continue
        
        # Skip lines that are all uppercase (likely headers)
        if line.isupper() and len(line) < 50:
            continue
        
        # Skip lines that start with bullet points or symbols
        if line.startswith(('•', '-', '–', '(', ')', '◦')):
            continue
        
        # Skip very short lines or lines that look like dates
        if len(line) < 8 or re.match(r'^[A-Za-z]+ \d{4}$', line):
            continue
        
        # This looks like a project name - clean it up
        project_name = line.strip('•-– ')
        
        # Skip if it contains typical update text patterns
        if any(word in project_name for word in ['Staff', 'City', 'Project', 'Complete', 'Advertise', 'Begin']):
            continue
        
        if project_name and len(project_name) > 8:
            capital_design_projects.append(project_name)

# Deduplicate while preserving meaningful names
capital_design_projects = list(set(capital_design_projects))

# Flexible matching between design projects and funding projects
matched_count = 0
matched_details = []

for design_project in capital_design_projects:
    design_clean = design_project.lower().replace('project', '').strip()
    
    for funding_project in funding_projects:
        funding_clean = funding_project.lower().replace('project', '').strip()
        
        # Check for direct substring matches
        if (design_clean in funding_clean or funding_clean in design_clean):
            matched_count += 1
            matched_details.append({
                'design_project': design_project,
                'funding_project': funding_project
            })
            break
        
        # Check for key term overlap (for longer names)
        if len(design_clean) > 15 and len(funding_clean) > 15:
            design_terms = set([word for word in design_clean.split() if len(word) > 4])
            funding_terms = set([word for word in funding_clean.split() if len(word) > 4])
            
            # If they share multiple key terms, consider it a match
            common_terms = design_terms.intersection(funding_terms)
            if len(common_terms) >= 2:
                matched_count += 1
                matched_details.append({
                    'design_project': design_project,
                    'funding_project': funding_project
                })
                break

print('__RESULT__:')
print(json.dumps({
    'total_matches': matched_count,
    'matched_projects': matched_details,
    'capital_design_projects_count': len(capital_design_projects),
    'funding_projects_over_50k_count': len(funding_projects)
}))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json'}

exec(code, env_args)
