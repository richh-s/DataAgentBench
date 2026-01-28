code = """import json

# Load variables from storage. They may be file paths (strings) or actual lists.

def load_var(v):
    if isinstance(v, str):
        with open(v, 'r', encoding='utf-8') as f:
            return json.load(f)
    return v

citations = load_var(var_call_fQqt0qo1VsgwgRHo16Hm6e5v)
acm_docs = load_var(var_call_2L1eSx7puUSg4GXOGe8NuCPG)

# Build set of titles from ACM-matching documents (strip .txt)
acm_titles = set()
for d in acm_docs:
    fn = d.get('filename', '')
    if fn.endswith('.txt'):
        acm_titles.add(fn[:-4])
    else:
        acm_titles.add(fn)

# Iterate citations and collect those whose title is in acm_titles
matched_counts = []
matched_titles = []
for rec in citations:
    title = rec.get('title')
    if title in acm_titles:
        try:
            cnt = int(rec.get('citation_count', 0))
        except:
            try:
                cnt = int(float(rec.get('citation_count', 0)))
            except:
                cnt = 0
        matched_counts.append(cnt)
        matched_titles.append(title)

n = len(matched_counts)
if n > 0:
    total = sum(matched_counts)
    avg = total / n
    avg_rounded = round(avg, 2)
else:
    total = 0
    avg = None
    avg_rounded = None

result = {
    'average_citation_count': avg_rounded,
    'matched_papers': n,
    'total_citation_count': total,
    'matched_titles_sample': matched_titles[:20]
}

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_2L1eSx7puUSg4GXOGe8NuCPG': 'file_storage/call_2L1eSx7puUSg4GXOGe8NuCPG.json', 'var_call_fQqt0qo1VsgwgRHo16Hm6e5v': 'file_storage/call_fQqt0qo1VsgwgRHo16Hm6e5v.json'}

exec(code, env_args)
