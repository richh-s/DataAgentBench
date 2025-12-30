code = """import json, os, re

# Load citation data
path_citations = var_call_UAdC7f7WH1H127OYa0hgMgxf
with open(path_citations, 'r') as f:
    citations = json.load(f)

# Load paper docs
path_docs = var_call_daqgqCQtHXI6llRr32nrggSO
with open(path_docs, 'r') as f:
    docs = json.load(f)

# Build lookup from title to venue using filename/text heuristics
venue_by_title = {}
for d in docs:
    filename = d.get('filename','')
    text = d.get('text','') or ''
    title = re.sub(r"\.txt$","", filename)
    # Heuristic: consider it CHI if 'CHI ' appears near top or "CHI '" pattern, or "CHI Conference" etc.
    header = text[:2000].upper()
    is_chi = False
    if 'CHI ' in header or "CHI '" in header or 'ACM CHI' in header or 'CHI CONFERENCE' in header:
        is_chi = True
    if is_chi and title:
        venue_by_title[title] = 'CHI'

# Sum citation counts for CHI papers cited in 2020
total_citations = 0
for c in citations:
    title = c.get('title','')
    if venue_by_title.get(title) == 'CHI':
        try:
            cnt = int(c.get('citation_count',0))
        except Exception:
            cnt = 0
        total_citations += cnt

import json as js
result = js.dumps(total_citations)
print("__RESULT__:")
print(result)"""

env_args = {'var_call_UAdC7f7WH1H127OYa0hgMgxf': 'file_storage/call_UAdC7f7WH1H127OYa0hgMgxf.json', 'var_call_daqgqCQtHXI6llRr32nrggSO': 'file_storage/call_daqgqCQtHXI6llRr32nrggSO.json'}

exec(code, env_args)
