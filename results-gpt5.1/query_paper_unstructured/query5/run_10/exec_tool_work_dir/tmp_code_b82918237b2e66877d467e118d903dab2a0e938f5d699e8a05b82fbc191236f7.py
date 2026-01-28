code = """import json, pandas as pd

# Load citation data
data_path = var_call_BQQYY4L6tIvYFh3UYewHdOwN
with open(data_path, 'r') as f:
    citations = json.load(f)

# Load paper docs metadata (from filenames and text) to detect CHI venue
paper_path = var_call_hP86qRBr99iUpaMtQhyhQgkp
with open(paper_path, 'r') as f:
    papers = json.load(f)

# Build a mapping from title to whether it's a CHI paper
chi_titles = set()
for doc in papers:
    filename = doc.get('filename', '')
    title = filename[:-4] if filename.lower().endswith('.txt') else filename
    text = doc.get('text', '').upper()
    if 'CHI ' in text or " CHI'" in text or '\nCHI ' in text:
        chi_titles.add(title)

# Sum citation counts in 2020 for CHI papers

total_citations = 0
for row in citations:
    title = row.get('title')
    if title in chi_titles:
        try:
            c = int(row.get('citation_count', 0))
        except ValueError:
            c = 0
        total_citations += c

result = json.dumps(total_citations)
print("__RESULT__:")
print(result)"""

env_args = {'var_call_BQQYY4L6tIvYFh3UYewHdOwN': 'file_storage/call_BQQYY4L6tIvYFh3UYewHdOwN.json', 'var_call_S7yrIgrZeQtjm55fRo9hpRPi': ['paper_docs'], 'var_call_hP86qRBr99iUpaMtQhyhQgkp': 'file_storage/call_hP86qRBr99iUpaMtQhyhQgkp.json'}

exec(code, env_args)
