code = """import json
import re
from collections import defaultdict

# Load the MongoDB documents
mongo_result = locals()['var_functions.query_db:0']

# If it's a file path, read the file
if isinstance(mongo_result, str) and mongo_result.endswith('.json'):
    with open(mongo_result, 'r') as f:
        papers = json.load(f)
else:
    papers = mongo_result

# Extract paper information from documents
paper_info = []

for paper in papers:
    filename = paper.get('filename', '')
    text = paper.get('text', '')
    
    # Extract title from filename
    title = filename.replace('.txt', '') if filename else ''
    
    # Extract year - look for patterns like '2015', 'SEPTEMBER 7-11, 2015', etc.
    year = None
    year_matches = re.findall(r'(?:19|20)\d{2}', text)
    if year_matches:
        # Usually the first year in the document is the publication year
        year = int(year_matches[0])
    
    # Extract venue - look for common venue patterns
    venue = None
    venue_patterns = [
        r'CHI\s*\'\d{2}', r'Ubicomp\s*\'\d{2}', r'CSCW', r'DIS', r'PervasiveHealth',
        r'WWW', r'IUI', r'OzCHI', r'TEI', r'AH', r'UBICOMP\s*\'\d{2}',
        r'UbiComp\s*\'\d{2}', r'Pervasive\s*Health'
    ]
    
    for pattern in venue_patterns:
        match = re.search(pattern, text, re.IGNORECASE)
        if match:
            venue = match.group(0)
            break
    
    # Extract source/publisher
    source = None
    source_patterns = [
        r'ACM', r'IEEE', r'PubMed'
    ]
    
    for pattern in source_patterns:
        match = re.search(pattern, text, re.IGNORECASE)
        if match:
            source = match.group(0)
            break
    
    # Extract domain - look for mentions of research domains
    domain = []
    domain_keywords = [
        'food', 'physical activity', 'sleep', 'mental', 'finances', 'productivity',
        'screen time', 'social interactions', 'location', 'chronic', 'diabetes',
        'health behavior', 'weight', 'nutrition', 'eating', 'diet'
    ]
    
    text_lower = text.lower()
    for keyword in domain_keywords:
        if keyword in text_lower:
            domain.append(keyword)
    
    # Extract contribution type
    contribution = []
    contribution_keywords = [
        'empirical', 'artifact', 'theoretical', 'survey', 'methodological'
    ]
    
    for keyword in contribution_keywords:
        if keyword.lower() in text_lower:
            contribution.append(keyword)
    
    paper_info.append({
        'title': title,
        'year': year,
        'venue': venue,
        'source': source,
        'domain': domain,
        'contribution': contribution,
        'original_filename': filename
    })

# Count papers with food domain
food_papers = [p for p in paper_info if 'food' in p['domain'] or 'nutrition' in p['domain'] or 'eating' in p['domain'] or 'diet' in p['domain']]
print(f"Total papers: {len(paper_info)}")
print(f"Papers with food domain: {len(food_papers)}")

# Show some examples
print("\nExample food domain papers:")
for p in food_papers[:5]:
    print(f"- {p['title']} (domains: {p['domain']})")

print('__RESULT__:')
print(json.dumps({
    'total_papers': len(paper_info),
    'food_papers_count': len(food_papers),
    'food_papers': food_papers
}))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': [{'id': '1', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '4', 'citation_year': '2017'}, {'id': '2', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '95', 'citation_year': '2018'}, {'id': '3', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '32', 'citation_year': '2012'}, {'id': '4', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '29', 'citation_year': '2013'}, {'id': '5', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '18', 'citation_year': '2014'}]}

exec(code, env_args)
