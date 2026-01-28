code = """import json
import re

# Load data from files
citations_path = locals()['var_functions.query_db:26']
with open(citations_path, 'r') as f:
    citations = json.load(f)

paper_docs_path = locals()['var_functions.query_db:28']
with open(paper_docs_path, 'r') as f:
    paper_docs = json.load(f)

print('Loaded', len(citations), 'citation records and', len(paper_docs), 'paper documents')

# Extract info from papers
empirical_papers = []
for doc in paper_docs:
    text = doc.get('text', '')
    filename = doc.get('filename', '')
    if not text or not filename:
        continue
    
    title = filename.replace('.txt', '')
    
    # Extract year from first 2000 chars
    text_start = text[:2000]
    year_match = re.search(r'(\b20\d{2}\b)', text_start)
    year = int(year_match.group(1)) if year_match else None
    
    # Check if empirical
    empirical = 'empirical' in text.lower()
    
    if year and year > 2016 and empirical:
        empirical_papers.append({'title': title})

print('Found', len(empirical_papers), 'empirical papers after 2016')

# Create citation lookup
citation_lookup = {}
for cit in citations:
    citation_lookup[cit['title']] = int(cit['total_citations'])

# Match and get results
results = []
for paper in empirical_papers:
    title = paper['title']
    if title in citation_lookup:
        results.append({'title': title, 'total_citations': citation_lookup[title]})

# Sort by citations
results.sort(key=lambda x: x['total_citations'], reverse=True)

print('Final results count:', len(results))
print('Top 5:')
for i, r in enumerate(results[:5]):
    print(i+1, r['title'][:60] + '...', r['total_citations'])

# Output
print('__RESULT__:')
print(json.dumps(results))"""

env_args = {'var_functions.list_db:0': ['paper_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': [{'id': '1', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '4', 'citation_year': '2017'}, {'id': '2', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '95', 'citation_year': '2018'}, {'id': '3', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '32', 'citation_year': '2012'}, {'id': '4', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '29', 'citation_year': '2013'}, {'id': '5', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '18', 'citation_year': '2014'}, {'id': '6', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '95', 'citation_year': '2015'}, {'id': '7', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '14', 'citation_year': '2016'}, {'id': '8', 'title': 'Sundroid: Solar Radiation Awareness with Smartphones', 'citation_count': '12', 'citation_year': '2012'}, {'id': '9', 'title': 'Sundroid: Solar Radiation Awareness with Smartphones', 'citation_count': '76', 'citation_year': '2013'}, {'id': '10', 'title': 'Sundroid: Solar Radiation Awareness with Smartphones', 'citation_count': '55', 'citation_year': '2014'}], 'var_functions.query_db:26': 'file_storage/functions.query_db:26.json', 'var_functions.query_db:28': 'file_storage/functions.query_db:28.json'}

exec(code, env_args)
