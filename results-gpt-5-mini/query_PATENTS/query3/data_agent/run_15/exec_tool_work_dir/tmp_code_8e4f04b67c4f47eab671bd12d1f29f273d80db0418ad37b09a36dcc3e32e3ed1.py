code = """import json
res = json.loads(var_call_nEScUS7euyA0RkHW13nOw9tj)
# Build mapping from cpc code to title
cpc_rows = var_call_6q7Qin7pCKBpno4PZQ3Mv8lB
mapping = {r['symbol']: r['titleFull'] for r in cpc_rows}
output = []
for item in res:
    assignee = item['assignee']
    codes = item['cpc_codes']
    titles = [mapping.get(code, '') for code in codes]
    # pair each assignee with full titles (combine if multiple)
    for t in titles:
        output.append({'assignee': assignee, 'cpc_titleFull': t})
print('__RESULT__:')
print(json.dumps(output))"""

env_args = {'var_call_lFZ8uNxaeU5pX5Ch15ofoav1': 'file_storage/call_lFZ8uNxaeU5pX5Ch15ofoav1.json', 'var_call_X0QLcnAs0WWuHXE5JbGpCQuc': 'file_storage/call_X0QLcnAs0WWuHXE5JbGpCQuc.json', 'var_call_nEScUS7euyA0RkHW13nOw9tj': [{'assignee': 'The US patent filing (application number US-4007205-A)', 'cpc_codes': ['G01V1/01']}, {'assignee': 'The US patent application (no. US-201715785968-A) is held by BLOOM ENERGY CORP and', 'cpc_codes': ['H01M4/9066', 'H01M8/2425']}], 'var_call_6q7Qin7pCKBpno4PZQ3Mv8lB': [{'symbol': 'H01M8/2425', 'titleFull': 'High-temperature cells with solid electrolytes'}, {'symbol': 'H01M4/9066', 'titleFull': 'Metals or alloys specially used in fuel cell operating at high temperature, e.g. SOFC of metal-ceramic composites or mixtures, e.g. cermets'}, {'symbol': 'G01V1/01', 'titleFull': 'Measuring or predicting earthquakes'}]}

exec(code, env_args)
