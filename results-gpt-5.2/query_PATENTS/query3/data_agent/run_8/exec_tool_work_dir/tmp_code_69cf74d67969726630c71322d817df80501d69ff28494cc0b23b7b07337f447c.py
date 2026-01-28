code = """import json, re
import pandas as pd

# Load large query result if needed
src = var_call_47XoEKYUkAFjoJCttXjRK0gU
if isinstance(src, str):
    with open(src, 'r', encoding='utf-8') as f:
        records = json.load(f)
else:
    records = src

def extract_assignee(patents_info: str):
    if not patents_info:
        return None
    # patterns like 'owned by XYZ' or 'is owned by XYZ'
    m = re.search(r"owned by ([^,\.]+)", patents_info, flags=re.IGNORECASE)
    if m:
        return m.group(1).strip()
    return None

def parse_citations(citation_str: str):
    if not citation_str:
        return []
    try:
        arr = json.loads(citation_str)
        pubs = []
        for x in arr:
            pn = (x or {}).get('publication_number')
            if pn:
                pubs.append(pn)
        return pubs
    except Exception:
        return []

rows=[]
for r in records:
    assignee = extract_assignee(r.get('Patents_info',''))
    if not assignee:
        continue
    cits = parse_citations(r.get('citation',''))
    for pn in cits:
        rows.append({'citing_assignee': assignee, 'cited_pub': pn})

citdf = pd.DataFrame(rows).drop_duplicates()

# find cited publications that are assigned to UNIV CALIFORNIA
# We'll scan publicationinfo for patents_info mentioning 'owned by UNIV CALIFORNIA'
# (use records already loaded; but it includes various assignees; need full table.
# Query all UC-owned patents and their publication numbers.

print('__RESULT__:')
print(json.dumps({'n_citation_links': int(len(citdf)), 'sample': citdf.head(5).to_dict(orient='records')}))"""

env_args = {'var_call_1rYrvyDMz1z3QQtjsFzHstWw': ['publicationinfo'], 'var_call_Ms9eMaShBwv17k0wWTZQFXz7': [], 'var_call_5eTr8UabZxWiZbQfiXRw0lFv': [], 'var_call_47XoEKYUkAFjoJCttXjRK0gU': 'file_storage/call_47XoEKYUkAFjoJCttXjRK0gU.json', 'var_call_C9RLBBJLeuadpJoDEshNxw3R': ['cpc_definition'], 'var_call_5nl6c85ItrHDBnsYe6dKNRfh': [{'symbol': 'A01K2227/108', 'titleFull': 'Swine'}, {'symbol': 'A01K2227/105', 'titleFull': 'Murine'}, {'symbol': 'A01K2227/101', 'titleFull': 'Bovine'}, {'symbol': 'A01K2227/107', 'titleFull': 'Rabbit'}, {'symbol': 'A01K2227/103', 'titleFull': 'Ovine'}]}

exec(code, env_args)
