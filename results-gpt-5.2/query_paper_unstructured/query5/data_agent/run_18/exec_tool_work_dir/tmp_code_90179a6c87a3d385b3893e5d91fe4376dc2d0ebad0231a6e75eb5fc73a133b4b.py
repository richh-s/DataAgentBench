code = """import json, re

path_docs = var_call_83MpOqyahzqLwNuseTcsNb0P
with open(path_docs, 'r', encoding='utf-8') as f:
    docs = json.load(f)

def venue_guess(text):
    t = (text or '').lower()
    if re.search(r"\bchi\s*'?\s*\d{2}\b", t) or re.search(r"\bproceedings\s+of\s+the\s+chi\b", t) or re.search(r"\bacm\s+chi\b", t):
        return 'CHI'
    if 'ubicomp' in t:
        return 'Ubicomp'
    if 'cscw' in t:
        return 'CSCW'
    if re.search(r"\bdis\s*'?\s*\d{2}\b", t) or 'designing interactive systems' in t:
        return 'DIS'
    return None

from collections import Counter
c = Counter()
for d in docs:
    c[venue_guess(d.get('text',''))] += 1

print('__RESULT__:')
print(json.dumps(c))"""

env_args = {'var_call_xwJY1upmut1pJPLyopTrMQnS': 'file_storage/call_xwJY1upmut1pJPLyopTrMQnS.json', 'var_call_83MpOqyahzqLwNuseTcsNb0P': 'file_storage/call_83MpOqyahzqLwNuseTcsNb0P.json', 'var_call_zgW9zjWAApz4Rsd2InxZkzdh': {'total_citations': 0, 'num_papers': 0}, 'var_call_bpG8GJcobGk6FC7r4GXH89ue': 'file_storage/call_bpG8GJcobGk6FC7r4GXH89ue.json'}

exec(code, env_args)
