code = """import json

# Load previous execute_python result file (contains JSON mapping)
with open(var_call_k9TVZHanAWqmwYhUI85EZ1hU, 'r', encoding='utf-8') as f:
    prev = json.load(f)

# CPC definitions result is directly available as a Python list variable
cpc_defs = var_call_RKK01vv0EBKkkmPo6bGudGBd

# Build a dict from symbol to title
symbol_to_title = {d['symbol']: d['titleFull'] for d in cpc_defs}

# Build final plain-text answer
lines = []
for assignee, codes in prev['assignee_to_codes'].items():
    titles = []
    for code in codes:
        title = symbol_to_title.get(code)
        if title:
            titles.append(title)
        else:
            titles.append(f"(no title found for {code})")
    line = f"{assignee} — {"; ".join(titles)}"
    lines.append(line)

answer_text = "\n".join(lines)

print('__RESULT__:')
print(json.dumps(answer_text))"""

env_args = {'var_call_I4hk2pqe9rYk4bmj5JQZTH25': 'file_storage/call_I4hk2pqe9rYk4bmj5JQZTH25.json', 'var_call_RW7kbA3pxaFUAPSgP4dmIzLU': 'file_storage/call_RW7kbA3pxaFUAPSgP4dmIzLU.json', 'var_call_k9TVZHanAWqmwYhUI85EZ1hU': {'assignee_to_codes': {'The US patent filing (application number US-4007205-A)': ['G01V1/01'], 'The US patent application (no. US-201715785968-A) is held by BLOOM ENERGY CORP and': ['H01M8/2425'], 'The US application (ID US-201414520615-A)': ['C30B11/003'], 'SCHOWALTER LEO J': ['H01L21/0262']}, 'codes': ['C30B11/003', 'G01V1/01', 'H01L21/0262', 'H01M8/2425']}, 'var_call_RKK01vv0EBKkkmPo6bGudGBd': [{'symbol': 'G01V1/01', 'titleFull': 'Measuring or predicting earthquakes'}, {'symbol': 'C30B11/003', 'titleFull': 'Heating or cooling of the melt or the crystallised material'}, {'symbol': 'H01M8/2425', 'titleFull': 'High-temperature cells with solid electrolytes'}, {'symbol': 'H01L21/0262', 'titleFull': 'Reduction or decomposition of gaseous compounds, e.g. CVD'}]}

exec(code, env_args)
