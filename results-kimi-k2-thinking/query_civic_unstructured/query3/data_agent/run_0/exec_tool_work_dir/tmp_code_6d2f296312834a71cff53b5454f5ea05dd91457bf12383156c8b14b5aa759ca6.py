code = """import json

# Load funding data
with open('var_functions.query_db:0', 'r') as f:
    funding = json.load(f)

# Load civic documents  
with open('var_functions.query_db:5', 'r') as f:
    civic = json.load(f)

# Find FEMA/emergency projects in funding data
target_projects = []
for r in funding:
    name_lower = r.get('Project_Name', '').lower()
    if 'fema' in name_lower or 'emergency' in name_lower:
        target_projects.append({
            'Project_Name': r.get('Project_Name'),
            'Funding_Source': r.get('Funding_Source', ''),
            'Amount': int(r.get('Amount', 0))
        })

# Extract status information from civic documents
status_lookup = {}
for doc in civic:
    text = doc.get('text', '')
    lines = text.split('\n')
    
    # Simple approach: find lines that might be project names
    for i in range(len(lines)):
        line = lines[i].strip()
        if line and len(line) > 5 and len(line) < 100:
            # Check if followed by project indicators
            if i + 5 < len(lines):
                next_text = '\n'.join(lines[i:i+10])
                next_text_lower = next_text.lower()
                
                if 'updates:' in next_text_lower or 'project schedule:' in next_text_lower:
                    # Determine status from document
                    status = 'Unknown'
                    doc_lower = text.lower()
                    if 'construction was completed' in doc_lower:
                        status = 'completed'
                    elif 'under construction' in doc_lower or 'out to bid' in doc_lower:
                        status = 'construction'
                    elif 'design' in doc_lower:
                        status = 'design'
                    elif 'not started' in doc_lower:
                        status = 'not_started'
                    
                    status_lookup[line] = status

# Match projects with their statuses
results = []
for proj in target_projects:
    pname = proj['Project_Name']
    pstatus = 'Unknown'
    
    # Try exact match
    if pname in status_lookup:
        pstatus = status_lookup[pname]
    else:
        # Try partial match using base name
        base_parts = pname.split('(')
        base_name = base_parts[0].strip()
        for key in status_lookup.keys():
            if base_name.lower() in key.lower():
                pstatus = status_lookup[key]
                break
    
    results.append({
        'Project_Name': pname,
        'Funding_Source': proj['Funding_Source'],
        'Amount': proj['Amount'],
        'Status': pstatus
    })

# Output results
print('__RESULT__:')
print(json.dumps(results, indent=2))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.list_db:2': ['civic_docs'], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json'}

exec(code, env_args)
