code = """import json
data = var_call_sav05sLYsUhVocITeKBvTyAS
if isinstance(data, str):
    with open(data, 'r') as f:
        records = json.load(f)
else:
    records = data
out = []
for r in records:
    name = r.get('Project_Name','')
    source = r.get('Funding_Source','')
    combined = (str(name) + ' ' + str(source)).lower()
    if 'fema' in combined or 'emergency' in combined:
        out.append({'Project_Name': name, 'Funding_Source': source, 'Amount': r.get('Amount'), 'Status': r.get('Status')})
print("__RESULT__:")
print(json.dumps(out))"""

env_args = {'var_call_igZlSbiLWjIZqU8d0FYKe2z4': 'file_storage/call_igZlSbiLWjIZqU8d0FYKe2z4.json', 'var_call_cQ1zQFelFE9RnIqGqbRuGGrR': 'file_storage/call_cQ1zQFelFE9RnIqGqbRuGGrR.json', 'var_call_sav05sLYsUhVocITeKBvTyAS': 'file_storage/call_sav05sLYsUhVocITeKBvTyAS.json'}

exec(code, env_args)
