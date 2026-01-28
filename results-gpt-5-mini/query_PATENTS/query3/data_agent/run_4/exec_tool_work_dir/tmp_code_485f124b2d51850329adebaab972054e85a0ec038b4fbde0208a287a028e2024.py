code = """import json
# load previous processed mapping
var = var_call_jvdn5OSXKL0Yji7XObXtXMF4
mapping = json.loads(var)

# load cpc query result
with open(var_call_Lj8SYLZddyvG5NfcP22ckYz6, 'r', encoding='utf-8') as f:
    cpc_rows = json.load(f)

symbol_to_title = {r['symbol']: r.get('titleFull') for r in cpc_rows}

# build final answers excluding UNIV CALIFORNIA itself (per user request)
results = []
for assignee, codes in mapping['assignee_to_codes'].items():
    if assignee.upper().strip() == 'UNIV CALIFORNIA':
        continue
    for code in codes:
        title = symbol_to_title.get(code)
        results.append({'assignee': assignee, 'cpc': code, 'titleFull': title})

# If results empty, prepare message
if not results:
    final = {'message': 'No citing assignees (excluding UNIV CALIFORNIA) found in the matched records.'}
else:
    final = results

print('__RESULT__:')
print(json.dumps(final))"""

env_args = {'var_call_uAbbEpB6ZBwfzaiEz02vBDm9': 'file_storage/call_uAbbEpB6ZBwfzaiEz02vBDm9.json', 'var_call_jvdn5OSXKL0Yji7XObXtXMF4': {'assignee_to_codes': {'UNIV CALIFORNIA': ['C12N15/111']}, 'codes': ['C12N15/111']}, 'var_call_Lj8SYLZddyvG5NfcP22ckYz6': [{'symbol': 'C12N15/111', 'titleFull': 'General methods applicable to biologically active non-coding nucleic acids'}]}

exec(code, env_args)
