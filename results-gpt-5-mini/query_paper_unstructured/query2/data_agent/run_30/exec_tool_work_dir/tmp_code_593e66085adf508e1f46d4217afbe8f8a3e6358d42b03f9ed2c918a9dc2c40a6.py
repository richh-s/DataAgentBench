code = """import json

# Load the results from storage files provided by previous tool calls
with open(var_call_1VUd0b950omADNTduzY6Xtny, 'r') as f:
    citations_2018 = json.load(f)
with open(var_call_hT328I5c0fbcA341DWP9PmhF, 'r') as f:
    acm_papers = json.load(f)

# Build set of titles from ACM paper documents by stripping .txt from filenames
acm_titles = set()
for doc in acm_papers:
    fn = doc.get('filename', '')
    if fn.endswith('.txt'):
        title = fn[:-4]
    else:
        title = fn
    acm_titles.add(title)

# Filter citations for 2018 that match ACM titles and compute average
matched_counts = []
for rec in citations_2018:
    title = rec.get('title')
    cit = rec.get('citation_count')
    try:
        cit_int = int(cit)
    except Exception:
        # skip non-integer citation counts
        continue
    if title in acm_titles:
        matched_counts.append(cit_int)

if len(matched_counts) == 0:
    result = {"average_citation_count": None, "num_papers": 0}
else:
    avg = sum(matched_counts) / len(matched_counts)
    # keep as float with reasonable precision
    result = {"average_citation_count": round(avg, 4), "num_papers": len(matched_counts)}

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_Se2VTjYD72wLPtqiVi6VH0zr': ['paper_docs'], 'var_call_06UYjhRrpGC5IfTxYzMOLUjH': ['Citations', 'sqlite_sequence'], 'var_call_1VUd0b950omADNTduzY6Xtny': 'file_storage/call_1VUd0b950omADNTduzY6Xtny.json', 'var_call_hT328I5c0fbcA341DWP9PmhF': 'file_storage/call_hT328I5c0fbcA341DWP9PmhF.json'}

exec(code, env_args)
