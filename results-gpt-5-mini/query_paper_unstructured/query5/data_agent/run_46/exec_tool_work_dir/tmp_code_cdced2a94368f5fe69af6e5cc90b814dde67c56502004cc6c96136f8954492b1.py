code = """import json, re

# Load tool results from storage file paths
with open(var_call_uEXXygsM0MXYDT9Xr0aS4mNG, 'r', encoding='utf-8') as f:
    citations = json.load(f)
with open(var_call_ZpRLwxr35kslvSSpoVMVs7G0, 'r', encoding='utf-8') as f:
    paper_docs = json.load(f)

# Build set of titles for papers presented at CHI based on presence of the word CHI in text
chi_titles = set()
for doc in paper_docs:
    text = doc.get('text', '')
    # consider word boundary, case-insensitive
    if re.search(r"\bCHI\b", text, re.IGNORECASE):
        filename = doc.get('filename', '')
        if filename.lower().endswith('.txt'):
            title = filename[:-4]
        else:
            title = filename
        chi_titles.add(title)

# Find citations in 2020 for those titles
results = []
total_citations = 0
for rec in citations:
    title = rec.get('title')
    # citation_count may be string; convert safely
    try:
        count = int(rec.get('citation_count', 0))
    except:
        try:
            count = int(float(rec.get('citation_count', 0)))
        except:
            count = 0
    if title in chi_titles:
        results.append({'title': title, 'citation_count': count})
        total_citations += count

# Sort results by citation_count desc
results = sorted(results, key=lambda x: x['citation_count'], reverse=True)

output = {'papers': results, 'total_citations_2020_for_CHI_papers': total_citations}

print("__RESULT__:")
print(json.dumps(output))"""

env_args = {'var_call_uEXXygsM0MXYDT9Xr0aS4mNG': 'file_storage/call_uEXXygsM0MXYDT9Xr0aS4mNG.json', 'var_call_ZpRLwxr35kslvSSpoVMVs7G0': 'file_storage/call_ZpRLwxr35kslvSSpoVMVs7G0.json'}

exec(code, env_args)
