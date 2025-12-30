code = """import json, re
from pathlib import Path

# Load full results
with open(var_call_BavLPIaAliFtj9dVy0rO62yv, 'r') as f:
    papers = json.load(f)
with open(var_call_RRzIjmVRfGRo2k5KuwNJjueR, 'r') as f:
    citations = json.load(f)

# Extract title (filename without .txt), year, and detect physical activity domain
records = []
for doc in papers:
    filename = doc.get('filename','')
    text = doc.get('text','') or ''
    title = re.sub(r"\.txt$","", filename)
    # Heuristic: year 2016 appears near venue header or copyright
    m = re.search(r"20(1[0-9]|20)", text)
    year = int(m.group(0)) if m else None
    domain = 'physical activity' if re.search(r"physical activity", text, re.I) else None
    records.append({"title": title, "year": year, "domain": domain})

# Filter to 2016 and physical activity
pa2016_titles = {r['title'] for r in records if r['year'] == 2016 and r['domain'] == 'physical activity'}

# Build citation lookup
cit_lut = {}
for row in citations:
    t = row['title']
    if t.startswith('"') and t.endswith('"'):
        t = t[1:-1]
    cit_lut[t] = int(row['total_citations'])

result = []
for title in sorted(pa2016_titles):
    result.append({"title": title, "total_citations": cit_lut.get(title, 0)})

out = json.dumps(result)
print("__RESULT__:")
print(out)"""

env_args = {'var_call_BavLPIaAliFtj9dVy0rO62yv': 'file_storage/call_BavLPIaAliFtj9dVy0rO62yv.json', 'var_call_RRzIjmVRfGRo2k5KuwNJjueR': 'file_storage/call_RRzIjmVRfGRo2k5KuwNJjueR.json'}

exec(code, env_args)
