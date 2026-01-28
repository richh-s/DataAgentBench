code = """import json
import re

# Load the full MongoDB results
mongo_result_path = var_functions.query_db:2
with open(mongo_result_path, 'r') as f:
    papers = json.load(f)

# Function to extract paper information from text
extracted_papers = []

for paper in papers:
    filename = paper['filename']
    text = paper['text']
    
    # Extract title from filename
    title = filename.replace('.txt', '')
    
    # Extract year - look for patterns like '2016', '2015', etc.
    year_match = re.search(r'(20\d{2})', text)
    year = int(year_match.group(1)) if year_match else None
    
    # Extract domain - look for 'physical activity', 'food', 'sleep', etc.
    # Common domains from hints: "food", "physical activity", "sleep", "mental", "finances", "productivity", "screen time", "social interactions", "location", "chronic", "diabetes", "health_behavior"
    domains = []
    domain_keywords = {
        'physical activity': ['physical activity', 'fitness', 'exercise', 'workout', 'step count'],
        'food': ['food', 'diet', 'nutrition', 'eating'],
        'sleep': ['sleep', 'sleeping'],
        'mental': ['mental', 'psychology', 'stress', 'anxiety', 'depression'],
        'finances': ['finance', 'money', 'expense', 'budget'],
        'productivity': ['productivity', 'work', 'task'],
        'screen time': ['screen time', 'phone use', 'device use'],
        'social interactions': ['social', 'interaction', 'communication'],
        'location': ['location', 'place', 'gps'],
        'chronic': ['chronic', 'disease'],
        'diabetes': ['diabetes'],
        'health_behavior': ['health behavior', 'health', 'wellness']
    }
    
    text_lower = text.lower()
    for domain, keywords in domain_keywords.items():
        if any(keyword in text_lower for keyword in keywords):
            domains.append(domain)
    
    # Extract venue - look for common venues
    venues = []
    venue_patterns = ['CHI', 'Ubicomp', 'CSCW', 'DIS', 'PervasiveHealth', 'WWW', 'IUI', 'OzCHI', 'TEI', 'AH', 'UbiComp']
    for venue in venue_patterns:
        if venue in text:
            venues.append(venue)
    
    # Extract source - look for ACM, IEEE, PubMed
    sources = []
    source_patterns = ['ACM', 'IEEE', 'PubMed']
    for source in source_patterns:
        if source in text:
            sources.append(source)
    
    # Extract contribution type
    contributions = []
    contribution_patterns = {
        'empirical': ['empirical', 'study', 'survey', 'interview', 'experiment', 'evaluation'],
        'artifact': ['system', 'tool', 'application', 'app', 'prototype', 'design'],
        'theoretical': ['theoretical', 'model', 'framework', 'concept'],
        'survey': ['survey', 'review', 'literature'],
        'methodological': ['method', 'methodology', 'approach']
    }
    
    for contrib, keywords in contribution_patterns.items():
        if any(keyword in text_lower for keyword in keywords):
            contributions.append(contrib)
    
    extracted_papers.append({
        'title': title,
        'year': year,
        'domains': domains,
        'venues': venues,
        'sources': sources,
        'contributions': contributions
    })

# Filter papers from 2016 with 'physical activity' domain
papers_2016_physical_activity = []
for paper in extracted_papers:
    if paper['year'] == 2016 and 'physical activity' in paper['domains']:
        papers_2016_physical_activity.append(paper)

print('__RESULT__:')
print(json.dumps({
    'total_papers_found': len(papers_2016_physical_activity),
    'papers': papers_2016_physical_activity
}, indent=2))"""

env_args = {'var_functions.list_db:0': ['paper_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.list_db:5': ['Citations', 'sqlite_sequence'], 'var_functions.query_db:6': [{'id': '1', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '4', 'citation_year': '2017'}, {'id': '2', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '95', 'citation_year': '2018'}, {'id': '3', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '32', 'citation_year': '2012'}, {'id': '4', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '29', 'citation_year': '2013'}, {'id': '5', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '18', 'citation_year': '2014'}]}

exec(code, env_args)
