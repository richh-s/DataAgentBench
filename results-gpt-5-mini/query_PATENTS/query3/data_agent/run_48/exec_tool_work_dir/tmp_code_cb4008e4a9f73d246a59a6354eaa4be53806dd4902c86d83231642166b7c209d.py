code = """import json

# Load previous mapping from file
with open(var_call_k9TVZHanAWqmwYhUI85EZ1hU, 'r', encoding='utf-8') as f:
    prev = json.load(f)

# cpc definitions available as variable
cpc_defs = var_call_RKK01vv0EBKkkmPo6bGudGBd

# Build mapping symbol -> titleFull
symbol_to_title = {item['symbol']: item.get('titleFull') for item in cpc_defs}

# Build final mapping: assignee -> list of titleFull strings
final_mapping = {}
for assignee, codes in prev.get('assignee_to_codes', {}).items():
    titles = []
    for code in codes:
        title = symbol_to_title.get(code)
        if title is None:
            title = None
        titles.append({'code': code, 'titleFull': title})
    final_mapping[assignee] = titles

print('__RESULT__:')
print(json.dumps(final_mapping))"""

env_args = {'var_call_I4hk2pqe9rYk4bmj5JQZTH25': 'file_storage/call_I4hk2pqe9rYk4bmj5JQZTH25.json', 'var_call_RW7kbA3pxaFUAPSgP4dmIzLU': 'file_storage/call_RW7kbA3pxaFUAPSgP4dmIzLU.json', 'var_call_k9TVZHanAWqmwYhUI85EZ1hU': {'assignee_to_codes': {'The US patent filing (application number US-4007205-A)': ['G01V1/01'], 'The US patent application (no. US-201715785968-A) is held by BLOOM ENERGY CORP and': ['H01M8/2425'], 'The US application (ID US-201414520615-A)': ['C30B11/003'], 'SCHOWALTER LEO J': ['H01L21/0262']}, 'codes': ['C30B11/003', 'G01V1/01', 'H01L21/0262', 'H01M8/2425']}, 'var_call_RKK01vv0EBKkkmPo6bGudGBd': [{'symbol': 'G01V1/01', 'titleFull': 'Measuring or predicting earthquakes'}, {'symbol': 'C30B11/003', 'titleFull': 'Heating or cooling of the melt or the crystallised material'}, {'symbol': 'H01M8/2425', 'titleFull': 'High-temperature cells with solid electrolytes'}, {'symbol': 'H01L21/0262', 'titleFull': 'Reduction or decomposition of gaseous compounds, e.g. CVD'}]}

exec(code, env_args)
