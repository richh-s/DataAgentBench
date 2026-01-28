code = """import json, re
with open(var_call_tuqqN3NpZI1xl0x9HxF4hR5u, 'r', encoding='utf-8') as f:
    paper_docs = json.load(f)
chi_docs = []
for doc in paper_docs:
    filename = doc.get('filename','')
    title = filename[:-4] if filename.lower().endswith('.txt') else filename
    text = doc.get('text','')
    if re.search(r'\bCHI\b', text):
        chi_docs.append(title)

# limit output
sample = chi_docs[:50]
res = {'num_chi_docs': len(chi_docs), 'sample_chi_titles': sample}
print('__RESULT__:')
print(json.dumps(res))"""

env_args = {'var_call_ULoT7Yja3x7BR5LtpdHMT3FN': 'file_storage/call_ULoT7Yja3x7BR5LtpdHMT3FN.json', 'var_call_S1gKjKKYJATqzsNixyTxNMeF': 'file_storage/call_S1gKjKKYJATqzsNixyTxNMeF.json', 'var_call_JHht0QJIKkseVC2KHr0Pw9dz': ['paper_docs'], 'var_call_tuqqN3NpZI1xl0x9HxF4hR5u': 'file_storage/call_tuqqN3NpZI1xl0x9HxF4hR5u.json', 'var_call_IMGIEf2TQ8By8Hm7XZfF9wir': {'total_citations_2020_for_CHI_papers': 0, 'num_chi_papers_cited_in_2020': 0, 'papers': []}}

exec(code, env_args)
