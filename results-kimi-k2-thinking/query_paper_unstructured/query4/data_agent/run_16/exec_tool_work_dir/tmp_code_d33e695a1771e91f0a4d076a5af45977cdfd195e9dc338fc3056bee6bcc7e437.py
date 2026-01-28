code = """import json
import re

# Access the stored file path for paper documents
path_key = 'var_functions.query_db:2'
in_file = locals()[path_key]

# Read the data
with open(in_file, 'r') as f:
    paper_docs = json.load(f)

print('Total papers loaded:', len(paper_docs))

# Extract structured information from papers
papers = []

for doc in paper_docs:
    filename = doc.get('filename', '')
    text = doc.get('text', '')
    
    # Extract title from filename
    title = filename.replace('.txt', '') if filename else ''
    
    # Extract year - look for 4-digit numbers, prefer recent years
    year = None
    year_matches = re.findall(r'(19|20)\d{2}', text)
    if year_matches:
        # Filter for years between 2000-2025
        valid_years = [int(y) for y in year_matches if 2000 <= int(y) <= 2025]
        if valid_years:
            year = max(valid_years)  # Use most recent year found
    
    # Extract domains - comprehensive keyword search
    text_lower = text.lower()
    domains = []
    
    # Domain keywords mapping
    domain_keywords = {
        'physical activity': ['physical activity', 'fitness', 'exercise', 'walking', 'running', 
                             'steps', 'step count', 'active', 'workout', 'sedentary',
                             'calories burned', 'heart rate', 'physical'],
        'food': ['food', 'diet', 'eating', 'nutrition', 'meal', 'calorie intake', 'weight'],
        'sleep': ['sleep', 'bedtime', 'rest', 'circadian'],
        'mental': ['mental', 'mood', 'stress', 'emotion', 'psychological', 'wellbeing', 'anxiety'],
        'finances': ['finances', 'financial', 'money', 'spending', 'budget', 'expense', 'income'],
        'location': ['location', 'place', 'gps', 'geographic', 'mobility', 'spatial'],
        'screen time': ['screen time', 'phone use', 'digital'],
        'social': ['social interactions', 'social', 'communication', 'friends', 'family']
    }
    
    for domain, keywords in domain_keywords.items():
        if any(keyword in text_lower for keyword in keywords):
            domains.append(domain)
    
    # Deduplicate domains, prioritizing 'physical activity' if present
    unique_domains = list(set(domains))
    
    # Extract venue
    venues = []
    venue_patterns = ['CHI', 'Ubicomp', 'CSCW', 'DIS', 'PervasiveHealth', 'WWW', 'IUI', 'OzCHI', 'TEI', 'AH']
    for venue in venue_patterns:
        if venue.upper() in text.upper():
            venues.append(venue)
    
    # Extract source
    sources = []
    source_patterns = ['ACM', 'IEEE', 'PubMed']
    for source in source_patterns:
        if source.upper() in text.upper():
            sources.append(source)
    
    if title and year and domains:
        papers.append({
            'title': title,
            'year': year,
            'domains': unique_domains,
            'venues': venues,
            'sources': sources
        })

# Filter for 2016 physical activity papers
papers_2016_physical_activity = []
for paper in papers:
    if paper['year'] == 2016 and 'physical activity' in paper['domains']:
        papers_2016_physical_activity.append(paper['title'])

# Display summary
year_counts = {}
domain_counts = {}
for paper in papers:
    year_counts[paper['year']] = year_counts.get(paper['year'], 0) + 1
    for domain in paper['domains']:
        domain_counts[domain] = domain_counts.get(domain, 0) + 1

print('\nPaper distribution by year:')
for year in sorted(year_counts.keys()):
    print(f'  {year}: {year_counts[year]}')

print('\nPaper distribution by domain:')
for domain in sorted(domain_counts.keys(), key=lambda x: domain_counts[x], reverse=True)[:10]:
    print(f'  {domain}: {domain_counts[domain]}')

print(f'\nFound {len(papers_2016_physical_activity)} papers from 2016 in physical activity domain:')
for title in papers_2016_physical_activity:
    print(f'  - {title}')

print('__RESULT__:')
print(json.dumps(papers_2016_physical_activity))"""

env_args = {'var_functions.list_db:0': ['paper_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.execute_python:8': [], 'var_functions.list_db:10': ['Citations', 'sqlite_sequence'], 'var_functions.query_db:12': [{'id': '1', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '4', 'citation_year': '2017'}, {'id': '2', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '95', 'citation_year': '2018'}, {'id': '3', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '32', 'citation_year': '2012'}, {'id': '4', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '29', 'citation_year': '2013'}, {'id': '5', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '18', 'citation_year': '2014'}, {'id': '6', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '95', 'citation_year': '2015'}, {'id': '7', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '14', 'citation_year': '2016'}, {'id': '8', 'title': 'Sundroid: Solar Radiation Awareness with Smartphones', 'citation_count': '12', 'citation_year': '2012'}, {'id': '9', 'title': 'Sundroid: Solar Radiation Awareness with Smartphones', 'citation_count': '76', 'citation_year': '2013'}, {'id': '10', 'title': 'Sundroid: Solar Radiation Awareness with Smartphones', 'citation_count': '55', 'citation_year': '2014'}]}

exec(code, env_args)
