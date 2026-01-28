code = """import json
import re

# Load 2020 citations from storage (var_functions.query_db:4)
citations_key = 'var_functions.query_db:4'
if citations_key in locals():
    citations_file = locals()[citations_key]
    with open(citations_file, 'r') as f:
        citations_2020 = json.load(f)
else:
    # Try direct access
    citations_2020 = locals().get(citations_key, [])

# Load paper documents from storage (var_functions.query_db:5)
papers_key = 'var_functions.query_db:5'
if papers_key in locals():
    papers_file = locals()[papers_key]
    with open(papers_file, 'r') as f:
        paper_docs = json.load(f)
else:
    paper_docs = locals().get(papers_key, [])

# Build mapping of paper titles to venue
paper_venues = {}
for doc in paper_docs:
    filename = doc.get('filename', '')
    if filename:
        title = filename.replace('.txt', '')
        text_upper = doc.get('text', '').upper()
        
        # Check if CHI paper
        is_chi = 'CHI' in text_upper
        paper_venues[title] = is_chi

# Calculate total citations for CHI papers
total_citations = 0
for citation in citations_2020:
    title = citation.get('title', '')
    count = int(citation.get('citation_count', 0))
    
    if paper_venues.get(title, False):
        total_citations += count

result = str(total_citations)
print('__RESULT__:')
print(result)"""

env_args = {'var_functions.query_db:0': [{'id': '16', 'title': 'Sundroid: Solar Radiation Awareness with Smartphones', 'citation_count': '65', 'citation_year': '2020'}, {'id': '17', 'title': 'A Quantified-Self Framework for Exploring and Enhancing Personal Productivity', 'citation_count': '4', 'citation_year': '2020'}, {'id': '27', 'title': 'Why We Use and Abandon Smart Devices', 'citation_count': '36', 'citation_year': '2020'}, {'id': '36', 'title': 'One Step Forward, Two Steps Back: The Key to Wearables in the Field is the App', 'citation_count': '98', 'citation_year': '2020'}, {'id': '42', 'title': "I'Ll Be Back: On the Multiple Lives of Users of a Mobile Activity Tracking Application", 'citation_count': '78', 'citation_year': '2020'}], 'var_functions.query_db:1': 'file_storage/functions.query_db:1.json', 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json'}

exec(code, env_args)
