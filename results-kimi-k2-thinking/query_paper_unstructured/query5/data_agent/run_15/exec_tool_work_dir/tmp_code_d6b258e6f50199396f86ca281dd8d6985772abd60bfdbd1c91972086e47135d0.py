code = """import json
import re

# Load 2020 citations (key: var_functions.query_db:4)
citations_key = "var_functions.query_db:4"
citations_data = locals()[citations_key]

# Load paper documents (key: var_functions.query_db:5)
papers_key = "var_functions.query_db:5"
papers_data = locals()[papers_key]

# Handle file paths
if isinstance(citations_data, str) and citations_data.endswith('.json'):
    with open(citations_data, 'r') as f:
        citations_2020 = json.load(f)
else:
    citations_2020 = citations_data

if isinstance(papers_data, str) and papers_data.endswith('.json'):
    with open(papers_data, 'r') as f:
        paper_docs = json.load(f)
else:
    paper_docs = papers_data

# Create mapping: paper title -> is CHI venue
chi_papers = {}
for doc in paper_docs:
    filename = doc.get('filename', '')
    if filename:
        title = filename.replace('.txt', '')
        text = doc.get('text', '')
        # Check for CHI venue in paper text
        is_chi = bool(re.search(r'CHI', text, re.IGNORECASE))
        chi_papers[title] = is_chi

# Calculate total citations for CHI papers in 2020
total_chi_citations = 0
chi_papers_cited = 0

for citation in citations_2020:
    title = citation.get('title', '')
    count = int(citation.get('citation_count', 0))
    
    if chi_papers.get(title, False):
        total_chi_citations += count
        chi_papers_cited += 1

result = str(total_chi_citations)
print('__RESULT__:')
print(result)"""

env_args = {'var_functions.query_db:0': [{'id': '16', 'title': 'Sundroid: Solar Radiation Awareness with Smartphones', 'citation_count': '65', 'citation_year': '2020'}, {'id': '17', 'title': 'A Quantified-Self Framework for Exploring and Enhancing Personal Productivity', 'citation_count': '4', 'citation_year': '2020'}, {'id': '27', 'title': 'Why We Use and Abandon Smart Devices', 'citation_count': '36', 'citation_year': '2020'}, {'id': '36', 'title': 'One Step Forward, Two Steps Back: The Key to Wearables in the Field is the App', 'citation_count': '98', 'citation_year': '2020'}, {'id': '42', 'title': "I'Ll Be Back: On the Multiple Lives of Users of a Mobile Activity Tracking Application", 'citation_count': '78', 'citation_year': '2020'}], 'var_functions.query_db:1': 'file_storage/functions.query_db:1.json', 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.execute_python:20': 243}

exec(code, env_args)
