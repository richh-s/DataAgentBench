code = """import json, re
with open(var_call_chz6IYwvo5dsQr5G93GseU5t, 'r') as f:
    citations = json.load(f)
with open(var_call_v97IdNNmwUCcjthQMwcT7PEo, 'r') as f:
    docs = json.load(f)

def norm(s):
    if s is None: return ''
    s = s.strip().lower()
    # remove surrounding quotes
    if (s.startswith('"') and s.endswith('"')) or (s.startswith("'") and s.endswith("'")):
        s = s[1:-1].strip()
    # remove non-alphanumeric
    s = re.sub(r'[^a-z0-9]+', ' ', s)
    s = re.sub(r'\s+', ' ', s).strip()
    return s

cit_titles = [norm(rec.get('title')) for rec in citations]
doc_titles = {}
for doc in docs:
    fn = doc.get('filename','')
    if fn.lower().endswith('.txt'):
        title = fn[:-4]
    else:
        title = fn
    doc_titles[norm(title)] = title

# find exact normalized matches
matches = []
for rec in citations:
    n = norm(rec.get('title'))
    if n in doc_titles:
        matches.append({'cit_title': rec.get('title'), 'doc_filename': doc_titles[n], 'total_citations': rec.get('total_citations')})

# search for CHI in full text for doc titles
chi_norms = set()
for doc in docs:
    fn = doc.get('filename','')
    title = fn[:-4] if fn.lower().endswith('.txt') else fn
    text = doc.get('text','')
    if re.search(r"\bCHI\b", text, re.IGNORECASE):
        chi_norms.add(norm(title))

# find which matches are CHI
chi_matches = [m for m in matches if norm(m['doc_filename']) in chi_norms]

out = {'total_citation_records': len(citations), 'total_docs': len(docs), 'exact_normalized_matches': len(matches), 'chi_docs_count': len(chi_norms), 'chi_exact_matches': chi_matches[:50]}
print("__RESULT__:")
print(json.dumps(out))"""

env_args = {'var_call_chz6IYwvo5dsQr5G93GseU5t': 'file_storage/call_chz6IYwvo5dsQr5G93GseU5t.json', 'var_call_v97IdNNmwUCcjthQMwcT7PEo': 'file_storage/call_v97IdNNmwUCcjthQMwcT7PEo.json', 'var_call_wy2o3v2azT6V0L4RrbCoo8Rg': []}

exec(code, env_args)
