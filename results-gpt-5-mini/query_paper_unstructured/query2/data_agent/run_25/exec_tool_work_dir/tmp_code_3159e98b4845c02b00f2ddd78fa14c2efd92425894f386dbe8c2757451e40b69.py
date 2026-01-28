code = """import json

# Load results from previous tool calls stored in files
with open(var_call_JJ1nT595UZgseVjL3CzGETy1, 'r', encoding='utf-8') as f:
    acm_docs = json.load(f)
with open(var_call_hpcHjYg2QXcDmUMjJFlzbv1w, 'r', encoding='utf-8') as f:
    citations = json.load(f)

# Extract titles from ACM-related paper documents (filename without .txt)
acm_titles = set()
for doc in acm_docs:
    fn = doc.get('filename', '')
    title = fn.rsplit('.txt', 1)[0].strip()
    if title:
        acm_titles.add(title)

# Match citations from 2018 to ACM titles and compute average
matched = []
for rec in citations:
    t = rec.get('title', '').strip()
    cc = rec.get('citation_count', None)
    try:
        cc_int = int(cc) if cc is not None else None
    except:
        try:
            cc_int = int(float(cc))
        except:
            cc_int = None
    if t in acm_titles and cc_int is not None:
        matched.append({'title': t, 'citation_count': cc_int})

count = len(matched)
if count > 0:
    total = sum(x['citation_count'] for x in matched)
    average = total / count
else:
    total = 0
    average = None

result = {
    'average_citation_count': average,
    'matched_paper_count': count,
    'total_citations': total
}

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_JJ1nT595UZgseVjL3CzGETy1': 'file_storage/call_JJ1nT595UZgseVjL3CzGETy1.json', 'var_call_hpcHjYg2QXcDmUMjJFlzbv1w': 'file_storage/call_hpcHjYg2QXcDmUMjJFlzbv1w.json'}

exec(code, env_args)
