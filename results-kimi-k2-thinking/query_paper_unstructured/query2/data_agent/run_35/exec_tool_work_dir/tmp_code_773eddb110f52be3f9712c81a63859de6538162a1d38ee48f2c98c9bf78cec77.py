code = """import json

# Read paper documents from MongoDB
with open('/tmp/tmp6_9_93m6.json', 'r') as f:
    paper_docs = json.load(f)

# Read citations data for 2018
with open('/tmp/tmpd_a3l3k7.json', 'r') as f:
    citations_2018 = json.load(f)

# Extract paper information (title, source, year, venue, domain, contribution)
papers_info = []

for doc in paper_docs:
    filename = doc.get('filename', '')
    text = doc.get('text', '')
    
    # Extract title from filename (remove .txt extension)
    title = filename.replace('.txt', '') if filename else ''
    
    # Check if paper is published by ACM
    # Look for ACM indicators in the text
    is_acm = 'ACM' in text or 'acm' in text.lower()
    
    # Extract year - look for patterns like YYYY or 'YY
    import re
    year_match = re.search(r"(20\d{2})", text)
    year = int(year_match.group(1)) if year_match else None
    
    # Extract venue - look for common conference patterns
    venue_match = re.search(r"(CHI|Ubicomp|UbiComp|CSCW|DIS|PervasiveHealth|WWW|IUI|OzCHI|TEI|AH)\s*'?\d{2}", text)
    venue = venue_match.group(1) if venue_match else None
    
    # Extract domain - check for common HCI research domains
    domains = []
    domain_keywords = {
        'food': ['food', 'eating', 'diet', 'nutrition'],
        'physical activity': ['physical activity', 'exercise', 'fitness', 'steps', 'walking', 'running'],
        'sleep': ['sleep', 'bedtime', 'rest'],
        'mental': ['mental', 'psychology', 'cognitive', 'stress', 'anxiety', 'depression'],
        'finances': ['finance', 'money', 'expense', 'budget'],
        'productivity': ['productivity', 'work', 'task', 'time management'],
        'screen time': ['screen time', 'digital device', 'smartphone', 'computer'],
        'social interactions': ['social', 'interaction', 'communication', 'relationship'],
        'location': ['location', 'place', 'gps', 'geographic'],
        'chronic': ['chronic', 'disease', 'illness'],
        'diabetes': ['diabetes', 'diabetic'],
        'health_behavior': ['health behavior', 'health', 'wellness', 'wellbeing']
    }
    
    text_lower = text.lower()
    for domain, keywords in domain_keywords.items():
        if any(keyword in text_lower for keyword in keywords):
            domains.append(domain)
    
    # Extract contribution type
    contributions = []
    contribution_keywords = {
        'empirical': ['study', 'survey', 'interview', 'experiment', 'evaluation', 'field study'],
        'artifact': ['system', 'tool', 'prototype', 'application', 'app', 'design', 'implementation'],
        'theoretical': ['model', 'framework', 'theory', 'concept', 'taxonomy', 'conceptual'],
        'survey': ['survey', 'review', 'literature review'],
        'methodological': ['method', 'methodology', 'approach', 'technique', 'process']
    }
    
    for contrib_type, keywords in contribution_keywords.items():
        if any(keyword in text_lower for keyword in keywords):
            contributions.append(contrib_type)
    
    papers_info.append({
        'title': title,
        'source': 'ACM' if is_acm else 'Unknown',
        'year': year,
        'venue': venue,
        'domains': domains,
        'contributions': contributions
    })

# Convert citations to a dictionary for easy lookup
citations_dict = {}
for citation in citations_2018:
    title = citation.get('title', '')
    citation_count = int(citation.get('citation_count', 0))
    citations_dict[title] = citation_count

# Find ACM papers that have citations in 2018
acm_citations = []
matched_papers = []

for paper in papers_info:
    if paper['source'] == 'ACM' and paper['title'] in citations_dict:
        citation_count = citations_dict[paper['title']]
        acm_citations.append(citation_count)
        matched_papers.append({
            'title': paper['title'],
            'citation_count': citation_count
        })

# Calculate average
if acm_citations:
    avg_citations = sum(acm_citations) / len(acm_citations)
    result = {
        'average_citation_count': round(avg_citations, 2),
        'total_acm_papers_cited': len(acm_citations),
        'total_citations': sum(acm_citations)
    }
else:
    result = {
        'average_citation_count': 0,
        'total_acm_papers_cited': 0,
        'total_citations': 0,
        'message': 'No ACM papers found with citations in 2018'
    }

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['paper_docs'], 'var_functions.list_db:1': ['Citations', 'sqlite_sequence'], 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json'}

exec(code, env_args)
