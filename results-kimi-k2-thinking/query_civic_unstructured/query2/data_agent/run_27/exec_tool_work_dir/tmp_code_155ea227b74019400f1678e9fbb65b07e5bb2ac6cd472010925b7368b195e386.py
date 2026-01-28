code = """import json, re

# Load data from files
civic_docs_path = locals()['var_functions.query_db:16']
funding_path = locals()['var_functions.query_db:17']

with open(civic_docs_path) as f:
    civic_docs = json.load(f)
with open(funding_path) as f:
    funding_data = json.load(f)

# Extract project information
total_funding = 0
funded_projects = []

for doc in civic_docs:
    text = doc['text']
    lines = text.split('\n')
    
    # Look for completed park projects in 2022
    for i, line in enumerate(lines):
        if 'completed' in line.lower() and '2022' in line:
            # Find project name (previous meaningful line)
            proj_name = None
            for j in range(i-1, max(0,i-8), -1):
                prev = lines[j].strip()
                if prev and not prev.startswith('(') and len(prev) > 5:
                    proj_name = prev
                    break
            
            if proj_name:
                # Clean project name
                proj_name = re.sub(r'^[•◦\s]+', '', proj_name).strip()
                if 'park' in proj_name.lower():
                    # Find matching funding
                    for fund in funding_data:
                        fund_name = fund['Project_Name']
                        if (proj_name.lower() in fund_name.lower() or 
                            fund_name.lower() in proj_name.lower()):
                            amount = int(fund['Amount'])
                            total_funding += amount
                            funded_projects.append(proj_name)

# Create result
result = {"total_funding": total_funding, "projects": funded_projects}

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:3': 'file_storage/functions.query_db:3.json', 'var_functions.query_db:16': 'file_storage/functions.query_db:16.json', 'var_functions.query_db:17': 'file_storage/functions.query_db:17.json'}

exec(code, env_args)
