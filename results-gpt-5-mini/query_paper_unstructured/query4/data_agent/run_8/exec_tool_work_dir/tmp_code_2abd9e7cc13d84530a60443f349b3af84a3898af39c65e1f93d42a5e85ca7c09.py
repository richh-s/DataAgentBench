code = """import json, re
# Load 2016 query results
path_2016 = var_call_gUiVN02qOUhmza0f7d94gstw
with open(path_2016, 'r', encoding='utf-8') as f:
    docs_2016 = json.load(f)

# Load citations aggregated result
cit_path = var_call_q3fRohL6dfYLUpdNcEng2Q3T
with open(cit_path, 'r', encoding='utf-8') as f:
    citations = json.load(f)

# Build citation map
cit_map = {rec.get('title'): int(rec.get('total_citations')) for rec in citations}

# Keywords to identify physical activity domain
keywords = [r'physical activity', r'activity tracking', r'activity tracker', r'physical-activity', r'fitness', r'exercise', r'activity tracking', r'physical activity tracker']

matches = []
for rec in docs_2016:
    text = rec.get('text','')
    filename = rec.get('filename','')
    title = filename[:-4] if filename.endswith('.txt') else filename
    txt_lower = text.lower()
    if any(re.search(k, txt_lower) for k in keywords):
        matches.append(title)

# Deduplicate and sort
matches = sorted(list(dict.fromkeys(matches)))

# Prepare output with citation totals if available
output = []
for t in matches:
    tc = 0
    if t in cit_map:
        tc = cit_map[t]
    else:
        # try case-insensitive match
        for k,v in cit_map.items():
            if k.lower() == t.lower():
                tc = v
                break
    output.append({'title': t, 'total_citations': tc})

print("__RESULT__:")
print(json.dumps(output))"""

env_args = {'var_call_8FYthHJvjhDSYs9BfJ0YBmBx': 'file_storage/call_8FYthHJvjhDSYs9BfJ0YBmBx.json', 'var_call_oOocD6aMAYGkkKk6tGFYyHgQ': [], 'var_call_PXFJFUAWbkatsTSRln5Fzxb6': 'file_storage/call_PXFJFUAWbkatsTSRln5Fzxb6.json', 'var_call_q3fRohL6dfYLUpdNcEng2Q3T': 'file_storage/call_q3fRohL6dfYLUpdNcEng2Q3T.json', 'var_call_AfArtvjDP1c5o2bBahze5i1m': [], 'var_call_gUiVN02qOUhmza0f7d94gstw': 'file_storage/call_gUiVN02qOUhmza0f7d94gstw.json'}

exec(code, env_args)
