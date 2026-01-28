code = """import json, re
with open(var_call_alz8YsLna785rrDdT0mcZbf1, 'r', encoding='utf-8') as f:
    docs = json.load(f)

out = []
for d in docs:
    filename = d.get('filename','')
    title = filename.rsplit('.txt',1)[0]
    text = d.get('text','') or ''
    low = text.lower()
    # find first year occurrence
    m = re.search(r"\b(19\d{2}|20\d{2})\b", text)
    year = int(m.group(0)) if m else None
    has_empirical = 'empirical' in low
    has_n = bool(re.search(r"\bn\s*=\s*\d+\b", low))
    out.append({"title": title, "year": year, "has_empirical": has_empirical, "has_n_pattern": has_n})

# filter those with year >2016
filtered = [o for o in out if o['year'] and o['year']>2016]
# limit to 200 entries
filtered = filtered[:200]
print('__RESULT__:')
print(json.dumps(filtered))"""

env_args = {'var_call_alz8YsLna785rrDdT0mcZbf1': 'file_storage/call_alz8YsLna785rrDdT0mcZbf1.json', 'var_call_X2192vFUq5O3YNmHFwyYpOFW': 'file_storage/call_X2192vFUq5O3YNmHFwyYpOFW.json', 'var_call_Ipk2HEXmxO0XlFyQxPkH1tPV': [], 'var_call_CdDClq1sR0DbU3AQURW5XmHj': []}

exec(code, env_args)
