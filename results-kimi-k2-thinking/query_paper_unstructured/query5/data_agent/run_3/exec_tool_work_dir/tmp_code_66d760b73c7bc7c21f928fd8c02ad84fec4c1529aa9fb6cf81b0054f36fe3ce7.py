code = """import json, re, os

citations_data = locals()['var_functions.query_db:7']
papers_data = locals()['var_functions.query_db:8']

if isinstance(citations_data, str):
    with open(citations_data, 'r') as f:
        citations_data = json.load(f)

if isinstance(papers_data, str):
    with open(papers_data, 'r') as f:
        papers_data = json.load(f)

chi_2020_citations = []
for citation in citations_data:
    if citation.get('citation_year') == 2020:
        citation_title = citation.get('title', '').lower()
        for paper in papers_data:
            paper_filename = paper.get('filename', '')
            if 'chi' in paper_filename.lower():
                paper_title = paper_filename.replace('.txt', '').lower()
                if paper_title == citation_title or citation_title in paper_title or paper_title in citation_title:
                    chi_2020_citations.append(int(citation.get('citation_count', 0)))
                    break

total_citations = sum(chi_2020_citations)

print('__RESULT__:')
print(json.dumps({'total_chi_citations_2020': total_citations, 'chi_papers_counted': len(chi_2020_citations)}))"""

env_args = {'var_functions.list_db:0': ['paper_docs'], 'var_functions.query_db:2': [{'id': '16', 'title': 'Sundroid: Solar Radiation Awareness with Smartphones', 'citation_count': '65', 'citation_year': '2020'}, {'id': '17', 'title': 'A Quantified-Self Framework for Exploring and Enhancing Personal Productivity', 'citation_count': '4', 'citation_year': '2020'}, {'id': '27', 'title': 'Why We Use and Abandon Smart Devices', 'citation_count': '36', 'citation_year': '2020'}, {'id': '36', 'title': 'One Step Forward, Two Steps Back: The Key to Wearables in the Field is the App', 'citation_count': '98', 'citation_year': '2020'}, {'id': '42', 'title': "I'Ll Be Back: On the Multiple Lives of Users of a Mobile Activity Tracking Application", 'citation_count': '78', 'citation_year': '2020'}], 'var_functions.query_db:3': 'file_storage/functions.query_db:3.json', 'var_functions.query_db:7': 'file_storage/functions.query_db:7.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json'}

exec(code, env_args)
