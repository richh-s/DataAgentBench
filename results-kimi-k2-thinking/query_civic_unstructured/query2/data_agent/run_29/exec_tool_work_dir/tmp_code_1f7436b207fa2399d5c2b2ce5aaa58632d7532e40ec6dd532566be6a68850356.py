code = """import json

# Access the civic documents from the storage variable
# The key for civic_docs result is var_functions.query_db:2
civic_docs = locals().get('var_functions.query_db:2', [])

# Access the funding data from the storage variable  
# The key for funding result is var_functions.query_db:16
funding_data = locals().get('var_functions.query_db:16', [])

# If the data is stored as file paths instead of the actual data, read the files
if isinstance(civic_docs, str) and civic_docs.endswith('.json'):
    with open(civic_docs, 'r') as f:
        civic_docs = json.load(f)

if isinstance(funding_data, str) and funding_data.endswith('.json'):
    with open(funding_data, 'r') as f:
        funding_data = json.load(f)

# Extract park projects completed in 2022
park_projects = []

for doc in civic_docs:
    text = doc.get('text', '')
    if not text:
        continue
    
    # Look for park-related project names and completion info
    lines = text.split('\n')
    current_project = None
    
    for i, line in enumerate(lines):
        line = line.strip()
        if not line:
            continue
        
        # Check if line is a park project name
        if 'park' in line.lower() or 'playground' in line.lower():
            # Verify it's a project by checking context
            is_valid = False
            for j in range(max(0, i-2), min(len(lines), i+10)):
                context = lines[j].lower()
                if any(marker in context for marker in ['updates:', 'project schedule:', 'construction:', '(cid:', 'completed']):
                    is_valid = True
                    break
            
            if is_valid:
                current_project = line
                
                # Look for completion in 2022
                found_2022 = False
                for j in range(i, min(len(lines), i+15)):
                    check = lines[j]
                    check_lower = check.lower()
                    
                    if ('completed' in check_lower or 'completion' in check_lower) and '2022' in check:
                        found_2022 = True
                        break
                
                if found_2022:
                    park_projects.append(current_project)

# Remove duplicates
park_projects = list(set(park_projects))

# Match with funding data
def normalize_name(s):
    return ' '.join(s.lower().split())

funding_totals = {}
for park in park_projects:
    park_norm = normalize_name(park)
    for fund in funding_data:
        fund_name = fund['Project_Name']
        fund_norm = normalize_name(fund_name)
        
        # Match if one contains the other or significant overlap
        if (park_norm in fund_norm or fund_norm in park_norm):
            if park not in funding_totals:
                funding_totals[park] = 0
            funding_totals[park] += int(fund['Amount'])

# Total funding
total_funding = sum(funding_totals.values())

result = {
    'total_funding': total_funding
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:16': 'file_storage/functions.query_db:16.json'}

exec(code, env_args)
