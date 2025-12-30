code = """import json, re
from statistics import mean

# Load full citations result
with open(var_call_yElMa91PjYZO6l8YvMW5pICS, 'r') as f:
    citations = json.load(f)

# Load full paper docs result
with open(var_call_FK4sLdsZeY4NCA5oMMOhhR8b, 'r') as f:
    docs = json.load(f)

# Build title -> source mapping from docs using text heuristics
source_by_title = {}
for d in docs:
    filename = d.get('filename','')
    title = filename.replace('.txt','')
    text = d.get('text','')
    # Heuristic: look for 'Copyright' line mentioning ACM or IEEE or PubMed
    m = re.search(r'Copyright[^\n]*', text, re.IGNORECASE)
    source = None
    if m:
        line = m.group(0).lower()
        if 'acm' in line:
            source = 'ACM'
        elif 'ieee' in line:
            source = 'IEEE'
        elif 'pubmed' in line:
            source = 'PubMed'
    # Fallback: look for 'Permission to make digital or hard copies' which is typical ACM
    if source is None and re.search(r'permission\s+to\s+make\s+digital\s+or\s+hard\s+copies', text, re.IGNORECASE):
        source = 'ACM'
    if source:
        source_by_title[title] = source

# Collect citation counts in 2018 for ACM papers
acm_counts = []
for c in citations:
    title = c['title']
    count = int(c['citation_count'])
    source = source_by_title.get(title)
    if source == 'ACM':
        acm_counts.append(count)

avg_citations = mean(acm_counts) if acm_counts else None

import math
if avg_citations is not None:
    avg_citations = round(avg_citations, 2)

result = avg_citations

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_yElMa91PjYZO6l8YvMW5pICS': 'file_storage/call_yElMa91PjYZO6l8YvMW5pICS.json', 'var_call_FK4sLdsZeY4NCA5oMMOhhR8b': 'file_storage/call_FK4sLdsZeY4NCA5oMMOhhR8b.json'}

exec(code, env_args)
