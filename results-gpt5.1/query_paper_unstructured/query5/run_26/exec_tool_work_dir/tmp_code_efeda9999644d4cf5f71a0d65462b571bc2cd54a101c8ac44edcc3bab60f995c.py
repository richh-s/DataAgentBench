code = """import json, pandas as pd
from pathlib import Path

# Load citations data
citations = var_call_HWC7GIcFOdJ0iGTOTIl4gn6B
if isinstance(citations, str) and citations.endswith('.json'):
    citations = json.loads(Path(citations).read_text())

# Load paper docs metadata
paper_docs = var_call_VHe0djlfPY03tWiZWr0bf6V3
if isinstance(paper_docs, str) and paper_docs.endswith('.json'):
    paper_docs = json.loads(Path(paper_docs).read_text())

# Build a mapping from title to whether it's a CHI paper
chi_titles = set()
for doc in paper_docs:
    filename = doc.get('filename','')
    text = doc.get('text','') or ''
    title = filename[:-4] if filename.lower().endswith('.txt') else filename
    is_chi = ' chi ' in text.lower() or "chi '" in text.lower() or 'chi,' in text.lower()
    # Heuristic: look for ACM CHI conference strings
    if 'chi conference on human factors in computing systems' in text.lower() or "chi '" in text.lower():
        is_chi = True
    if is_chi:
        chi_titles.add(title)

# Sum citation counts in 2020 for CHI titles

chi_citations_total = 0
for row in citations:
    title = row.get('title')
    if title in chi_titles:
        try:
            chi_citations_total += int(row.get('citation_count', 0))
        except Exception:
            pass

result = chi_citations_total

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_HWC7GIcFOdJ0iGTOTIl4gn6B': 'file_storage/call_HWC7GIcFOdJ0iGTOTIl4gn6B.json', 'var_call_VHe0djlfPY03tWiZWr0bf6V3': 'file_storage/call_VHe0djlfPY03tWiZWr0bf6V3.json'}

exec(code, env_args)
