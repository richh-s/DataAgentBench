code = """import json
import re

# Load paper documents
with open(locals()['var_functions.query_db:2'], 'r') as f:
    paper_docs = json.load(f)

print('Total papers:', len(paper_docs))

# First, let's understand domain patterns in these papers
# Check a few papers to see how domains are represented
for i in range(min(10, len(paper_docs))):
    doc = paper_docs[i]
    text = doc.get('text', '').lower()[:2000]
    
    # Look for domain-related keywords
    keywords = ['physical activity', 'fitness', 'exercise', 'food', 'sleep', 'mental', 'finances', 'location']
    
    found = []
    for kw in keywords:
        if kw in text:
            found.append(kw)
    
    if found:
        print(f"\nPaper {i}: {doc.get('filename')}")
        print(f"  Domains: {found}")
        print(f"  First 200 chars: {doc.get('text', '')[:200]}...")

# Now let's try to identify all papers in physical activity domain
physical_activity_papers = []

domain_terms = [
    'physical activity',
    'fitness',
    'exercise', 
    'walking',
    'running',
    'steps',
    'step count',
    'activity tracker',
    'activity tracking',
    'wearable',
    'wearables'
]

for doc in paper_docs:
    text_lower = doc.get('text', '').lower()
    filename = doc.get('filename', '')
    title = filename.replace('.txt', '')
    
    # Check for physical activity domain
    has_domain = any(term in text_lower for term in domain_terms)
    
    if has_domain:
        # Extract year - look for publication year patterns
        year_match = re.search(r'(20\d{2})', text_lower)
        year = int(year_match.group()) if year_match else None
        
        physical_activity_papers.append({
            'title': title,
            'year': year
        })

print(f"\n\nFound {len(physical_activity_papers)} papers in physical activity domain")
print("Year distribution:")
year_counts = {}
for paper in physical_activity_papers:
    year = paper['year']
    year_counts[year] = year_counts.get(year, 0) + 1

for year in sorted(year_counts.keys()):
    if year is not None:
        print(f"  {year}: {year_counts[year]}")

# Filter for 2016
papers_2016 = [p for p in physical_activity_papers if p['year'] == 2016]
print(f"\n2016 physical activity papers: {len(papers_2016)}")
for p in papers_2016:
    print(f"  - {p['title']}")

print('\n__RESULT__:')
print(json.dumps([p['title'] for p in papers_2016]))"""

env_args = {'var_functions.list_db:0': ['paper_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.execute_python:8': [], 'var_functions.list_db:10': ['Citations', 'sqlite_sequence'], 'var_functions.query_db:12': [{'id': '1', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '4', 'citation_year': '2017'}, {'id': '2', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '95', 'citation_year': '2018'}, {'id': '3', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '32', 'citation_year': '2012'}, {'id': '4', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '29', 'citation_year': '2013'}, {'id': '5', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '18', 'citation_year': '2014'}, {'id': '6', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '95', 'citation_year': '2015'}, {'id': '7', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '14', 'citation_year': '2016'}, {'id': '8', 'title': 'Sundroid: Solar Radiation Awareness with Smartphones', 'citation_count': '12', 'citation_year': '2012'}, {'id': '9', 'title': 'Sundroid: Solar Radiation Awareness with Smartphones', 'citation_count': '76', 'citation_year': '2013'}, {'id': '10', 'title': 'Sundroid: Solar Radiation Awareness with Smartphones', 'citation_count': '55', 'citation_year': '2014'}], 'var_functions.query_db:15': 'file_storage/functions.query_db:15.json', 'var_functions.execute_python:18': [], 'var_functions.execute_python:24': ['A Trip to the Moon: Personalized Animated Movies for Self-reflection', 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App'], 'var_functions.execute_python:28': [{'title': 'A Trip to the Moon: Personalized Animated Movies for Self-reflection', 'total_citation_count': 265}, {'title': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App', 'total_citation_count': 266}, {'title': 'ArmSleeve: A Patient Monitoring System to Support Occupational Therapists in Stroke Rehabilitation', 'total_citation_count': 452}]}

exec(code, env_args)
