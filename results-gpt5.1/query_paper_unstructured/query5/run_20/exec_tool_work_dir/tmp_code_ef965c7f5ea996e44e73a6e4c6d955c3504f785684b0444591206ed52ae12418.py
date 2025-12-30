code = """import json, re
from pathlib import Path

with open(var_call_LTqIfOQ5gBCCkN5ArrTxCEYJ, 'r') as f:
    citations = json.load(f)
with open(var_call_LRwvKYV75bDUgQn6SYjRqyHT, 'r') as f:
    papers = json.load(f)

chi_titles = set()
for doc in papers:
    filename = doc.get('filename','')
    text = doc.get('text','') or ''
    title = re.sub(r'\.txt$','', filename).strip()
    header = text[:2000].upper()
    if ' CHI ' in header or "CHI '" in header or ' CHI,' in header or '\nCHI ' in header:
        chi_titles.add(title)

total_citations = 0
for row in citations:
    title = row.get('title','')
    if title in chi_titles:
        try:
            c = int(row.get('citation_count', 0))
        except Exception:
            c = 0
        total_citations += c

result = json.dumps({'total_citations_CHI_2020': total_citations})
print("__RESULT__:")
print(result)"""

env_args = {'var_call_LTqIfOQ5gBCCkN5ArrTxCEYJ': 'file_storage/call_LTqIfOQ5gBCCkN5ArrTxCEYJ.json', 'var_call_LRwvKYV75bDUgQn6SYjRqyHT': 'file_storage/call_LRwvKYV75bDUgQn6SYjRqyHT.json'}

exec(code, env_args)
