code = """import json, re

# Load files
with open(var_call_IgMGRy82fd6CM3YSp579uesP, 'r', encoding='utf-8') as f:
    docs = json.load(f)
with open(var_call_bj5IIhfHCAcIpURljX3hdbZG, 'r', encoding='utf-8') as f:
    citations = json.load(f)

# Helpers
def normalize_title(t):
    if t is None:
        return ''
    s = str(t).strip()
    s = re.sub(r"^[\"']+|[\"']+$", '', s)
    s = re.sub(r"\s+", ' ', s)
    return s.lower()

# Build citation map
cit_map = {}
for rec in citations:
    t = rec.get('title')
    tot = rec.get('total_citations', 0)
    try:
        tot_i = int(tot)
    except Exception:
        tot_i = 0
    cit_map[normalize_title(t)] = tot_i

# Find docs published in 2016 and mentioning physical activity
results = []
for doc in docs:
    text = doc.get('text', '')
    if not isinstance(text, str):
        continue
    # check for 'physical activity'
    if re.search(r'physical activity', text, re.I) is None:
        continue
    # check for publication year 2016 near top
    header = text[:1500]
    if '2016' not in header:
        continue
    filename = doc.get('filename', '')
    title = re.sub(r'\.txt$', '', filename)
    norm = normalize_title(title)
    total = cit_map.get(norm, 0)
    results.append({'title': title, 'total_citations': total})

print("__RESULT__:")
print(json.dumps(results))"""

env_args = {'var_call_GCr1zw7xx9xk1G0vBAUywNW4': ['paper_docs'], 'var_call_IgMGRy82fd6CM3YSp579uesP': 'file_storage/call_IgMGRy82fd6CM3YSp579uesP.json', 'var_call_fbCH73ERsJiR8V8GgNikjxAJ': ['Citations', 'sqlite_sequence'], 'var_call_bj5IIhfHCAcIpURljX3hdbZG': 'file_storage/call_bj5IIhfHCAcIpURljX3hdbZG.json', 'var_call_mAbq0VBhcWHcGWwAPGfTBtxu': {'docs_count': 35, 'citations_count': 252}}

exec(code, env_args)
