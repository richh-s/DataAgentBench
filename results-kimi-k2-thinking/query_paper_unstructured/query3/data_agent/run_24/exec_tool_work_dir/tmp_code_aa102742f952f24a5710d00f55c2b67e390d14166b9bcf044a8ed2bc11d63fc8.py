code = """import json
import re

# Read paper documents
paper_docs_path = var_functions.query_db:2
with open(paper_docs_path, 'r') as f:
    paper_docs = json.load(f)

# Extract paper information from documents
papers_info = []
for doc in paper_docs:
    # Extract title from filename
    filename = doc.get('filename', '')
    title = filename.replace('.txt', '') if filename else 'Unknown Title'
    
    # Extract text for analysis
    text = doc.get('text', '')
    
    # Extract year (look for year patterns like '2017', "'17", etc.)
    year = None
    year_patterns = [
        r'(?:19|20)\d{2}',  # Four digit years 1900-2099
        r"'\d{2}"  # Two digit years like '17
    ]
    
    # Look for venue and year markers (e.g., CHI '17, 2017)
    venue_patterns = r'(?:CHI|Ubicomp|UbiComp|CSCW|DIS|PervasiveHealth|WWW|IUI|OzCHI|TEI|AH|UBICOMP)\s*[\'"]?\s*(?:20)?\d{2}'
    matches = re.findall(venue_patterns, text, re.IGNORECASE)
    
    if matches:
        for match in matches:
            year_match = re.search(r'(?:19|20)\d{2}', match)
            if year_match:
                year = int(year_match.group())
                break
    
    # If not found, look for any four-digit year in the text
    if not year:
        year_match = re.search(r'(?:19|20)\d{2}', text)
        if year_match:
            year = int(year_match.group())
    
    # Determine contribution type - look for 'empirical' in text
    contribution = ''
    # Common ways contributions are mentioned in academic papers
    contrib_patterns = [
        r'empirical\s+study',
        r'empirical\s+research',
        r'empirical\s+work',
        r'empirical\s+investigation',
        r'empirical\s+analysis',
        r'empirical\s+evaluation',
        r'empirical\s+contribution',
        r'empirical\s+evidence',
        r'empirical\s+data',
        r'empirical\s+findings'
    ]
    
    text_lower = text.lower()
    contrib_matches = []
    for pattern in contrib_patterns:
        if re.search(pattern, text_lower):
            contrib_matches.append('empirical')
            break
    
    contribution = ','.join(contrib_matches) if contrib_matches else ''
    
    papers_info.append({
        'title': title,
        'year': year,
        'contribution': contribution
    })

# Read citations
citations_path = var_functions.query_db:3
with open(citations_path, 'r') as f:
    citations = json.load(f)

# Create a dictionary to sum citations per paper
citation_sums = {}
for cit in citations:
    title = cit.get('title', '')
    count = int(cit.get('citation_count', 0))
    if title in citation_sums:
        citation_sums[title] += count
    else:
        citation_sums[title] = count

# Join papers with citations and filter
results = []
for paper in papers_info:
    # Only consider papers after 2016 and with empirical contribution
    if paper['year'] and paper['year'] > 2016 and paper['contribution'] == 'empirical':
        title = paper['title']
        if title in citation_sums:
            results.append({
                'title': title,
                'total_citation_count': citation_sums[title]
            })

# If no results found, let's check why
if not results:
    # Debug: Check how many papers have empirical contribution
    empirical_papers = [p for p in papers_info if p['contribution'] == 'empirical']
    empirical_after_2016 = [p for p in empirical_papers if p['year'] and p['year'] > 2016]
    
    # Debug: Check papers with citations
    papers_with_citations = [p for p in papers_info if p['title'] in citation_sums]
    empirical_with_citations = [p for p in empirical_after_2016 if p['title'] in citation_sums]
    
    results = {
        'debug_info': {
            'total_papers': len(papers_info),
            'empirical_papers': len(empirical_papers),
            'empirical_after_2016': len(empirical_after_2016),
            'papers_with_citations': len(papers_with_citations),
            'empirical_with_citations': len(empirical_with_citations)
        },
        'empirical_papers_sample': empirical_after_2016[:5],
        'citations_sample': list(citation_sums.items())[:5]
    }

# Print result in required format
print('__RESULT__:')
print(json.dumps(results, indent=2))"""

env_args = {'var_functions.list_db:0': ['paper_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:3': 'file_storage/functions.query_db:3.json'}

exec(code, env_args)
