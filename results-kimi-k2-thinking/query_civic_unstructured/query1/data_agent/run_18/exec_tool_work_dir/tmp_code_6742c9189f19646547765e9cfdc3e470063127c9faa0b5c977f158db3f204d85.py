code = """import json
import re

# Load the funding data (projects with > $50,000 funding)
funding_file = var_functions.query_db:50
if isinstance(funding_file, str) and funding_file.endswith('.json'):
    with open(funding_file, 'r') as f:
        funding_projects = json.load(f)
else:
    funding_projects = funding_file

# Load the civic documents
civic_file = var_functions.query_db:51
if isinstance(civic_file, str) and civic_file.endswith('.json'):
    with open(civic_file, 'r') as f:
        civic_docs = json.load(f)
else:
    civic_docs = civic_file

# Extract capital projects with design status from civic documents
design_projects = []

for doc in civic_docs:
    text = doc.get('text', '')
    
    # Find the design section
    design_start = text.find('Capital Improvement Projects (Design)')
    if design_start < 0:
        continue
    
    # Get the design section text (end at next major section)
    after_design = text[design_start:]
    end_pos = len(after_design)
    
    # Find where design section ends
    for marker in ['Capital Improvement Projects (Construction)', 
                   'Capital Improvement Projects (Not Started)', 
                   'Disaster Recovery Projects']:
        marker_pos = after_design.find(marker)
        if marker_pos > 0 and marker_pos < end_pos:
            end_pos = marker_pos
    
    design_section = after_design[:end_pos]
    
    # Extract project names from design section
    # Look for lines that are likely project names (not metadata)
    for line in design_section.split('\n'):
        line = line.strip()
        
        # Skip short lines, metadata, and bullet points
        if len(line) < 10:
            continue
        if line.startswith('(') or line.startswith('•') or line.startswith('●'):
            continue
        if 'cid:' in line or ':' in line:
            continue
        
        # Skip update/schedule lines
        skip_terms = ['Updates', 'Schedule', 'Complete Design', 'Advertise', 'Begin Construction', 
                      'Project Description', 'Project Schedule', 'Estimated Schedule']
        if any(term in line for term in skip_terms):
            continue
        
        # Look for project indicators
        project_indicators = ['Project', 'Improvements', 'Repairs', 'Infrastructure', 'Master Plan', 
                             'Study', 'Replacement', 'Facility']
        
        if any(indicator in line for indicator in project_indicators):
            # Clean the project name
            clean_name = re.sub(r'[^A-Za-z0-9\s&]', '', line).strip()
            if clean_name and len(clean_name) > 5:
                design_projects.append(clean_name)

# Remove duplicates
unique_design_projects = list(set(design_projects))

# Get list of funded project names for comparison
funded_names = [f['Project_Name'] for f in funding_projects]

# Match design projects with funded projects
matched_projects = []

for design_proj in unique_design_projects:
    design_lower = design_proj.lower()
    design_words = set(design_lower.split())
    
    for funded_name in funded_names:
        funded_lower = funded_name.lower()
        
        # Direct match (substring)
        if design_proj in funded_name or funded_name in design_proj:
            matched_projects.append(design_proj)
            break
        
        # Word overlap matching (at least 3 words in common)
        funded_words = set(funded_lower.split())
        common_words = design_words & funded_words
        
        if len(common_words) >= 3:
            matched_projects.append(design_proj)
            break

# Count the matches
count = len(matched_projects)

# Return result
print('__RESULT__:')
print(json.dumps({'count': count, 'sample_matches': matched_projects[:10]}))"""

env_args = {'var_functions.list_db:0': ['Funding'], 'var_functions.query_db:1': 'file_storage/functions.query_db:1.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:50': 'file_storage/functions.query_db:50.json', 'var_functions.query_db:51': 'file_storage/functions.query_db:51.json'}

exec(code, env_args)
