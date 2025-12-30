code = """import json
import statistics

# Load citations data from file
path = var_call_Ni5HV3OuSuYmfLKkOA7hioc7
with open(path, 'r') as f:
    citations = json.load(f)

# Build a set of titles cited in 2018
titles_2018 = {c['title'] for c in citations}

# Load paper docs metadata (we only have full text, so we will heuristically detect ACM source)
path_docs = var_call_8SFkndCfpXYARlXnd2No5iU1
with open(path_docs, 'r') as f:
    docs = json.load(f)

acm_titles = set()
for d in docs:
    text = d.get('text', '')
    # Heuristic: if 'Copyright' and 'ACM' appear near each other or 'ACM' appears in copyright/permissions lines
    if 'ACM' in text:
        # Additional heuristic: look for 'Permission to make digital or hard copies' which is ACM boilerplate
        if 'Permission  to  make  digital  or  hard  copies' in text or 'Request permissions from permissions@acm.org' in text or 'Copyright' in text:
            filename = d.get('filename', '')
            if filename.lower().endswith('.txt'):
                title = filename[:-4]
            else:
                title = filename
            acm_titles.add(title)

# Intersection: papers that are ACM and cited in 2018
acm_cited_2018 = [c for c in citations if c['title'] in acm_titles]

# Convert citation_count to int and compute average
counts = [int(c['citation_count']) for c in acm_cited_2018]
avg = statistics.mean(counts) if counts else 0

result = json.dumps({'average_citation_count_acm_2018': avg, 'num_papers': len(counts)})
print("__RESULT__:")
print(result)"""

env_args = {'var_call_Ni5HV3OuSuYmfLKkOA7hioc7': 'file_storage/call_Ni5HV3OuSuYmfLKkOA7hioc7.json', 'var_call_8SFkndCfpXYARlXnd2No5iU1': 'file_storage/call_8SFkndCfpXYARlXnd2No5iU1.json'}

exec(code, env_args)
