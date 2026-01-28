code = """import json

# Load the query results from the provided storage file paths
with open(var_call_IlMszRd1UZv6aPUexbqmcjp5, 'r') as f:
    paper_docs = json.load(f)
with open(var_call_WlFhvDX7eDlIqVpuOPyp3hHU, 'r') as f:
    citations_2018 = json.load(f)

# Build set of titles from paper_docs filenames (remove .txt extension)
titles = set()
for d in paper_docs:
    fn = d.get('filename', '')
    if fn.endswith('.txt'):
        titles.add(fn[:-4])
    else:
        titles.add(fn)

# Filter citations to those whose title is in titles set
matched = []
for rec in citations_2018:
    title = rec.get('title')
    cc = rec.get('citation_count')
    try:
        cc_int = int(cc)
    except Exception:
        # skip records with non-integer citation_count
        continue
    if title in titles:
        matched.append(cc_int)

count = len(matched)
avg = round(sum(matched)/count, 2) if count > 0 else 0

output = {"average_citation_count": avg, "matching_paper_count": count}

print("__RESULT__:")
print(json.dumps(output))"""

env_args = {'var_call_IlMszRd1UZv6aPUexbqmcjp5': 'file_storage/call_IlMszRd1UZv6aPUexbqmcjp5.json', 'var_call_WlFhvDX7eDlIqVpuOPyp3hHU': 'file_storage/call_WlFhvDX7eDlIqVpuOPyp3hHU.json'}

exec(code, env_args)
