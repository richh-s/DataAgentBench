code = """import json, os
# Re-load variables

def load_var(v):
    import os, json
    if isinstance(v, str) and os.path.exists(v):
        with open(v, 'r', encoding='utf-8') as f:
            return json.load(f)
    return v

citations = load_var(var_call_miSkNz8p6p7BDfA93znX6uJl)
papers = load_var(var_call_sVulWUpU30niks3BaBshOK9e)

# Create map of paper title -> filename-derived title
paper_titles = set()
for d in papers:
    fn = d.get('filename')
    if fn and fn.lower().endswith('.txt'):
        paper_titles.add(fn[:-4])

# Find matched citation records and also collect titles
matched_records = []
for rec in citations:
    t = rec.get('title')
    if t in paper_titles:
        try:
            cc = int(rec.get('citation_count'))
        except:
            try:
                cc = int(float(rec.get('citation_count')))
            except:
                continue
        matched_records.append({'title': t, 'citation_count': cc})

# Sort matched_records by citation_count desc and print top 10
matched_sorted = sorted(matched_records, key=lambda x: x['citation_count'], reverse=True)
output = {
    'matched_count': len(matched_sorted),
    'top_10_by_citations': matched_sorted[:10]
}
print('__RESULT__:')
print(json.dumps(output))"""

env_args = {'var_call_miSkNz8p6p7BDfA93znX6uJl': 'file_storage/call_miSkNz8p6p7BDfA93znX6uJl.json', 'var_call_sVulWUpU30niks3BaBshOK9e': 'file_storage/call_sVulWUpU30niks3BaBshOK9e.json', 'var_call_E9zo6Yr9OkdioCseI3gjlPbS': {'average_citation_count': 59.36, 'paper_count': 55, 'total_citations': 3265}}

exec(code, env_args)
