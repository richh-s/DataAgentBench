code = """import json, re

# Load funding data
funding_path = locals()['var_functions.query_db:0']
with open(funding_path) as f:
    funding_records = json.load(f)

# Load civic documents
civic_path = locals()['var_functions.query_db:2']
with open(civic_path) as f:
    civic_documents = json.load(f)

# Get projects with funding > $50,000
funding_dict = {}
for rec in funding_records:
    if rec.get('Amount'):
        amount_int = int(rec['Amount'])
        if amount_int > 50000:
            funding_dict[rec['Project_Name']] = amount_int

print('Capital projects with funding > 50000:', len(funding_dict))

# Extract design status projects from civic documents
design_project_names = []

for doc in civic_documents:
    text = doc.get('text', '')
    
    # Find design status projects section
    design_section_start = text.find('Capital Improvement Projects (Design)')
    if design_section_start >= 0:
        design_section_end = text.find('Capital Improvement Projects (Construction)', design_section_start)
        if design_section_end < 0:
            design_section_end = len(text)
        
        design_section = text[design_section_start:design_section_end]
        
        # Split into blocks (projects separated by blank lines)
        blocks = design_section.split('\n\n')
        for block in blocks:
            block = block.strip()
            if block and len(block) > 20:
                lines = [line.strip() for line in block.split('\n') if line.strip()]
                if lines:
                    project_name = lines[0]
                    # Validate it's a project name
                    if (project_name and 'Updates:' not in project_name 
                        and 'Schedule:' not in project_name and not project_name.startswith('(')
                        and not project_name.startswith('•') and not project_name.isupper()
                        and len(project_name) > 10):
                        design_project_names.append(project_name)

print('Extracted design projects:', len(design_project_names))

# Match design projects with funding data
def normalize_project(name):
    # Remove suffixes and clean
    name = re.sub(r'\s*\([^)]*\)$', '', name)  # Remove (FEMA) etc
    name = re.sub(r'\s+(Project|Improvements|Repairs)$', '', name, flags=re.IGNORECASE)
    return name.strip().lower()

matched_design_projects = []
seen_project_names = set()

for design_name in design_project_names:
    normalized_design = normalize_project(design_name)
    
    for fund_project_name in funding_dict:
        if fund_project_name in seen_project_names:
            continue
            
        normalized_fund = normalize_project(fund_project_name)
        
        # Check for matches using substring
        if normalized_design in normalized_fund or normalized_fund in normalized_design:
            matched_design_projects.append({
                'project_name': fund_project_name,
                'funding_amount': funding_dict[fund_project_name],
                'status': 'design',
                'type': 'capital'
            })
            seen_project_names.add(fund_project_name)

print('Matched design projects with funding > 50000:', len(matched_design_projects))

# Display verification
for idx, proj in enumerate(matched_design_projects[:10]):
    print(f"{idx+1}. {proj['project_name']} - ${proj['funding_amount']}")

final_result = {
    'count': len(matched_design_projects),
    'projects': matched_design_projects[:15]
}

print('__RESULT__:')
print(json.dumps(final_result))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json'}

exec(code, env_args)
