code = """import json, re
from statistics import mean

# Load citations data
path_citations = var_call_7eQNi6UcnOvCPMak6QfzFvEH
with open(path_citations, 'r') as f:
    citations = json.load(f)

# Load paper docs
path_docs = var_call_12WTiludKUpIDYjoCx3BPKYk
with open(path_docs, 'r') as f:
    docs = json.load(f)

# Build index from title to source using heuristic: look for 'Copyright YYYY © ACM' or 'ACM' near top
acm_titles = set()
for doc in docs:
    filename = doc.get('filename','')
    title = filename.rsplit('.txt',1)[0]
    text = doc.get('text','')
    header = text[:4000]
    # Heuristic: consider ACM if 'ACM' appears in header and not 'IEEE' or 'PubMed' dominating
    if 'ACM' in header and 'Copyright' in header:
        acm_titles.add(title)

# Now filter citations for those whose title is ACM
acm_citation_counts = []
for row in citations:
    title = row['title']
    if title in acm_titles:
        try:
            c = int(row['citation_count'])
        except:
            continue
        acm_citation_counts.append(c)

avg = mean(acm_citation_counts) if acm_citation_counts else None

result = {"average_citation_count_acm_2018": avg, "paper_count": len(acm_citation_counts)}

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_7eQNi6UcnOvCPMak6QfzFvEH': 'file_storage/call_7eQNi6UcnOvCPMak6QfzFvEH.json', 'var_call_12WTiludKUpIDYjoCx3BPKYk': 'file_storage/call_12WTiludKUpIDYjoCx3BPKYk.json'}

exec(code, env_args)
