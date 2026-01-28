code = """import json
# Read the paper documents from the stored file path
paper_docs_path = var_functions.query_db:2
with open(paper_docs_path, 'r') as f:
    paper_docs = json.load(f)

# Let's explore the structure and extract key information
print(f"Total papers loaded: {len(paper_docs)}")

# Show a few papers to understand the structure
for i, doc in enumerate(paper_docs[:3]):
    print(f"\nPaper {i+1}:")
    print(f"Filename: {doc.get('filename')}")
    print(f"First 200 chars of text: {doc.get('text', '')[:200]}...")

# Let's try to extract year and domain information from the text
def extract_paper_info(text, filename):
    """Extract title, year, venue, source, and domain from paper text"""
    # Title from filename
    title = filename.replace('.txt', '') if filename else ''
    
    # Try to find year - look for patterns like YYYY
    import re
    year_match = re.search(r'(19|20)\d{2}', text)
    year = int(year_match.group()) if year_match else None
    
    # Try to identify domain - look for keywords related to domains
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
    
    # Try to identify venue - look for common conference/journal names
    venues = []
    venue_patterns = ['CHI', 'Ubicomp', 'CSCW', 'DIS', 'PervasiveHealth', 'WWW', 'IUI', 'OzCHI', 'TEI', 'AH', 'UIST']
    for venue in venue_patterns:
        if venue.upper() in text.upper():
            venues.append(venue)
    
    # Try to identify source/publisher
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
for doc in paper_docs:
    info = extract_paper_info(doc.get('text', ''), doc.get('filename', ''))
    papers_info.append(info)

# Show some examples
print("\n\nExtracted information from first 5 papers:")
for i, info in enumerate(papers_info[:5]):
    print(f"{i+1}. Title: {info['title']}")
    print(f"   Year: {info['year']}")
    print(f"   Domains: {info['domains']}")
    print(f"   Venues: {info['venues']}")
    print(f"   Sources: {info['sources']}")

# Count papers by year
year_counts = {}
for info in papers_info:
    year = info['year']
    if year:
        year_counts[year] = year_counts.get(year, 0) + 1

print(f"\n\nPaper counts by year: {dict(sorted(year_counts.items()))}")

# Filter for 2016 physical activity papers
papers_2016_physical_activity = []
for info in papers_info:
    if info['year'] == 2016 and 'physical activity' in info['domains']:
        papers_2016_physical_activity.append(info['title'])

print(f"\n\n2016 papers in physical activity domain: {len(papers_2016_physical_activity)}")
print(papers_2016_physical_activity[:10])  # Show first 10

print('__RESULT__:')
print(json.dumps({
    'total_papers': len(paper_docs),
    'papers_2016_physical_activity': papers_2016_physical_activity,
    'year_counts': year_counts
}))"""

env_args = {'var_functions.list_db:0': ['paper_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json'}

exec(code, env_args)
