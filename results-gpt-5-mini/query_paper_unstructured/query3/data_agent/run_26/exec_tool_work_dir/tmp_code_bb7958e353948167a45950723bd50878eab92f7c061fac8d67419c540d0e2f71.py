code = """import json
import re
# Load the Mongo query result from file path variable provided by previous tool
path = var_call_qdPezJyiGQ882BWNhhrL3cAR
with open(path, 'r', encoding='utf-8') as f:
    records = json.load(f)

results = []
for r in records:
    filename = r.get('filename','')
    title = filename[:-4] if filename.lower().endswith('.txt') else filename
    text = r.get('text','')
    if not text:
        continue
    # check for 'empirical' contribution anywhere
    if re.search(r'\bempirical\b', text, re.IGNORECASE) is None:
        continue
    # search for publication year in the header (first 2000 chars), prefer years 2017-2024
    header = text[:2000]
    m = re.search(r'20(1[7-9]|2[0-4])', header)
    year = None
    if m:
        year = int(m.group(0))
    else:
        # search whole text for any 2017-2024 and pick the smallest occurrence position
        m_all = list(re.finditer(r'20(1[7-9]|2[0-4])', text))
        if m_all:
            # choose the one with smallest start position
            m_all_sorted = sorted(m_all, key=lambda x: x.start())
            year = int(m_all_sorted[0].group(0))
    if year is None:
        continue
    if year <= 2016:
        continue
    results.append({'title': title, 'year': year})

# Remove duplicates (if any), keep earliest year if duplicates
unique = {}
for r in results:
    t = r['title']
    y = r['year']
    if t not in unique or y < unique[t]:
        unique[t] = y
out = [{'title': t, 'year': unique[t]} for t in sorted(unique.keys())]

print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_a50SROerJh7cg2CaFPe5HUSq': ['paper_docs'], 'var_call_8DV18aV221C1QGLy9PTJoWRD': ['Citations', 'sqlite_sequence'], 'var_call_qdPezJyiGQ882BWNhhrL3cAR': 'file_storage/call_qdPezJyiGQ882BWNhhrL3cAR.json'}

exec(code, env_args)
