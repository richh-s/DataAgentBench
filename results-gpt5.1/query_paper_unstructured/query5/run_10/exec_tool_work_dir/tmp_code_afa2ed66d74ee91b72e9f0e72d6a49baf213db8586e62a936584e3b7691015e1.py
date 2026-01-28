code = """import json, pandas as pd

data_path = var_call_BQQYY4L6tIvYFh3UYewHdOwN
with open(data_path, 'r') as f:
    citations = json.load(f)

paper_path = var_call_hP86qRBr99iUpaMtQhyhQgkp
with open(paper_path, 'r') as f:
    papers = json.load(f)

chi_titles = set()
for doc in papers:
    filename = doc.get('filename', '')
    if filename.lower().endswith('.txt'):
        title = filename[:-4]
    else:
        title = filename
    text = doc.get('text', '').upper()
    if ' CHI ' in text or '\nCHI ' in text or "CHI CONFERENCE" in text:
        chi_titles.add(title)

total_citations = 0
for row in citations:
    title = row.get('title')
    if title in chi_titles:
        try:
            c = int(row.get('citation_count', 0))
        except Exception:
            c = 0
        total_citations += c

result = json.dumps(total_citations)
print("__RESULT__:")
print(result)"""

env_args = {'var_call_BQQYY4L6tIvYFh3UYewHdOwN': 'file_storage/call_BQQYY4L6tIvYFh3UYewHdOwN.json', 'var_call_S7yrIgrZeQtjm55fRo9hpRPi': ['paper_docs'], 'var_call_hP86qRBr99iUpaMtQhyhQgkp': 'file_storage/call_hP86qRBr99iUpaMtQhyhQgkp.json'}

exec(code, env_args)
