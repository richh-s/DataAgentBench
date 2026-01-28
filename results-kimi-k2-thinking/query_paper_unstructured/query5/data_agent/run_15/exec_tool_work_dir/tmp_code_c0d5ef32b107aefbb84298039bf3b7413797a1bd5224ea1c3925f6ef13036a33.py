code = """import json
import re

# Load citations data
cit_file = var_functions.query_db_4
with open(cit_file, 'r') as f:
    citations = json.load(f)

# Load paper documents data
papers_file = var_functions.query_db_5
with open(papers_file, 'r') as f:
    papers = json.load(f)

# Build dictionary of paper titles to venue info
paper_info = {}
for paper in papers:
    filename = paper.get('filename', '')
    text = paper.get('text', '')
    if filename:
        title = filename.replace('.txt', '')
        text_upper = text.upper()
        
        # Check for CHI venue
        is_chi = bool(re.search(r'CHI', text_upper))
        paper_info[title] = is_chi

# Sum citations for CHI papers
total_chi_citations = 0
chi_count = 0
matched = 0

for citation in citations:
    ctitle = citation.get('title', '')
    ccount = int(citation.get('citation_count', 0))
    
    if ctitle in paper_info and paper_info[ctitle]:
        total_chi_citations += ccount
        chi_count += 1
    if ctitle in paper_info:
        matched += 1

result = {'total_chi_citations_2020': total_chi_citations}
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': [{'id': '16', 'title': 'Sundroid: Solar Radiation Awareness with Smartphones', 'citation_count': '65', 'citation_year': '2020'}, {'id': '17', 'title': 'A Quantified-Self Framework for Exploring and Enhancing Personal Productivity', 'citation_count': '4', 'citation_year': '2020'}, {'id': '27', 'title': 'Why We Use and Abandon Smart Devices', 'citation_count': '36', 'citation_year': '2020'}, {'id': '36', 'title': 'One Step Forward, Two Steps Back: The Key to Wearables in the Field is the App', 'citation_count': '98', 'citation_year': '2020'}, {'id': '42', 'title': "I'Ll Be Back: On the Multiple Lives of Users of a Mobile Activity Tracking Application", 'citation_count': '78', 'citation_year': '2020'}], 'var_functions.query_db:1': 'file_storage/functions.query_db:1.json', 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json'}

exec(code, env_args)
