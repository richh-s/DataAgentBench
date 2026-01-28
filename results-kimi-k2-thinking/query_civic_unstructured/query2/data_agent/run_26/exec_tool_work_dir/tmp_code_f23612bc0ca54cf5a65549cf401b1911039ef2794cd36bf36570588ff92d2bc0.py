code = """import json

# Load data from storage variables
civic_docs = locals().get('var_functions.query_db:20')
funding_recs = locals().get('var_functions.query_db:5')

funding_map = {}
for rec in funding_recs:
    funding_map[rec['Project_Name']] = int(rec['Amount'])

# Search for park projects completed in 2022
park_projs = []

for doc in civic_docs:
    text = doc['text']
    if text.find('park') >= 0 or text.find('Park') >= 0:
        lines = text.splitlines()
        for i in range(len(lines)):
            line = lines[i].strip()
            if len(line) > 10 and (line.lower().find('park') >= 0 or line.lower().find('playground') >= 0):
                # Check context for completion in 2022
                context_start = max(0, i-8)
                context_end = min(len(lines), i+8)
                context_parts = []
                for j in range(context_start, context_end):
                    context_parts.append(lines[j])
                context = ' '.join(context_parts)
                
                if context.lower().find('completed') >= 0 and context.lower().find('2022') >= 0:
                    clean = line.replace('(cid:190)', '').replace('(cid:131)', '').strip()
                    park_projs.append(clean)

# Remove duplicates
unique = list(set(park_projs))

# Calculate total funding
total = 0
for proj in unique:
    if proj in funding_map:
        total += funding_map[proj]
    else:
        # Try partial matches
        proj_lower = proj.lower()
        for funded_name in funding_map:
            if proj_lower in funded_name.lower():
                total += funding_map[funded_name]
                break

print('Total funding:', total)
print('Projects found:', len(unique))

result_value = '$' + str(total)
print('__RESULT__:')
print(json.dumps(result_value))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.list_db:2': ['civic_docs'], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.query_db:20': 'file_storage/functions.query_db:20.json'}

exec(code, env_args)
