code = """import json

# Load the MongoDB query result (list of docs with filename) and the SQLite query result (citations for 2018)
with open(var_call_a02TVkPqLrRwBY2LoJp1cY3D, 'r') as f:
    paper_docs = json.load(f)
with open(var_call_ZeVx0LEQnRIGmvz4ZlcP8pWH, 'r') as f:
    citations_2018 = json.load(f)

# Build set of titles from paper_docs where text contained 'ACM' (we queried for text matching 'ACM')
acm_titles = set()
for d in paper_docs:
    fn = d.get('filename', '')
    if fn.endswith('.txt'):
        title = fn[:-4]
    else:
        title = fn
    acm_titles.add(title)

# Filter citations for titles in ACM set
matched = []
for rec in citations_2018:
    t = rec.get('title')
    cc = rec.get('citation_count')
    try:
        cc_int = int(cc)
    except:
        try:
            cc_int = int(float(cc))
        except:
            continue
    if t in acm_titles:
        matched.append(cc_int)

# Compute average
if len(matched) == 0:
    result = {"average_citation": None, "matched_papers": 0}
else:
    avg = sum(matched) / len(matched)
    result = {"average_citation": avg, "matched_papers": len(matched)}

import json
print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_a02TVkPqLrRwBY2LoJp1cY3D': 'file_storage/call_a02TVkPqLrRwBY2LoJp1cY3D.json', 'var_call_ZeVx0LEQnRIGmvz4ZlcP8pWH': 'file_storage/call_ZeVx0LEQnRIGmvz4ZlcP8pWH.json'}

exec(code, env_args)
