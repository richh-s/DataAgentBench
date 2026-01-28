code = """import json, pandas as pd, re

# Load full citation data
with open(var_call_0suTOury4oTqzCJWqBtu02Sd, 'r') as f:
    citations = json.load(f)

# Load paper docs metadata (we'll parse venue from text heuristically)
with open(var_call_jyE7oZbDXwmn1XWHXVr2AqWL, 'r') as f:
    docs = json.load(f)

# Build mapping from title to venue using filename/text
chi_titles = set()
for doc in docs:
    filename = doc.get('filename','')
    text = doc.get('text','') or ''
    # title is filename without .txt
    if filename.lower().endswith('.txt'):
        title = filename[:-4]
    else:
        title = filename
    # Heuristic: identify CHI venue from text header lines
    header = text[:1000].upper()
    if 'CHI ' in header or "CONFERENCE ON HUMAN FACTORS IN COMPUTING SYSTEMS" in header:
        chi_titles.add(title)

# Sum citation counts in 2020 for CHI papers
chi_citation_total = 0
for row in citations:
    title = row.get('title','')
    if title in chi_titles:
        try:
            chi_citation_total += int(row.get('citation_count',0))
        except ValueError:
            pass

result = chi_citation_total

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_0suTOury4oTqzCJWqBtu02Sd': 'file_storage/call_0suTOury4oTqzCJWqBtu02Sd.json', 'var_call_jyE7oZbDXwmn1XWHXVr2AqWL': 'file_storage/call_jyE7oZbDXwmn1XWHXVr2AqWL.json'}

exec(code, env_args)
