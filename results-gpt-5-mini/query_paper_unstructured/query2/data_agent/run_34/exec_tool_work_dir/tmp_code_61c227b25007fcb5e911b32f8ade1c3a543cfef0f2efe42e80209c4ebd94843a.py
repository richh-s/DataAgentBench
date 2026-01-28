code = """import json
# Load tool results from storage file paths
with open(var_call_kyKLqw5u9jvNalx9yUkEIiFm, 'r') as f:
    citations = json.load(f)
with open(var_call_KSVs9jS8bC95Vbj2gYq6YK2X, 'r') as f:
    docs = json.load(f)
# Build filename -> text map
docs_map = {d.get('filename',''): d.get('text','') for d in docs}
# Iterate citations and select those whose corresponding doc contains 'ACM'
total = 0
count = 0
selected_titles = []
for rec in citations:
    title = rec.get('title')
    if title is None:
        continue
    filename = title + '.txt'
    text = docs_map.get(filename)
    if not text:
        continue
    if 'acm' in text.lower():
        try:
            c = int(rec.get('citation_count', 0))
        except Exception:
            try:
                c = int(float(rec.get('citation_count', 0)))
            except Exception:
                continue
        total += c
        count += 1
        selected_titles.append(title)

if count > 0:
    avg = total / count
    avg_rounded = round(avg, 2)
else:
    avg_rounded = None

result = {
    'average_citation_count': avg_rounded,
    'paper_count': count
}

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_kyKLqw5u9jvNalx9yUkEIiFm': 'file_storage/call_kyKLqw5u9jvNalx9yUkEIiFm.json', 'var_call_zWuBwaQo1LjCZ7dFZUI0hp1x': ['paper_docs'], 'var_call_KSVs9jS8bC95Vbj2gYq6YK2X': 'file_storage/call_KSVs9jS8bC95Vbj2gYq6YK2X.json'}

exec(code, env_args)
