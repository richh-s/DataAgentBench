code = """import json
import re

# Load paper documents from the file
with open('/tmp/tmp8q6u6mry.json', 'r') as f:
    paper_docs = json.load(f)

print('Successfully loaded', len(paper_docs), 'papers')

# Function to extract paper information from text

def extract_paper_info(doc):
    text = doc.get('text', '')
    filename = doc.get('filename', '')
    
    # Extract title from filename
    title = filename.replace('.txt', '')
    
    # Extract year from text
    year_match = re.search(r'(\d{4})', text[:2000])  # Look in first 2000 chars
    year = int(year_match.group(0)) if year_match else None
    
    # Check if contribution type is empirical
    # Look for empirical in various parts of the text
    contribution_types = ['empirical']
    contribution_text = text.lower()
    
    is_empirical = any(ct in contribution_text for ct in contribution_types)
    
    return {
        'title': title,
        'year': year,
        'filename': filename,
        'is_empirical': is_empirical
    }

# Process all papers
processed_papers = []
for doc in paper_docs:
    info = extract_paper_info(doc)
    if info['year'] and info['year'] > 2016 and info['is_empirical']:
        processed_papers.append(info)

print('Found', len(processed_papers), 'empirical papers after 2016')

# Save the titles for joining with citations
titles = [p['title'] for p in processed_papers]

print('\nSample titles (first 5):')
for t in titles[:5]:
    print(t)

# Load all citations to aggregate counts
citations = locals()['var_functions.query_db:5']

# Aggregate citation counts by title
citation_counts = {}
for cit in citations:
    if cit['title'] in titles:
        citation_counts[cit['title']] = citation_counts.get(cit['title'], 0) + int(cit['citation_count'])

print('\nNumber of papers with citations:', len(citation_counts))

# Prepare final results
results = []
for paper in processed_papers:
    total_citations = citation_counts.get(paper['title'], 0)
    results.append({
        'title': paper['title'],
        'total_citations': total_citations
    })

# Sort by citation count descending
results.sort(key=lambda x: x['total_citations'], reverse=True)

print('\nTop 10 results:')
for r in results[:10]:
    print(f"{r['title'][:50]}... - {r['total_citations']} citations")

# Return final results
import json as js
__RESULT__ = js.dumps(results)
print('__RESULT__:')
print(__RESULT__)"""

env_args = {'var_functions.list_db:0': ['paper_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': [{'id': '1', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '4', 'citation_year': '2017'}, {'id': '2', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '95', 'citation_year': '2018'}, {'id': '3', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '32', 'citation_year': '2012'}, {'id': '4', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '29', 'citation_year': '2013'}, {'id': '5', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '18', 'citation_year': '2014'}, {'id': '6', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '95', 'citation_year': '2015'}, {'id': '7', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '14', 'citation_year': '2016'}, {'id': '8', 'title': 'Sundroid: Solar Radiation Awareness with Smartphones', 'citation_count': '12', 'citation_year': '2012'}, {'id': '9', 'title': 'Sundroid: Solar Radiation Awareness with Smartphones', 'citation_count': '76', 'citation_year': '2013'}, {'id': '10', 'title': 'Sundroid: Solar Radiation Awareness with Smartphones', 'citation_count': '55', 'citation_year': '2014'}]}

exec(code, env_args)
