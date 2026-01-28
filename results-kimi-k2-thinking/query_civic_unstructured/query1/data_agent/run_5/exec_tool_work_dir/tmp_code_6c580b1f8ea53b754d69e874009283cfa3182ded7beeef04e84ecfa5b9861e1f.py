code = """import json

# Load the funding data file
funding_file = locals()['var_functions.query_db:0']
with open(funding_file) as f:
    funding_records = json.load(f)

# Load the civic documents file
civic_file = locals()['var_functions.query_db:2']
with open(civic_file) as f:
    civic_documents = json.load(f)

# Step 1: Filter funding records for amounts greater than $50,000
funding_dict = {}
for rec in funding_records:
    amount_val = rec.get('Amount')
    if amount_val:
        amount_int = int(amount_val)
        if amount_int > 50000:
            funding_dict[rec['Project_Name']] = amount_int

print('Projects with funding > $50,000:', len(funding_dict))

# Step 2: Extract capital projects with design status from civic documents
design_project_list = []

for document in civic_documents:
    text = document.get('text', '')
    
    # Find design section by string position
    design_start = text.find('Capital Improvement Projects (Design)')
    if design_start >= 0:
        construction_start = text.find('Capital Improvement Projects (Construction)', design_start)
        if construction_start < 0:
            construction_start = len(text)
        
        design_section = text[design_start:construction_start]
        
        # Split into project blocks separated by blank lines
        blocks = design_section.split('\n\n')
        for block in blocks:
            block = block.strip()
            if block and len(block) > 20:
                # Extract first non-empty line as project name
                lines = [line.strip() for line in block.split('\n') if line.strip()]
                if lines:
                    project_name_candidate = lines[0]
                    # Filter out metadata lines
                    if ('Design)' not in project_name_candidate and 
                        'Updates:' not in project_name_candidate and 
                        'Schedule:' not in project_name_candidate and
                        not project_name_candidate.startswith('(') and
                        not project_name_candidate.startswith('•') and
                        not project_name_candidate.isupper() and
                        len(project_name_candidate) > 10):
                        design_project_list.append(project_name_candidate)

print('Capital projects with design status:', len(design_project_list))

# Step 3: Match design projects with funding data
def normalize_name(n):
    # Simple name normalization without regex
    if '(' in n:
        n = n.split('(')[0]
    n = n.replace('Project', '').replace('Improvements', '').replace('Repairs', '')
    return n.strip().lower()

matched_results = []
matched_funding_names = set()

for design_project_name in design_project_list:
    normalized_design = normalize_name(design_project_name)
    
    for funding_project_name in funding_dict:
        if funding_project_name in matched_funding_names:
            continue
        
        normalized_funding = normalize_name(funding_project_name)
        
        # Check for substring match
        if normalized_design in normalized_funding or normalized_funding in normalized_design:
            matched_results.append({
                'project_name': funding_project_name,
                'funding': funding_dict[funding_project_name],
                'type': 'capital',
                'status': 'design'
            })
            matched_funding_names.add(funding_project_name)

print('Matched design projects with funding > $50k:', len(matched_results))

# Show first 10 matches for verification
for i, proj in enumerate(matched_results[:10]):
    print(f"{ i+1 }. { proj['project_name'] } - ${ proj['funding'] }")

# Return final result
result = {'count': len(matched_results), 'projects': matched_results[:15]}
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json'}

exec(code, env_args)
