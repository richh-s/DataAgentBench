code = """import json, re
with open(var_call_tuqqN3NpZI1xl0x9HxF4hR5u, 'r', encoding='utf-8') as f:
    paper_docs = json.load(f)

venues = ["CHI","UBICOMP","CSCW","DIS","PervasiveHealth","WWW","IUI","OzCHI","TEI","AH"]
counts = {v:0 for v in venues}
matches = {v:[] for v in venues}
for doc in paper_docs:
    filename = doc.get('filename','')
    title = filename[:-4] if filename.lower().endswith('.txt') else filename
    text = doc.get('text','')
    ut = text.upper()
    for v in venues:
        if v.upper() in ut:
            counts[v] += 1
            matches[v].append(title)

# Also check for 'PROCEEDINGS OF THE SIGCHI' exact phrase
sigchi_titles = []
for doc in paper_docs:
    filename = doc.get('filename','')
    title = filename[:-4] if filename.lower().endswith('.txt') else filename
    text = doc.get('text','')
    if 'PROCEEDINGS OF THE SIGCHI' in text.upper() or 'SIGCHI' in text.upper():
        sigchi_titles.append(title)

result = {'venue_counts': counts, 'sample_CHI_titles': matches['CHI'][:50], 'sigchi_matches': sigchi_titles[:50]}
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_ULoT7Yja3x7BR5LtpdHMT3FN': 'file_storage/call_ULoT7Yja3x7BR5LtpdHMT3FN.json', 'var_call_S1gKjKKYJATqzsNixyTxNMeF': 'file_storage/call_S1gKjKKYJATqzsNixyTxNMeF.json', 'var_call_JHht0QJIKkseVC2KHr0Pw9dz': ['paper_docs'], 'var_call_tuqqN3NpZI1xl0x9HxF4hR5u': 'file_storage/call_tuqqN3NpZI1xl0x9HxF4hR5u.json', 'var_call_IMGIEf2TQ8By8Hm7XZfF9wir': {'total_citations_2020_for_CHI_papers': 0, 'num_chi_papers_cited_in_2020': 0, 'papers': []}, 'var_call_dmAugWSZzgEn6uu9F2U93qiR': {'num_chi_docs': 0, 'sample_chi_titles': []}}

exec(code, env_args)
