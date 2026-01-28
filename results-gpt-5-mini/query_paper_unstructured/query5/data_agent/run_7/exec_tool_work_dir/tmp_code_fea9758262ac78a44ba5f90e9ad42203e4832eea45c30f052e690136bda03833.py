code = """import json, re
# Load tool results from storage files
with open(var_call_chz6IYwvo5dsQr5G93GseU5t, 'r') as f:
    citations = json.load(f)
with open(var_call_v97IdNNmwUCcjthQMwcT7PEo, 'r') as f:
    docs = json.load(f)

# Normalization helper
def norm_title(t):
    if t is None:
        return t
    t = t.strip()
    # remove surrounding quotes
    if (t.startswith('"') and t.endswith('"')) or (t.startswith("'") and t.endswith("'")):
        t = t[1:-1].strip()
    return t

# Build citation map: title -> total citations (int)
cit_map = {}
for rec in citations:
    t = norm_title(rec.get('title'))
    try:
        c = int(rec.get('total_citations'))
    except:
        # handle strings with commas
        c = int(str(rec.get('total_citations')).replace(',', ''))
    cit_map[t] = c

# Find CHI papers from docs
chi_titles = set()
for doc in docs:
    filename = doc.get('filename', '')
    if filename.lower().endswith('.txt'):
        title = filename[:-4]
    else:
        title = filename
    title = title.strip()
    header = doc.get('text', '')[:1000]
    if re.search(r"\bCHI\b", header, re.IGNORECASE):
        chi_titles.add(norm_title(title))

# Join
results = []
for t, c in cit_map.items():
    if t in chi_titles:
        results.append({'title': t, 'total_citations': c})

# Sort by citations descending
results.sort(key=lambda x: x['total_citations'], reverse=True)

print("__RESULT__:")
print(json.dumps(results))"""

env_args = {'var_call_chz6IYwvo5dsQr5G93GseU5t': 'file_storage/call_chz6IYwvo5dsQr5G93GseU5t.json', 'var_call_v97IdNNmwUCcjthQMwcT7PEo': 'file_storage/call_v97IdNNmwUCcjthQMwcT7PEo.json'}

exec(code, env_args)
