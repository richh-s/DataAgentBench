code = """import json
import re

# Load data
with open(locals()['var_functions.query_db:40'], 'r') as f:
    funding_data = json.load(f)

with open(locals()['var_functions.query_db:5'], 'r', encoding='utf-8') as f:
    civic_docs = json.load(f)

# Extract capital projects with design status
design_projects = set()

# Process each civic document
for doc in civic_docs:
    text = doc.get('text', '')
    
    # Look for the design section
    design_match = re.search(r'Capital Improvement Projects \(Design\)(.*?)(?:\n\n[A-Z]|\Z)', text, re.DOTALL)
    if design_match:
        design_section = design_match.group(1)
        
        # Extract project names from this section
        # Project names appear as titles before bullet points or update sections
        potential_projects = re.findall(r'\n([A-Z][a-zA-Z0-9\s&\-\/\(\)]+?(?:Project)?)\s*\n[\s\u2022\-]', design_section)
        
        for proj in potential_projects:
            name = proj.strip()
            # Filter out non-capital projects
            clean_name = re.sub(r'\s*\([^)]*\)$', '', name).strip()
            
            # Check if it's a capital project (not FEMA/disaster focused)
            lower_name = clean_name.lower()
            if ('fema' not in lower_name and 'disaster' not in lower_name and 
                len(clean_name) > 5 and 'project' in lower_name):
                design_projects.add(clean_name)

# Match with funding data > $50,000
matched_projects = set()

for funding in funding_data:
    amount = int(funding['Amount'])
    if amount > 50000:
        project_name = funding['Project_Name']
        # Normalize project name for matching
        base_name = re.sub(r'\s*\([^)]*\)$', '', project_name).strip()
        
        if base_name in design_projects:
            matched_projects.add(base_name)

result = {'count': len(matched_projects)}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:40': 'file_storage/functions.query_db:40.json'}

exec(code, env_args)
