code = """import json, re
from statistics import mean

# Load data from previous calls
with open(var_call_rG5SAMT6YeVu2Ve9bBoMTCMV, 'r') as f:
    citations = json.load(f)
with open(var_call_EJXRCT60rjRXYnU3CWM3P17X, 'r') as f:
    papers = json.load(f)

# Build a lookup from title to whether source is ACM
acm_titles = set()
for doc in papers:
    text = doc.get('text','')
    # Heuristic: consider it ACM if 'Copyright' line mentions ACM or if 'ACM' appears near 'Copyright'
    if re.search(r'Copyright .*ACM', text, re.IGNORECASE) or re.search(r'ACM Classification Keywords', text, re.IGNORECASE):
        filename = doc.get('filename','')
        if filename.lower().endswith('.txt'):
            title = filename[:-4]
        else:
            title = filename
        acm_titles.add(title.strip())

# Filter citations for ACM papers
acm_citations = []
for row in citations:
    title = row['title']
    if title in acm_titles:
        try:
            c = int(row['citation_count'])
        except Exception:
            continue
        acm_citations.append(c)

avg_citations = mean(acm_citations) if acm_citations else 0

result = {
  'average_citation_count_2018_acm': avg_citations,
  'num_papers_counted': len(acm_citations)
}

out = json.dumps(result)
print("__RESULT__:")
print(out)"""

env_args = {'var_call_rG5SAMT6YeVu2Ve9bBoMTCMV': 'file_storage/call_rG5SAMT6YeVu2Ve9bBoMTCMV.json', 'var_call_EJXRCT60rjRXYnU3CWM3P17X': 'file_storage/call_EJXRCT60rjRXYnU3CWM3P17X.json'}

exec(code, env_args)
