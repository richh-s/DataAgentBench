code = """import json
# Load the query results from storage variables
with open(var_call_sCxzoYCpxRM0ekx0Pzus346O, 'r', encoding='utf-8') as f:
    citations = json.load(f)
with open(var_call_EftYzygcs0x46DV9hSLzlo2W, 'r', encoding='utf-8') as f:
    paper_docs = json.load(f)

# Build set of CHI paper titles from filenames (strip .txt)
chi_titles = set()
for doc in paper_docs:
    fn = doc.get('filename', '')
    if fn.lower().endswith('.txt'):
        title = fn[:-4]
    else:
        title = fn
    chi_titles.add(title.strip())

# Normalize citation titles by stripping surrounding quotes and whitespace
matches = []
total = 0
for rec in citations:
    t = rec.get('title', '')
    # remove surrounding quotes if present
    t_clean = t.strip()
    if (t_clean.startswith('"') and t_clean.endswith('"')) or (t_clean.startswith("'") and t_clean.endswith("'")):
        t_clean = t_clean[1:-1].strip()
    # Match exact
    if t_clean in chi_titles:
        try:
            c = int(rec.get('citation_count', 0))
        except:
            c = 0
        matches.append({'title': t_clean, 'citation_count': c})
        total += c

# Prepare result
result = {'total_citations': total, 'papers': matches}

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_sCxzoYCpxRM0ekx0Pzus346O': 'file_storage/call_sCxzoYCpxRM0ekx0Pzus346O.json', 'var_call_EftYzygcs0x46DV9hSLzlo2W': 'file_storage/call_EftYzygcs0x46DV9hSLzlo2W.json'}

exec(code, env_args)
