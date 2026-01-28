code = """import json
import re

# Load funding data
funding_file = var_functions.query_db:4
if isinstance(funding_file, str) and funding_file.endswith('.json'):
    with open(funding_file, 'r') as f:
        funding_data = json.load(f)
else:
    funding_data = var_functions.query_db:4

# Load civic docs
civic_file = var_functions.query_db:5
if isinstance(civic_file, str) and civic_file.endswith('.json'):
    with open(civic_file, 'r') as f:
        civic_docs = json.load(f)
else:
    civic_docs = var_functions.query_db:5

# Filter funding > $50,000
high_funding = [f for f in funding_data if isinstance(f, dict) and int(f.get('Amount', 0)) > 50000]

# Find capital projects with design status
results = []

for doc in civic_docs:
    if not isinstance(doc, dict):
        continue
    
    text = doc.get('text', '')
    if not text:
        continue
    
    # Check if document has Capital Improvement Projects (Design) section
    if 'Capital Improvement Projects (Design)' not in text:
        continue
    
    # Extract design section
    parts = text.split('Capital Improvement Projects (Design)')
    if len(parts) < 2:
        continue
    
    design_section = parts[1].split('Capital Improvement Projects (Construction)')[0]
    
    # Process each funding record
    for funding in high_funding:
        project_name = funding.get('Project_Name', '')
        if not project_name:
            continue
        
        # Check base name (without suffixes)
        base_name = project_name.split(' (')[0]
        
        # Check if project is in design section
        if base_name in design_section:
            # Determine if it's a capital project (not disaster recovery)
            is_disaster = 'FEMA' in project_name.upper() or 'CalOES' in project_name or 'CalJPIA' in project_name
            is_in_design = base_name in design_section
            
            if is_in_design and not is_disaster:
                results.append({
                    'Project_Name': project_name,
                    'Funding': int(funding['Amount']),
                    'Source': funding['Funding_Source']
                })

# Remove duplicates
unique_results = []
seen = set()
for r in results:
    if r['Project_Name'] not in seen:
        unique_results.append(r)
        seen.add(r['Project_Name'])

final_result = {
    'count': len(unique_results),
    'projects': unique_results
}

print('__RESULT__:')
print(json.dumps(final_result))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.list_db:1': ['Funding'], 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.execute_python:14': {'funding_records': 276, 'civic_docs': 5}}

exec(code, env_args)
