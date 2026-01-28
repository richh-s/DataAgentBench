code = """import json
import re

# Read paper documents
paper_docs_file = var_functions.query_db:6
with open(paper_docs_file, 'r') as f:
    paper_docs = json.load(f)

# Read 2020 citations
citations_file = var_functions.query_db:4
with open(citations_file, 'r') as f:
    citations_2020 = json.load(f)

# Extract metadata from paper documents
paper_metadata = []
for doc in paper_docs:
    text = doc.get('text', '')
    filename = doc.get('filename', '')
    
    # Extract title from filename (without .txt)
    title_from_filename = filename.replace('.txt', '') if filename else ''
    
    # Look for CHI venue in the text
    venue = None
    year = None
    
    # Check first 10 lines for CHI conference information
    lines = text.split('\n')[:10]
    header_text = ' '.join(lines)
    
    # Patterns to identify CHI papers
    chi_patterns = [
        r'CHI\s*\'?\d{2}\b',  # CHI '15, CHI 15
        r'CHI\s*20\d{2}\b',  # CHI 2015
        r'Proceedings of the .*?CHI',  # Proceedings of CHI
        r'ACM .*?CHI',  # ACM CHI
    ]
    
    is_chi = False
    for pattern in chi_patterns:
        if re.search(pattern, header_text, re.IGNORECASE):
            is_chi = True
            break
    
    # Extract year if CHI paper found
    if is_chi:
        # Try to find 4-digit year first
        year_match = re.search(r'\b(20\d{2})\b', header_text)
        if year_match:
            year = int(year_match.group(1))
        else:
            # Try CHI 'XX format
            chi_year_match = re.search(r"CHI\s*\'?(\d{2})\b", header_text, re.IGNORECASE)
            if chi_year_match:
                year_str = chi_year_match.group(1)
                if year_str.startswith('9'):
                    year = int('19' + year_str)
                else:
                    year = int('20' + year_str)
    
    if is_chi:
        paper_metadata.append({
            'title': title_from_filename,
            'venue': 'CHI',
            'year': year,
            'filename': filename
        })

# Create a mapping of titles to citation counts for 2020
citation_map = {item['title']: int(item['citation_count']) for item in citations_2020}

# Find CHI papers with 2020 citations
total_citations = 0
matched_papers = []

for paper in paper_metadata:
    paper_title = paper['title']
    if paper_title in citation_map:
        citation_count = citation_map[paper_title]
        total_citations += citation_count
        matched_papers.append({
            'title': paper_title,
            'year': paper['year'],
            'citations_2020': citation_count
        })

print('__RESULT__:')
print(json.dumps({
    'total_chi_papers_found': len(paper_metadata),
    'chi_papers_with_2020_citations': len(matched_papers),
    'total_citation_count_2020': total_citations,
    'sample_matched_papers': matched_papers[:5]
}))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:1': [{'id': '16', 'title': 'Sundroid: Solar Radiation Awareness with Smartphones', 'citation_count': '65', 'citation_year': '2020'}, {'id': '17', 'title': 'A Quantified-Self Framework for Exploring and Enhancing Personal Productivity', 'citation_count': '4', 'citation_year': '2020'}, {'id': '27', 'title': 'Why We Use and Abandon Smart Devices', 'citation_count': '36', 'citation_year': '2020'}, {'id': '36', 'title': 'One Step Forward, Two Steps Back: The Key to Wearables in the Field is the App', 'citation_count': '98', 'citation_year': '2020'}, {'id': '42', 'title': "I'Ll Be Back: On the Multiple Lives of Users of a Mobile Activity Tracking Application", 'citation_count': '78', 'citation_year': '2020'}, {'id': '47', 'title': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App', 'citation_count': '16', 'citation_year': '2020'}, {'id': '56', 'title': "Closing the Gap: Supporting Patients' Transition to Self-Management After Hospitalization", 'citation_count': '91', 'citation_year': '2020'}, {'id': '67', 'title': "Beyond Behavior: The Coach's Perspective on Technology in Health Coaching", 'citation_count': '82', 'citation_year': '2020'}, {'id': '76', 'title': 'Exploring the Design Space of Glanceable Feedback for Physical Activity Trackers', 'citation_count': '10', 'citation_year': '2020'}, {'id': '88', 'title': 'Reflective Informatics: Conceptual Dimensions for Designing Technologies of Reflection', 'citation_count': '100', 'citation_year': '2020'}], 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json'}

exec(code, env_args)
