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

# Extract paper information with improved year detection
extracted_papers = []

for paper in papers:
    # Extract title from filename
    filename = paper['filename']
    title = filename.replace('.txt', '')
    
    # Extract year from text using multiple patterns
    text = paper['text']
    year = None
    
    # Pattern 1: Look for venue year format like "UBICOMP '15, September 7-11, 2015"
    venue_pattern = r"[A-Z][a-zA-Z]*\s+'\d{2},[^\n]*\n[^\n]*(20\d{2})"
    venue_year_match = re.search(venue_pattern, text)
    if venue_year_match:
        year = int(venue_year_match.group(1))
    
    # Pattern 2: Look for copyright year
    if not year:
        copyright_match = re.search(r"Copyright[^\n]*20\d{2}", text)
        if copyright_match:
            year_match = re.search(r"20\d{2}", copyright_match.group(0))
            if year_match:
                year = int(year_match.group(0))
    
    # Pattern 3: Look for any 20xx year in the first few lines
    if not year:
        lines = text.split('\n')[:10]
        for line in lines:
            year_matches = re.findall(r"20\d{2}", line)
            if year_matches:
                year = int(year_matches[0])
                break
    
    # Check for empirical contribution
    text_lower = text.lower() if text else ""
    has_empirical = 'empirical' in text_lower or 'empirically' in text_lower
    
    extracted_papers.append({
        '_id': paper['_id'],
        'title': title,
        'year': year,
        'has_empirical': has_empirical
    })

# Filter papers: empirical contribution AND year > 2016
empirical_papers_after_2016 = [
    p for p in extracted_papers 
    if p['has_empirical'] and p['year'] and p['year'] > 2016
]

# Create a mapping of titles for easy lookup
title_to_paper = {p['title']: p for p in empirical_papers_after_2016}

# Group citations by title and sum them
citations_by_title = {}
for citation in citations:
    title = citation['title']
    count = int(citation['citation_count'])
    
    if title in title_to_paper:
        if title not in citations_by_title:
            citations_by_title[title] = 0
        citations_by_title[title] += count

# Prepare final results
results = []
for title, total_citations in citations_by_title.items():
    results.append({
        'title': title,
        'total_citations': total_citations,
        'year': title_to_paper[title]['year']
    })

# Sort by citation count (descending)
results.sort(key=lambda x: x['total_citations'], reverse=True)

# Print final results
output = {
    'filtered_papers': empirical_papers_after_2016,
    'citation_results': results,
    'summary': f'Found {len(results)} papers with empirical contributions after 2016'
}

print('__RESULT__:')
print(json.dumps(output, indent=2))"""

env_args = {'var_functions.list_db:0': ['paper_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.list_db:5': ['Citations', 'sqlite_sequence'], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.execute_python:12': 'file_storage/functions.execute_python:12.json', 'var_functions.execute_python:14': {'paper_count': 5, 'citation_count': 1405}, 'var_functions.execute_python:18': {'extracted': [{'_id': '694f5530284b10b11dc0a869', 'title': 'A Lived Informatics Model of Personal Informatics', 'year': 2005, 'has_empirical': False}, {'_id': '694f5530284b10b11dc0a86a', 'title': 'A Stage-based Model of Personal Informatics Systems', 'year': 2001, 'has_empirical': False}, {'_id': '694f5530284b10b11dc0a86b', 'title': 'A Trip to the Moon: Personalized Animated Movies for Self-reflection', 'year': 2000, 'has_empirical': True}, {'_id': '694f5530284b10b11dc0a86c', 'title': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App', 'year': 2000, 'has_empirical': True}, {'_id': '694f5530284b10b11dc0a86d', 'title': 'ArmSleeve: A Patient Monitoring System to Support Occupational Therapists in Stroke Rehabilitation', 'year': 2004, 'has_empirical': False}], 'count': 5}}

exec(code, env_args)
