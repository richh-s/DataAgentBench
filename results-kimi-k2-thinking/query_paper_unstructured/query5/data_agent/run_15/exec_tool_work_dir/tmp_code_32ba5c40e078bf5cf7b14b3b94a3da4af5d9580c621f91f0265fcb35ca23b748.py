code = """import json
import re
from collections import defaultdict

# Load all citations from 2020
citations_2020 = locals()['var_functions.query_db:4']
if isinstance(citations_2020, str) and citations_2020.endswith('.json'):
    with open(citations_2020, 'r') as f:
        citations_2020 = json.load(f)

print(f"Total citations in 2020: {len(citations_2020)}")

# Load paper documents
paper_docs_path = locals()['var_functions.query_db:5']
if isinstance(paper_docs_path, str) and paper_docs_path.endswith('.json'):
    with open(paper_docs_path, 'r') as f:
        paper_docs = json.load(f)

print(f"Total paper documents: {len(paper_docs)}")

# Create a mapping from title (matching filename without .txt) to paper info
paper_info_map = {}
for doc in paper_docs:
    filename = doc.get('filename', '')
    text = doc.get('text', '')
    
    # Extract title from filename (remove .txt)
    title = filename.replace('.txt', '') if filename else ''
    
    # Initialize extracted info
    venue = ''
    year = ''
    
    # Look for CHI venue markers in text (common patterns)
    # Many papers have venue info at the beginning or headers
    text_upper = text.upper()
    
    # Common CHI patterns
    chi_patterns = [
        r'CHI\s*\'?\d{2}',  # CHI '20, CHI20, etc.
        r'CHI\s+CONFERENCE',
        r'PROCEEDINGS\s+OF\s+CHI',
        r'CHI\s+\d{4}'  # CHI 2020, CHI 2019, etc.
    ]
    
    is_chi = False
    for pattern in chi_patterns:
        if re.search(pattern, text_upper):
            is_chi = True
            venue = 'CHI'
            break
    
    # Also try to extract year from common patterns
    year_match = re.search(r'CHI\s*\'?(\d{2})', text)
    if year_match:
        year = '20' + year_match.group(1)
    else:
        year_match = re.search(r'CHI\s+(\d{4})', text)
        if year_match:
            year = year_match.group(1)
    
    # If not CHI, try to extract other venue info
    if not is_chi:
        # Look for other common venue patterns
        venue_patterns = [
            (r'UBICOMP', 'Ubicomp'),
            (r'CSCW', 'CSCW'),
            (r'DIS', 'DIS'),
            (r'PERVASIVEHEALTH', 'PervasiveHealth'),
            (r'WWW', 'WWW'),
            (r'IUI', 'IUI'),
            (r'OZCHI', 'OzCHI'),
            (r'TEI', 'TEI'),
            (r'AH', 'AH')
        ]
        
        for pattern, venue_name in venue_patterns:
            if re.search(pattern, text_upper):
                venue = venue_name
                break
    
    paper_info_map[title] = {'venue': venue, 'year': year, 'filename': filename}

# Count papers by venue for debugging
venue_counts = defaultdict(int)
for title, info in paper_info_map.items():
    if info['venue']:
        venue_counts[info['venue']] += 1

print(f"Papers found by venue: {dict(venue_counts)}")

# Now match with citations and sum citation counts for CHI papers
total_chi_citations = 0
chi_papers_count = 0
matched_citations = 0

for citation in citations_2020:
    cite_title = citation.get('title', '')
    citation_count = int(citation.get('citation_count', 0))
    
    # Find matching paper
    if cite_title in paper_info_map:
        matched_citations += 1
        paper_info = paper_info_map[cite_title]
        if paper_info['venue'] == 'CHI':
            total_chi_citations += citation_count
            chi_papers_count += 1
            # print(f"CHI paper: {cite_title}, citations: {citation_count}")

print(f"Total citations matched to papers: {matched_citations}")
print(f"CHI papers cited in 2020: {chi_papers_count}")
print(f"Total citation counts for CHI papers in 2020: {total_chi_citations}")

result = {
    'total_chi_citations_2020': total_chi_citations,
    'chi_papers_count': chi_papers_count,
    'total_matched_citations': matched_citations
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': [{'id': '16', 'title': 'Sundroid: Solar Radiation Awareness with Smartphones', 'citation_count': '65', 'citation_year': '2020'}, {'id': '17', 'title': 'A Quantified-Self Framework for Exploring and Enhancing Personal Productivity', 'citation_count': '4', 'citation_year': '2020'}, {'id': '27', 'title': 'Why We Use and Abandon Smart Devices', 'citation_count': '36', 'citation_year': '2020'}, {'id': '36', 'title': 'One Step Forward, Two Steps Back: The Key to Wearables in the Field is the App', 'citation_count': '98', 'citation_year': '2020'}, {'id': '42', 'title': "I'Ll Be Back: On the Multiple Lives of Users of a Mobile Activity Tracking Application", 'citation_count': '78', 'citation_year': '2020'}], 'var_functions.query_db:1': 'file_storage/functions.query_db:1.json', 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json'}

exec(code, env_args)
