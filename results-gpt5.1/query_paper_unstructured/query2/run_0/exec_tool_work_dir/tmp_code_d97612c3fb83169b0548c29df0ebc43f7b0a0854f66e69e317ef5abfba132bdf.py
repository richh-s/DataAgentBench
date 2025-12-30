code = """import json, re
import pandas as pd

# Load full citations result
with open(var_call_LSAYYigUNZF6E9fbRY5IBtDB, 'r') as f:
    citations = json.load(f)

# Load full paper docs result
with open(var_call_JQc7lzt5kOmrZbXsK5GNbYtP, 'r') as f:
    docs = json.load(f)

# Build mapping from title to source (ACM or not) by regex on text
source_map = {}
for d in docs:
    title = d.get('filename','').rsplit('.txt',1)[0]
    text = d.get('text','')[:4000].upper()
    # Heuristic: if 'ACM' appears near copyright/permission lines
    is_acm = 'ACM' in text
    source_map[title] = 'ACM' if is_acm else 'OTHER'

# Filter citations for ACM papers only
acm_citations = []
for c in citations:
    title = c['title']
    if source_map.get(title) == 'ACM':
        try:
            cnt = int(c['citation_count'])
        except Exception:
            continue
        acm_citations.append(cnt)

avg = float(sum(acm_citations))/len(acm_citations) if acm_citations else None

result = avg

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_LSAYYigUNZF6E9fbRY5IBtDB': 'file_storage/call_LSAYYigUNZF6E9fbRY5IBtDB.json', 'var_call_V4m8fqaf63Uqjs9iYMGzBiO8': ['paper_docs'], 'var_call_JQc7lzt5kOmrZbXsK5GNbYtP': 'file_storage/call_JQc7lzt5kOmrZbXsK5GNbYtP.json'}

exec(code, env_args)
