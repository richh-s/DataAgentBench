code = """import json, re

# Load the query results from storage files
with open(var_call_4EzpzOptxeaMqYDgNd8NPBpX, 'r', encoding='utf-8') as f:
    citations = json.load(f)
with open(var_call_w0MmkzoelZmlFsuj0FRHSE9M, 'r', encoding='utf-8') as f:
    docs = json.load(f)

# Build a mapping from title (filename without .txt) to doc metadata
doc_map = {}
for d in docs:
    filename = d.get('filename', '')
    title = filename.rsplit('.txt', 1)[0]
    text = d.get('text', '') or ''
    text_lower = text.lower()
    # Determine source heuristically
    source = None
    if 'acm' in text_lower:
        source = 'ACM'
    elif 'ieee' in text_lower:
        source = 'IEEE'
    elif 'pubmed' in text_lower or 'springer' in text_lower:
        source = 'PubMed'
    else:
        source = 'Unknown'
    # Extract year (first 4-digit year between 1900 and 2030)
    match = re.search(r"\b(19|20)\d{2}\b", text)
    year = int(match.group()) if match else None
    doc_map[title] = {'source': source, 'year': year}

# Collect citation counts for citations in 2018 that correspond to ACM papers
counts = []
missing_titles = []
for rec in citations:
    title = rec.get('title')
    raw_count = rec.get('citation_count')
    try:
        count = int(float(raw_count))
    except Exception:
        continue
    meta = doc_map.get(title)
    if not meta:
        missing_titles.append(title)
        continue
    if meta.get('source') == 'ACM':
        counts.append(count)

# Compute average
if counts:
    avg = sum(counts) / len(counts)
else:
    avg = None

result = {
    'average_citation_count': avg,
    'acm_paper_count': len(counts),
    'total_citation_records_considered': len(citations),
    'missing_document_matches': len(missing_titles)
}

import json
print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_4EzpzOptxeaMqYDgNd8NPBpX': 'file_storage/call_4EzpzOptxeaMqYDgNd8NPBpX.json', 'var_call_w0MmkzoelZmlFsuj0FRHSE9M': 'file_storage/call_w0MmkzoelZmlFsuj0FRHSE9M.json'}

exec(code, env_args)
