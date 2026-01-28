code = """import json
import re

# Load citations data
citations_path = var_functions.query_db:5
with open(citations_path, 'r') as f:
    citations = json.load(f)

# Load papers data
papers_path = var_functions.query_db:8
with open(papers_path, 'r') as f:
    papers = json.load(f)

print('Loaded %d citations for 2020' % len(citations))
print('Loaded %d papers' % len(papers))

# Build venue mapping for papers
paper_venues = {}
venues = ['CHI', 'Ubicomp', 'CSCW', 'DIS', 'PervasiveHealth', 'WWW', 'IUI', 'OzCHI', 'TEI', 'AH']

for paper in papers:
    title = paper['filename'].replace('.txt', '')
    text = paper['text']
    venue = None
    for v in venues:
        if v in text:
            venue = v
            break
    paper_venues[title] = venue

# Calculate total citations for CHI papers in 2020
total_citations = 0
chi_papers_count = 0

for citation in citations:
    title = citation['title']
    if title in paper_venues and paper_venues[title] == 'CHI':
        total_citations += int(citation['citation_count'])
        chi_papers_count += 1

result = {'total_citations_2020': total_citations, 'num_chi_papers': chi_papers_count}
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['paper_docs'], 'var_functions.query_db:2': [{'id': '16', 'title': 'Sundroid: Solar Radiation Awareness with Smartphones', 'citation_count': '65', 'citation_year': '2020'}, {'id': '17', 'title': 'A Quantified-Self Framework for Exploring and Enhancing Personal Productivity', 'citation_count': '4', 'citation_year': '2020'}, {'id': '27', 'title': 'Why We Use and Abandon Smart Devices', 'citation_count': '36', 'citation_year': '2020'}, {'id': '36', 'title': 'One Step Forward, Two Steps Back: The Key to Wearables in the Field is the App', 'citation_count': '98', 'citation_year': '2020'}, {'id': '42', 'title': "I'Ll Be Back: On the Multiple Lives of Users of a Mobile Activity Tracking Application", 'citation_count': '78', 'citation_year': '2020'}], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json'}

exec(code, env_args)
