code = """import json
import re

# Load 2020 citations
citations_file = var_functions.query_db_4
with open(citations_file, 'r') as f:
    citations_2020 = json.load(f)

# Load paper documents
papers_file = var_functions.query_db_5
with open(papers_file, 'r') as f:
    paper_docs = json.load(f)

# Create mapping: paper title -> is CHI paper
chi_papers = {}
for doc in paper_docs:
    filename = doc.get('filename', '')
    if not filename:
        continue
    
    title = filename.replace('.txt', '')
    text = doc.get('text', '')
    
    # Check if it's a CHI paper by looking for CHI in the text
    is_chi = bool(re.search(r'CHI', text, re.IGNORECASE))
    chi_papers[title] = is_chi

# Count total citations for CHI papers in 2020
total_citations = 0
chi_paper_count = 0

for citation in citations_2020:
    paper_title = citation.get('title', '')
    citation_count = int(citation.get('citation_count', 0))
    
    if chi_papers.get(paper_title, False):
        total_citations += citation_count
        chi_paper_count += 1

result = {
    'total_citations': total_citations,
    'chi_papers_count': chi_paper_count
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': [{'id': '16', 'title': 'Sundroid: Solar Radiation Awareness with Smartphones', 'citation_count': '65', 'citation_year': '2020'}, {'id': '17', 'title': 'A Quantified-Self Framework for Exploring and Enhancing Personal Productivity', 'citation_count': '4', 'citation_year': '2020'}, {'id': '27', 'title': 'Why We Use and Abandon Smart Devices', 'citation_count': '36', 'citation_year': '2020'}, {'id': '36', 'title': 'One Step Forward, Two Steps Back: The Key to Wearables in the Field is the App', 'citation_count': '98', 'citation_year': '2020'}, {'id': '42', 'title': "I'Ll Be Back: On the Multiple Lives of Users of a Mobile Activity Tracking Application", 'citation_count': '78', 'citation_year': '2020'}], 'var_functions.query_db:1': 'file_storage/functions.query_db:1.json', 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.execute_python:20': 243}

exec(code, env_args)
