code = """import json, pandas as pd, re

# Load full citations result
with open(var_call_t7ZZADaWbCOZEHiUooliVnro, 'r') as f:
    citations = json.load(f)

# Load full paper docs result
with open(var_call_GonpxH68lbripYEsuXtl1DUk, 'r') as f:
    papers = json.load(f)

# Build mapping from title to source (ACM or not) using simple heuristic on text
# We'll say a paper is ACM if its text contains 'Copyright' and 'ACM' near each other or "ACM" clearly in the copyright line

def infer_source(text):
    if not isinstance(text, str):
        return None
    # Look for typical ACM strings
    acm_patterns = [
        r"Copyright\s+\d{4}.*ACM",
        r"ACM\s+\d{4}",
        r"Permission to make digital or hard copies.*ACM",
        r"Association for Computing Machinery",
        r"ACM\s+978-",
    ]
    for pat in acm_patterns:
        if re.search(pat, text, flags=re.IGNORECASE|re.DOTALL):
            return "ACM"
    return None

# Build dict: title -> source
title_to_source = {}
for doc in papers:
    filename = doc.get('filename')
    if not filename or not isinstance(filename, str):
        continue
    title = filename
    if title.lower().endswith('.txt'):
        title = title[:-4]
    source = infer_source(doc.get('text', ''))
    if source:
        title_to_source[title] = source

# Filter citations for ACM papers via title join and compute average citation_count
acm_citations = []
for row in citations:
    title = row.get('title')
    if title in title_to_source and title_to_source[title] == 'ACM':
        try:
            c = int(row.get('citation_count'))
        except (TypeError, ValueError):
            continue
        acm_citations.append(c)

if acm_citations:
    avg_citations = sum(acm_citations) / len(acm_citations)
else:
    avg_citations = None

result = {
    'average_citation_count_acm_2018': avg_citations,
    'num_acm_papers': len(acm_citations)
}

out = json.dumps(result)
print("__RESULT__:")
print(out)"""

env_args = {'var_call_t7ZZADaWbCOZEHiUooliVnro': 'file_storage/call_t7ZZADaWbCOZEHiUooliVnro.json', 'var_call_GonpxH68lbripYEsuXtl1DUk': 'file_storage/call_GonpxH68lbripYEsuXtl1DUk.json'}

exec(code, env_args)
