code = """import json

# Get civic documents
civic_docs = locals()['var_functions.query_db:2']
if isinstance(civic_docs, str) and civic_docs.endswith('.json'):
    with open(civic_docs, 'r') as f:
        civic_docs = json.load(f)

print('Civic docs count: ' + str(len(civic_docs)))

# Simple approach: look for completion mentions with 2022 in each document
park_2022_projects = []

for doc in civic_docs:
    text = doc.get('text', '')
    lines = text.split('\n')
    
    # Look for lines mentioning 2022 and completion
    for i, line in enumerate(lines):
        line = line.strip()
        if not line:
            continue
        
        # Check for completion in 2022
        if '2022' in line and 'complete' in line.lower():
            # Look at surrounding lines for context
            start = max(0, i-5)
            end = min(len(lines), i+3)
            context = ' '.join(lines[start:end])
            
            # Check if it's park-related
            context_lower = context.lower()
            if 'park' in context_lower or 'walkway' in context_lower or 'shade' in context_lower:
                # Get the project name from nearby lines
                for k in range(i-3, i+1):
                    if k >= 0 and k < len(lines):
                        candidate = lines[k].strip()
                        if candidate and len(candidate) > 10 and not candidate.startswith('Public'):
                            if 'project' in candidate.lower() or 'improvements' in candidate.lower() or 'repairs' in candidate.lower():
                                park_2022_projects.append(candidate)
                                break

# Remove duplicates
unique_projects = []
for proj in park_2022_projects:
    if proj not in unique_projects:
        unique_projects.append(proj)

print('Park projects in 2022: ' + str(len(unique_projects)))

# Load funding data
funding = locals()['var_functions.query_db:5']
if isinstance(funding, str) and funding.endswith('.json'):
    with open(funding, 'r') as f:
        funding = json.load(f)

# Match and sum funding
total_funding = 0
matching_funds = []

for project_name in unique_projects:
    for fund in funding:
        fund_name = fund['Project_Name']
        # Check for match
        if project_name == fund_name or project_name in fund_name or fund_name in project_name:
            amount = int(fund['Amount'])
            total_funding += amount
            matching_funds.append({
                'project': project_name,
                'matched_funding': fund_name,
                'amount': amount
            })
            break

result = json.dumps({
    'total_funding': total_funding,
    'matched_projects': matching_funds
})

print('__RESULT__:')
print(result)"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json'}

exec(code, env_args)
