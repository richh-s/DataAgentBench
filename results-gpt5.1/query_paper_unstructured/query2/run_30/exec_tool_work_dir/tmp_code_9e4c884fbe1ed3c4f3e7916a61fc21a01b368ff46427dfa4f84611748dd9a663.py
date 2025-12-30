code = """import json, re
from statistics import mean

# Load full citations result
with open(var_call_DduOnjdngqjMrYGc5GsMXPPY, 'r') as f:
    citations = json.load(f)

# Load full paper docs result
with open(var_call_1ep05rWUeSunhDtdgui57LaT, 'r') as f:
    papers = json.load(f)

# Build map from title to source by heuristically detecting ACM in text
source_by_title = {}
for doc in papers:
    filename = doc.get('filename','')
    title = filename.rsplit('.txt',1)[0]
    text = doc.get('text','').upper()
    # Heuristic: if 'ACM' appears near copyright or permission lines, mark as ACM
    if 'ACM' in text:
        source = 'ACM'
    else:
        source = 'OTHER'
    source_by_title[title] = source

# Collect citation counts for ACM papers in 2018
acm_citations = []
for row in citations:
    title = row['title']
    count = int(row['citation_count'])
    source = source_by_title.get(title)
    if source == 'ACM':
        acm_citations.append(count)

avg_citations = mean(acm_citations) if acm_citations else 0

import json as json_mod
result = json_mod.dumps(avg_citations)
print("__RESULT__:")
print(result)"""

env_args = {'var_call_DduOnjdngqjMrYGc5GsMXPPY': 'file_storage/call_DduOnjdngqjMrYGc5GsMXPPY.json', 'var_call_1ep05rWUeSunhDtdgui57LaT': 'file_storage/call_1ep05rWUeSunhDtdgui57LaT.json'}

exec(code, env_args)
