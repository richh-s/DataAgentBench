code = """import json
import re

# Load data
paper_docs_path = locals()['var_functions.query_db:2']
citations_path = locals()['var_functions.query_db:5']

with open(paper_docs_path, 'r') as f:
    paper_docs = json.load(f)

with open(citations_path, 'r') as f:
    citations = json.load(f)

# Analyze the data to understand what's available
years = {}
empirical_count = 0
total_count = 0

for doc in paper_docs:
    filename = doc.get('filename', '')
    title = filename.replace('.txt', '') if filename else ''
    text = doc.get('text', '')
    
    year_match = re.search(r'(20[0-2][0-9])', text[:2000])
    year = int(year_match.group(1)) if year_match else None
    
    text_lower = text.lower()
    has_empirical = bool(re.search(r'empirical|study|survey|interview|experiment|evaluation', text_lower))
    
    if year:
        years[year] = years.get(year, 0) + 1
        if has_empirical:
            empirical_count += 1
    
    total_count += 1

# Get citation stats
citations_by_title = {}
for citation in citations:
    cit_title = citation.get('title', '').lower()
    cit_count = int(citation.get('citation_count', 0))
    citations_by_title[cit_title] = citations_by_title.get(cit_title, 0) + cit_count

# Check papers after 2016
papers_after_2016 = []
for doc in paper_docs:
    filename = doc.get('filename', '')
    title = filename.replace('.txt', '') if filename else ''
    text = doc.get('text', '')
    
    year_match = re.search(r'(20[0-2][0-9])', text[:2000])
    year = int(year_match.group(1)) if year_match else None
    
    if year and year > 2016:
        papers_after_2016.append({
            'title': title,
            'year': year,
            'has_text': len(text) > 0
        })

results = {
    'total_papers': total_count,
    'papers_with_year': sum(years.values()),
    'empirical_papers': empirical_count,
    'years_distribution': dict(sorted(years.items())),
    'papers_after_2016': len(papers_after_2016),
    'citations_count': len(citations),
    'unique_cited_papers': len(citations_by_title)
}

print('__RESULT__:')
print(json.dumps(results))"""

env_args = {'var_functions.list_db:0': ['paper_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.list_db:6': ['Citations', 'sqlite_sequence'], 'var_functions.execute_python:16': [{'title': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App', 'total_citations': 0}], 'var_functions.execute_python:22': [{'title': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App', 'total_citations': 266}]}

exec(code, env_args)
