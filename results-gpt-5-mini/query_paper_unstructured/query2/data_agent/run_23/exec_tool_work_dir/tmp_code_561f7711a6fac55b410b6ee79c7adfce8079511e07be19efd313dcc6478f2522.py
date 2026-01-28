code = """import json
from pathlib import Path

# Load the stored query results from previous tool calls
# var_call_sDNt37ig38hHm3wLg60aDJcW and var_call_ajCWp7VWryBK5K8E4s2Hy1ig are expected to be file paths (strings)

p1 = var_call_sDNt37ig38hHm3wLg60aDJcW
p2 = var_call_ajCWp7VWryBK5K8E4s2Hy1ig

# Helper to load JSON from path or use directly if it's already a list
def load_var(v):
    if isinstance(v, str) and Path(v).exists():
        return json.loads(Path(v).read_text())
    return v

paper_docs = load_var(p1)
citations_2018 = load_var(p2)

# Build set of titles from paper_docs filenames (remove .txt)
paper_titles = set()
for d in paper_docs:
    fn = d.get('filename')
    if not fn:
        continue
    title = fn
    if title.endswith('.txt'):
        title = title[:-4]
    paper_titles.add(title)

# Filter citations for titles present in paper_titles and compute average
matched = []
for rec in citations_2018:
    t = rec.get('title')
    c = rec.get('citation_count')
    try:
        c_int = int(c)
    except:
        # skip invalid
        continue
    if t in paper_titles:
        matched.append({'title': t, 'citation_count': c_int})

count = len(matched)
avg = None
if count > 0:
    avg_val = sum(r['citation_count'] for r in matched) / count
    avg = avg_val

result = {
    'average_citation_count': avg,
    'num_acm_papers_cited_in_2018': count,
    'matched_records_sample': matched[:20]
}

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_sDNt37ig38hHm3wLg60aDJcW': 'file_storage/call_sDNt37ig38hHm3wLg60aDJcW.json', 'var_call_ajCWp7VWryBK5K8E4s2Hy1ig': 'file_storage/call_ajCWp7VWryBK5K8E4s2Hy1ig.json'}

exec(code, env_args)
