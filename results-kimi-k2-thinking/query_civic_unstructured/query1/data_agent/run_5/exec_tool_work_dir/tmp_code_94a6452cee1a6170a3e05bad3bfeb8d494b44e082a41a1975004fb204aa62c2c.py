code = """import json, re

# Load funding data
with open(locals()['var_functions.query_db:0']) as f:
    funding_records = json.load(f)

# Load civic documents data
with open(locals()['var_functions.query_db:2']) as f:
    civic_documents = json.load(f)

# Filter funding records for amounts > $50,000
funded_projects = {}
for rec in funding_records:
    if rec.get('Amount'):
        amount_int = int(rec['Amount'])
        if amount_int > 50000:
            funded_projects[rec['Project_Name']] = amount_int

print('Projects with funding > $50k:', len(funded_projects))

# Extract capital projects with design status from civic documents
capital_design_projects = []
for doc in civic_documents:
    text = doc.get('text', '')
    
    # Find the design status section
    design_marker = 'Capital Improvement Projects (Design)'
    construction_marker = 'Capital Improvement Projects (Construction)'
    
    if design_marker in text:
        start_idx = text.index(design_marker)
        end_idx = text.find(construction_marker, start_idx)
        if end_idx < 0:
            end_idx = len(text)
        
        design_section = text[start_idx:end_idx]
        
        # Split into project blocks
        blocks = design_section.split('\n\n')
        for block in blocks:
            block = block.strip()
            if len(block) > 20:
                # Get first non-empty line as project name
                lines = [line.strip() for line in block.split('\n') if line.strip()]
                if lines:
                    project_name = lines[0]
                    # Validate it's likely a project name
                    if ('Design)' not in project_name and 'Updates:' not in project_name and 
                        'Schedule:' not in project_name and not project_name.startswith('(') and
                        not project_name.startswith('•') and not project_name.isupper() and 
                        len(project_name) > 10):
                        capital_design_projects.append(project_name)

print('Capital projects with design status:', len(capital_design_projects))

# Match projects by name (normalized)
def normalize_name(name):
    # Simple cleaning without regex issues
    name = name.split('(')[0]
    name = name.replace('Project', '').replace('Improvements', '').replace('Repairs', '')
    return name.strip().lower()

final_matches = []
used_funding_names = set()

for design_name in capital_design_projects:
    design_norm = normalize_name(design_name)
    
    for fund_name in funded_projects:
        if fund_name in used_funding_names:
            continue
        
        fund_norm = normalize_name(fund_name)
        
        # Check for substring match
        if design_norm in fund_norm or fund_norm in design_norm:
            final_matches.append({
                'project_name': fund_name,
                'amount': funded_projects[fund_name],
                'type': 'capital',
                'status': 'design'
            })
            used_funding_names.add(fund_name)

print('Final matched count:', len(final_matches))

# Sample output for verification
for i, proj in enumerate(final_matches[:10]):
    print(f"{i+1}. {proj['project_name']} - ${proj['amount']}")

result = {'count': len(final_matches), 'projects': final_matches[:15]}
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json'}

exec(code, env_args)
