code = """import json

# Access previous tool results directly as variables
prev_raw = var_call_k9TVZHanAWqmwYhUI85EZ1hU
cpc_defs = var_call_RKK01vv0EBKkkmPo6bGudGBd

# prev_raw may be a JSON string or a dict
if isinstance(prev_raw, str):
    try:
        prev = json.loads(prev_raw)
    except Exception:
        # if it's a printed JSON line, attempt to extract JSON after '__RESULT__:'
        if '__RESULT__:' in prev_raw:
            prev = json.loads(prev_raw.split('__RESULT__:')[-1].strip())
        else:
            raise
elif isinstance(prev_raw, dict):
    prev = prev_raw
else:
    prev = prev_raw

# Build mapping symbol -> title
symbol_to_title = {d['symbol']: d.get('titleFull') for d in cpc_defs}

# Build final mapping
final = {}
for assignee, codes in prev.get('assignee_to_codes', {}).items():
    entries = []
    for code in codes:
        title = symbol_to_title.get(code)
        entries.append({'code': code, 'titleFull': title})
    final[assignee] = entries

print('__RESULT__:')
print(json.dumps(final))"""

env_args = {'var_call_I4hk2pqe9rYk4bmj5JQZTH25': 'file_storage/call_I4hk2pqe9rYk4bmj5JQZTH25.json', 'var_call_RW7kbA3pxaFUAPSgP4dmIzLU': 'file_storage/call_RW7kbA3pxaFUAPSgP4dmIzLU.json', 'var_call_k9TVZHanAWqmwYhUI85EZ1hU': {'assignee_to_codes': {'The US patent filing (application number US-4007205-A)': ['G01V1/01'], 'The US patent application (no. US-201715785968-A) is held by BLOOM ENERGY CORP and': ['H01M8/2425'], 'The US application (ID US-201414520615-A)': ['C30B11/003'], 'SCHOWALTER LEO J': ['H01L21/0262']}, 'codes': ['C30B11/003', 'G01V1/01', 'H01L21/0262', 'H01M8/2425']}, 'var_call_RKK01vv0EBKkkmPo6bGudGBd': [{'symbol': 'G01V1/01', 'titleFull': 'Measuring or predicting earthquakes'}, {'symbol': 'C30B11/003', 'titleFull': 'Heating or cooling of the melt or the crystallised material'}, {'symbol': 'H01M8/2425', 'titleFull': 'High-temperature cells with solid electrolytes'}, {'symbol': 'H01L21/0262', 'titleFull': 'Reduction or decomposition of gaseous compounds, e.g. CVD'}]}

exec(code, env_args)
