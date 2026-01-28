code = """import json
# Load data from storage-provided file paths
with open(var_call_g40xwB5ycos8LBi3NohVmx2d, 'r') as f:
    paper_docs = json.load(f)
with open(var_call_LbzBpUM7gYMliTM7wAQpW1XC, 'r') as f:
    citations = json.load(f)

# Extract titles from paper_docs filenames (remove .txt)
paper_titles = []
for doc in paper_docs:
    fn = doc.get('filename','')
    if fn.endswith('.txt'):
        title = fn[:-4]
    else:
        title = fn
    paper_titles.append(title.strip())

# Build normalized citation totals mapping
cit_map = {}
for rec in citations:
    t = rec.get('title','')
    if t is None:
        continue
    key = t.strip().casefold()
    try:
        val = int(rec.get('total_citations', 0))
    except:
        try:
            val = int(float(rec.get('total_citations', 0)))
        except:
            val = 0
    cit_map[key] = cit_map.get(key, 0) + val

# Sum citations for paper titles that are in the paper_docs (food domain candidates)
matched_titles = []
total = 0
for t in paper_titles:
    key = t.casefold()
    if key in cit_map:
        matched_titles.append(t)
        total += cit_map[key]

# Prepare result
result = {
    'total_citations_for_food_domain': total,
    'matched_paper_count': len(matched_titles),
    'matched_titles': matched_titles
}

import json as _json
print('__RESULT__:')
print(_json.dumps(result))"""

env_args = {'var_call_zx5Q53CmAqLO9GOxEwPyWwUS': ['paper_docs'], 'var_call_g40xwB5ycos8LBi3NohVmx2d': 'file_storage/call_g40xwB5ycos8LBi3NohVmx2d.json', 'var_call_Pitdtx0DbMQx4iEWrQwlsfGJ': ['Citations', 'sqlite_sequence'], 'var_call_LbzBpUM7gYMliTM7wAQpW1XC': 'file_storage/call_LbzBpUM7gYMliTM7wAQpW1XC.json'}

exec(code, env_args)
