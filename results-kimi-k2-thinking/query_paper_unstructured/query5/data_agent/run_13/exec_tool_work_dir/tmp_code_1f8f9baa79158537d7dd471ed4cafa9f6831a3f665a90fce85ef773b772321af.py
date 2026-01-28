code = """import json
import re

# Load the data again more carefully
citations_var = locals()['var_functions.query_db:5']
if isinstance(citations_var, str):
    with open(citations_var, 'r') as f:
        citations_data = json.load(f)
else:
    citations_data = citations_var

papers_var = locals()['var_functions.query_db:6']
if isinstance(papers_var, str):
    with open(papers_var, 'r') as f:
        papers_data = json.load(f)
else:
    papers_data = papers_var

# Create a more robust venue extraction
def extract_venue_info(paper):
    text = paper.get('text', '')
    filename = paper.get('filename', '').replace('.txt', '')
    
    # Look for venue indicators in the text
    venue_indicators = []
    
    # Check for CHI
    if re.search(r'\bCHI\b', text):
        venue_indicators.append('CHI')
    if 'Human Factors in Computing Systems' in text:
        venue_indicators.append('CHI')
    
    # Try to extract year
    year = None
    year_patterns = [
        r'CHI\s*[\'?](20\d{2})',
        r'Proceedings of.*?20(\d{2})',
        r'\b(20\d{2})\b'
    ]
    
    for pattern in year_patterns:
        match = re.search(pattern, text)
        if match:
            found_year = match.group(1)
            if len(found_year) == 2:
                year = int('20' + found_year)
            elif len(found_year) == 4:
                year = int(found_year)
            break
    
    return {
        'title': filename,
        'venue': 'CHI' if venue_indicators else None,
        'year': year,
        'filename': filename
    }

# Extract CHI papers
chi_papers = []
for paper in papers_data:
    info = extract_venue_info(paper)
    if info['venue'] == 'CHI':
        chi_papers.append(info)

print('Found %d CHI papers total' % len(chi_papers))

# Create clean title mapping for CHI papers
def normalize_title(title):
    if not title:
        return ''
    # Just lowercase and remove extra spaces, keep most words
    title = title.lower().strip()
    title = re.sub(r'\s+', ' ', title)
    # Remove common punctuation but keep alphanumeric and spaces
    title = re.sub(r'[^a-z0-9\s]', '', title)
    return title

chi_title_map = {}
for paper in chi_papers:
    clean = normalize_title(paper['title'])
    chi_title_map[clean] = paper

# Find CHI citations in 2020
total_citations = 0
matched_papers = []

for citation in citations_data:
    if isinstance(citation, dict) and int(citation.get('citation_year', 0)) == 2020:
        cite_title = citation.get('title', '')
        clean_cite_title = normalize_title(cite_title)
        
        # Check for exact match
        if clean_cite_title in chi_title_map:
            count = int(citation.get('citation_count', 0))
            total_citations += count
            matched_papers.append({
                'title': chi_title_map[clean_cite_title]['title'],
                'citations': count
            })

print('Matched %d papers with 2020 citations' % len(matched_papers))
print('Total citation count: %d' % total_citations)

if matched_papers:
    print('\nSample matched papers:')
    for p in matched_papers[:5]:
        print('- %s: %d citations' % (p['title'], p['citations']))

result = {
    'total_citation_count': total_citations,
    'number_of_chi_papers': len(matched_papers),
    'matches': matched_papers
}
print('__RESULT__:')
print(json.dumps(result, indent=2))"""

env_args = {'var_functions.list_db:0': ['paper_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.execute_python:12': {'total_citations': 243, 'papers_count': 4}}

exec(code, env_args)
