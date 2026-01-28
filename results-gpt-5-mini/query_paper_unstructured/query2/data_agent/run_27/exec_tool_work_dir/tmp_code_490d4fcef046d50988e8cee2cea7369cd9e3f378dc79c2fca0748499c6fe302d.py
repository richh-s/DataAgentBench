code = """import json
import os

# Load citations result
path_citations = var_call_rYrnG7HjLdLINm4evdHhbh9M
if isinstance(path_citations, str) and os.path.exists(path_citations):
    with open(path_citations, 'r', encoding='utf-8') as f:
        citations = json.load(f)
else:
    citations = path_citations

# Load paper docs result
path_papers = var_call_Y5KLczuSB4Aa3jrGHH0xi7q9
if isinstance(path_papers, str) and os.path.exists(path_papers):
    with open(path_papers, 'r', encoding='utf-8') as f:
        papers = json.load(f)
else:
    papers = path_papers

# Build set of titles from paper filenames (strip .txt)
acm_titles = set()
for doc in papers:
    filename = doc.get('filename', '')
    if filename.lower().endswith('.txt'):
        title = filename[:-4]
    else:
        title = filename
    acm_titles.add(title)

# Filter citations for those titles (citations already for 2018)
matched_counts = []
for rec in citations:
    title = rec.get('title')
    count_raw = rec.get('citation_count')
    try:
        count = int(count_raw)
    except Exception:
        try:
            count = int(float(count_raw))
        except Exception:
            continue
    if title in acm_titles:
        matched_counts.append(count)

if len(matched_counts) == 0:
    avg = None
    total = 0
    n = 0
else:
    total = sum(matched_counts)
    n = len(matched_counts)
    avg = total / n

result = {
    'average_citation_count': avg,
    'matched_papers': n,
    'total_citation_count': total
}

import json
print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_rYrnG7HjLdLINm4evdHhbh9M': 'file_storage/call_rYrnG7HjLdLINm4evdHhbh9M.json', 'var_call_Y5KLczuSB4Aa3jrGHH0xi7q9': 'file_storage/call_Y5KLczuSB4Aa3jrGHH0xi7q9.json'}

exec(code, env_args)
