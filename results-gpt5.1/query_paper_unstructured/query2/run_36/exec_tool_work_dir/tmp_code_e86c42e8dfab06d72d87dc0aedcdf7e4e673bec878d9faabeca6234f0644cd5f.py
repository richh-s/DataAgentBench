code = """import json
import re

# Load citations for 2018 from file
with open(var_call_tASRzYJkrGWskl29ruU13GHW, 'r') as f:
    citations_2018 = json.load(f)

# Build a set of titles cited in 2018
titles_2018 = {rec['title'] for rec in citations_2018}

# Load paper docs
with open(var_call_JfMu0oVXhc2XcrU6MTLZQlfe, 'r') as f:
    paper_docs = json.load(f)

# Helper to detect ACM source from text
acm_pattern = re.compile(r"ACM", re.IGNORECASE)

acm_titles = set()
for doc in paper_docs:
    text = doc.get('text', '')
    if acm_pattern.search(text):
        # title is filename without .txt
        filename = doc.get('filename', '')
        title = filename[:-4] if filename.lower().endswith('.txt') else filename
        acm_titles.add(title)

# Filter citations to those whose titles are ACM
acm_citations = [rec for rec in citations_2018 if rec['title'] in acm_titles]

# Compute average citation_count for these
if acm_citations:
    counts = [int(rec['citation_count']) for rec in acm_citations]
    avg = sum(counts) / len(counts)
else:
    avg = None

result = avg

from math import isnan
if result is None or (isinstance(result, float) and isnan(result)):
    out = json.dumps(None)
else:
    out = json.dumps(result)

print("__RESULT__:")
print(out)"""

env_args = {'var_call_tASRzYJkrGWskl29ruU13GHW': 'file_storage/call_tASRzYJkrGWskl29ruU13GHW.json', 'var_call_JfMu0oVXhc2XcrU6MTLZQlfe': 'file_storage/call_JfMu0oVXhc2XcrU6MTLZQlfe.json'}

exec(code, env_args)
