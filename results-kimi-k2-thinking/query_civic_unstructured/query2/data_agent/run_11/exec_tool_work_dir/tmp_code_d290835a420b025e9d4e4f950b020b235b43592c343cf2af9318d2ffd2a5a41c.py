code = """import json

# Get civic documents from storage
civic_docs = var_functions.query_db:60
with open(civic_docs) as f:
    docs = json.load(f)

# Get funding data from storage
funding = var_functions.query_db:48
with open(funding) as f:
    funds = json.load(f)

# Find completed park projects from 2022
park_2022 = []

for doc in docs:
    t = doc.get('text','')
    if 'Park' in t and '2022' in t and ('completed' in t.lower() or 'completion' in t.lower()):
        lines = t.split('\n')
        for line in lines:
            line = line.strip()
            if 'Park' in line and len(line) > 10:
                # Skip headers
                if 'Subject' in line or 'Page' in line or 'Item' in line or line.startswith('('):
                    continue
                # Look for completion status nearby
                next_part = '\n'.join(lines[max(0, lines.index(line)-2):lines.index(line)+10])
                if 'completed' in next_part.lower() and '2022' in next_part:
                    park_2022.append(line)

unique_parks = list(set(park_2022))

# Find funding matches
funding_total = 0
funding_details = []

for proj in unique_parks:
    for rec in funds:
        name = rec.get('Project_Name','')
        if proj.lower() in name.lower():
            amt = int(rec.get('Amount',0))
            funding_total += amt
            funding_details.append([proj, name, amt])

print('__RESULT__:')
print(json.dumps({'project_count': len(unique_parks), 'total_funding': funding_total, 'projects': unique_parks, 'funding_matches': funding_details}))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.list_db:2': ['civic_docs'], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.execute_python:12': {'civic_docs_count': 38, 'funding_records_count': 38, 'status': 'Data loaded successfully'}, 'var_functions.query_db:48': 'file_storage/functions.query_db:48.json', 'var_functions.query_db:60': 'file_storage/functions.query_db:60.json'}

exec(code, env_args)
