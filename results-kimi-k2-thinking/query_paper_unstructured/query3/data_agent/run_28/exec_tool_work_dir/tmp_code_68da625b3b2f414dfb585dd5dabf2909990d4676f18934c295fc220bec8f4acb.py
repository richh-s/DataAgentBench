code = """import json
import re

# Load paper documents
papers_file = locals()['var_functions.query_db:6']
with open(papers_file, 'r') as f:
    papers = json.load(f)

# Load citations
citations_file = locals()['var_functions.query_db:8']
with open(citations_file, 'r') as f:
    citations = json.load(f)

# Extract paper information
extracted_papers = []

for paper in papers:
    # Extract title from filename
    filename = paper['filename']
    title = filename.replace('.txt', '')
    
    # Extract year from text
    text = paper['text']
    year = None
    
    # Simple pattern: find 20xx in the document
    year_matches = re.findall(r"20\d{2}", text)
    if year_matches:
        # Take the first occurrence that's >= 2000
        for y in year_matches:
            year_int = int(y)
            if year_int >= 2000:
                year = year_int
                break
    
    # Check for empirical contribution
    text_lower = text.lower() if text else ""
    has_empirical = 'empirical' in text_lower or 'empirically' in text_lower
    
    extracted_papers.append({
        'title': title,
        'year': year,
        'has_empirical': has_empirical
    })

# Filter papers after 2016 with empirical contribution
filtered_papers = []
for p in extracted_papers:
    if p['has_empirical'] and p['year'] and p['year'] > 2016:
        filtered_papers.append(p)

# Sum citations by title
title_to_citations = {}
for citation in citations:
    title = citation['title']
    count = int(citation['citation_count'])
    title_to_citations[title] = title_to_citations.get(title, 0) + count

# Join papers with citations
results = []
for paper in filtered_papers:
    title = paper['title']
    if title in title_to_citations:
        results.append({
            'title': title,
            'total_citations': title_to_citations[title],
            'year': paper['year']
        })

# Sort by citation count
results.sort(key=lambda x: x['total_citations'], reverse=True)

output = {
    'papers_analyzed': len(papers),
    'citations_analyzed': len(citations),
    'empirical_papers_after_2016': len(results),
    'results': results
}

print('__RESULT__:')
print(json.dumps(output))"""

env_args = {'var_functions.list_db:0': ['paper_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.list_db:5': ['Citations', 'sqlite_sequence'], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.execute_python:12': 'file_storage/functions.execute_python:12.json', 'var_functions.execute_python:14': {'paper_count': 5, 'citation_count': 1405}, 'var_functions.execute_python:18': {'extracted': [{'_id': '694f5530284b10b11dc0a869', 'title': 'A Lived Informatics Model of Personal Informatics', 'year': 2005, 'has_empirical': False}, {'_id': '694f5530284b10b11dc0a86a', 'title': 'A Stage-based Model of Personal Informatics Systems', 'year': 2001, 'has_empirical': False}, {'_id': '694f5530284b10b11dc0a86b', 'title': 'A Trip to the Moon: Personalized Animated Movies for Self-reflection', 'year': 2000, 'has_empirical': True}, {'_id': '694f5530284b10b11dc0a86c', 'title': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App', 'year': 2000, 'has_empirical': True}, {'_id': '694f5530284b10b11dc0a86d', 'title': 'ArmSleeve: A Patient Monitoring System to Support Occupational Therapists in Stroke Rehabilitation', 'year': 2004, 'has_empirical': False}], 'count': 5}}

exec(code, env_args)
