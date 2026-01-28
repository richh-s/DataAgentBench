code = """import json, re

# Load data
funding_file = var_functions.query_db:2
with open(funding_file, 'r') as f:
    funding_data = json.load(f)

civic_file = var_functions.query_db:6  
with open(civic_file, 'r') as f:
    civic_docs = json.load(f)

# Get all unique project names from funding
funding_projects = set()
for f in funding_data:
    name = f['Project_Name']
    clean_name = re.sub(r'\s*\([^)]*\)\s*$', '', name).strip()
    funding_projects.add(name)
    funding_projects.add(clean_name)

# Extract capital design projects from civic docs
capital_design_names = set()

for doc in civic_docs:
    text = doc.get('text', '')
    # Look for the design section
    design_start = text.find('Capital Improvement Projects (Design)')
    construction_start = text.find('Capital Improvement Projects (Construction)')
    
    if design_start >= 0:
        # Extract text between design and construction sections
        if construction_start >= 0:
            design_text = text[design_start:construction_start]
        else:
            design_text = text[design_start:]
        
        # Split into lines and find project names
        for line in design_text.split('\n'):
            line = line.strip()
            if line and len(line) > 10:
                # Skip headers and meta lines
                skip = False
                for word in ['RECOMMENDED', 'ACTION', 'DISCUSSION', 'SUBJECT', 'Page', 'Agenda', 'Capital Improvement', 'Projects', 'Updates:', 'Schedule:']:
                    if word in line.upper():
                        skip = True
                
                if not skip and not line.startswith('(') and not line.startswith('\u2022'):
                    # Check if it's a disaster project
                    is_disaster = any(k in line for k in ['FEMA', 'CalOES', 'CalJPIA', 'fire'])
                    if not is_disaster:  # Only capital projects
                        capital_design_names.add(line)

# Get funding for projects > $50k
funding_gt_50k = {}
for f in funding_data:
    amount = float(f.get('Amount', 0))
    if amount > 50000:
        name = f['Project_Name']
        clean_name = re.sub(r'\s*\([^)]*\)\s*$', '', name).strip()
        funding_gt_50k[name] = amount
        funding_gt_50k[clean_name] = amount

# Count matches
count = 0
matched_projects = []

for proj_name in capital_design_names:
    proj_clean = re.sub(r'\s*\([^)]*\)\s*$', '', proj_name).strip()
    
    # Check if this project has funding > $50k
    if proj_name in funding_gt_50k or proj_clean in funding_gt_50k:
        count += 1
        amount = funding_gt_50k.get(proj_name) or funding_gt_50k.get(proj_clean, 0)
        matched_projects.append({
            'Project_Name': proj_name,
            'Funding_Amount': amount
        })

result = {
    'count': count,
    'matched_projects': matched_projects,
    'total_capital_design': len(capital_design_names)
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['Funding'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.list_db:4': ['civic_docs'], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json'}

exec(code, env_args)
