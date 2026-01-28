code = """import json
import re

# Load data from files
civic_file = locals()['var_functions.query_db:2']
funding_file = locals()['var_functions.query_db:6']

with open(civic_file, 'r') as f:
    civic_docs = json.load(f)

with open(funding_file, 'r') as f:
    funding_data = json.load(f)

# Find disaster projects that mention 2022 in civic documents
potential_projects = set()

for doc in civic_docs:
    text = doc.get('text', '')
    if '2022' in text and ('FEMA' in text or 'CalOES' in text or 'CalJPIA' in text or 'fire' in text):
        # Extract lines that might be disaster projects
        for line in text.split('\n'):
            line = line.strip()
            if len(line) > 10:
                if 'FEMA' in line or 'CalOES' in line or 'CalJPIA' in line:
                    # Clean up the project name
                    clean_name = re.sub(r'^[\d\s\-\•\.]+', '', line)
                    potential_projects.add(clean_name.split('(')[0].strip())

# Also extract project names from funding that are disaster-related
disaster_funding_projects = []
for fund in funding_data:
    name = fund.get('Project_Name', '')
    if 'FEMA' in name or 'CalOES' in name or 'CalJPIA' in name:
        disaster_funding_projects.append(fund)

total_amount = 0
for proj in disaster_funding_projects:
    total_amount += int(proj.get('Amount', 0))

result = f"Total funding: ${total_amount:,}"
print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.list_db:5': ['Funding'], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json'}

exec(code, env_args)
