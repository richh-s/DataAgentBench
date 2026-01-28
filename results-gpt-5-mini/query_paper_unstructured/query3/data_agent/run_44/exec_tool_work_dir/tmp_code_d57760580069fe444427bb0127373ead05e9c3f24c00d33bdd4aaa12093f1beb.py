code = """import json, re
with open(var_call_alz8YsLna785rrDdT0mcZbf1, 'r', encoding='utf-8') as f:
    docs = json.load(f)
with open(var_call_X2192vFUq5O3YNmHFwyYpOFW, 'r', encoding='utf-8') as f:
    citations = json.load(f)

cit_map = {}
for rec in citations:
    t = rec.get('title')
    try:
        c = int(rec.get('total_citations'))
    except:
        try:
            c = int(float(rec.get('total_citations')))
        except:
            c = None
    cit_map[t] = c

keywords = ['empirical', 'empiric', 'empirically', 'user study', 'field study', 'laboratory study', 'lab study', 'participant', 'participants', 'we conducted', 'we ran a study', 'study recruited', 'n=']

results = []
for d in docs:
    filename = d.get('filename','')
    title = filename.rsplit('.txt',1)[0]
    text = (d.get('text') or '').lower()
    # find year anywhere
    year = None
    m = re.search(r"\b(19\d{2}|20\d{2})\b", text)
    if m:
        year = int(m.group(0))
    # check keywords
    has_empirical = any(k in text for k in keywords)
    if year is not None and year > 2016 and has_empirical:
        total_cit = cit_map.get(title)
        results.append({"title": title, "total_citations": total_cit, "year": year})

# sort by total_citations desc, None last
results_sorted = sorted(results, key=lambda x: (-(x['total_citations'] or 0), x['title']))
print('__RESULT__:')
print(json.dumps(results_sorted))"""

env_args = {'var_call_alz8YsLna785rrDdT0mcZbf1': 'file_storage/call_alz8YsLna785rrDdT0mcZbf1.json', 'var_call_X2192vFUq5O3YNmHFwyYpOFW': 'file_storage/call_X2192vFUq5O3YNmHFwyYpOFW.json', 'var_call_Ipk2HEXmxO0XlFyQxPkH1tPV': []}

exec(code, env_args)
