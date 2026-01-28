code = """import json
import re

# Get variables from storage
citations_path = locals()['var_functions.query_db:38']
papers_path = locals()['var_functions.query_db:28']

print('Paths loaded')

# Load citations (small sample first)
with open(citations_path, 'r') as f:
    citations = json.load(f)

print('Citations loaded:', len(citations))

# Load papers
with open(papers_path, 'r') as f:
    papers = json.load(f)

print('Papers loaded:', len(papers))

# Check for recent papers
recent_papers = []
for p in papers:
    text = p.get('text', '')
    if not text:
        continue
    
    # Find years
    years = re.findall(r'(20\d{2})', text[:3000])
    if years:
        year = int(max(years))  # Take the largest year found
        if year > 2016:
            title = p.get('filename', '').replace('.txt', '')
            recent_papers.append({'title': title, 'year': year, 'text': text})

print('Recent papers found:', len(recent_papers))

# Find empirical ones
empirical_papers = []
for paper in recent_papers:
    if 'empirical' in paper['text'].lower():
        empirical_papers.append(paper)

print('Empirical papers after 2016:', len(empirical_papers))

# Get citation counts
titles_with_citations = {c['title']: int(c['total_citations']) for c in citations}

# Build results
results = []
for paper in empirical_papers:
    title = paper['title']
    if title in titles_with_citations:
        results.append({
            'title': title,
            'total_citations': titles_with_citations[title]
        })

print('Final results:', len(results))

# Sort and format
results.sort(key=lambda x: x['total_citations'], reverse=True)

# Output
print('__RESULT__:')
print(json.dumps(results, indent=2))"""

env_args = {'var_functions.list_db:0': ['paper_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': [{'id': '1', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '4', 'citation_year': '2017'}, {'id': '2', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '95', 'citation_year': '2018'}, {'id': '3', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '32', 'citation_year': '2012'}, {'id': '4', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '29', 'citation_year': '2013'}, {'id': '5', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '18', 'citation_year': '2014'}, {'id': '6', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '95', 'citation_year': '2015'}, {'id': '7', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '14', 'citation_year': '2016'}, {'id': '8', 'title': 'Sundroid: Solar Radiation Awareness with Smartphones', 'citation_count': '12', 'citation_year': '2012'}, {'id': '9', 'title': 'Sundroid: Solar Radiation Awareness with Smartphones', 'citation_count': '76', 'citation_year': '2013'}, {'id': '10', 'title': 'Sundroid: Solar Radiation Awareness with Smartphones', 'citation_count': '55', 'citation_year': '2014'}], 'var_functions.query_db:26': 'file_storage/functions.query_db:26.json', 'var_functions.query_db:28': 'file_storage/functions.query_db:28.json', 'var_functions.execute_python:32': [], 'var_functions.query_db:38': 'file_storage/functions.query_db:38.json', 'var_functions.execute_python:40': []}

exec(code, env_args)
