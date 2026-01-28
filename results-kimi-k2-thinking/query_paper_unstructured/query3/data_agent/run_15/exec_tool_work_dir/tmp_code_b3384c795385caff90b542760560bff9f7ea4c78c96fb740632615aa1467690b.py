code = """import json
import re

# Load the papers data from the file
papers_file = locals()['var_functions.query_db:8']
with open(papers_file, 'r') as f:
    papers_data = json.load(f)

# Parse paper information from text
parsed_papers = []

for paper in papers_data:
    text = paper.get('text', '')
    filename = paper.get('filename', '')
    
    # Extract title from filename
    title = filename.replace('.txt', '') if filename else ''
    
    # Extract year - look for 4-digit year patterns
    year_match = re.search(r'(20\d{2})', text)
    year = None
    if year_match:
        try:
            year = int(year_match.group(1))
            if year < 2000 or year > 2025:
                year = None
        except:
            year = None
    
    # Extract contribution type
    contribution = None
    text_lower = text.lower()
    if 'empirical' in text_lower:
        contribution = 'empirical'
    elif 'artifact' in text_lower:
        contribution = 'artifact'
    elif 'theoretical' in text_lower:
        contribution = 'theoretical'
    elif 'survey' in text_lower:
        contribution = 'survey'
    elif 'methodological' in text_lower:
        contribution = 'methodological'
    
    # Extract venue
    venue = None
    if 'CHI' in text:
        venue = 'CHI'
    elif 'Ubicomp' in text or 'UbiComp' in text:
        venue = 'Ubicomp'
    elif 'CSCW' in text:
        venue = 'CSCW'
    elif 'DIS' in text:
        venue = 'DIS'
    elif 'PervasiveHealth' in text:
        venue = 'PervasiveHealth'
    elif 'WWW' in text:
        venue = 'WWW'
    elif 'IUI' in text:
        venue = 'IUI'
    
    # Extract source/publisher
    source = None
    if 'ACM' in text:
        source = 'ACM'
    elif 'IEEE' in text:
        source = 'IEEE'
    elif 'PubMed' in text:
        source = 'PubMed'
    
    # Extract domain (multiple possible)
    domains = []
    domain_keywords = {
        'food': ['food', 'diet', 'eating'],
        'physical activity': ['physical activity', 'fitness', 'exercise'],
        'sleep': ['sleep'],
        'mental': ['mental', 'psychology', 'mood'],
        'finances': ['finances', 'financial', 'money', 'expense'],
        'productivity': ['productivity'],
        'location': ['location', 'place', 'geo'],
        'diabetes': ['diabetes']
    }
    
    for domain, keywords in domain_keywords.items():
        for keyword in keywords:
            if keyword in text_lower:
                domains.append(domain)
                break
    
    domain = ','.join(set(domains)) if domains else None
    
    parsed_papers.append({
        'title': title,
        'year': year,
        'venue': venue,
        'source': source,
        'domain': domain,
        'contribution': contribution,
        'original_filename': filename
    })

# Filter papers with empirical contribution published after 2016
empirical_papers_after_2016 = [
    p for p in parsed_papers 
    if p['contribution'] == 'empirical' and p['year'] and p['year'] > 2016
]

# Load citation data
citations_data = locals()['var_functions.query_db:6']

# For each empirical paper after 2016, find its total citations
result = []
for paper in empirical_papers_after_2016:
    title = paper['title']
    # Find matching citations
    total_citations = 0
    for citation in citations_data:
        if citation['title'] == title:
            total_citations += int(citation['citation_count'])
    
    result.append({
        'title': title,
        'year': paper['year'],
        'total_citations': total_citations
    })

# Return result
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:6': [{'id': '1', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '4', 'citation_year': '2017'}, {'id': '2', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '95', 'citation_year': '2018'}, {'id': '3', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '32', 'citation_year': '2012'}, {'id': '4', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '29', 'citation_year': '2013'}, {'id': '5', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '18', 'citation_year': '2014'}], 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json'}

exec(code, env_args)
