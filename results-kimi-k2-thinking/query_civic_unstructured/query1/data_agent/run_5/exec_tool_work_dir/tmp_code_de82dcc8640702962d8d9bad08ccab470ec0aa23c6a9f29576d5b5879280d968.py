code = """import json

# Load data files
with open(locals()['var_functions.query_db:0']) as f:
    funding_data = json.load(f)

with open(locals()['var_functions.query_db:2']) as f:
    civic_docs = json.load(f)

# Get funded projects > $50,000
funded_projects = {}
for record in funding_data:
    amount_str = record.get('Amount', '0')
    if amount_str:
        amount_int = int(amount_str)
        if amount_int > 50000:
            funded_projects[record['Project_Name']] = amount_int

print('Projects with funding > 50000:', len(funded_projects))

# Extract design status projects
design_project_names = []

for document in civic_docs:
    text = document.get('text', '')
    
    # Find design status projects section (capital projects in design)
    design_marker = 'Capital Improvement Projects (Design)'
    construction_marker = 'Capital Improvement Projects (Construction)'
    
    design_index = text.find(design_marker)
    if design_index >= 0:
        construction_index = text.find(construction_marker, design_index)
        if construction_index < 0:
            construction_index = len(text)
        
        section = text[design_index:construction_index]
        
        # Split into blocks for each project
        blocks = section.split('\n\n')
        for block in blocks:
            block = block.strip()
            if block and len(block) > 20:
                lines = [line.strip() for line in block.split('\n') if line.strip()]
                if lines:
                    first_line = lines[0]
                    # Verify this is a project name (not metadata)
                    if (first_line and 'Updates' not in first_line and 'Schedule' not in first_line
                        and not first_line.startswith('(') and not first_line.startswith('•')
                        and not first_line.isupper() and len(first_line) > 10):
                        design_project_names.append(first_line)

print('Design status project names:', len(design_project_names))

# Match design projects with funding > $50,000
def clean_for_matching(name):
    # Simple cleaning without regex
    if '(' in name:
        name = name.split('(')[0]
    name = name.replace('Project', '').replace('Improvements', '').replace('Repairs', '')
    return name.strip().lower()

matched_projects = []
used_funding_names = set()

for design_project in design_project_names:
    design_clean = clean_for_matching(design_project)
    
    for funded_name in funded_projects:
        if funded_name in used_funding_names:
            continue
        
        funded_clean = clean_for_matching(funded_name)
        
        # Check if one name contains the other (case-insensitive)
        if design_clean in funded_clean or funded_clean in design_clean:
            matched_projects.append({
                'project_name': funded_name,
                'amount': funded_projects[funded_name]
            })
            used_funding_names.add(funded_name)

print('Final matched project count:', len(matched_projects))

# Show first 10 for verification
for i, proj in enumerate(matched_projects[:10]):
    print(f"{i+1}. {proj['project_name']} - ${proj['amount']}")

# Prepare final answer
final_result = {
    'count': len(matched_projects),
    'projects': matched_projects[:15]
}

print('__RESULT__:')
print(json.dumps(final_result))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json'}

exec(code, env_args)
