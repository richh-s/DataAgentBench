code = """import json, re
from statistics import mean

# Load prior results
import_path_citations = var_call_oqRImsd7ANgcP25Htbpk8vyi
import_path_papers = var_call_bvWWn1vzaIzweCIptECnH1VF

with open(import_path_citations, 'r') as f:
    citations = json.load(f)
with open(import_path_papers, 'r') as f:
    papers = json.load(f)

# Build mapping from title to source by parsing text for 'Copyright' lines mentioning ACM
source_by_title = {}
for doc in papers:
    filename = doc.get('filename','')
    title = filename[:-4] if filename.lower().endswith('.txt') else filename
    text = doc.get('text','')
    m = re.search(r'Copyright\s+\d{4}[^\n]*ACM', text, re.IGNORECASE)
    if m:
        source_by_title[title] = 'ACM'

# Filter citations for ACM papers in 2018
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

result = avg_citations

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_oqRImsd7ANgcP25Htbpk8vyi': 'file_storage/call_oqRImsd7ANgcP25Htbpk8vyi.json', 'var_call_bvWWn1vzaIzweCIptECnH1VF': 'file_storage/call_bvWWn1vzaIzweCIptECnH1VF.json'}

exec(code, env_args)
