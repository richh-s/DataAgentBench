code = """import json, re

# Load funding data
funding_file = open(str(var_functions.query_db:2))
funding_data = json.load(funding_file)
funding_file.close()

# Load civic documents
civic_file = open(str(var_functions.query_db:6))
civic_data = json.load(civic_file)
civic_file.close()

# Create funding map for projects > $50,000
funding_map = {}
for rec in funding_data:
    amount = float(rec.get('Amount', 0))
    if amount > 50000:
        name = rec['Project_Name']
        clean_name = re.sub(r'\s*\([^)]*\)\s*$', '', name).strip()
        funding_map[name] = amount
        funding_map[clean_name] = amount

# Extract capital design projects
capital_design = []

for doc in civic_data:
    text = doc.get('text', '')
    lines = text.split('\n')
    in_design = False
    
    for line in lines:
        line = line.strip()
        
        if 'Capital Improvement Projects (Design)' in line:
            in_design = True
        elif 'Capital Improvement Projects (Construction)' in line:
            in_design = False
        
        if in_design and line and len(line) > 15:
            if any(x in line for x in ['FEMA', 'CalOES', 'CalJPIA', 'fire']):
                continue
            if line.startswith('(') or 'Page' in line or 'Agenda' in line:
                continue
            if 'RECOMMENDED' in line.upper() or 'Updates:' in line or 'Schedule:' in line:
                continue
            if 'Capital Improvement Projects' in line:
                continue
            
            capital_design.append(line)

# Count matches
count = 0
matched = []

for proj in capital_design:
    clean_proj = re.sub(r'\s*\([^)]*\)\s*$', '', proj).strip()
    if proj in funding_map or clean_proj in funding_map:
        count += 1
        amount = funding_map.get(proj) or funding_map.get(clean_proj, 0)
        matched.append({'project': proj, 'funding': int(amount)})

result = {'count': count, 'matched_projects': matched}
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['Funding'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.list_db:4': ['civic_docs'], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.query_db:30': 'file_storage/functions.query_db:30.json', 'var_functions.query_db:32': 'file_storage/functions.query_db:32.json'}

exec(code, env_args)
