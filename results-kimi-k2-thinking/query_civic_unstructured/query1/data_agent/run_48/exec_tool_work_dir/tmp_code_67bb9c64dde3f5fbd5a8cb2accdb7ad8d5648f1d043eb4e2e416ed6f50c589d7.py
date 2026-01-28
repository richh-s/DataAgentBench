code = """import json, re

# Load data from files
funding_file_path = var_functions.query_db:0
civic_file_path = var_functions.query_db:2

with open(funding_file_path) as f:
    funding_data = json.load(f)

with open(civic_file_path) as f:
    civic_docs = json.load(f)

# Build funding map for projects > $50k
funding_map = {}
for f in funding_data:
    if int(f['Amount']) > 50000:
        funding_map[f['Project_Name']] = int(f['Amount'])

# Extract capital design projects from civic docs
design_projects = []

for doc in civic_docs:
    text = doc.get('text', '')
    
    # Look for design section
    if 'Capital Improvement Projects (Design)' not in text:
        continue
    
    # Get section after Design header
    start_pos = text.find('Capital Improvement Projects (Design)') + len('Capital Improvement Projects (Design)')
    design_section = text[start_pos:]
    
    # Cut off at next major section
    for marker in ['Capital Improvement Projects (Construction)', 'Capital Improvement Projects (Not Started)', 'Disaster Recovery Projects']:
        marker_pos = design_section.find(marker)
        if marker_pos != -1:
            design_section = design_section[:marker_pos]
            break
    
    # Find project names by looking for lines that are not bullets/schedule items
    for line in design_section.split('\n'):
        line = line.strip()
        # Skip short lines and lines with keywords
        if len(line) >= 10 and 'Updates:' not in line and 'Schedule:' not in line and 'cid:' not in line and not line.isupper():
            # Clean up bullets
            clean_line = re.sub(r'^[A-Z]\.\s*', '', line)
            clean_line = re.sub(r'^\d+\.\s*', '', clean_line)
            if len(clean_line) > 10 and not clean_line.startswith('('):
                design_projects.append(clean_line)

# Count matches
matched = 0
for proj in design_projects:
    # Direct name match
    if proj in funding_map or any(proj in fund_name for fund_name in funding_map.keys()):
        matched += 1
        continue
    
    # Word-based matching
    proj_words = set(proj.lower().replace('(', '').replace(')', '').split())
    for fund_name in funding_map.keys():
        fund_words = set(fund_name.lower().replace('(', '').replace(')', '').split())
        if len(proj_words) >= 3 and len(fund_words) >= 3:
            common = proj_words.intersection(fund_words)
            if len(common) >= 2:
                matched += 1
                break

print('__RESULT__:')
print(json.dumps(matched))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:10': [{'count': '276'}]}

exec(code, env_args)
