code = """import json
# Load storage variables which are file paths to JSON results
with open(var_call_eZpMOxKtp6FPL24OYbIS6ZQi, 'r') as f:
    paper_docs = json.load(f)
with open(var_call_IaUQlLbFMwPT9StvPOOVc6zS, 'r') as f:
    citations_agg = json.load(f)

# Extract titles from paper_docs filenames (remove .txt)
paper_titles = set()
for doc in paper_docs:
    fn = doc.get('filename', '')
    if fn.lower().endswith('.txt'):
        title = fn[:-4]
    else:
        title = fn
    paper_titles.add(title)

# Build a mapping from citation title to total citations (as int)
cit_map = {}
for rec in citations_agg:
    t = rec.get('title')
    # some titles may have surrounding whitespace
    if t is None:
        continue
    t = t.strip()
    val = rec.get('total_citations', 0)
    try:
        val_int = int(val)
    except:
        try:
            val_int = int(float(val))
        except:
            val_int = 0
    cit_map[t] = val_int

# Sum total citations for titles that are in paper_titles
matched = []
total = 0
for t, c in cit_map.items():
    if t in paper_titles:
        matched.append({'title': t, 'citations': c})
        total += c

result = {'domain': 'food', 'total_citations': total, 'matched_papers_count': len(matched)}

import json
print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_ogGKy9sAfAG4ZqJfm9IgkV6Z': ['paper_docs'], 'var_call_eZpMOxKtp6FPL24OYbIS6ZQi': 'file_storage/call_eZpMOxKtp6FPL24OYbIS6ZQi.json', 'var_call_IaUQlLbFMwPT9StvPOOVc6zS': 'file_storage/call_IaUQlLbFMwPT9StvPOOVc6zS.json'}

exec(code, env_args)
