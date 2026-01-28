code = """import json
from statistics import mean

# Load the query results from storage file paths
with open(var_call_sOitUIyDGgqwlAszssKOVUX1, 'r') as f:
    citations = json.load(f)
with open(var_call_b3cZnY2cji31wexAvWAqf6Ij, 'r') as f:
    papers = json.load(f)

# Build set of paper titles from paper_docs filenames (strip .txt)
acm_titles = set()
for doc in papers:
    fn = doc.get('filename', '')
    if fn:
        title = fn.rsplit('.txt', 1)[0]
        acm_titles.add(title)

# Filter citations for 2018 were already queried; now keep only those whose title is in acm_titles
matched_counts = []
for rec in citations:
    t = rec.get('title')
    cc = rec.get('citation_count')
    if t in acm_titles and cc is not None and cc != '':
        try:
            matched_counts.append(int(cc))
        except:
            try:
                matched_counts.append(int(float(cc)))
            except:
                pass

if matched_counts:
    avg = sum(matched_counts) / len(matched_counts)
    # keep as float with reasonable precision
    avg_val = float(avg)
else:
    avg_val = None

result = {"average_citation_count": avg_val, "paper_count": len(matched_counts)}

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_sOitUIyDGgqwlAszssKOVUX1': 'file_storage/call_sOitUIyDGgqwlAszssKOVUX1.json', 'var_call_b3cZnY2cji31wexAvWAqf6Ij': 'file_storage/call_b3cZnY2cji31wexAvWAqf6Ij.json'}

exec(code, env_args)
