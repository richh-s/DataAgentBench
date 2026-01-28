code = """import json, re, os, sys

# Load the full paper documents from the file path stored in the variable
file_path = var_functions.query_db:2
with open(file_path, 'r') as f:
    paper_docs = json.load(f)

# Extract information from paper documents
paper_info = []

for doc in paper_docs:
    filename = doc['filename']
    text = doc['text']
    
    # Extract title from filename
    title = filename.replace('.txt', '')
    
    # Extract year - look for patterns like '2016', 'y2016', etc.
    year_match = re.search(r'(\b(20|19)\d{2}\b)', text)
    year = year_match.group(1) if year_match else None
    
    # Extract venue - look for common HCI venue mentions
    venues = ['CHI', 'Ubicomp', 'Ubicomp', 'CSCW', 'DIS', 'PervasiveHealth', 'WWW', 'IUI', 'OzCHI', 'TEI', 'AH', 'UbiComp', 'UbiComp']
    venue_match = None
    for venue in venues:
        if venue.lower() in text.lower():
            venue_match = venue
            break
    venue = venue_match if venue_match else None
    
    # Extract domain - look for 'physical activity', 'food', 'sleep', etc.
    domains = ['physical activity', 'food', 'sleep', 'mental', 'finances', 'productivity', 'screen time', 'social interactions', 'location', 'chronic', 'diabetes', 'health_behavior']
    domain = []
    for d in domains:
        if d.lower() in text.lower():
            domain.append(d)
    
    # Extract source - look for ACM, IEEE, PubMed
    sources = ['ACM', 'IEEE', 'PubMed']
    source = []
    for s in sources:
        if s.lower() in text.lower():
            source.append(s)
    
    # Extract contribution type
    contributions = ['empirical', 'artifact', 'theoretical', 'survey', 'methodological']
    contribution = []
    for c in contributions:
        if c.lower() in text.lower():
            contribution.append(c)
    
    paper_info.append({
        'title': title,
        'year': int(year) if year and year.isdigit() else None,
        'venue': venue,
        'domains': domain,
        'sources': source,
        'contributions': contribution
    })

# Load citation data
citation_data = var_functions.query_db:5

# For debugging, let's print some info about what we found
print('__RESULT__:')
print(json.dumps({
    'paper_count': len(paper_info),
    'sample_papers': paper_info[:5],
    'citation_count': len(citation_data),
    'sample_citations': citation_data[:5]
}))"""

env_args = {'var_functions.list_db:0': ['paper_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': [{'id': '1', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '4', 'citation_year': '2017'}, {'id': '2', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '95', 'citation_year': '2018'}, {'id': '3', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '32', 'citation_year': '2012'}, {'id': '4', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '29', 'citation_year': '2013'}, {'id': '5', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '18', 'citation_year': '2014'}]}

exec(code, env_args)
