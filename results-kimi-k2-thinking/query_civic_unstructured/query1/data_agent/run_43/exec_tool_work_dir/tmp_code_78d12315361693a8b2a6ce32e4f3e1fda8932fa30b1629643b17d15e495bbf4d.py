code = """import json
import os

# Load funding data
funding_path = var_functions.query_db:60
funding_data = json.load(open(funding_path))

# Load civic documents
civic_path = var_functions.query_db:6
civic_docs = json.load(open(civic_path))

# Build funding map
funding_map = {}
for item in funding_data:
    funding_map[item['Project_Name']] = int(item['Amount'])

# Find design projects
all_design = set()
for doc in civic_docs:
    text = doc.get('text', '')
    if 'Capital Improvement Projects' in text and 'Design' in text:
        for line in text.split('\n'):
            line = line.strip()
            if line and len(line) > 9 and line[0].isalpha():
                all_design.add(line)

# Count matches
matched = 0
for proj in all_design:
    for funded in funding_map:
        if funding_map[funded] > 50000:
            p = proj.lower()
            f = funded.lower()
            if p in f or f in p:
                if abs(len(proj) - len(funded)) < 40:
                    matched += 1
                    break

result = dict(count=matched)
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.list_db:2': ['Funding'], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:60': 'file_storage/functions.query_db:60.json'}

exec(code, env_args)
