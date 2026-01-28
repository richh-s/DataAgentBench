code = """import json
import re

# Load large results from storage file paths
with open(var_call_IPADvlMw81ScJ8DeT2Id57iQ, 'r', encoding='utf-8') as f:
    citations = json.load(f)
with open(var_call_igXg9bpal532b5b5aHinFvfo, 'r', encoding='utf-8') as f:
    papers = json.load(f)

# Build set of titles for papers whose text indicates CHI venue
chi_titles = set()
for p in papers:
    filename = p.get('filename', '')
    title = filename[:-4] if filename.lower().endswith('.txt') else filename
    text = p.get('text', '') or ''
    # Search for whole-word CHI (case-sensitive) to avoid matching 'machine'
    if re.search(r"\bCHI\b", text):
        chi_titles.add(title)

# Match citation records to CHI titles and sum citation_count for 2020
matched = []
for c in citations:
    title = c.get('title')
    cc = c.get('citation_count')
    try:
        count = int(cc)
    except:
        try:
            count = int(float(cc))
        except:
            count = 0
    if title in chi_titles:
        matched.append({'title': title, 'citation_count': count})

total = sum(x['citation_count'] for x in matched)

result = {
    'total_citations_2020_for_CHI_papers': total,
    'num_chi_papers_cited_in_2020': len(matched),
    'papers': matched
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_IPADvlMw81ScJ8DeT2Id57iQ': 'file_storage/call_IPADvlMw81ScJ8DeT2Id57iQ.json', 'var_call_igXg9bpal532b5b5aHinFvfo': 'file_storage/call_igXg9bpal532b5b5aHinFvfo.json'}

exec(code, env_args)
