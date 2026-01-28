code = """import json

funding_file = var_functions.query_db:2
civic_file = var_functions.query_db:5

with open(funding_file) as f:
    funding_data = json.load(f)

with open(civic_file) as f:
    civic_docs = json.load(f)

# Extract potential project names from civic docs
potential_projects = []

for doc in civic_docs:
    text = doc.get('text', '')
    if 'Capital Improvement Projects' in text and 'Design' in text:
        lines = text.split('\n')
        for line in lines:
            line = line.strip()
            if line and len(line) < 80 and len(line) > 5:
                lower = line.lower()
                if 'update' not in lower and 'schedule' not in lower:
                    if 'road' in lower or 'avenue' in lower or 'park' in lower or 'canyon' in lower or 'drive' in lower:
                        potential_projects.append(line)

unique_projects = list(set(potential_projects))

# Filter funding projects > 50000
funding_lookup = {}
for item in funding_data:
    amt = int(item['Amount'])
    if amt > 50000:
        funding_lookup[item['Project_Name']] = amt

# Match projects by simple comparison
matched = 0
for proj in unique_projects:
    proj_words = set(proj.lower().split())
    for fund_name in funding_lookup.keys():
        fund_words = set(fund_name.lower().split())
        # Check for overlap
        if proj_words & fund_words:
            common = len(proj_words & fund_words)
            if common >= 2:  # At least 2 words match
                matched += 1
                break

print('__RESULT__:')
print(json.dumps({'count': matched}))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json'}

exec(code, env_args)
