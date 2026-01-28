code = """import json
import re

# Load the funding data
funding_file = var_functions.query_db:0
with open(funding_file, 'r') as f:
    funding_data = json.load(f)

# Load the filtered civic documents
civic_file = var_functions.query_db:8
with open(civic_file, 'r') as f:
    civic_docs = json.load(f)

# Create funding dictionary with lowercase keys for matching
funding_dict = {}
for record in funding_data:
    try:
        amount = int(record.get('Amount', 0))
        if amount > 50000:
            project_name = record.get('Project_Name', '').strip()
            if project_name:
                funding_dict[project_name.lower()] = {
                    'original_name': project_name,
                    'amount': amount
                }
    except:
        continue

print('Funding records > $50K: ' + str(len(funding_dict)))

# Extract project names from Design section
design_projects = []

for doc in civic_docs:
    text = doc.get('text', '')
    
    # Get Design section boundaries
    design_start = text.find('Capital Improvement Projects (Design)')
    if design_start == -1:
        continue
    
    # Find where Design section ends
    next_section_start = len(text)
    for marker in ['Capital Improvement Projects (Construction)', 
                   'Capital Improvement Projects (Not Started)',
                   'DISASTER RECOVERY PROJECTS']:
        pos = text.find(marker, design_start + 50)
        if pos > design_start and pos < next_section_start:
            next_section_start = pos
    
    design_section = text[design_start:next_section_start]
    
    # Find project names - they appear as headings before update blocks
    lines = design_section.split('\n')
    
    for i, line in enumerate(lines):
        line = line.strip()
        
        # Skip irrelevant lines
        if not line or len(line) < 10:
            continue
        
        skip_words = ['cid:', 'Updates:', 'Project Schedule:', 'Complete Design:', 
                      'Advertise:', 'Begin Construction:', 'Page', 'RECOMMENDED ACTION:',
                      'DISCUSSION:', 'Capital Improvement Projects', 'Project Description:']
        if any(word in line for word in skip_words):
            continue
        
        if line.isupper() and len(line.split()) <= 3:
            continue
        
        # Project names are typically title case and descriptive
        if line[0].isupper() and len(line.split()) >= 2:
            # Check if this is followed by project updates/schedule
            is_project = False
            for j in range(i+1, min(i+4, len(lines))):
                next_line = lines[j].lower()
                if 'updates:' in next_line or 'project schedule:' in next_line or 'staff' in next_line:
                    is_project = True
                    break
            
            if is_project or 'Project' in line or 'Improvements' in line or 'Drainage' in line:
                if line not in design_projects:
                    design_projects.append(line)

print('Design projects found: ' + str(len(design_projects)))

# Match projects with funding
matched = []
for project in design_projects:
    project_lower = project.lower()
    
    # Direct match
    if project_lower in funding_dict:
        matched.append(project)
    else:
        # Try partial matching
        for funded_lower, funded_info in funding_dict.items():
            # Check if project names overlap significantly
            proj_words = set(project_lower.split())
            funded_words = set(funded_lower.split())
            
            # If they share at least 2 words or one contains the other
            shared_words = proj_words.intersection(funded_words)
            if (len(shared_words) >= 2 or 
                project_lower in funded_lower or 
                funded_lower in project_lower):
                matched.append(project)
                break

# Remove duplicates
unique_matched = list(set(matched))
print('Matched projects: ' + str(len(unique_matched)))

result = len(unique_matched)
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:1': 'file_storage/functions.query_db:1.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json'}

exec(code, env_args)
