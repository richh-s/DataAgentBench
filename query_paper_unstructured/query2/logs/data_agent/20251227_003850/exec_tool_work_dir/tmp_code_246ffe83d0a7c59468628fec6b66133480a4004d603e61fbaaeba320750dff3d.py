code = """import json
import os

# Load citations for 2018
citations_path = var_call_N5i7a39gwMbmdTH2x3oF4vgP
with open(citations_path, 'r', encoding='utf-8') as f:
    citations_2018 = json.load(f)

# Load paper documents
docs_path = var_call_Wo6Adw0lsMDvdWWaD5ipE5lZ
with open(docs_path, 'r', encoding='utf-8') as f:
    paper_docs = json.load(f)

# Helper to detect ACM source from text heuristically
def is_acm_source(text: str) -> bool:
    if not text:
        return False
    t = text.lower()
    head = t[:3000]
    # Strong indicators
    if 'permissions@acm.org' in t:
        return True
    if 'association for computing machinery' in t:
        return True
    # Common ACM copyright/permission phrasing
    if ('permission to make digital or hard copies' in t and 'acm' in t):
        return True
    if ('copyright' in head and 'acm' in head):
        return True
    # Proceedings style
    if 'proceedings of the acm' in t:
        return True
    return False

# Build set of ACM titles from paper_docs (filename without .txt)
acm_titles = set()
for doc in paper_docs:
    filename = doc.get('filename')
    text = doc.get('text', '')
    if isinstance(filename, str):
        title = filename[:-4] if filename.lower().endswith('.txt') else filename
    else:
        title = None
    if title and is_acm_source(text):
        acm_titles.add(title)

# Filter citations to those whose title is in acm_titles and compute average citation_count
counts = []
for rec in citations_2018:
    title = rec.get('title')
    if title in acm_titles:
        cc = rec.get('citation_count')
        try:
            cc_int = int(cc)
        except Exception:
            try:
                cc_int = int(float(cc))
            except Exception:
                continue
        counts.append(cc_int)

avg = None
if counts:
    avg = sum(counts) / len(counts)

# Prepare JSON-serializable result
result = json.dumps({'average_citation_count_for_acm_cited_2018': avg})
print("__RESULT__:")
print(result)"""

env_args = {'var_call_N5i7a39gwMbmdTH2x3oF4vgP': 'file_storage/call_N5i7a39gwMbmdTH2x3oF4vgP.json', 'var_call_Wo6Adw0lsMDvdWWaD5ipE5lZ': 'file_storage/call_Wo6Adw0lsMDvdWWaD5ipE5lZ.json'}

exec(code, env_args)
