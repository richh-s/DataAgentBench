code = """import json

# Access the file paths
funding_file = locals()['var_functions.query_db:2']
civic_file = locals()['var_functions.query_db:5']

# Load the data
with open(funding_file) as f:
    funding_data = json.load(f)

with open(civic_file) as f:
    civic_docs = json.load(f)

# Extract project names from civic docs
design_capitals = []

for doc in civic_docs:
    text = doc.get('text', '')
    if 'Capital' in text and 'Design' in text:
        # Split text into lines and look for project names
        lines = str(text).split('\n')
        for line in lines:
            line = line.strip()
            # Filter for likely project names
            if 10 < len(line) < 70:
                line_lower = line.lower()
                # Skip headers and labels
                if 'update' not in line_lower and 'schedule' not in line_lower:
                    if 'road' in line_lower or 'avenue' in line_lower or 'drive' in line_lower:
                        design_capitals.append(line)
                    elif 'park' in line_lower and 'update' not in line_lower:
                        design_capitals.append(line)
                    elif 'canyon' in line_lower:
                        design_capitals.append(line)

# Remove duplicates
unique_projects = []
seen = set()
for proj in design_capitals:
    if proj not in seen:
        seen.add(proj)
        unique_projects.append(proj)

# Filter funding data for amounts > 50000
funding_dict = {}
for rec in funding_data:
    amount = int(rec['Amount'])
    if amount > 50000:
        funding_dict[rec['Project_Name']] = amount

# Match projects
matched = 0

for project in unique_projects:
    proj_lower = str(project).lower().replace(' ', '')
    proj_lower = ''.join(c for c in proj_lower if c.isalnum())
    
    for fund_name in funding_dict.keys():
        fund_lower = str(fund_name).lower().replace(' ', '')
        fund_lower = ''.join(c for c in fund_lower if c.isalnum())
        
        # Check if one contains the other
        if proj_lower in fund_lower or fund_lower in proj_lower:
            matched += 1
            break

# Format result as JSON
result = {'count': matched}
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json'}

exec(code, env_args)
