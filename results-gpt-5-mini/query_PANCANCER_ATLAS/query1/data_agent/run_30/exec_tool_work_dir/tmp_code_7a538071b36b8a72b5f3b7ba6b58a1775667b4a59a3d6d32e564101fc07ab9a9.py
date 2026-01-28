code = """import json
p = var_call_4ciXcjLXQEDt4Wv6O50QBdNc
with open(p, 'r') as f:
    data = json.load(f)
# find rows mentioning glioma or Lower Grade or Brain or LGG
matches = []
for r in data:
    pd = r.get('Patient_description', '')
    if any(k in pd.lower() for k in ['glioma', 'lower', 'lgg', 'brain']):
        matches.append({'Patient_description': pd, 'histological_type': r.get('histological_type'), 'tumor_tissue_site': r.get('tumor_tissue_site')})
# collect unique histological_type
uniq_hist = sorted(list({(m['histological_type'] if m['histological_type'] is not None else None) for m in matches}))
result = {'matched_count': len(matches), 'unique_histological_type_sample': uniq_hist[:50], 'sample_matches': matches[:10]}
import json as _json
print("__RESULT__:")
print(_json.dumps(result))"""

env_args = {'var_call_712rnEX72Xwagvg93fcaojTw': ['clinical_info'], 'var_call_CdTCNUezwXjwKCtVVMmPXEXH': ['Mutation_Data', 'RNASeq_Expression'], 'var_call_4ciXcjLXQEDt4Wv6O50QBdNc': 'file_storage/call_4ciXcjLXQEDt4Wv6O50QBdNc.json'}

exec(code, env_args)
