code = """import json
import re

# Read the paper documents from the stored file path
paper_docs_key = 'var_functions.query_db:2'
paper_docs_path = locals()[paper_docs_key]

with open(paper_docs_path, 'r') as f:
    paper_docs = json.load(f)

# Extract information from paper text
def extract_paper_info(text, filename):
    """Extract title, year, venue, source, and domain from paper text"""
    title = filename.replace('.txt', '') if filename else ''
    
    year_match = re.search(r'(19|20)\d{2}', text)
    year = int(year_match.group()) if year_match else None
    
    text_lower = text.lower()
    domains = []
    
    domain_keywords = {
        'physical activity': ['physical activity', 'fitness', 'exercise', 'walking', 'running', 'step'],
        'food': ['food', 'diet', 'eating', 'nutrition', 'meal'],
        'sleep': ['sleep', 'bedtime', 'rest'],
        'mental': ['mental', 'mood', 'stress', 'emotion', 'psychological'],
        'finances': ['finances', 'financial', 'money', 'spending', 'budget'],
        'location': ['location', 'place', 'gps', 'geographic']
    }
    
    for domain, keywords in domain_keywords.items():
        if any(keyword in text_lower for keyword in keywords):
            domains.append(domain)
    
    venues = []
    venue_patterns = ['CHI', 'Ubicomp', 'CSCW', 'DIS', 'PervasiveHealth', 'WWW', 'IUI', 'OzCHI', 'TEI', 'AH', 'UIST']
    for venue in venue_patterns:
        if venue.upper() in text.upper():
            venues.append(venue)
    
    sources = []
    source_patterns = ['ACM', 'IEEE', 'PubMed']
    for source in source_patterns:
        if source.upper() in text.upper():
            sources.append(source)
    
    return {
        'title': title,
        'year': year,
        'domains': domains,
        'venues': venues,
        'sources': sources
    }

# Extract information from all papers
papers_info = []
papers_by_title = {}

for doc in paper_docs:
    info = extract_paper_info(doc.get('text', ''), doc.get('filename', ''))
    papers_info.append(info)
    papers_by_title[info['title']] = info

# Filter for 2016 physical activity papers
papers_2016_physical_activity = []
for info in papers_info:
    if info['year'] == 2016 and 'physical activity' in info['domains']:
        papers_2016_physical_activity.append(info['title'])

print(f"Total papers: {len(paper_docs)}")
print(f"2016 papers in physical activity domain: {len(papers_2016_physical_activity)}")
print(f"Sample papers: {papers_2016_physical_activity[:5]}")

print('__RESULT__:')
print(json.dumps(papers_2016_physical_activity))"""

env_args = {'var_functions.list_db:0': ['paper_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json'}

exec(code, env_args)
