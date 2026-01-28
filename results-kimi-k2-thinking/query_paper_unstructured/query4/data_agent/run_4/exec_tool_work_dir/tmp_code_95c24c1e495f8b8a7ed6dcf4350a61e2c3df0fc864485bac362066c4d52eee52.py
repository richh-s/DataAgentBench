code = """import json
import re

# Read the full paper documents data
with open(var_functions.query_db:2, 'r') as f:
    paper_docs = json.load(f)

print(f"Total paper documents: {len(paper_docs)}")

# Extract fields from paper documents
papers_info = []

for idx, doc in enumerate(paper_docs):
    text = doc['text']
    filename = doc['filename']
    
    # Extract title from filename
    title = filename.replace('.txt', '')
    
    # Initialize extraction
    year = None
    venue = None
    source = None
    domain = []
    contribution = []
    
    # Extract year from text (look for 4-digit numbers indicating year)
    # Common patterns: YYYY (e.g., '2015'), copyright year, etc.
    year_match = re.search(r'(\b(20\d{2})\b)', text)
    if year_match:
        year = int(year_match.group(1))
        # Try to narrow down to actual publication year (usually near the beginning)
        # Look for patterns like "Copyright YYYY" or "ACM YYYY"
        copyright_match = re.search(r'Copyright\s*[@©]?\s*(20\d{2})', text)
        if copyright_match:
            year = int(copyright_match.group(1))
    
    # Extract venue from text
    # Look for common venue patterns
    venue_patterns = [
        (r'\b(CHI)\s*\'?\s*(20\d{2})?\b', 'CHI'),
        (r'\b(UbiComp|UBICOMP)\s*\'?\s*(\d{4})?\b', 'UbiComp'),
        (r'\b(CSCW)\s*\'?\s*(\d{4})?\b', 'CSCW'),
        (r'\b(DIS)\s*\'?\s*(\d{4})?\b', 'DIS'),
        (r'\b(PervasiveHealth)\b', 'PervasiveHealth'),
        (r'\b(WWW)\b', 'WWW'),
        (r'\b(IUI)\b', 'IUI'),
        (r'\b(OzCHI)\b', 'OzCHI'),
        (r'\b(TEI)\b', 'TEI'),
        (r'\b(AH)\b', 'AH')
    ]
    
    for pattern, venue_name in venue_patterns:
        if re.search(pattern, text):
            venue = venue_name
            break
    
    # Extract source from text
    source_patterns = [
        (r'\bACM\b', 'ACM'),
        (r'\bIEEE\b', 'IEEE'),
        (r'\bPubMed\b', 'PubMed')
    ]
    
    for pattern, source_name in source_patterns:
        if re.search(pattern, text):
            source = source_name
            break
    
    # Extract domains from text using keyword matching
    text_lower = text.lower()
    domain_keywords = {
        'food': ['food', 'eating', 'diet', 'nutrition'],
        'physical activity': ['physical activity', 'fitness', 'exercise', 'workout', 'activity tracking'],
        'sleep': ['sleep', 'sleeping'],
        'mental': ['mental', 'psychology', 'mindfulness', 'stress', 'anxiety', 'mood'],
        'finances': ['financial', 'finance', 'money', 'expense', 'budget', 'payment'],
        'productivity': ['productivity', 'work', 'task', 'time management'],
        'screen time': ['screen time', 'digital', 'phone use'],
        'social interactions': ['social', 'interaction', 'relationship'],
        'location': ['location', 'place', 'geographic'],
        'chronic': ['chronic', 'disease'],
        'diabetes': ['diabetes', 'diabetic'],
        'health_behavior': ['health', 'behavior', 'wellness']
    }
    
    for domain_name, keywords in domain_keywords.items():
        if any(keyword in text_lower for keyword in keywords):
            domain.append(domain_name)
    
    # Extract contributions from text
    contribution_keywords = {
        'empirical': ['empirical', 'study', 'survey', 'interview', 'experiment'],
        'artifact': ['system', 'tool', 'prototype', 'application', 'interface', 'design'],
        'theoretical': ['model', 'theory', 'framework', 'conceptual'],
        'survey': ['survey', 'review', 'systematic'],
        'methodological': ['method', 'methodology', 'approach']
    }
    
    for contrib_name, keywords in contribution_keywords.items():
        if any(keyword in text_lower for keyword in keywords):
            contribution.append(contrib_name)
    
    papers_info.append({
        'title': title,
        'year': year,
        'venue': venue,
        'source': source,
        'domain': domain,
        'contribution': contribution
    })

# Filter papers published in 2016 in the 'physical activity' domain
papers_2016_physical_activity = []
for paper in papers_info:
    if paper['year'] == 2016 and 'physical activity' in paper['domain']:
        papers_2016_physical_activity.append(paper)

print(f"Papers from 2016 in physical activity domain: {len(papers_2016_physical_activity)}")

# For each such paper, I need to find its citation count from citations_database
paper_titles = [paper['title'] for paper in papers_2016_physical_activity]
print(f"Found {len(paper_titles)} papers to check citations for:")
for title in paper_titles[:5]:  # Print first 5
    print(f"  - {title}")

# Store results for next step
result = {
    'papers_2016_physical_activity': papers_2016_physical_activity,
    'paper_titles': paper_titles
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json'}

exec(code, env_args)
