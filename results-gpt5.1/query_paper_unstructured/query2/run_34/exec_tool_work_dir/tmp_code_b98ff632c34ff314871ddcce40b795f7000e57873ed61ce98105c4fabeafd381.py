code = """import json, re
from statistics import mean

path_citations = var_call_oqRImsd7ANgcP25Htbpk8vyi
path_papers = var_call_bvWWn1vzaIzweCIptECnH1VF

with open(path_citations, 'r') as f:
    citations = json.load(f)
with open(path_papers, 'r') as f:
    papers = json.load(f)

source_by_title = {}
for doc in papers:
    filename = doc.get('filename', '')
    if filename.lower().endswith('.txt'):
        title = filename[:-4]
    else:
        title = filename
    text = doc.get('text', '')
    if re.search(r'Copyright\s+\d{4}[^\n]*ACM', text, re.IGNORECASE):
        source_by_title[title] = 'ACM'

acm_citations_2018 = []
for row in citations:
    title = row['title']
    if source_by_title.get(title) == 'ACM':
        try:
            c = int(row['citation_count'])
        except Exception:
            continue
        acm_citations_2018.append(c)

avg_citations = mean(acm_citations_2018) if acm_citations_2018 else 0

print("__RESULT__:")
print(json.dumps(avg_citations))"""

env_args = {'var_call_oqRImsd7ANgcP25Htbpk8vyi': 'file_storage/call_oqRImsd7ANgcP25Htbpk8vyi.json', 'var_call_bvWWn1vzaIzweCIptECnH1VF': 'file_storage/call_bvWWn1vzaIzweCIptECnH1VF.json'}

exec(code, env_args)
