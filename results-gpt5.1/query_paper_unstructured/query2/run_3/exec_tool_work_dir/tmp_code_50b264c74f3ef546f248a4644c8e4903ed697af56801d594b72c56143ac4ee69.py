code = """import json, re
from statistics import mean

# Load citations for 2018
path_citations = var_call_ydfRZE3TcYBzrcXGM600Om9H
with open(path_citations, 'r') as f:
    citations = json.load(f)

# Load paper docs
path_papers = var_call_Vcqy3YthO7DsjiQGHt3bUHng
with open(path_papers, 'r') as f:
    papers = json.load(f)

# Build lookup: title -> source (publisher) inferred from text
source_by_title = {}
for doc in papers:
    filename = doc.get('filename','')
    title = filename[:-4] if filename.lower().endswith('.txt') else filename
    text = doc.get('text','').upper()
    source = None
    if 'PERMISSION TO MAKE DIGITAL OR HARD COPIES' in text and 'ACM' in text:
        source = 'ACM'
    elif 'INSTITUTE OF ELECTRICAL AND ELECTRONICS ENGINEERS' in text or 'IEEE' in text:
        source = 'IEEE'
    elif 'PUBMED' in text:
        source = 'PubMed'
    if source:
        source_by_title[title] = source

# Filter citations for ACM papers
acm_citation_counts = []
for row in citations:
    title = row['title']
    src = source_by_title.get(title)
    if src == 'ACM':
        try:
            c = int(row['citation_count'])
        except Exception:
            continue
        acm_citation_counts.append(c)

avg_citations = mean(acm_citation_counts) if acm_citation_counts else None

import json as _json
result = _json.dumps({'average_citation_count_acm_2018': avg_citations, 'num_papers': len(acm_citation_counts)})
print("__RESULT__:")
print(result)"""

env_args = {'var_call_ydfRZE3TcYBzrcXGM600Om9H': 'file_storage/call_ydfRZE3TcYBzrcXGM600Om9H.json', 'var_call_Vcqy3YthO7DsjiQGHt3bUHng': 'file_storage/call_Vcqy3YthO7DsjiQGHt3bUHng.json'}

exec(code, env_args)
