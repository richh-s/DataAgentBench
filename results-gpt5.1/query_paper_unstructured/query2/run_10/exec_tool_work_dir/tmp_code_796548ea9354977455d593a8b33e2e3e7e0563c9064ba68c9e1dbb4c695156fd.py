code = """import json, statistics, re

# Load citation data from file
path = var_call_lsWldRJaFTJSjFDEDGbarYm1
with open(path, 'r') as f:
    citations = json.load(f)

# Build set of titles cited in 2018
titles_2018 = {c['title'] for c in citations}

# Load paper docs metadata
path_docs = var_call_WQtJkM28vx3esAsXQ3mJ2taZ
with open(path_docs, 'r') as f:
    paper_docs = json.load(f)

# Helper to guess source from text
acm_pattern = re.compile(r"ACM", re.IGNORECASE)
ieee_pattern = re.compile(r"IEEE", re.IGNORECASE)

acm_titles = set()
for doc in paper_docs:
    filename = doc.get('filename','')
    title = filename.rsplit('.txt',1)[0]
    text = doc.get('text','')
    if not title or title not in titles_2018:
        continue
    # very rough heuristic: if ACM appears in copyright/permission section
    if acm_pattern.search(text):
        acm_titles.add(title)

# Collect citation counts for ACM papers cited in 2018
acm_citations = [int(c['citation_count']) for c in citations if c['title'] in acm_titles]

avg = statistics.mean(acm_citations) if acm_citations else None

result = json.dumps({"average_citation_count_acm_2018": avg, "num_papers": len(acm_citations)})
print("__RESULT__:")
print(result)"""

env_args = {'var_call_lsWldRJaFTJSjFDEDGbarYm1': 'file_storage/call_lsWldRJaFTJSjFDEDGbarYm1.json', 'var_call_WQtJkM28vx3esAsXQ3mJ2taZ': 'file_storage/call_WQtJkM28vx3esAsXQ3mJ2taZ.json'}

exec(code, env_args)
