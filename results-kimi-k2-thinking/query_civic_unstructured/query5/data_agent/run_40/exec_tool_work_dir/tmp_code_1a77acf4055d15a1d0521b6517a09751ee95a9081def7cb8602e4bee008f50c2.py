code = """import json

civic_docs_file = '/tmp/tmp2d2u8k1a.json'
funding_file = '/tmp/tmp0k5s9q8h.json'

# Load civic documents
with open(civic_docs_file) as f:
    civic_docs = json.load(f)

# Load funding data
with open(funding_file) as f:
    funding_data = json.load(f)

# Create funding lookup by project name
funding_lookup = {}
for rec in funding_data:
    name = rec.get('Project_Name', '')
    amt = int(rec.get('Amount', 0))
    funding_lookup[name] = amt

# Find disaster projects that started in 2022
total_funding = 0
matched_projects = []

for doc in civic_docs:
    text = doc.get('text', '')
    lines = text.split('\n')
    
    for i in range(len(lines)):
        line = lines[i].strip()
        
        # Check for disaster indicators
        is_disaster = False
        if '(FEMA Project)' in line:
            is_disaster = True
        elif '(CalJPIA Project)' in line:
            is_disaster = True
        elif '(CalOES Project)' in line:
            is_disaster = True
        elif 'FEMA/CalOES Project' in line:
            is_disaster = True
            
        if is_disaster:
            proj_name = line
            
            # Look for start date in following lines
            start_info = ''
            for j in range(i+1, min(i+6, len(lines))):
                next_line = lines[j].strip().lower()
                if 'st:' in next_line or 'start:' in next_line:
                    start_info = lines[j].strip()
                    break
            
            # Check if started in 2022 and has funding
            if '2022' in start_info:
                amount = funding_lookup.get(proj_name, 0)
                if amount > 0:
                    total_funding += amount
                    matched_projects.append({
                        'name': proj_name,
                        'funding': amount,
                        'start_date': start_info
                    })

# Prepare output
output = {
    'total_funding': total_funding,
    'project_count': len(matched_projects),
    'projects': matched_projects
}

print('__RESULT__:')
print(json.dumps(output))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:3': 'file_storage/functions.query_db:3.json', 'var_functions.query_db:14': 'file_storage/functions.query_db:14.json'}

exec(code, env_args)
