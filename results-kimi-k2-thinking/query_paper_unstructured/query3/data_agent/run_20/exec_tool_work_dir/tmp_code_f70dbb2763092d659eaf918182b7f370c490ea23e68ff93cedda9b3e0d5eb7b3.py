code = """import json
import re

# Access file paths
paper_docs_file = locals()['var_functions.query_db:8']
citations_file = locals()['var_functions.query_db:10']

# Load data
with open(paper_docs_file, 'r') as f:
    paper_docs = json.load(f)

with open(citations_file, 'r') as f:
    citations = json.load(f)

# Function to extract paper info from text
def extract_paper_info(doc):
    filename = doc.get('filename', '')
    text = doc.get('text', '')
    
    # Extract title from filename
    title = filename.replace('.txt', '') if filename else ''
    
    # Extract year - look for patterns like 2017, '17, etc.
    year = None
    # Look in first 500 chars for year patterns
    header = text[:500]
    
    # Pattern 1: Full year like 2017, 2018, etc.
    year_match = re.search(r"(?:20)?1[7-9]|(?:20)?2[0-9]", header)
    if year_match:
        year_str = year_match.group()
        if len(year_str) == 2:
            year = int('20' + year_str)
        else:
            year = int(year_str)
    
    # Extract contribution type - look for keywords
    contribution = []
    text_lower = text.lower()
    
    if 'empirical' in text_lower:
        contribution.append('empirical')
    if 'artifact' in text_lower or 'system' in text_lower or 'prototype' in text_lower:
        contribution.append('artifact')
    if 'theoretical' in text_lower or 'theory' in text_lower:
        contribution.append('theoretical')
    if 'survey' in text_lower or 'review' in text_lower:
        contribution.append('survey')
    if 'methodological' in text_lower or 'method' in text_lower:
        contribution.append('methodological')
    
    return {
        'title': title,
        'year': year,
        'contribution': contribution
    }

# Extract info for all papers
papers_info = []
for doc in paper_docs:
    info = extract_paper_info(doc)
    if info['title']:  # Only include if we have a title
        papers_info.append(info)

# Filter for empirical papers after 2016
empirical_papers = [
    p for p in papers_info 
    if 'empirical' in p['contribution'] and p['year'] and p['year'] > 2016
]

# Get total citations per paper title
citation_totals = {}
for cit in citations:
    title = cit.get('title', '')
    count = int(cit.get('citation_count', 0))
    if title:
        citation_totals[title] = citation_totals.get(title, 0) + count

# Get results for empirical papers after 2016
results = []
for paper in empirical_papers:
    title = paper['title']
    total_citations = citation_totals.get(title, 0)
    results.append({
        'title': title,
        'total_citations': total_citations,
        'year': paper['year']
    })

# Sort by citations descending
results.sort(key=lambda x: x['total_citations'], reverse=True)

print('__RESULT__:')
print(json.dumps(results))"""

env_args = {'var_functions.list_db:0': ['paper_docs'], 'var_functions.list_db:1': ['Citations', 'sqlite_sequence'], 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json', 'var_functions.query_db:6': [{'id': '1', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '4', 'citation_year': '2017'}, {'id': '2', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '95', 'citation_year': '2018'}, {'id': '3', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '32', 'citation_year': '2012'}, {'id': '4', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '29', 'citation_year': '2013'}, {'id': '5', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '18', 'citation_year': '2014'}], 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json', 'var_functions.execute_python:14': {'total_papers': 5, 'total_citations': 1405, 'first_paper_title': 'A Lived Informatics Model of Personal Informatics.txt'}}

exec(code, env_args)
