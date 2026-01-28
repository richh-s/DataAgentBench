code = """import json
import re

# Read the funding data
funding_file_path = locals()['var_functions.query_db:0']
with open(funding_file_path, 'r') as f:
    funding_data = json.load(f)

# Read the civic docs data  
civic_docs_file_path = locals()['var_functions.query_db:2']
with open(civic_docs_file_path, 'r') as f:
    civic_docs = json.load(f)

# Get projects with funding > $50,000
funding_projects = [f for f in funding_data if f['Amount'] and int(f['Amount']) > 50000]
funding_names_amounts = {p['Project_Name']: int(p['Amount']) for p in funding_projects}

print(f'Found {len(funding_projects)} funding records with Amount > $50,000')

# Extract capital projects with design status from civic documents
projects_with_design_status = []

for doc in civic_docs:
    text = doc.get('text', '')
    
    # Look for design projects section
    # The pattern is: 'Capital Improvement Projects (Design)' followed by project listings
    design_section = re.search(r'Capital Improvement Projects \(Design\)(.*?)(?=Capital Improvement Projects \(Construction\)|Disaster Recovery Projects|$)', text, re.DOTALL)
    
    if design_section:
        design_text = design_section.group(1)
        
        # Split into blocks - projects are separated by blank lines
        blocks = re.split(r'\n\s*\n', design_text)
        
        for block in blocks:
            block = block.strip()
            if not block:
                continue
                
            # Project names are typically the first line before bullet points or indented text
            lines = block.split('\n')
            project_name = None
            
            for line in lines:
                line = line.strip()
                # Skip empty lines, bullet points, and status markers
                if (line and not line.startswith('(') and not line.startswith('•')
                    and not line.startswith('-') and 'Updates:' not in line
                    and 'Schedule:' not in line and not line.isupper()):
                    # This looks like a project name
                    project_name = line
                    break
            
            if project_name and len(project_name) > 5:
                projects_with_design_status.append({
                    'project_name': project_name,
                    'type': 'capital',
                    'status': 'design'
                })

print(f'Found {len(projects_with_design_status)} projects with design status')

# Normalize project names for matching
def normalize_name(name):
    # Remove project type suffixes and clean
    name = re.sub(r'\s+Project$', '', name, flags=re.IGNORECASE)
    name = re.sub(r'\s+\(Design\)$', '', name, flags=re.IGNORECASE)
    return name.strip()

# Match design projects with funding data
matched_design_projects = []
matched_names = set()

for doc_proj in projects_with_design_status:
    doc_name = normalize_name(doc_proj['project_name'])
    
    for fund_name, amount in funding_names_amounts.items():
        norm_fund_name = normalize_name(fund_name)
        
        # Check for matches
        if (doc_name.lower() in norm_fund_name.lower() or 
            norm_fund_name.lower() in doc_name.lower() or
            doc_name.replace('Improvements', '').lower() in norm_fund_name.lower()):
            
            if fund_name not in matched_names:
                matched_design_projects.append({
                    'project_name': fund_name,
                    'amount': amount,
                    'status': 'design'
                })
                matched_names.add(fund_name)

print(f'Matched {len(matched_design_projects)} capital projects with design status and funding > $50,000')

# Show first few matches as verification
for i, proj in enumerate(matched_design_projects[:8]):
    print(f'{i+1}. {proj["project_name"]} - ${proj["amount"]}')

# Final result
result = {
    'count': len(matched_design_projects),
    'projects': matched_design_projects[:15]
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json'}

exec(code, env_args)
