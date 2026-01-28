code = """import json, pandas as pd

# Load citation data
with open(var_call_VPPQvpsMrfQvguUHtCs2e9jT, 'r') as f:
    citations = json.load(f)

# Load paper docs metadata (filename and text)
with open(var_call_fVNar3gYVfk7mfnr1h3nI9ep, 'r') as f:
    papers = json.load(f)

# Build a mapping from title (filename without .txt) to inferred venue (simple heuristic)
venue_map = {}
for doc in papers:
    filename = doc.get('filename', '')
    text = doc.get('text', '')
    if not filename or not text:
        continue
    title = filename[:-4] if filename.lower().endswith('.txt') else filename
    # Heuristic: check early part of text for venue keyword 'CHI'
    header = text[:2000].upper()
    venue = None
    if 'CHI ' in header or "CHI'" in header or '\nCHI\n' in header:
        venue = 'CHI'
    # store only if we detected CHI
    if venue == 'CHI':
        venue_map[title] = venue

# Sum citation counts for titles that are CHI papers
chi_citation_total = 0
for rec in citations:
    title = rec.get('title')
    if not title:
        continue
    if title in venue_map:
        try:
            chi_citation_total += int(rec.get('citation_count', 0))
        except Exception:
            pass

result = chi_citation_total

out = json.dumps(result)
print("__RESULT__:")
print(out)"""

env_args = {'var_call_VPPQvpsMrfQvguUHtCs2e9jT': 'file_storage/call_VPPQvpsMrfQvguUHtCs2e9jT.json', 'var_call_fVNar3gYVfk7mfnr1h3nI9ep': 'file_storage/call_fVNar3gYVfk7mfnr1h3nI9ep.json'}

exec(code, env_args)
