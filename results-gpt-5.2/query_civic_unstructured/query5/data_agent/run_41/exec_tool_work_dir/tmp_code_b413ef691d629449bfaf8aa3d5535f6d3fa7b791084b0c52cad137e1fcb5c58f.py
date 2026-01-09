code = """import json, re
with open(var_call_z2Qekco9lHo7XagX0PqaxbPV,'r') as f:
    docs=json.load(f)
texts='|'.join(d.get('text','') for d in docs)
print('__RESULT__:')
print(json.dumps({'has_disaster': bool(re.search(r'Disaster', texts, flags=re.IGNORECASE)), 'len': len(texts)}))"""

env_args = {'var_call_MOqftnFibvUkFDBpZBPW0v1V': ['Funding'], 'var_call_1mO1zBqsDiMHvjH7DlP4LYVA': 'file_storage/call_1mO1zBqsDiMHvjH7DlP4LYVA.json', 'var_call_YcNxcpvNJ1ntUMcyfXH3rkSl': ['civic_docs'], 'var_call_0YuvyDk8s1YDWSMEFutJShlK': 'file_storage/call_0YuvyDk8s1YDWSMEFutJShlK.json', 'var_call_z2Qekco9lHo7XagX0PqaxbPV': 'file_storage/call_z2Qekco9lHo7XagX0PqaxbPV.json', 'var_call_ZthsKbieV1eqdO7yBF6vIdJR': {'n': 500}, 'var_call_igYpGVqfnS8uWdcfhdZ0AuSw': {'docs': 5, 'first_filename': 'malibucity_agenda__01262022-1835.txt', 'first_len': 16311}}

exec(code, env_args)
