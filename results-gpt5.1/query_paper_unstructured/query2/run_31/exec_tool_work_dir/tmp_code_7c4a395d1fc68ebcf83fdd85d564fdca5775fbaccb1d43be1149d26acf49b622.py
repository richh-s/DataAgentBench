code = """import json
import re

with open(var_call_iDBGbZDvuwmT8FncEtM7kYqP, 'r') as f:
    citations_2018 = json.load(f)

with open(var_call_42rNs9p8323TyGpk7IsDivYX, 'r') as f:
    paper_docs = json.load(f)

def extract_source(text):
    for line in text.split('\n'):
        low = line.lower()
        if ('copyright' in low) and ('acm' in low):
            return 'ACM'
    return None

filename_to_source = {}
for doc in paper_docs:
    filename = doc.get('filename', '')
    title = re.sub(r'\.txt$', '', filename)
    source = extract_source(doc.get('text', ''))
    if source:
        filename_to_source[title] = source

acm_citations = []
for rec in citations_2018:
    title = rec.get('title')
    if filename_to_source.get(title) == 'ACM':
        try:
            c = int(rec.get('citation_count'))
        except (TypeError, ValueError):
            continue
        acm_citations.append(c)

if acm_citations:
    avg_citations = sum(acm_citations) / len(acm_citations)
else:
    avg_citations = None

result = json.dumps({"average_citation_count_acm_2018": avg_citations, "paper_count": len(acm_citations)})

print("__RESULT__:")
print(result)"""

env_args = {'var_call_iDBGbZDvuwmT8FncEtM7kYqP': 'file_storage/call_iDBGbZDvuwmT8FncEtM7kYqP.json', 'var_call_42rNs9p8323TyGpk7IsDivYX': 'file_storage/call_42rNs9p8323TyGpk7IsDivYX.json'}

exec(code, env_args)
