code = """import json, re, os

# Load the citations for 2020
citations_2020_file = locals().get('var_functions.query_db:10')
with open(citations_2020_file, 'r') as f:
    citations_2020 = json.load(f)

# Load the paper docs
paper_docs_file = locals().get('var_functions.query_db:5')
with open(paper_docs_file, 'r') as f:
    paper_docs = json.load(f)

# Extract paper information
papers = []
for doc in paper_docs:
    filename = doc.get('filename', '')
    text = doc.get('text', '')
    
    # Extract title from filename (remove .txt)
    title = filename.replace('.txt', '') if filename else ''
    
    # Extract venue - look for CHI, UbiComp, CSCW, etc. in the text
    venue = None
    # Common venue patterns
    venue_patterns = [
        (r'CHI\s*\'?\d{2}|CHI\s*\d{4}|CHI\s*Conference|Proceedings of the CHI', 'CHI'),
        (r'UbiComp|Ubicomp|Pervasive|Proceedings of the ACM International Joint Conference on Pervasive and Ubiquitous Computing', 'UbiComp'),
        (r'CSCW|Proceedings of the ACM Conference on Computer Supported Cooperative Work', 'CSCW'),
        (r'DIS|Designing Interactive Systems', 'DIS'),
        (r'PervasiveHealth|Proceedings of the International Conference on Pervasive Computing Technologies for Healthcare', 'PervasiveHealth'),
        (r'WWW|Proceedings of the International World Wide Web Conference', 'WWW'),
        (r'IUI|Proceedings of the ACM Conference on Intelligent User Interfaces', 'IUI'),
        (r'OzCHI', 'OzCHI'),
        (r'TEI|Proceedings of the International Conference on Tangible, Embedded, and Embodied Interaction', 'TEI'),
        (r'AH|Augmented Human', 'AH')
    ]
    
    for pattern, venue_name in venue_patterns:
        if re.search(pattern, text, re.IGNORECASE):
            venue = venue_name
            break
    
    # Extract year - look for 4-digit years around 2000-2025
    year_match = re.search(r'((?:19|20)\d{2})', text)
    year = int(year_match.group(1)) if year_match else None
    
    papers.append({
        'title': title,
        'venue': venue,
        'year': year,
        'filename': filename
    })

# Filter CHI papers
chi_papers = [p for p in papers if p['venue'] == 'CHI']
print(f'Total papers: {len(papers)}')
print(f'CHI papers: {len(chi_papers)}')

# Create a mapping of title to citation count for 2020
citation_map = {c['title']: int(c['citation_count']) for c in citations_2020}

# Match CHI papers with their 2020 citations
total_citations = 0
matched_papers = []

for paper in chi_papers:
    title = paper['title']
    # Try exact match first
    if title in citation_map:
        count = citation_map[title]
        total_citations += count
        matched_papers.append((title, count))
    else:
        # Try fuzzy matching - look for similar titles
        for cite_title, count in citation_map.items():
            if title.lower() in cite_title.lower() or cite_title.lower() in title.lower():
                total_citations += count
                matched_papers.append((title, count, cite_title))
                break

print(f'Matched papers: {len(matched_papers)}')
print(f'Total citation count for CHI papers in 2020: {total_citations}')

# Show some examples
print('\nSample matched papers:')
for i, item in enumerate(matched_papers[:10]):
    print(f"{i+1}. {item[0]} - {item[1]} citations")

result = {
    'total_chi_papers': len(chi_papers),
    'matched_papers': len(matched_papers),
    'total_citation_count': total_citations
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['paper_docs'], 'var_functions.query_db:2': [{'id': '16', 'title': 'Sundroid: Solar Radiation Awareness with Smartphones', 'citation_count': '65', 'citation_year': '2020'}, {'id': '17', 'title': 'A Quantified-Self Framework for Exploring and Enhancing Personal Productivity', 'citation_count': '4', 'citation_year': '2020'}, {'id': '27', 'title': 'Why We Use and Abandon Smart Devices', 'citation_count': '36', 'citation_year': '2020'}, {'id': '36', 'title': 'One Step Forward, Two Steps Back: The Key to Wearables in the Field is the App', 'citation_count': '98', 'citation_year': '2020'}, {'id': '42', 'title': "I'Ll Be Back: On the Multiple Lives of Users of a Mobile Activity Tracking Application", 'citation_count': '78', 'citation_year': '2020'}], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json'}

exec(code, env_args)
