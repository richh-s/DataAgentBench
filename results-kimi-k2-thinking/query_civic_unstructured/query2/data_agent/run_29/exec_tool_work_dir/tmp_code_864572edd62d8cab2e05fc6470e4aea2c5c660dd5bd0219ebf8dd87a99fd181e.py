code = """import json

# Load data
with open('/tmp/tmpz5hptp8z.json', 'r') as f:
    civic_docs = json.load(f)
with open('/tmp/tmphs_qx5r1.json', 'r') as f:
    funding_data = json.load(f)

# Find park-related projects completed in 2022
park_projects = []

for doc in civic_docs:
    text = doc.get('text', '')
    lines = text.split(chr(10))
    
    for i in range(len(lines)):
        line = lines[i].strip()
        if not line:
            continue
        
        # Check for park in project name
        line_lower = line.lower()
        if 'park' in line_lower or 'playground' in line_lower:
            # Look ahead for completion in 2022
            found = False
            for j in range(i, min(i+15, len(lines))):
                check_line = lines[j].strip().lower()
                if ('completed' in check_line or 'completion' in check_line) and '2022' in lines[j]:
                    park_projects.append(line)
                    found = True
                    break
            if found:
                continue

# Remove duplicates
park_projects = list(set(park_projects))

# Match with funding
def normalize(s):
    return s.lower().strip()

funding_amounts = {}
for park in park_projects:
    park_norm = normalize(park)
    for fund in funding_data:
        fund_name = normalize(fund['Project_Name'])
        if park_norm in fund_name or fund_name in park_norm:
            amount = int(fund['Amount'])
            if park in funding_amounts:
                funding_amounts[park] += amount
            else:
                funding_amounts[park] = amount

# Calculate total
total_funding = sum(funding_amounts.values())

result = {
    'park_projects_2022': park_projects,
    'total_funding': total_funding
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:16': 'file_storage/functions.query_db:16.json'}

exec(code, env_args)
