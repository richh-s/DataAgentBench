code = """import json
import re

# Load the large query results from storage-provided file paths
with open(var_call_FMSV1XAWKu9ENKZGTzjMjJWx, 'r', encoding='utf-8') as f:
    citations = json.load(f)
with open(var_call_n8s9SEQQPpWqOWaxbK0fkd0A, 'r', encoding='utf-8') as f:
    papers = json.load(f)

# Build map from filename without .txt to paper record
paper_map = {}
for p in papers:
    filename = p.get('filename','')
    key = filename[:-4] if filename.lower().endswith('.txt') else filename
    paper_map[key] = p

matched = []
total = 0
for c in citations:
    title = c.get('title')
    # match title exactly to filename without .txt
    paper = paper_map.get(title)
    if not paper:
        continue
    text = paper.get('text','')
    # look for CHI as a distinct token (case-insensitive)
    if re.search(r"\bCHI\b", text, re.IGNORECASE):
        try:
            count = int(c.get('citation_count', 0))
        except:
            try:
                count = int(float(c.get('citation_count',0)))
            except:
                count = 0
        matched.append({'title': title, 'citation_count': count})
        total += count

# Prepare output
output = {'total_citations': total, 'papers': matched}

print('__RESULT__:')
print(json.dumps(output))"""

env_args = {'var_call_WzZNvCCfKSHCUcpJzTb5LW0e': ['paper_docs'], 'var_call_Z5HJl5AazCIWo041ET2vt29C': ['Citations', 'sqlite_sequence'], 'var_call_n8s9SEQQPpWqOWaxbK0fkd0A': 'file_storage/call_n8s9SEQQPpWqOWaxbK0fkd0A.json', 'var_call_FMSV1XAWKu9ENKZGTzjMjJWx': 'file_storage/call_FMSV1XAWKu9ENKZGTzjMjJWx.json'}

exec(code, env_args)
