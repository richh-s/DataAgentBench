code = """import json
import re

# Load data
with open('file_storage/functions.query_db:2.json', 'r') as f:
    paper_docs = json.load(f)

with open('file_storage/functions.query_db:5.json', 'r') as f:
    citations = json.load(f)

# Let's examine the papers more carefully
papers = []
for doc in paper_docs:
    filename = doc.get('filename', '')
    text = doc.get('text', '')
    
    title = filename.replace('.txt', '')
    
    # Extract year more comprehensively
    year = None
    year_matches = re.findall(r'(19|20)\d{2}', text)
    if year_matches:
        year = int(year_matches[0])
    
    # Check for various contribution types
    text_lower = text.lower()
    is_empirical = 'empirical' in text_lower
    is_theoretical = 'theoretical' in text_lower
    is_survey = 'survey' in text_lower
    
    papers.append({
        'title': title,
        'year': year,
        'is_empirical': is_empirical,
        'has_year': year is not None
    })

# Filter papers by year
papers_by_year = {}
for p in papers:
    if p['year']:
        if p['year'] not in papers_by_year:
            papers_by_year[p['year']] = []
        papers_by_year[p['year']].append(p)

# Get empirical papers after 2016
empirical_after_2016 = [p for p in papers if p['is_empirical'] and p['year'] and p['year'] > 2016]

result = {
    'total_papers': len(papers),
    'papers_with_year': len([p for p in papers if p['year']]),
    'year_distribution': {year: len(papers) for year, papers in papers_by_year.items()},
    'empirical_papers': len([p for p in papers if p['is_empirical']]),
    'empirical_by_year': {},
    'empirical_after_2016': len(empirical_after_2016),
    'empirical_after_2016_list': empirical_after_2016
}

# Count empirical papers by year
for p in papers:
    if p['is_empirical'] and p['year']:
        year = p['year']
        if year not in result['empirical_by_year']:
            result['empirical_by_year'][year] = 0
        result['empirical_by_year'][year] += 1

# If no papers after 2016, check if we should relax criteria
all_titles = [p['title'] for p in papers]
citations_by_title = {}
for cit in citations:
    title = cit.get('title', '')
    if title in all_titles:
        count = int(cit.get('citation_count', 0))
        if title not in citations_by_title:
            citations_by_title[title] = 0
        citations_by_title[title] += count

result['total_citations_found'] = len(citations_by_title)

print('__RESULT__:')
print(json.dumps(result, indent=2))"""

env_args = {'var_functions.list_db:0': ['paper_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.execute_python:14': {'paper_docs_type': "<class 'str'>", 'citations_type': "<class 'str'>", 'paper_docs_is_str': True, 'citations_is_str': True, 'paper_docs_preview': 'file_storage/functions.query_db:2.json', 'citations_preview': 'file_storage/functions.query_db:5.json'}, 'var_functions.execute_python:16': {'paper_docs_loaded': 5, 'citations_loaded': 1405}, 'var_functions.execute_python:20': []}

exec(code, env_args)
