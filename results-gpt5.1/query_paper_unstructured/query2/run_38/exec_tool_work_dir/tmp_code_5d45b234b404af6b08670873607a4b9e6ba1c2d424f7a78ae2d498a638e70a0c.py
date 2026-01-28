code = """import json, re
from statistics import mean

# Load citation records for 2018
path_citations = var_call_phqeJ26j0dB5DTNk4wmSBHEd
with open(path_citations, 'r') as f:
    citations_2018 = json.load(f)

# Load paper documents
path_papers = var_call_lcglkvuSoSLUQvCqXpi6SRkb
with open(path_papers, 'r') as f:
    papers = json.load(f)

# Build lookup of title -> source (publisher)
source_by_title = {}
for doc in papers:
    filename = doc.get('filename','')
    title = re.sub(r"\.txt$","", filename).strip()
    text = doc.get('text','')
    m = re.search(r"\bACM\b", text)
    if m:
        source = 'ACM'
    else:
        # crude heuristic: if 'IEEE' appears and 'ACM' does not, label IEEE, else unknown
        if re.search(r"\bIEEE\b", text):
            source = 'IEEE'
        else:
            source = 'UNKNOWN'
    if title:
        source_by_title[title] = source

# Filter citations to ACM papers and compute average citation_count
acm_counts = []
for rec in citations_2018:
    title = rec.get('title')
    if not title:
        continue
    if source_by_title.get(title) == 'ACM':
        try:
            c = int(rec.get('citation_count'))
        except (TypeError, ValueError):
            continue
        acm_counts.append(c)

avg_citations = mean(acm_counts) if acm_counts else None

import math
if avg_citations is not None:
    avg_citations = round(avg_citations, 2)

result = avg_citations

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_phqeJ26j0dB5DTNk4wmSBHEd': 'file_storage/call_phqeJ26j0dB5DTNk4wmSBHEd.json', 'var_call_lcglkvuSoSLUQvCqXpi6SRkb': 'file_storage/call_lcglkvuSoSLUQvCqXpi6SRkb.json'}

exec(code, env_args)
