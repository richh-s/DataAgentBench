code = """import json, re

# Load docs
with open(var_call_AIXjEpfUvdIcrQM9aiyt3Ncc, 'r') as f:
    paper_docs = json.load(f)

# Load citations list from JSON string
citations_2018 = json.loads(var_call_xBiYV60jNAjjtZUaBG5HfFo5)


def extract_source(text):
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
    if src and title:
        source_by_title[title] = src

acm_counts = []
for rec in citations_2018:
    if not isinstance(rec, dict):
        continue
    title = rec.get('title')
    src = source_by_title.get(title)
    if src == 'ACM':
        try:
            c = int(rec.get('citation_count'))
        except Exception:
            continue
        acm_counts.append(c)

avg = sum(acm_counts)/len(acm_counts) if acm_counts else None

print("__RESULT__:")
print(json.dumps(avg))"""

env_args = {'var_call_xBiYV60jNAjjtZUaBG5HfFo5': 'file_storage/call_xBiYV60jNAjjtZUaBG5HfFo5.json', 'var_call_AIXjEpfUvdIcrQM9aiyt3Ncc': 'file_storage/call_AIXjEpfUvdIcrQM9aiyt3Ncc.json', 'var_call_Dw53EfwPtmioXkZvVELAK3AV': {'type': "<class 'str'>"}}

exec(code, env_args)
