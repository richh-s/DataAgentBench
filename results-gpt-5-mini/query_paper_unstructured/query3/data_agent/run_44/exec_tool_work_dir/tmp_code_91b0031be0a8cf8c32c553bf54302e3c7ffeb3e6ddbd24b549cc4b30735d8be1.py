code = """import json, re
# Load data from tool results stored in files
with open(var_call_alz8YsLna785rrDdT0mcZbf1, 'r', encoding='utf-8') as f:
    docs = json.load(f)
with open(var_call_X2192vFUq5O3YNmHFwyYpOFW, 'r', encoding='utf-8') as f:
    citations = json.load(f)

# Build citation map title -> total_citations (int)
cit_map = {}
for rec in citations:
    t = rec.get('title')
    # citation total might be string, convert safely
    try:
        c = int(rec.get('total_citations'))
    except:
        try:
            c = int(float(rec.get('total_citations')))
        except:
            c = None
    cit_map[t] = c

results = []
for d in docs:
    filename = d.get('filename','')
    title = filename.rsplit('.txt',1)[0]
    text = d.get('text','') or ''
    # find year: prefer in first 400 chars
    year = None
    m = re.search(r"\b(19\d{2}|20\d{2})\b", text[:400])
    if m:
        year = int(m.group(0))
    else:
        m2 = re.search(r"\b(19\d{2}|20\d{2})\b", text)
        if m2:
            year = int(m2.group(0))
    # check empirical in text (case-insensitive)
    is_empirical = 'empirical' in text.lower()
    if year is not None and year > 2016 and is_empirical:
        # get citation count if available
        total_cit = cit_map.get(title)
        # If citation not found, leave as None
        results.append({"title": title, "total_citations": total_cit})

# Sort results by total_citations descending (None at end), then title
def sort_key(x):
    return (-(x['total_citations'] or 0), x['title'])
results_sorted = sorted(results, key=sort_key)

import json
print("__RESULT__:")
print(json.dumps(results_sorted))"""

env_args = {'var_call_alz8YsLna785rrDdT0mcZbf1': 'file_storage/call_alz8YsLna785rrDdT0mcZbf1.json', 'var_call_X2192vFUq5O3YNmHFwyYpOFW': 'file_storage/call_X2192vFUq5O3YNmHFwyYpOFW.json'}

exec(code, env_args)
