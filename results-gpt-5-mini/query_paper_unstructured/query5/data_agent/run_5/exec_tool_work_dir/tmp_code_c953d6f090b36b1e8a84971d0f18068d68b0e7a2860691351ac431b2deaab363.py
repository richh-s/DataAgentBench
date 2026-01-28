code = """import json
# Load previous tool results from storage paths
with open(var_call_19XDnOlqndQy2stmvg5LxRpF, 'r') as f:
    citations = json.load(f)
with open(var_call_hIyXercpEWdma46qQcNB9lEc, 'r') as f:
    paper_docs = json.load(f)

# Build set of paper titles from paper_docs filenames (remove .txt)
chi_titles = set()
for doc in paper_docs:
    fn = doc.get('filename', '')
    if fn.endswith('.txt'):
        title = fn[:-4]
    else:
        title = fn
    chi_titles.add(title)

# Match citations for 2020 (citations list already filtered by year in query)
matched = []
total = 0
for rec in citations:
    title = rec.get('title')
    # citation_count may be string; convert
    try:
        count = int(rec.get('citation_count', 0))
    except:
        try:
            count = int(float(rec.get('citation_count', 0)))
        except:
            count = 0
    if title in chi_titles:
        matched.append({'title': title, 'citation_count': count})
        total += count

# Sort matched by citation_count descending
matched_sorted = sorted(matched, key=lambda x: x['citation_count'], reverse=True)

output = {
    'papers': matched_sorted,
    'total_citations_2020_for_CHI_papers': total,
    'num_papers': len(matched_sorted)
}

print("__RESULT__:")
print(json.dumps(output))"""

env_args = {'var_call_v7HMDIbGHNsuIfvtYfbxVgUs': ['paper_docs'], 'var_call_aYzyJZaT1u0HPO8aCjMmrqqU': ['Citations', 'sqlite_sequence'], 'var_call_19XDnOlqndQy2stmvg5LxRpF': 'file_storage/call_19XDnOlqndQy2stmvg5LxRpF.json', 'var_call_hIyXercpEWdma46qQcNB9lEc': 'file_storage/call_hIyXercpEWdma46qQcNB9lEc.json', 'var_call_w6GNjithhlXABlcTzzXHBLb0': 'file_storage/call_w6GNjithhlXABlcTzzXHBLb0.json'}

exec(code, env_args)
