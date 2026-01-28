code = """import json
from statistics import mean

# Load ACM paper docs filenames result
with open(var_call_lffTGnigPAH5rF6fGAq7vsYl, 'r') as f:
    acm_docs = json.load(f)

# Extract titles from filenames (strip .txt)
acm_titles = set()
for d in acm_docs:
    fn = d.get('filename', '')
    if fn.endswith('.txt'):
        acm_titles.add(fn[:-4])
    else:
        acm_titles.add(fn)

# Load citations for 2018
with open(var_call_zsMH1klnNoCBLrbD5eQpGe9N, 'r') as f:
    citations_2018 = json.load(f)

# Match and collect citation counts
matched_counts = []
for rec in citations_2018:
    title = rec.get('title')
    # try direct match
    if title in acm_titles:
        try:
            matched_counts.append(int(rec.get('citation_count', 0)))
        except:
            try:
                matched_counts.append(int(float(rec.get('citation_count'))))
            except:
                pass

# Compute average
if len(matched_counts) > 0:
    avg = sum(matched_counts) / len(matched_counts)
    result = {"average_citation_count": avg, "matched_papers": len(matched_counts)}
else:
    result = {"average_citation_count": None, "matched_papers": 0}

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_lffTGnigPAH5rF6fGAq7vsYl': 'file_storage/call_lffTGnigPAH5rF6fGAq7vsYl.json', 'var_call_zsMH1klnNoCBLrbD5eQpGe9N': 'file_storage/call_zsMH1klnNoCBLrbD5eQpGe9N.json'}

exec(code, env_args)
