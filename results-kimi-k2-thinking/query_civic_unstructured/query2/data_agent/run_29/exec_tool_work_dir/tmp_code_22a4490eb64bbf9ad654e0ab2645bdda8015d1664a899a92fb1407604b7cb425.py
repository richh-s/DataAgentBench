code = """import json

# Load data from files
civic_docs = json.load(open('/tmp/tmpz5hptp8z.json'))
funding_data = json.load(open('/tmp/tmphs_qx5r1.json'))

# Find park projects completed in 2022
park_projects_2022 = []

for doc in civic_docs:
    text = doc.get('text', '')
    lines = text.split('\n')
    
    # Look for park projects with 2022 completion dates
    for i, line in enumerate(lines):
        line = line.strip()
        if not line:
            continue
            
        # Check if this is a park project name
        line_lower = line.lower()
        if 'park' in line_lower or 'playground' in line_lower:
            # Look ahead for completion info
            for j in range(i, min(i+10, len(lines))):
                next_line = lines[j].strip()
                next_lower = next_line.lower()
                
                if any(phrase in next_lower for phrase in ['completed', 'completion']):
                    if '2022' in next_line:
                        park_projects_2022.append(line)
                        break

# Normalize names for matching
def normalize(s):
    return s.lower().strip()

# Match with funding
matched_funding = []
project_funding_map = {}

for park_proj in park_projects_2022:
    park_norm = normalize(park_proj)
    for fund in funding_data:
        fund_name = fund['Project_Name']
        fund_norm = normalize(fund_name)
        
        # Match if one contains the other
        if fund_norm in park_norm or park_norm in fund_norm:
            amount = int(fund['Amount'])
            matched_funding.append({
                'project': park_proj,
                'funding_name': fund_name,
                'amount': amount
            })
            # Avoid duplicates
            if park_proj not in project_funding_map:
                project_funding_map[park_proj] = 0
            project_funding_map[park_proj] += amount

# Total funding
total_funding = sum(f['amount'] for f in matched_funding)

result = {
    'park_projects': list(set(park_projects_2022)),
    'funding_records': matched_funding,
    'total_funding': total_funding
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:16': 'file_storage/functions.query_db:16.json'}

exec(code, env_args)
