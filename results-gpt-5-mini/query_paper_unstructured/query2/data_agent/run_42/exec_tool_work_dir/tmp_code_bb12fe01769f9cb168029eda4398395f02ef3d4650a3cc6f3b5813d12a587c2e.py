code = """import json

# Access variables from previous tool calls (provided in storage)
paper_docs_var = var_call_GbuaTr5ohZU6CckypqvaSnbr
citations_var = var_call_ziZJf93MNCSRgtn202EhbrzI

def load_var(v):
    if isinstance(v, str):
        with open(v, 'r', encoding='utf-8') as f:
            return json.load(f)
    return v

paper_docs = load_var(paper_docs_var)
citations = load_var(citations_var)

# Build set of titles from paper_docs (filename without .txt)
acm_titles = set()
for doc in paper_docs:
    fn = doc.get('filename', '')
    if fn.endswith('.txt'):
        title = fn[:-4]
    else:
        title = fn
    title = title.strip()
    if title:
        acm_titles.add(title)

# Aggregate citation counts for titles present in acm_titles
total = 0
count = 0
for rec in citations:
    title = rec.get('title')
    if title in acm_titles:
        try:
            cc = int(rec.get('citation_count', 0))
        except:
            try:
                cc = int(float(rec.get('citation_count', 0)))
            except:
                cc = 0
        total += cc
        count += 1

avg = round(total / count, 2) if count > 0 else None
result = {"average_citation_count": avg, "paper_count": count}

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_GbuaTr5ohZU6CckypqvaSnbr': 'file_storage/call_GbuaTr5ohZU6CckypqvaSnbr.json', 'var_call_ziZJf93MNCSRgtn202EhbrzI': 'file_storage/call_ziZJf93MNCSRgtn202EhbrzI.json'}

exec(code, env_args)
