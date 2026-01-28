code = """import json, re
# Load the large query results from storage variables
path_citations = var_call_gFwFvyf3mPGfKL0vFQmrcJZX
path_papers = var_call_kcMrujPTFLPyK4epIvakeN2T

with open(path_citations, 'r', encoding='utf-8') as f:
    citations = json.load(f)
with open(path_papers, 'r', encoding='utf-8') as f:
    papers = json.load(f)

# Build set of titles for papers whose text indicates venue CHI
chi_titles = set()
for doc in papers:
    filename = doc.get('filename','')
    title = filename[:-4] if filename.lower().endswith('.txt') else filename
    text = doc.get('text','')
    # consider CHI if the token CHI appears in the text (case-insensitive)
    if re.search(r"\bCHI\b", text, flags=re.IGNORECASE):
        chi_titles.add(title)

# Filter citations for citation_year 2020 were already filtered in SQL query; now match titles
results = []
total = 0
for rec in citations:
    t = rec.get('title')
    # citation_count may be string, convert to int safely
    try:
        c = int(rec.get('citation_count', 0))
    except:
        try:
            c = int(float(rec.get('citation_count', 0)))
        except:
            c = 0
    if t in chi_titles:
        results.append({'title': t, 'citation_count': c})
        total += c

# Sort results by citation_count descending
results_sorted = sorted(results, key=lambda x: x['citation_count'], reverse=True)

out = {'papers': results_sorted, 'total_citations': total, 'num_papers': len(results_sorted)}

print("__RESULT__:")
print(json.dumps(out))"""

env_args = {'var_call_gFwFvyf3mPGfKL0vFQmrcJZX': 'file_storage/call_gFwFvyf3mPGfKL0vFQmrcJZX.json', 'var_call_kcMrujPTFLPyK4epIvakeN2T': 'file_storage/call_kcMrujPTFLPyK4epIvakeN2T.json'}

exec(code, env_args)
