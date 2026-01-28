code = """import json
import re

# Load data
with open(locals()['var_functions.query_db:40'], 'r') as f:
    funding_data = json.load(f)

with open(locals()['var_functions.query_db:5'], 'r', encoding='utf-8') as f:
    civic_docs = json.load(f)

# Extract capital projects with design status from documents
design_projects = set()

for doc in civic_docs:
    text = doc.get('text', '')
    
    # Find the capital improvement design section
    pattern = r'Capital Improvement Projects \(Design\)(.+?)(?:\n\n[A-Z]|$)'
    design_match = re.search(pattern, text, re.DOTALL)
    
    if design_match:
        section = design_match.group(1)
        lines = section.split('\n')
        
        for line in lines:
            proj = line.strip()
            # Look for lines that appear to be project names
            if (len(proj) > 10 and 
                'Project' in proj and 
                'fema' not in proj.lower() and 
                'disaster' not in proj.lower()
               ):
                # Clean up the name
                clean_name = re.sub(r'\s*\([^)]*\)$', '', proj).strip()
                design_projects.add(clean_name)

# Match with funding over $50,000
matched_set = set()

for funding in funding_data:
    amount = int(funding['Amount'])
    if amount > 50000:
        proj_name = funding['Project_Name']
        base_name = re.sub(r'\s*\([^)]*\)$', '', proj_name).strip()
        
        if base_name in design_projects:
            matched_set.add(base_name)

result_json = json.dumps({'count': len(matched_set)})
print('__RESULT__:')
print(result_json)"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:40': 'file_storage/functions.query_db:40.json'}

exec(code, env_args)
