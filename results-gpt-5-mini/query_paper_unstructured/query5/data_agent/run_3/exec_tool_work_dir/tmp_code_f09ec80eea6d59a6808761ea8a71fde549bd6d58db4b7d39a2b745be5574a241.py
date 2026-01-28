code = """import json, os
# Load the stored query results from previous tool calls
path_mongo = var_call_xgDKIdaVTksZCZthfBfqUsQC
path_cite = var_call_3aMW1Fg4ermFqfFx2i15Jm5c

# Load JSON files
with open(path_mongo, 'r', encoding='utf-8') as f:
    mongo_docs = json.load(f)
with open(path_cite, 'r', encoding='utf-8') as f:
    citations = json.load(f)

# Extract titles from mongo filenames (remove .txt)
chi_titles = set()
for doc in mongo_docs:
    fn = doc.get('filename', '')
    if fn.lower().endswith('.txt'):
        title = fn[:-4]
    else:
        title = fn
    chi_titles.add(title)

# Match citations whose title is in chi_titles
matched = []
for rec in citations:
    t = rec.get('title')
    # Some citation_count may be strings; convert to int safely
    try:
        c = int(rec.get('citation_count', 0))
    except:
        try:
            c = int(float(rec.get('citation_count', 0)))
        except:
            c = 0
    if t in chi_titles:
        matched.append({'title': t, 'citation_count': c})

# Compute total
total = sum(r['citation_count'] for r in matched)

# Prepare result
result = {
    'num_chi_papers_cited_in_2020': len(matched),
    'total_citations_2020_for_these_chi_papers': total,
    'papers': matched
}

import json
print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_xgDKIdaVTksZCZthfBfqUsQC': 'file_storage/call_xgDKIdaVTksZCZthfBfqUsQC.json', 'var_call_3aMW1Fg4ermFqfFx2i15Jm5c': 'file_storage/call_3aMW1Fg4ermFqfFx2i15Jm5c.json'}

exec(code, env_args)
