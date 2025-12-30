code = """import json
import os

# Load citations
with open(locals()['var_function-call-4481896084510856696'], 'r') as f:
    citations = json.load(f)

cited_titles = {c['title'] for c in citations}
citation_map = {c['title']: c['citation_count'] for c in citations}

# Load papers
# The previous query result for paper_docs is in var_function-call-13653321032674723116
with open(locals()['var_function-call-13653321032674723116'], 'r') as f:
    papers = json.load(f)

print(f"Loaded {len(papers)} papers.")

found_papers = []
for p in papers:
    # Filename is title + .txt
    title = p['filename'].replace('.txt', '')
    if title in cited_titles:
        found_papers.append(p)

print(f"Found {len(found_papers)} papers matching cited titles.")

# Filter by source ACM
acm_citations = []
for p in found_papers:
    text = p.get('text', '')
    header = text[:5000] # Check first 5000 chars
    
    # Heuristic for ACM source
    # Look for "Copyright" and "ACM" or "permissions@acm.org"
    is_acm = False
    if "permissions@acm.org" in header:
        is_acm = True
    elif "Copyright" in header and "ACM" in header:
        # Check if they are close? Or just assume if both present it's likely ACM.
        # Sometimes "ACM" is in the title or keywords.
        # But "Copyright" usually indicates publisher.
        is_acm = True
    elif "published by ACM" in header.lower():
        is_acm = True
    elif "ACM" in header and "IEEE" not in header:
        # If ACM is mentioned and IEEE is not, likely ACM (e.g. ACM Classification)
        is_acm = True
        
    if is_acm:
        title = p['filename'].replace('.txt', '')
        count = citation_map.get(title)
        if count is not None:
            acm_citations.append(int(count))

if len(acm_citations) > 0:
    avg_citations = sum(acm_citations) / len(acm_citations)
else:
    avg_citations = 0

print(f"Found {len(acm_citations)} ACM papers.")
print("__RESULT__:")
print(json.dumps(avg_citations))"""

env_args = {'var_function-call-4481896084510856696': 'file_storage/function-call-4481896084510856696.json', 'var_function-call-12106380733343301840': 'file_storage/function-call-12106380733343301840.json', 'var_function-call-13470949196896071643': {'count': 158, 'unique_titles': 158}, 'var_function-call-13653321032674723116': 'file_storage/function-call-13653321032674723116.json'}

exec(code, env_args)
