code = """import json

# Load funding data
with open(locals()['var_functions.query_db:0']) as f:
    funding_recs = json.load(f)

# Load civic documents
with open(locals()['var_functions.query_db:2']) as f:
    civic_list = json.load(f)

# Filter funding > $50,000
funding_by_name = {}
for rec in funding_recs:
    amount_str = rec.get('Amount')
    if amount_str:
        amount_int = int(amount_str)
        if amount_int > 50000:
            funding_by_name[rec['Project_Name']] = amount_int

print('Funding records > $50k:', len(funding_by_name))

# Extract capital projects with design status
design_project_list = []

for doc in civic_list:
    text = doc.get('text', '')
    
    # Find design projects section
    if 'Capital Improvement Projects (Design)' in text:
        # Extract section between Design and Construction headers
        design_start = text.index('Capital Improvement Projects (Design)')
        construction_start = text.find('Capital Improvement Projects (Construction)', design_start)
        if construction_start < 0:
            construction_start = len(text)
        
        section_text = text[design_start:construction_start]
        
        # Split by blank lines to find individual projects
        blocks = section_text.split('\n\n')
        for block in blocks:
            block = block.strip()
            if block and len(block) > 20:
                # Get first non-empty line as potential project name
                lines = [line.strip() for line in block.split('\n') if line.strip()]
                if lines:
                    # Skip the section header itself
                    first_line = lines[0]
                    if 'Design)' not in first_line:
                        # Validate this looks like a project name
                        if (first_line and 'Updates' not in first_line and 'Schedule' not in first_line
                            and not first_line.startswith('(') and not first_line.startswith('•')
                            and not first_line.isupper() and len(first_line) > 10):
                            design_project_list.append(first_line)

print('Design status projects:', len(design_project_list))

# Match projects by normalized name
def normalize_name(name):
    # Basic cleaning without regex to avoid syntax errors
    name = name.split('(')[0]  # Remove (FEMA) etc
    name = name.replace('Project', '').replace('Improvements', '').replace('Repairs', '')
    return name.strip().lower()

matched_projects = []
seen_funding_names = set()

for design_name in design_project_list:
    design_clean = normalize_name(design_name)
    
    for fund_name in funding_by_name:
        if fund_name in seen_funding_names:
            continue
        
        fund_clean = normalize_name(fund_name)
        
        # Check if one contains the other (case-insensitive)
        if design_clean in fund_clean or fund_clean in design_clean:
            matched_projects.append({
                'project_name': fund_name,
                'funding': funding_by_name[fund_name],
                'status': 'design',
                'type': 'capital'
            })
            seen_funding_names.add(fund_name)

print('Matched design projects:', len(matched_projects))

# Show verification of matches
for i, proj in enumerate(matched_projects[:10]):
    print(f"{i+1}. {proj['project_name']} - ${proj['funding']}")

# Return final result
result = {'count': len(matched_projects), 'projects': matched_projects[:15]}
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json'}

exec(code, env_args)
