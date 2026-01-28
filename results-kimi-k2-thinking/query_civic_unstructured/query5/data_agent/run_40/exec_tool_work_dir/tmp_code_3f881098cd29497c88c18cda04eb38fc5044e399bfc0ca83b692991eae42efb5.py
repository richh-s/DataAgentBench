code = """import json, re

# Load funding data
funding_path = locals()['var_functions.query_db:67']
funding_lookup = {}
with open(funding_path, 'r') as f:
    funding_data = json.load(f)
    for rec in funding_data:
        name = rec.get('Project_Name', '')
        if name:
            funding_lookup[name] = int(rec.get('Amount', '0'))

# Process civic documents
civic_path = locals()['var_functions.query_db:66']
total_funding = 0
project_matches = []

with open(civic_path, 'r') as f:
    civic_docs = json.load(f)
    
for doc in civic_docs:
    text = doc.get('text', '')
    if not text:
        continue
    lines = text.split('\n')
    
    for i in range(len(lines)):
        line = lines[i].strip()
        if not line:
            continue
        
        # Check if this is a disaster-related project
        is_disaster = False
        if '(FEMA' in line or 'CalJPIA' in line or 'CalOES' in line:
            is_disaster = True
        
        if is_disaster:
            # Look for start date containing 2022 in nearby lines
            found_2022 = False
            start_range = range(max(0, i-3), min(len(lines), i+8))
            for j in start_range:
                ctx = lines[j]
                if '2022' in ctx:
                    lower_ctx = ctx.lower()
                    if 'st:' in lower_ctx or 'start:' in lower_ctx or 'schedule:' in lower_ctx:
                        found_2022 = True
                        break
            
            if found_2022:
                # Get funding amount
                amount = funding_lookup.get(line, 0)
                if amount > 0:
                    total_funding += amount
                    project_matches.append({'name': line, 'amount': amount})

# Generate result
result = {
    'total_funding': total_funding,
    'project_count': len(project_matches)
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:3': 'file_storage/functions.query_db:3.json', 'var_functions.query_db:14': 'file_storage/functions.query_db:14.json', 'var_functions.query_db:46': 'file_storage/functions.query_db:46.json', 'var_functions.query_db:58': 'file_storage/functions.query_db:58.json', 'var_functions.query_db:59': 'file_storage/functions.query_db:59.json', 'var_functions.query_db:66': 'file_storage/functions.query_db:66.json', 'var_functions.query_db:67': 'file_storage/functions.query_db:67.json'}

exec(code, env_args)
