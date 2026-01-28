code = """import json
import re

# Load the full MongoDB results
with open('/mnt/data/paper_docs_query.json', 'r') as f:
    papers = json.load(f)

# Function to extract paper metadata
paper_data = []

for paper in papers:
    text = paper.get('text', '')
    filename = paper.get('filename', '')
    
    # Extract title from filename
    title = filename.replace('.txt', '') if filename else ''
    
    # Extract year from text
    # Look for patterns like '2017', '2018', etc. in the text
    year_match = re.search(r'(19|20)\d{2}', text)
    year = int(year_match.group()) if year_match else None
    
    # Extract contribution type - look for 'empirical', 'artifact', 'theoretical', 'survey', 'methodological'
    contribution = []
    text_lower = text.lower()
    
    if 'empirical' in text_lower:
        contribution.append('empirical')
    if 'artifact' in text_lower:
        contribution.append('artifact')
    if 'theoretical' in text_lower:
        contribution.append('theoretical')
    if 'survey' in text_lower:
        contribution.append('survey')
    if 'methodological' in text_lower or 'methodology' in text_lower:
        contribution.append('methodological')
    
    # Extract venue - look for common HCI venues
    venues = ['CHI', 'Ubicomp', 'CSCW', 'DIS', 'PervasiveHealth', 'WWW', 'IUI', 'OzCHI', 'TEI', 'AH', 'UbiComp']
    venue = []
    for v in venues:
        if v in text:
            venue.append(v)
    
    # Extract source/publisher
    sources = ['ACM', 'IEEE', 'PubMed']
    source = []
    for s in sources:
        if s in text:
            source.append(s)
    
    # Extract domain
    domains = ['food', 'physical activity', 'sleep', 'mental', 'finances', 'productivity', 'screen time', 
               'social interactions', 'location', 'chronic', 'diabetes', 'health behavior', 'fertility', 
               'pregnancy', 'exercise', 'weight', 'nutrition']
    domain = []
    for d in domains:
        if d.lower() in text_lower:
            domain.append(d)
    
    paper_data.append({
        'title': title,
        'year': year,
        'venue': venue,
        'source': source,
        'domain': domain,
        'contribution': contribution
    })

# Count papers extracted
print(f"__RESULT__:")
print(json.dumps({
    "total_papers": len(paper_data),
    "sample_papers": paper_data[:3]
}, indent=2))"""

env_args = {'var_functions.list_db:0': ['paper_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': [{'id': '1', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '4', 'citation_year': '2017'}, {'id': '2', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '95', 'citation_year': '2018'}, {'id': '3', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '32', 'citation_year': '2012'}, {'id': '4', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '29', 'citation_year': '2013'}, {'id': '5', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '18', 'citation_year': '2014'}], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json'}

exec(code, env_args)
