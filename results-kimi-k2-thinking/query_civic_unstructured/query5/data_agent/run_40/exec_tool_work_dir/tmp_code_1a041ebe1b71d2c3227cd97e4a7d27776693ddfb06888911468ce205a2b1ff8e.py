code = """import json

# Load data
civic_docs_file = open('/tmp/tmp2d2u8k1a.json', 'r')
civic_docs = json.load(civic_docs_file)
civic_docs_file.close()

funding_file = open('/tmp/tmp0k5s9q8h.json', 'r')
funding_data = json.load(funding_file)
funding_file.close()

# Build funding lookup by project name
funding_lookup = {}
for rec in funding_data:
    proj_name = rec.get('Project_Name', '')
    if proj_name:
        funding_lookup[proj_name] = int(rec.get('Amount', 0))

# Initialize tracking
total_funding = 0
matched_projects = []

# Process each document
for doc in civic_docs:
    txt = doc.get('text', '')
    if not txt:
        continue
    
    # Simple approach: look for disaster projects with 2022 in their description
    lines = txt.split('\n')
    
    for i, line in enumerate(lines):
        line_clean = line.strip()
        
        # Check for disaster project indicators
        disaster_markers = ['(FEMA Project)', '(CalJPIA Project)', '(CalOES Project)', 'FEMA/CalOES Project']
        is_disaster = any(marker in line_clean for marker in disaster_markers)
        
        if is_disaster:
            proj_name = line_clean
            
            # Look for 2022 start date in nearby context
            nearby_text = ' '.join(lines[max(0,i-3):min(len(lines), i+6)])
            
            if '2022' in nearby_text and ('st:' in nearby_text.lower() or 'start:' in nearby_text.lower()):
                # Get funding amount
                amount = funding_lookup.get(proj_name, 0)
                if amount > 0:
                    total_funding += amount
                    matched_projects.append({
                        'name': proj_name,
                        'amount': amount
                    })

# Output result
output = {'total_funding': total_funding, 'project_count': len(matched_projects)}
print('__RESULT__:')
print(json.dumps(output))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:3': 'file_storage/functions.query_db:3.json', 'var_functions.query_db:14': 'file_storage/functions.query_db:14.json'}

exec(code, env_args)
