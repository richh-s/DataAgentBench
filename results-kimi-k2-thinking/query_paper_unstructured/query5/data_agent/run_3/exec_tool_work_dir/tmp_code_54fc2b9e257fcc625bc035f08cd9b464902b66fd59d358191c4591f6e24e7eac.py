code = """import json, re, os
citations_path = locals()['var_functions.query_db:7']
papers_path = locals()['var_functions.query_db:8']

with open(citations_path) as f:
    citations = json.load(f)

with open(papers_path) as f:
    papers = json.load(f)

chi_papers = []
for paper in papers:
    filename = paper.get('filename', '')
    text = paper.get('text', '').lower()
    if 'chi' in filename.lower() or re.search(r'chi\s+\d{2,4}', text):
        title = filename.replace('.txt', '')
        year_match = re.search(r'20\d\d', text)
        year = year_match.group() if year_match else None
        chi_papers.append({'title': title, 'year': year})

citations_2020 = [c for c in citations if c.get('citation_year') == 2020]

matched = []
for citation in citations_2020:
    cite_title = citation.get('title', '').lower()
    for paper in chi_papers:
        paper_title = paper['title'].lower()
        if paper_title == cite_title or paper_title in cite_title or cite_title in paper_title:
            matched.append(int(citation.get('citation_count', 0)))
            break

total = sum(matched)
print('__RESULT__:')
print(json.dumps({'total_citations_2020': total, 'chi_papers_counted': len(matched), 'total_chi_papers': len(chi_papers)}))"""

env_args = {'var_functions.list_db:0': ['paper_docs'], 'var_functions.query_db:2': [{'id': '16', 'title': 'Sundroid: Solar Radiation Awareness with Smartphones', 'citation_count': '65', 'citation_year': '2020'}, {'id': '17', 'title': 'A Quantified-Self Framework for Exploring and Enhancing Personal Productivity', 'citation_count': '4', 'citation_year': '2020'}, {'id': '27', 'title': 'Why We Use and Abandon Smart Devices', 'citation_count': '36', 'citation_year': '2020'}, {'id': '36', 'title': 'One Step Forward, Two Steps Back: The Key to Wearables in the Field is the App', 'citation_count': '98', 'citation_year': '2020'}, {'id': '42', 'title': "I'Ll Be Back: On the Multiple Lives of Users of a Mobile Activity Tracking Application", 'citation_count': '78', 'citation_year': '2020'}], 'var_functions.query_db:3': 'file_storage/functions.query_db:3.json', 'var_functions.query_db:7': 'file_storage/functions.query_db:7.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.execute_python:18': {'total_chi_citations_2020': 0, 'chi_papers_counted': 0}, 'var_functions.execute_python:22': {'citations_type': "<class 'str'>", 'papers_type': "<class 'str'>"}, 'var_functions.execute_python:24': {'total_citations': 0, 'papers_matched': 0}}

exec(code, env_args)
