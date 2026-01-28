code = """import json, pandas as pd

# Load full citations result
with open(var_call_Ss74RZcR0Loc5vcZ3w8t8iu6, 'r') as f:
    citations = json.load(f)

# Build a set of titles cited in 2018
cited_titles = {c['title'] for c in citations}

# From paper docs preview, infer source by searching for 'Copyright' and 'ACM'
# We need to know which of the cited titles are ACM papers. We'll scan the paper texts for 'Copyright' lines containing 'ACM'.

with open(var_call_CP3RZ4AxTp18yA6j02efX5H5, 'r') as f:
    docs = json.load(f)

acm_titles = set()
for d in docs:
    text = d.get('text', '')
    if 'ACM' in text and 'Copyright' in text:
        # filename without .txt is the title
        fn = d.get('filename', '')
        if fn.lower().endswith('.txt'):
            title = fn[:-4]
        else:
            title = fn
        acm_titles.add(title)

# Filter citations to those whose title is in acm_titles
acm_citations = [c for c in citations if c['title'] in acm_titles]

# Compute average citation_count (values are strings)
if acm_citations:
    counts = [int(c['citation_count']) for c in acm_citations]
    avg = sum(counts) / len(counts)
else:
    avg = None

result = avg

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_Ss74RZcR0Loc5vcZ3w8t8iu6': 'file_storage/call_Ss74RZcR0Loc5vcZ3w8t8iu6.json', 'var_call_CP3RZ4AxTp18yA6j02efX5H5': 'file_storage/call_CP3RZ4AxTp18yA6j02efX5H5.json'}

exec(code, env_args)
