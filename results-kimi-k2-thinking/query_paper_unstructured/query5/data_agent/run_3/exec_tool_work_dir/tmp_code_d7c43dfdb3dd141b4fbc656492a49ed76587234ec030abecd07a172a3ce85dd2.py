code = """import json, re, os
c_path = locals()['var_functions.query_db:7']
p_path = locals()['var_functions.query_db:8']

with open(c_path) as f:
    citations = json.load(f)
with open(p_path) as f:
    papers = json.load(f)

c2020 = [c for c in citations if c.get('citation_year') == 2020]
chi = []
for p in papers:
    t = p.get('text','').lower()
    if re.search(r'chi\s+\d{2,4}', t) or 'conference on human factors' in t:
        chi.append(p.get('filename','').replace('.txt',''))

c2020_titles = [c.get('title','').lower() for c in c2020]
chi_titles = [c.lower() for c in chi]

matches = []
for i,ct in enumerate(c2020_titles):
    for pt in chi_titles:
        if ct==pt or ct in pt or pt in ct:
            matches.append(int(c2020[i].get('citation_count',0)))
            break

total = sum(matches)
result = {'total': total, 'papers': len(matches), 'chi_total': len(chi), 'c2020_total': len(c2020)}
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['paper_docs'], 'var_functions.query_db:2': [{'id': '16', 'title': 'Sundroid: Solar Radiation Awareness with Smartphones', 'citation_count': '65', 'citation_year': '2020'}, {'id': '17', 'title': 'A Quantified-Self Framework for Exploring and Enhancing Personal Productivity', 'citation_count': '4', 'citation_year': '2020'}, {'id': '27', 'title': 'Why We Use and Abandon Smart Devices', 'citation_count': '36', 'citation_year': '2020'}, {'id': '36', 'title': 'One Step Forward, Two Steps Back: The Key to Wearables in the Field is the App', 'citation_count': '98', 'citation_year': '2020'}, {'id': '42', 'title': "I'Ll Be Back: On the Multiple Lives of Users of a Mobile Activity Tracking Application", 'citation_count': '78', 'citation_year': '2020'}], 'var_functions.query_db:3': 'file_storage/functions.query_db:3.json', 'var_functions.query_db:7': 'file_storage/functions.query_db:7.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.execute_python:18': {'total_chi_citations_2020': 0, 'chi_papers_counted': 0}, 'var_functions.execute_python:22': {'citations_type': "<class 'str'>", 'papers_type': "<class 'str'>"}, 'var_functions.execute_python:24': {'total_citations': 0, 'papers_matched': 0}, 'var_functions.execute_python:30': {'total_citations_2020': 0, 'chi_papers_counted': 0, 'total_chi_papers': 4}, 'var_functions.execute_python:34': {'total_citations': 0, 'papers_matched': 0, 'chi_papers_found': 0}, 'var_functions.execute_python:36': {'total_citations_2020': 0, 'papers_matched': 0, 'chi_papers_found': 5, 'sample_matches': []}}

exec(code, env_args)
