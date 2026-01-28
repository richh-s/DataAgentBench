code = """import json
# Load query results from storage file paths provided by previous tool calls
with open(var_call_AwnT5llpP4OaQ4K6v7BvasJn, 'r', encoding='utf-8') as f:
    acm_docs = json.load(f)
with open(var_call_dljWntUnqzMzbRDUDIR4Ol8E, 'r', encoding='utf-8') as f:
    citations = json.load(f)

# Build set of titles from ACM documents (filename without .txt)
acm_titles = set()
for doc in acm_docs:
    fn = doc.get('filename', '')
    if fn.lower().endswith('.txt'):
        title = fn[:-4]
    else:
        title = fn
    acm_titles.add(title.strip().lower())

# Find citations from 2018 that match ACM titles
matched_counts = []
for rec in citations:
    title = rec.get('title', '').strip().lower()
    try:
        count = int(rec.get('citation_count', 0))
    except:
        try:
            count = int(float(rec.get('citation_count', 0)))
        except:
            count = 0
    if title in acm_titles:
        matched_counts.append(count)

# Compute average
if len(matched_counts) > 0:
    total = sum(matched_counts)
    avg = total / len(matched_counts)
    result = {
        'average_citation_count': round(avg, 2),
        'paper_count': len(matched_counts),
        'total_citations': total
    }
else:
    result = {
        'average_citation_count': None,
        'paper_count': 0,
        'total_citations': 0
    }

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_AwnT5llpP4OaQ4K6v7BvasJn': 'file_storage/call_AwnT5llpP4OaQ4K6v7BvasJn.json', 'var_call_dljWntUnqzMzbRDUDIR4Ol8E': 'file_storage/call_dljWntUnqzMzbRDUDIR4Ol8E.json'}

exec(code, env_args)
