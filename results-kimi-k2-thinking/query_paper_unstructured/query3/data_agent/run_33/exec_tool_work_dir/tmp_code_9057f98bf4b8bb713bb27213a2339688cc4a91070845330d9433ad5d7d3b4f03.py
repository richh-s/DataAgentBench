code = """import json
import re

# Read the paper documents data
paper_docs_key = 'var_functions.query_db:0'
if paper_docs_key in locals():
    paper_docs_path = locals()[paper_docs_key]
    with open(paper_docs_path, 'r') as f:
        paper_docs = json.load(f)
    print(f'Loaded {len(paper_docs)} paper documents')
else:
    paper_docs = []

# Extract paper information from text
def extract_paper_info(doc):
    """Extract title, year, venue, source, domain, and contribution from paper text"""
    text = doc.get('text', '')
    filename = doc.get('filename', '')
    
    # Extract title from filename (remove .txt)
    title = filename.replace('.txt', '') if filename else 'Unknown'
    
    # Extract year - look for patterns like 'YYYY' or 
    year_patterns = [
        r'UBICOMP\s*\'(\d{2})',  # UBICOMP '15
        r'CHI\s*\'(\d{2})',      # CHI '16
        r'\b(20\d{2})\b',        # Full year 2015, 2016, etc.
        r'Copyright\s*\d{4}\s*©\s*\d{4}',  # Copyright line
    ]
    
    year = None
    for pattern in year_patterns:
        matches = re.findall(pattern, text)
        if matches:
            # Convert 2-digit year to 4-digit
            year_str = matches[0]
            if len(year_str) == 2:
                year = int('20' + year_str) if int(year_str) < 50 else int('19' + year_str)
            else:
                year = int(year_str)
            break
    
    # Extract venue - look for common conference abbreviations
    venue_patterns = [
        r'UBICOMP', r'CHI', r'CSCW', r'DIS', r'PervasiveHealth', 
        r'WWW', r'IUI', r'OzCHI', r'TEI', r'AH', r'UIST', r'MobileHCI'
    ]
    venue = None
    for pattern in venue_patterns:
        if re.search(pattern, text, re.IGNORECASE):
            venue = pattern.upper()
            break
    
    # Extract source - look for publishers
    source_patterns = [r'ACM', r'IEEE', r'PubMed']
    source = None
    for pattern in source_patterns:
        if re.search(pattern, text):
            source = pattern
            break
    
    # Extract domain - look for keywords
    domain_keywords = [
        'food', 'physical activity', 'sleep', 'mental', 'finances', 
        'productivity', 'screen time', 'social interactions', 'location',
        'chronic', 'diabetes', 'health behavior', 'weight', 'fitness'
    ]
    domains = [kw for kw in domain_keywords if kw.lower() in text.lower()]
    domain = ', '.join(domains) if domains else None
    
    # Extract contribution type
    contribution_keywords = [
        'empirical', 'artifact', 'theoretical', 'survey', 'methodological'
    ]
    contributions = [kw for kw in contribution_keywords if kw.lower() in text.lower()]
    contribution = ', '.join(contributions) if contributions else None
    
    return {
        'title': title,
        'year': year,
        'venue': venue,
        'source': source,
        'domain': domain,
        'contribution': contribution
    }

# Process all papers
papers_info = []
for doc in paper_docs:
    info = extract_paper_info(doc)
    papers_info.append(info)
    print(f"Title: {info['title']}")
    print(f"Year: {info['year']}")
    print(f"Venue: {info['venue']}")
    print(f"Contribution: {info['contribution']}")
    print(f"Domain: {info['domain']}")
    print("---")

# Filter papers with empirical contribution and published after 2016
filtered_papers = [p for p in papers_info if p['contribution'] and 'empirical' in p['contribution'].lower() and p['year'] and p['year'] > 2016]

print(f"\nFiltered papers (empirical, after 2016): {len(filtered_papers)}")
for paper in filtered_papers:
    print(f"- {paper['title']} ({paper['year']})")

# Output result
result = {
    'total_papers': len(papers_info),
    'filtered_papers': filtered_papers
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.execute_python:8': {'paper_docs_count': 5, 'citations_count': 1405}}

exec(code, env_args)
