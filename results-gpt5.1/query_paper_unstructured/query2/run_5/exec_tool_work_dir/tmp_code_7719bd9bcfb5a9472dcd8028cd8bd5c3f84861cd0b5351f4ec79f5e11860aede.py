code = """import json, re
from statistics import mean

# Load citations data
with open(var_call_Tb8O6XocSJoKURXAGdANW0za, 'r') as f:
    citations = json.load(f)

# Load paper docs data
with open(var_call_gBhc61YrtBSMRtsHrooJuKZe, 'r') as f:
    docs = json.load(f)

# Build a map from title to source by parsing text for 'Copyright' or publisher lines
source_by_title = {}
for doc in docs:
    filename = doc.get('filename', '')
    title = filename.rsplit('.txt', 1)[0]
    text = doc.get('text', '')
    lower = text.lower()
    source = None
    if 'acm' in lower:
        # Heuristic: if ACM appears near 'copyright' or 'permission' assume ACM
        if 'acm' in lower:
            source = 'ACM'
    elif 'ieee' in lower:
        source = 'IEEE'
    elif 'pubmed' in lower:
        source = 'PubMed'
    if source:
        source_by_title[title] = source

# Collect citation counts for ACM papers in 2018
acm_counts = []
for row in citations:
    title = row['title']
    if source_by_title.get(title) == 'ACM':
        try:
            c = int(row['citation_count'])
        except Exception:
            continue
        acm_counts.append(c)

avg_citations = mean(acm_counts) if acm_counts else 0

import json as _json
result = _json.dumps(avg_citations)
print("__RESULT__:")
print(result)"""

env_args = {'var_call_Tb8O6XocSJoKURXAGdANW0za': 'file_storage/call_Tb8O6XocSJoKURXAGdANW0za.json', 'var_call_gBhc61YrtBSMRtsHrooJuKZe': 'file_storage/call_gBhc61YrtBSMRtsHrooJuKZe.json'}

exec(code, env_args)
