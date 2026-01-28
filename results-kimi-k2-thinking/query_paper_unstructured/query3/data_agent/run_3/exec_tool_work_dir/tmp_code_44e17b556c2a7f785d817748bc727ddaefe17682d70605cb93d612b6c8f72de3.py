code = """import json
import re

# Load paper documents
with open('/tmp/tmp8q6u6mry.json', 'r') as f:
    paper_docs = json.load(f)

print('Loaded', len(paper_docs), 'papers')

# Function to extract paper info
def extract_info(doc):
    filename = doc.get('filename', '')
    text = doc.get('text', '')
    title = filename.replace('.txt', '')
    
    # Find year in text (look for 4-digit numbers, usually near the beginning)
    year_match = re.search(r'(\d{4})', text[:2000])
    year = int(year_match.group(1)) if year_match else None
    
    # Check if empirical (simple keyword search)
    is_empirical = 'empirical' in text.lower()
    
    return {'title': title, 'year': year, 'is_empirical': is_empirical}

# Filter papers: empirical and after 2016
filtered_papers = []
for doc in paper_docs:
    info = extract_info(doc)
    if info['year'] and info['year'] > 2016 and info['is_empirical']:
        filtered_papers.append(info)

print('Filtered to', len(filtered_papers), 'empirical papers after 2016')

titles = [p['title'] for p in filtered_papers]
print('Sample titles:', titles[:3])

# Access citations data from storage
citations = [
  {"id": "1", "title": "Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing", "citation_count": "4", "citation_year": "2017"}, 
  {"id": "2", "title": "Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing", "citation_count": "95", "citation_year": "2018"}, 
  {"id": "3", "title": "Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies", "citation_count": "32", "citation_year": "2012"}, 
  {"id": "4", "title": "Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies", "citation_count": "29", "citation_year": "2013"}, 
  {"id": "5", "title": "Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies", "citation_count": "18", "citation_year": "2014"}, 
  {"id": "6", "title": "Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies", "citation_count": "95", "citation_year": "2015"}, 
  {"id": "7", "title": "Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies", "citation_count": "14", "citation_year": "2016"}, 
  {"id": "8", "title": "Sundroid: Solar Radiation Awareness with Smartphones", "citation_count": "12", "citation_year": "2012"}, 
  {"id": "9", "title": "Sundroid: Solar Radiation Awareness with Smartphones", "citation_count": "76", "citation_year": "2013"}, 
  {"id": "10", "title": "Sundroid: Solar Radiation Awareness with Smartphones", "citation_count": "55", "citation_year": "2014"}
]

# Aggregate citation counts
citation_counts = {}
for cit in citations:
    if cit['title'] in titles:
        citation_counts[cit['title']] = citation_counts.get(cit['title'], 0) + int(cit['citation_count'])

print('Papers with citations:', len(citation_counts))

# Prepare results
results = []
for paper in filtered_papers:
    total_citations = citation_counts.get(paper['title'], 0)
    if total_citations > 0:  # Only include papers with citations
        results.append({'title': paper['title'], 'total_citations': total_citations})

results.sort(key=lambda x: x['total_citations'], reverse=True)

print('Top results:')
for r in results[:10]:
    print(r['title'][:50], '-', r['total_citations'])

# Output in required format
print("__RESULT__:")
print(json.dumps(results))"""

env_args = {'var_functions.list_db:0': ['paper_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': [{'id': '1', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '4', 'citation_year': '2017'}, {'id': '2', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '95', 'citation_year': '2018'}, {'id': '3', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '32', 'citation_year': '2012'}, {'id': '4', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '29', 'citation_year': '2013'}, {'id': '5', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '18', 'citation_year': '2014'}, {'id': '6', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '95', 'citation_year': '2015'}, {'id': '7', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '14', 'citation_year': '2016'}, {'id': '8', 'title': 'Sundroid: Solar Radiation Awareness with Smartphones', 'citation_count': '12', 'citation_year': '2012'}, {'id': '9', 'title': 'Sundroid: Solar Radiation Awareness with Smartphones', 'citation_count': '76', 'citation_year': '2013'}, {'id': '10', 'title': 'Sundroid: Solar Radiation Awareness with Smartphones', 'citation_count': '55', 'citation_year': '2014'}]}

exec(code, env_args)
