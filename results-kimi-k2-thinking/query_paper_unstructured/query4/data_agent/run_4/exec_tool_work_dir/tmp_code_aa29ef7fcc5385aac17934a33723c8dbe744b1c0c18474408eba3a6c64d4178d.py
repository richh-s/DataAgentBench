code = """import json
import re

# Read all paper documents from the file path
file_path = locals()['var_functions.query_db:2']
with open(file_path, 'r') as f:
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
    
    # Extract year - look for copyright year first, then 4-digit patterns after 2000
    copyright_match = re.search(r'Copyright\s*[@©]?\s*(20\d{2})', text)
    if copyright_match:
        year = int(copyright_match.group(1))
    else:
        year_match = re.search(r'\b(20\d{2})\b', text)
        if year_match:
            year = int(year_match.group(1))
    
    # Extract venue from text
    venue_patterns = [
        (r'\bCHI\s*\'?\s*(20\d{2})?\b', 'CHI'),
        (r'\bUbiComp|UBICOMP\s*\'?\s*(\d{4})?\b', 'UbiComp'),
        (r'\bCSCW\s*\'?\s*(\d{4})?\b', 'CSCW'),
        (r'\bDIS\s*\'?\s*(\d{4})?\b', 'DIS'),
        (r'\bPervasiveHealth\b', 'PervasiveHealth'),
        (r'\bWWW\b', 'WWW'),
        (r'\bIUI\b', 'IUI'),
        (r'\bOzCHI\b', 'OzCHI'),
        (r'\bTEI\b', 'TEI'),
        (r'\bAH\b', 'AH')
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
        'physical activity': ['physical activity', 'fitness', 'exercise', 'workout', 'step count'],
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
        'empirical': ['empirical', 'study', 'survey', 'interview', 'experiment', 'data collected'],
        'artifact': ['system', 'tool', 'prototype', 'application', 'interface', 'design'],
        'theoretical': ['model', 'theory', 'framework', 'conceptual'],
        'survey': ['survey', 'review', 'systematic review'],
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

# Get titles for citation lookup
paper_titles = [paper['title'] for paper in papers_2016_physical_activity]

# Store results for next step
result = {
    'papers_2016_physical_activity': papers_2016_physical_activity,
    'paper_titles': paper_titles
}

print('__RESULT__:')
print(json.dumps(result, indent=2))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json'}

exec(code, env_args)
