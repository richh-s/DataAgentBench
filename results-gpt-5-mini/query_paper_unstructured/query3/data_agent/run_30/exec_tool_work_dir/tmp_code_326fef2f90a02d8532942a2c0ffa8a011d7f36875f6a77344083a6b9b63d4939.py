code = """import json, re
with open(var_call_UMpMrz4lCiA9igDmtZ2PavIv, 'r', encoding='utf-8') as f:
    docs = json.load(f)
out = []
for d in docs[:50]:
    fn = d.get('filename','')
    text = d.get('text','') or ''
    low = text.lower()
    emp = 'empirical' in low
    # find year
    year = None
    m = re.search(r'\b(20[0-9]{2})\b', text)
    if m:
        year = int(m.group(0))
    snippet = text[:200].replace('\n', ' ')
    out.append({'filename': fn, 'year_found': year, 'empirical_present': emp, 'text_snippet': snippet})

print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_oZwUttyf1z8kVala5AUJPXmA': ['paper_docs'], 'var_call_grasnMaKKZOf38O99JQmcWKN': ['Citations', 'sqlite_sequence'], 'var_call_UMpMrz4lCiA9igDmtZ2PavIv': 'file_storage/call_UMpMrz4lCiA9igDmtZ2PavIv.json', 'var_call_ZrFlxzUHvMfCckRIwz8q3PLt': 'file_storage/call_ZrFlxzUHvMfCckRIwz8q3PLt.json', 'var_call_k80NjCbEIROUNEXL9cmvYB37': []}

exec(code, env_args)
