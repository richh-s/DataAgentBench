code = """import json
import re

# Load the citations data
citations_file = var_functions.query_db:5
with open(citations_file, 'r') as f:
    citations_data = json.load(f)

# Load the paper documents data
papers_file = var_functions.query_db:8
with open(papers_file, 'r') as f:
    papers_data = json.load(f)

print('Total citations in 2020: %d' % len(citations_data))
print('Total papers: %d' % len(papers_data))

# Create a dictionary to map paper titles to venues
paper_venues = {}
venues = ['CHI', 'Ubicomp', 'CSCW', 'DIS', 'PervasiveHealth', 'WWW', 'IUI', 'OzCHI', 'TEI', 'AH']

# Build the mapping
for paper in papers_data:
    filename = paper['filename']
    title = filename.replace('.txt', '')
    text = paper['text']
    
    venue_found = None
    for venue in venues:
        if venue.lower() in text.lower():
            venue_found = venue
            break
    
    paper_venues[title] = venue_found

# Find CHI papers with citations in 2020
total_citations = 0
matched_papers = 0

for citation in citations_data:
    citation_title = citation['title']
    citation_count = int(citation['citation_count'])
    
    if citation_title in paper_venues and paper_venues[citation_title] == 'CHI':
        total_citations += citation_count
        matched_papers += 1

result = {
    'total_citations_2020': total_citations,
    'num_chi_papers': matched_papers
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['paper_docs'], 'var_functions.query_db:2': [{'id': '16', 'title': 'Sundroid: Solar Radiation Awareness with Smartphones', 'citation_count': '65', 'citation_year': '2020'}, {'id': '17', 'title': 'A Quantified-Self Framework for Exploring and Enhancing Personal Productivity', 'citation_count': '4', 'citation_year': '2020'}, {'id': '27', 'title': 'Why We Use and Abandon Smart Devices', 'citation_count': '36', 'citation_year': '2020'}, {'id': '36', 'title': 'One Step Forward, Two Steps Back: The Key to Wearables in the Field is the App', 'citation_count': '98', 'citation_year': '2020'}, {'id': '42', 'title': "I'Ll Be Back: On the Multiple Lives of Users of a Mobile Activity Tracking Application", 'citation_count': '78', 'citation_year': '2020'}], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json'}

exec(code, env_args)
