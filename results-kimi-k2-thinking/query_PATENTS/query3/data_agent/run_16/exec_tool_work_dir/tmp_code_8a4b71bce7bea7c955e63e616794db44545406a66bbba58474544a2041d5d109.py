code = """import json
import pandas as pd

with open('/tmp/tmp0q5j9s0s.json', 'r') as f:
    full_data = json.load(f)

with open('/tmp/tmpk2i1u7_p.json', 'r') as f:
    uc_data = json.load(f)

print('Total records:', len(full_data))
print('UC records:', len(uc_data))

print('Sample Patents_info:')
print(uc_data[0]['Patents_info'])

print('Sample citation:')
citation_text = uc_data[0]['citation']
print(citation_text[:200] + '...' if len(citation_text) > 200 else citation_text)

cpc_field = uc_data[0].get('cpc', 'None')
print('CPC field type:', type(cpc_field))
if isinstance(cpc_field, str):
    print('CPC preview:', cpc_field[:200])
else:
    print('CPC value:', cpc_field)

result = {'total': len(full_data), 'uc': len(uc_data)}
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json'}

exec(code, env_args)
