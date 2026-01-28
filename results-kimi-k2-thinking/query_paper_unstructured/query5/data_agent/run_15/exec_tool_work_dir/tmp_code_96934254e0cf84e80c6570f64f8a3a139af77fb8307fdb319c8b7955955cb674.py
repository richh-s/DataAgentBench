code = """import json
import re

# Get the file paths
citations_file = var_functions.query_db_4
papers_file = var_functions.query_db_5

# Load all citations from 2020
with open(citations_file, 'r') as f:
    citations_2020 = json.load(f)

# Load all paper documents
with open(papers_file, 'r') as f:
    paper_docs = json.load(f)

# Create a dictionary mapping paper titles to their venues
paper_venues = {}
for doc in paper_docs:
    filename = doc.get('filename', '')
    text = doc.get('text', '')
    
    if not filename:
        continue
    
    title = filename.replace('.txt', '')
    text_upper = text.upper()
    
    # Check if this is a CHI paper
    is_chi = False
    chi_patterns = [
        r'CHI\s*\'?\d{2}',
        r'CHI\s+CONFERENCE',
        r'PROCEEDINGS\s+OF\s+CHI',
        r'CHI\s+\d{4}'
    ]
    
    for pattern in chi_patterns:
        if re.search(pattern, text_upper):
            is_chi = True
            break
    
    paper_venues[title] = is_chi

# Calculate total citations for CHI papers
total_citations = 0
chi_paper_count = 0
matched_count = 0

for citation in citations_2020:
    title = citation.get('title', '')
    citation_count = int(citation.get('citation_count', 0))
    
    if title in paper_venues:
        matched_count += 1
        if paper_venues[title]:
            total_citations += citation_count
            chi_paper_count += 1

result = {
    'total_chi_citations_2020': total_citations,
    'chi_papers_cited': chi_paper_count,
    'total_papers_matched': matched_count
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': [{'id': '16', 'title': 'Sundroid: Solar Radiation Awareness with Smartphones', 'citation_count': '65', 'citation_year': '2020'}, {'id': '17', 'title': 'A Quantified-Self Framework for Exploring and Enhancing Personal Productivity', 'citation_count': '4', 'citation_year': '2020'}, {'id': '27', 'title': 'Why We Use and Abandon Smart Devices', 'citation_count': '36', 'citation_year': '2020'}, {'id': '36', 'title': 'One Step Forward, Two Steps Back: The Key to Wearables in the Field is the App', 'citation_count': '98', 'citation_year': '2020'}, {'id': '42', 'title': "I'Ll Be Back: On the Multiple Lives of Users of a Mobile Activity Tracking Application", 'citation_count': '78', 'citation_year': '2020'}], 'var_functions.query_db:1': 'file_storage/functions.query_db:1.json', 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json'}

exec(code, env_args)
