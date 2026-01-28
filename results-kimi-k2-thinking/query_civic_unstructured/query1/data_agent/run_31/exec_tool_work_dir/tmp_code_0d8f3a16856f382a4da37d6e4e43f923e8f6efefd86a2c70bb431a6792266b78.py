code = """import json

funding_file = var_functions.query_db:2
civic_file = var_functions.query_db:5

with open(funding_file) as f:
    funding_data = json.load(f)

with open(civic_file) as f:
    civic_docs = json.load(f)

# Extract project names from civic docs (capital projects in design)
project_candidates = []

for doc in civic_docs:
    if isinstance(doc, dict) and 'text' in doc:
        text = doc['text']
        if 'Capital' in text and 'Design' in text:
            lines = text.split('\n')
            for line in lines:
                line = line.strip()
                if not line.startswith('(') and 10 < len(line) < 70:
                    lower_line = line.lower()
                    if 'update' not in lower_line and 'schedule' not in lower_line:
                        if 'road' in lower_line or 'avenue' in lower_line or 'park' in lower_line or 'canyon' in lower_line:
                            project_candidates.append(line)

# Remove duplicates
unique_candidates = list(set(project_candidates))

# Build lookup of funding amounts > 50000
funding_lookup = {}
for item in funding_data:
    amount = int(item['Amount'])
    if amount > 50000:
        funding_lookup[item['Project_Name']] = amount

# Match projects
matches = 0
for candidate in unique_candidates:
    candidate_lower = candidate.lower().replace(' ', '')
    for fund_name, fund_amount in funding_lookup.items():
        fund_name_lower = fund_name.lower().replace(' ', '')
        if candidate_lower in fund_name_lower or fund_name_lower in candidate_lower:
            matches += 1
            break

result = {'count': matches}
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json'}

exec(code, env_args)
