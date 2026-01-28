code = """import json
import re

# Access data from storage
civic_docs = locals()['var_functions.query_db:2']
funding_records = locals()['var_functions.query_db:5']

# Build funding lookup dictionary
funding_dict = {}
for record in funding_records:
    name = record.get('Project_Name', '').lower()
    amount = int(record.get('Amount', 0))
    if name and amount > 0:
        funding_dict[name] = amount

# Find disaster projects in text
all_disaster_names = set()
for doc in civic_docs:
    text = doc.get('text', '')
    lines = text.split('\n')
    for line in lines:
        line = line.strip()
        if any(x in line.lower() for x in ['fema', 'caljpia', 'caloes']):
            if len(line) > 5 and not line.startswith('('):
                all_disaster_names.add(line)

# Check for 2022 dates
disaster_2022 = []
for name in all_disaster_names:
    # Look through all documents for this project name and 2022 dates
    for doc in civic_docs:
        text = doc.get('text', '')
        if name in text and '2022' in text:
            # Check if this project has a 2022 date
            if re.search(r'2022', text):
                disaster_2022.append(name)
                break

# Remove duplicates
disaster_2022 = list(set(disaster_2022))

# Match with funding
total = 0
matches = []
for proj in disaster_2022:
    proj_lower = proj.lower()
    if proj_lower in funding_dict:
        amount = funding_dict[proj_lower]
        total += amount
        matches.append({"project": proj, "amount": amount})
    else:
        # Fuzzy match
        for fund_name, amount in funding_dict.items():
            if proj_lower in fund_name or fund_name in proj_lower:
                total += amount
                matches.append({"project": proj, "matched_funding": fund_name, "amount": amount})
                break

print('__RESULT__:')
print(json.dumps({"total_funding": total, "matched_projects": matches, "count": len(disaster_2022)}))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json'}

exec(code, env_args)
