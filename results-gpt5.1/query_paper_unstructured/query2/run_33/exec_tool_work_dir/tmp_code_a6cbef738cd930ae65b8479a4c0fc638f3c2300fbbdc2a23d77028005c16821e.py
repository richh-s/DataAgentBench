code = """import json, re

# Load citation records for 2018
path_citations = var_call_xSCFnDwiFIn28TbE3dKChrh7
with open(path_citations, 'r') as f:
    citations_2018 = json.load(f)

# Load paper documents
path_docs = var_call_8nbcZbITBDmxSKtmloej2QPS
with open(path_docs, 'r') as f:
    paper_docs = json.load(f)

# Build a lookup from title to inferred source (publisher)
# We'll infer "ACM" if the text contains common ACM markers.
acm_patterns = [
    r"ACM\s+Conference",
    r"ACM\s+Press",
    r"Copyright\s+20\d{2}\s+ACM",
    r"\u00a9\s*ACM",
    r"Association for Computing Machinery",
]

# Map from title (filename without .txt) to source string (e.g., 'ACM', 'IEEE', 'Other')
source_by_title = {}

for doc in paper_docs:
    filename = doc.get('filename', '')
    text = doc.get('text', '') or ''
    if not filename.lower().endswith('.txt'):
        continue
    title = filename[:-4]
    source = 'Other'
    for pat in acm_patterns:
        if re.search(pat, text, flags=re.IGNORECASE):
            source = 'ACM'
            break
    source_by_title[title] = source

# Filter citation records to those whose corresponding paper source is ACM
acm_citations = []
for rec in citations_2018:
    title = rec.get('title')
    if not title:
        continue
    source = source_by_title.get(title)
    if source == 'ACM':
        try:
            c = int(rec.get('citation_count'))
        except (TypeError, ValueError):
            continue
        acm_citations.append(c)

if acm_citations:
    avg_citations = sum(acm_citations) / len(acm_citations)
else:
    avg_citations = None

result = {
    'average_citation_count_acm_2018': avg_citations,
    'num_acm_papers_2018': len(acm_citations)
}

res_str = json.dumps(result)
print("__RESULT__:")
print(res_str)"""

env_args = {'var_call_xSCFnDwiFIn28TbE3dKChrh7': 'file_storage/call_xSCFnDwiFIn28TbE3dKChrh7.json', 'var_call_8nbcZbITBDmxSKtmloej2QPS': 'file_storage/call_8nbcZbITBDmxSKtmloej2QPS.json'}

exec(code, env_args)
