code = """import json
# load previous results
res_path = var_call_zO3Npg4VCbvpq3cvNhtRk7tp
with open(res_path, 'r', encoding='utf-8') as f:
    data = json.load(f)

out = []
for r in data:
    pname = (r.get('Project_Name') or '').lower()
    fsrc = (r.get('Funding_Source') or '').lower()
    status = r.get('Status')
    if 'fema' in pname or 'fema' in fsrc or 'emergency' in pname or 'emergency' in fsrc:
        out.append({'Project_Name': r.get('Project_Name'), 'Funding_Source': r.get('Funding_Source'), 'Amount': r.get('Amount'), 'Status': status})

# Also include projects where name contains '(FEMA' capitalizations
# (already covered by lowercasing)
print("__RESULT__:")
print(json.dumps(out))"""

env_args = {'var_call_Ncx1OMYqOJMCIzxbwcw2SGP4': 'file_storage/call_Ncx1OMYqOJMCIzxbwcw2SGP4.json', 'var_call_bPrtG60ziMydChYoQ8enDdFc': 'file_storage/call_bPrtG60ziMydChYoQ8enDdFc.json', 'var_call_zO3Npg4VCbvpq3cvNhtRk7tp': 'file_storage/call_zO3Npg4VCbvpq3cvNhtRk7tp.json'}

exec(code, env_args)
