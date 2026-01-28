code = """import json
import re

# Load data from previous calls
with open(var_call_AIXjEpfUvdIcrQM9aiyt3Ncc, 'r') as f:
    paper_docs = json.load(f)

citations_2018 = var_call_xBiYV60jNAjjtZUaBG5HfFo5

# Build mapping from title to source by parsing text for 'Permission to ... ACM' etc.

def extract_source(text):
    # Simple heuristic: look for 'Permission' boilerplate lines mentioning ACM or IEEE or PubMed
    lower = text.lower()
    if 'acm' in lower:
        return 'ACM'
    if 'ieee' in lower:
        return 'IEEE'
    if 'pubmed' in lower:
        return 'PubMed'
    return None

source_by_title = {}
for doc in paper_docs:
    filename = doc.get('filename', '')
    title = re.sub(r'\.txt$', '', filename)
    src = extract_source(doc.get('text', ''))
    if src:
        source_by_title[title] = src

# Filter citations for ACM papers
acm_citations = []
for rec in citations_2018:
    title = rec['title']
    src = source_by_title.get(title)
    if src == 'ACM':
        try:
            c = int(rec['citation_count'])
        except Exception:
            continue
        acm_citations.append(c)

if acm_citations:
    avg_citations = sum(acm_citations) / len(acm_citations)
else:
    avg_citations = None

result = avg_citations

from math import isnan

if result is None:
    out = json.dumps(None)
else:
    out = json.dumps(result)

print("__RESULT__:")
print(out)"""

env_args = {'var_call_xBiYV60jNAjjtZUaBG5HfFo5': 'file_storage/call_xBiYV60jNAjjtZUaBG5HfFo5.json', 'var_call_AIXjEpfUvdIcrQM9aiyt3Ncc': 'file_storage/call_AIXjEpfUvdIcrQM9aiyt3Ncc.json'}

exec(code, env_args)
