code = """import json, re

# Load funding and civic documents data
funding_path = var_functions.query_db:1
civic_path = var_functions.query_db:2

with open(funding_path, 'r') as f:
    funding_data = json.load(f)
with open(civic_path, 'r') as f:
    civic_docs = json.load(f)

# Extract capital projects with design status from civic documents
design_projects = []

for doc in civic_docs:
    text = doc.get('text', '')
    
    # Find where design section starts
    start = text.find('Capital Improvement Projects (Design)')
    if start < 0:
        continue
    
    # Find where design section ends
    section = text[start:]
    end_markers = ['Capital Improvement Projects (Construction)', 'Capital Improvement Projects (Not Started)', 'Disaster Recovery Projects']
    end = len(section)
    for marker in end_markers:
        pos = section.find(marker)
        if pos > 0 and pos < end:
            end = pos
    
    design_section = section[:end]
    
    # Parse lines to extract project names
    for line in design_section.splitlines():
        line = line.strip()
        if len(line) < 10 or line.startswith('(') or ':' in line:
            continue
        if 'cid:' in line or 'Updates' in line or 'Schedule' in line:
            continue
        
        if 'Project' in line or 'Improvements' in line or 'Repairs' in line:
            clean = re.sub(r'[^A-Za-z0-9\s]', '', line)
            clean = clean.strip()
            if clean:
                design_projects.append(clean)

# Remove duplicates
design_projects = list(set(design_projects))

# Get all funded project names
funded_names = [f['Project_Name'] for f in funding_data]

# Count how many design projects have funding matches
matched_count = 0

for design in design_projects:
    design_lower = design.lower()
    
    for funded in funded_names:
        funded_lower = funded.lower()
        
        # Direct substring matching
        if design_lower in funded_lower or funded_lower in design_lower:
            matched_count += 1
            break
        
        # Word overlap (at least 3 words in common)
        design_words = set(design_lower.split())
        funded_words = set(funded_lower.split())
        if len(design_words & funded_words) >= 3:
            matched_count += 1
            break

# Return the final answer as JSON
result = json.dumps({'count': matched_count})
print('__RESULT__:')
print(result)"""

env_args = {'var_functions.list_db:0': ['Funding'], 'var_functions.query_db:1': 'file_storage/functions.query_db:1.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json'}

exec(code, env_args)
