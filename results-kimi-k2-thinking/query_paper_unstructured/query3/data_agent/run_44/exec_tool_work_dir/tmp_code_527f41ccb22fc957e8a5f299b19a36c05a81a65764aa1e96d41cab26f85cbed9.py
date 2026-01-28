code = """import json
import re

# Read the citations data
citations_file = var_functions.query_db:5
citations_data = json.loads(open(citations_file).read())

# Read the paper documents data
papers_file = var_functions.query_db:6
papers_data = json.loads(open(papers_file).read())

# Extract title from filename
for paper in papers_data:
    if 'filename' in paper:
        paper['title'] = paper['filename'].replace('.txt', '')

# For each paper, extract year, venue, source, domain, contribution from text
year_pattern = r'\b(20\d{2})\b'
venue_pattern = r'(CHI|Ubicomp|CSCW|DIS|PervasiveHealth|WWW|IUI|OzCHI|TEI|AH)'
source_pattern = r'(ACM|IEEE|PubMed)'
contribution_pattern = r'(empirical|artifact|theoretical|survey|methodological)'

def extract_info(text):
    info = {
        'year': None,
        'venue': [],
        'source': [],
        'contribution': [],
        'domain': []
    }
    
    # Extract year
    year_match = re.search(year_pattern, text)
    if year_match:
        info['year'] = int(year_match.group(1))
    
    # Extract venue
    venues = re.findall(venue_pattern, text, re.IGNORECASE)
    info['venue'] = list(set([v.upper() for v in venues]))
    
    # Extract source
    sources = re.findall(source_pattern, text, re.IGNORECASE)
    info['source'] = list(set([s.upper() for s in sources]))
    
    # Extract contribution
    contributions = re.findall(contribution_pattern, text, re.IGNORECASE)
    info['contribution'] = list(set([c.lower() for c in contributions]))
    
    # Extract domain (look for common domain keywords)
    common_domains = ['food', 'physical activity', 'sleep', 'mental', 'finances', 'productivity', 'screen time', 'social interactions', 'location', 'chronic', 'diabetes', 'health_behavior']
    text_lower = text.lower()
    domains = []
    for domain in common_domains:
        if domain in text_lower:
            domains.append(domain)
    info['domain'] = list(set(domains))
    
    return info

# Process all papers
for paper in papers_data:
    if 'text' in paper:
        info = extract_info(paper['text'])
        paper.update(info)

# Filter papers with empirical contribution and year > 2016
empirical_papers = []
for paper in papers_data:
    if paper.get('year') and paper['year'] > 2016:
        if 'empirical' in paper.get('contribution', []):
            empirical_papers.append(paper)

print('__RESULT__:')
print(f"Total papers: {len(papers_data)}, Empirical papers after 2016: {len(empirical_papers)}")"""

env_args = {'var_functions.list_db:0': ['paper_docs'], 'var_functions.list_db:2': ['Citations', 'sqlite_sequence'], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json'}

exec(code, env_args)
