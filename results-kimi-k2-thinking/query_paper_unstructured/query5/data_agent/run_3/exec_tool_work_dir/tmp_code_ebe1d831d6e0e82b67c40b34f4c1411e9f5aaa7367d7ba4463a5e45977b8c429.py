code = """import json, re, os
c_path = locals()['var_functions.query_db:7']
p_path = locals()['var_functions.query_db:8']

with open(c_path) as f:
    citations = json.load(f)
with open(p_path) as f:
    papers = json.load(f)

# Find CHI papers and build lookup
chi_titles = set()
for p in papers:
    text = p.get('text','').lower()
    filename = p.get('filename','').lower()
    if 'chi' in filename or re.search(r'chi\s*(20)?\d{2,4}', text):
        title = p.get('filename','').replace('.txt','')
        chi_titles.add(title.lower())

# Find 2020 citations that match CHI papers
total = 0
count = 0
for c in citations:
    if str(c.get('citation_year','')) == '2020':
        cite_title = c.get('title','').lower()
        for chi_title in chi_titles:
            if chi_title == cite_title or chi_title in cite_title or cite_title in chi_title:
                total += int(c.get('citation_count',0))
                count += 1
                break

print('__RESULT__:')
print(json.dumps({'total_chi_citations_2020': total, 'chi_papers_cited': count}))"""

env_args = {'var_functions.list_db:0': ['paper_docs'], 'var_functions.query_db:2': [{'id': '16', 'title': 'Sundroid: Solar Radiation Awareness with Smartphones', 'citation_count': '65', 'citation_year': '2020'}, {'id': '17', 'title': 'A Quantified-Self Framework for Exploring and Enhancing Personal Productivity', 'citation_count': '4', 'citation_year': '2020'}, {'id': '27', 'title': 'Why We Use and Abandon Smart Devices', 'citation_count': '36', 'citation_year': '2020'}, {'id': '36', 'title': 'One Step Forward, Two Steps Back: The Key to Wearables in the Field is the App', 'citation_count': '98', 'citation_year': '2020'}, {'id': '42', 'title': "I'Ll Be Back: On the Multiple Lives of Users of a Mobile Activity Tracking Application", 'citation_count': '78', 'citation_year': '2020'}], 'var_functions.query_db:3': 'file_storage/functions.query_db:3.json', 'var_functions.query_db:7': 'file_storage/functions.query_db:7.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.execute_python:18': {'total_chi_citations_2020': 0, 'chi_papers_counted': 0}, 'var_functions.execute_python:22': {'citations_type': "<class 'str'>", 'papers_type': "<class 'str'>"}, 'var_functions.execute_python:24': {'total_citations': 0, 'papers_matched': 0}, 'var_functions.execute_python:30': {'total_citations_2020': 0, 'chi_papers_counted': 0, 'total_chi_papers': 4}, 'var_functions.execute_python:34': {'total_citations': 0, 'papers_matched': 0, 'chi_papers_found': 0}, 'var_functions.execute_python:36': {'total_citations_2020': 0, 'papers_matched': 0, 'chi_papers_found': 5, 'sample_matches': []}, 'var_functions.execute_python:40': {'total': 0, 'papers': 0, 'chi_total': 5, 'c2020_total': 0}}

exec(code, env_args)
