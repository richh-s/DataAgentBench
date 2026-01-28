code = """import json

# The variables contain file paths
with open(var_functions.query_db:2, 'r') as f:
    docs = json.load(f)

with open(var_functions.query_db:12, 'r') as f:
    fund = json.load(f)

print('Civic docs:', len(docs))
print('Funding records:', len(fund))

# Build funding lookup
funding = {}
for item in fund:
    funding[item['Project_Name']] = int(item['Amount'])

# Find projects that started in Spring 2022
matched = []
for doc in docs:
    text = doc.get('text', '').lower()
    if '2022' in text:
        # Look for spring or spring months
        has_spring = ('spring' in text) or ('march' in text) or ('april' in text) or ('may' in text)
        
        if has_spring:
            # Extract potential project names
            for line in doc.get('text', '').split('\n'):
                clean = line.strip()
                # Skip lines that are likely not project names
                if len(clean) > 15 and not clean.startswith('(') and clean.startswith('2022'):
                    # Check if this matches a funded project
                    if clean in funding and not any(m[0] == clean for m in matched):
                        matched.append((clean, funding[clean]))

# Also check for Morning View specifically
morning_view = '2022 Morning View Resurfacing & Storm Drain Improvements'
if morning_view in funding and not any(m[0] == morning_view for m in matched):
    matched.append((morning_view, funding[morning_view]))

total_count = len(matched)
total_funding = sum(m[1] for m in matched)

print('Total Spring 2022 projects:', total_count)
print('Total funding:', total_funding)

result = {'count': total_count, 'total_funding': total_funding}
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json'}

exec(code, env_args)
