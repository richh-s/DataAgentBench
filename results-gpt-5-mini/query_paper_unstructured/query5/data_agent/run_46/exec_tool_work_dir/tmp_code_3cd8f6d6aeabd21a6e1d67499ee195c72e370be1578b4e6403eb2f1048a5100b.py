code = """import json, re
with open(var_call_uEXXygsM0MXYDT9Xr0aS4mNG, 'r', encoding='utf-8') as f:
    citations = json.load(f)
with open(var_call_ZpRLwxr35kslvSSpoVMVs7G0, 'r', encoding='utf-8') as f:
    paper_docs = json.load(f)

# Build chi_titles using more specific pattern: look for 'CHI' near dates or apostrophe
chi_titles = set()
chi_docs = []
pattern = re.compile(r"CHI\b|\bCHI\s|'CHI|CHI'|\bACM CHI\b", re.IGNORECASE)
for doc in paper_docs:
    text = doc.get('text','')
    if pattern.search(text):
        filename = doc.get('filename','')
        if filename.lower().endswith('.txt'):
            title = filename[:-4]
        else:
            title = filename
        chi_titles.add(title)
        chi_docs.append(title)

cit_titles = [rec.get('title') for rec in citations]

# Compute intersection
inter = set(cit_titles).intersection(chi_titles)

sample_cit = cit_titles[:50]
sample_chi = list(chi_titles)[:50]

output = {
    'num_citations_records': len(citations),
    'num_paper_docs_returned': len(paper_docs),
    'num_chi_titles_detected': len(chi_titles),
    'citations_sample_first_50': sample_cit,
    'chi_titles_sample_first_50': sample_chi,
    'intersection_count': len(inter),
    'intersection_sample': list(inter)[:50]
}
print("__RESULT__:")
print(json.dumps(output))"""

env_args = {'var_call_uEXXygsM0MXYDT9Xr0aS4mNG': 'file_storage/call_uEXXygsM0MXYDT9Xr0aS4mNG.json', 'var_call_ZpRLwxr35kslvSSpoVMVs7G0': 'file_storage/call_ZpRLwxr35kslvSSpoVMVs7G0.json', 'var_call_YvAtRVaUVMjyGSfoiU8ReFWN': {'papers': [], 'total_citations_2020_for_CHI_papers': 0}}

exec(code, env_args)
