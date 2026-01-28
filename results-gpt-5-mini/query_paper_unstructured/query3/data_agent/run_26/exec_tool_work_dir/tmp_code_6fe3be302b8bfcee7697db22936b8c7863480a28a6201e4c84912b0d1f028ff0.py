code = """import json, re
path = var_call_mB4p9sAq4lpFrwci3VV5sX6H
with open(path, 'r', encoding='utf-8') as f:
    records = json.load(f)

results = []
for r in records:
    filename = r.get('filename','')
    title = filename[:-4] if filename.lower().endswith('.txt') else filename
    text = r.get('text','')
    if not text:
        continue
    # Check for 'empirical' anywhere
    if re.search(r'\bempirical\b', text, re.IGNORECASE) is None:
        continue
    # Find publication year occurrence (prefer earlier in text)
    years = list(re.finditer(r'20(1[7-9]|2[0-4])', text))
    year = None
    if years:
        # pick the earliest occurrence
        y = min(years, key=lambda m: m.start())
        year = int(y.group(0))
    # If no year, skip
    if year is None:
        continue
    if year <= 2016:
        continue
    results.append({'title': title, 'year': year})

# Deduplicate, keep smallest year if duplicates
unique = {}
for r in results:
    t = r['title']
    y = r['year']
    if t not in unique or y < unique[t]:
        unique[t] = y
out = [{'title': t, 'year': unique[t]} for t in sorted(unique.keys())]

print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_a50SROerJh7cg2CaFPe5HUSq': ['paper_docs'], 'var_call_8DV18aV221C1QGLy9PTJoWRD': ['Citations', 'sqlite_sequence'], 'var_call_qdPezJyiGQ882BWNhhrL3cAR': 'file_storage/call_qdPezJyiGQ882BWNhhrL3cAR.json', 'var_call_bMZXN2lTUc5GRRtVj2EHltEd': [], 'var_call_mB4p9sAq4lpFrwci3VV5sX6H': 'file_storage/call_mB4p9sAq4lpFrwci3VV5sX6H.json'}

exec(code, env_args)
