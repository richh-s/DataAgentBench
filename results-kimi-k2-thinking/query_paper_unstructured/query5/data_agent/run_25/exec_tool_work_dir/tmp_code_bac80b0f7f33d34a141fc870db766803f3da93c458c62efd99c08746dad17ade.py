code = """import json
import re

# Load the citations for 2020
citations_2020_file = locals()['var_functions.query_db:10']
with open(citations_2020_file, 'r') as f:
    citations_2020 = json.load(f)

# Load the paper docs
paper_docs_file = locals()['var_functions.query_db:5']
with open(paper_docs_file, 'r') as f:
    paper_docs = json.load(f)

# Process papers
papers = []
for doc in paper_docs:
    filename = doc.get('filename', '')
    text = doc.get('text', '')
    
    # Extract title
    title = filename.replace('.txt', '') if filename else ''
    
    # Extract venue
    venue = None
    # Check for CHI
    if re.search(r'CHI', text):
        venue = 'CHI'
    elif re.search(r'UbiComp|Ubicomp|Pervasive', text):
        venue = 'UbiComp'
    elif re.search(r'CSCW', text):
        venue = 'CSCW'
    elif re.search(r'DIS', text):
        venue = 'DIS'
    elif re.search(r'PervasiveHealth', text):
        venue = 'PervasiveHealth'
    elif re.search(r'WWW', text):
        venue = 'WWW'
    elif re.search(r'IUI', text):
        venue = 'IUI'
    elif re.search(r'OzCHI', text):
        venue = 'OzCHI'
    elif re.search(r'TEI', text):
        venue = 'TEI'
    elif re.search(r'AH', text):
        venue = 'AH'
    
    # Extract year
    year_match = re.search(r'((?:19|20)\d{2})', text)
    year = int(year_match.group(1)) if year_match else None
    
    papers.append({'title': title, 'venue': venue, 'year': year})

# Filter CHI papers
chi_papers = [p for p in papers if p['venue'] == 'CHI']

# Map titles to citation counts
citation_map = {}
for c in citations_2020:
    citation_map[c['title']] = int(c['citation_count'])

# Match and sum citations
total_citations = 0
matched_count = 0

for paper in chi_papers:
    title = paper['title']
    if title in citation_map:
        total_citations += citation_map[title]
        matched_count += 1

# Prepare result
result = {
    'total_chi_papers': len(chi_papers),
    'matched_papers': matched_count,
    'total_citation_count': total_citations
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['paper_docs'], 'var_functions.query_db:2': [{'id': '16', 'title': 'Sundroid: Solar Radiation Awareness with Smartphones', 'citation_count': '65', 'citation_year': '2020'}, {'id': '17', 'title': 'A Quantified-Self Framework for Exploring and Enhancing Personal Productivity', 'citation_count': '4', 'citation_year': '2020'}, {'id': '27', 'title': 'Why We Use and Abandon Smart Devices', 'citation_count': '36', 'citation_year': '2020'}, {'id': '36', 'title': 'One Step Forward, Two Steps Back: The Key to Wearables in the Field is the App', 'citation_count': '98', 'citation_year': '2020'}, {'id': '42', 'title': "I'Ll Be Back: On the Multiple Lives of Users of a Mobile Activity Tracking Application", 'citation_count': '78', 'citation_year': '2020'}], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json'}

exec(code, env_args)
