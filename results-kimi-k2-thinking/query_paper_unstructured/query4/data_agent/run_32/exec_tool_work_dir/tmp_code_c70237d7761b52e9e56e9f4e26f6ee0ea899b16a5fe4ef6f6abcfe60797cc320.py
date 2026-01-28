code = """import json, re

# Access stored results using locals()
paper_docs_file = locals()['var_functions.query_db:2']
citation_data = locals()['var_functions.query_db:5']

# Load paper documents
with open(paper_docs_file, 'r') as f:
    paper_docs = json.load(f)

# Extract paper information
paper_info = []
for doc in paper_docs:
    filename = doc['filename']
    text = doc['text']
    
    title = filename.replace('.txt', '')
    
    # Extract year
    year_match = re.search(r'(\b(20|19)\d{2}\b)', text)
    year = int(year_match.group(1)) if year_match else None
    
    # Extract venue
    venues = ['CHI', 'Ubicomp', 'UbiComp', 'CSCW', 'DIS', 'PervasiveHealth', 'WWW', 'IUI', 'OzCHI', 'TEI', 'AH']
    venue = None
    for v in venues:
        if v.lower() in text.lower():
            venue = v
            break
    
    # Extract domains
    domains = ['physical activity', 'food', 'sleep', 'mental', 'finances', 'productivity', 'screen time', 'social interactions', 'location', 'chronic', 'diabetes', 'health_behavior']
    domain_list = []
    for d in domains:
        if d.lower() in text.lower():
            domain_list.append(d)
    
    paper_info.append({
        'title': title,
        'year': year,
        'venue': venue,
        'domains': domain_list
    })

# Filter papers from 2016 in physical activity domain
papers_2016 = [p for p in paper_info if p['year'] == 2016 and 'physical activity' in p['domains']]

# Calculate total citations for these papers
citation_total = {}
for paper in papers_2016:
    citation_total[paper['title']] = 0

# Sum up citations
for citation in citation_data:
    title = citation['title']
    count = int(citation['citation_count'])
    if title in citation_total:
        citation_total[title] += count

# Prepare result
result = []
for title, total in citation_total.items():
    result.append({'title': title, 'total_citations': total})

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['paper_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': [{'id': '1', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '4', 'citation_year': '2017'}, {'id': '2', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '95', 'citation_year': '2018'}, {'id': '3', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '32', 'citation_year': '2012'}, {'id': '4', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '29', 'citation_year': '2013'}, {'id': '5', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '18', 'citation_year': '2014'}]}

exec(code, env_args)
