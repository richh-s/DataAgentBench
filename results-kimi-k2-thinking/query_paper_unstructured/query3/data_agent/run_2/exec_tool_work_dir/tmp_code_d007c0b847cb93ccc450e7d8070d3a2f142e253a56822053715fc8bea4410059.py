code = """import json, re

# Load data
paper_docs_path = locals()['var_functions.query_db:2']
citations_path = locals()['var_functions.query_db:5']

with open(paper_docs_path, 'r') as f:
    paper_docs = json.load(f)

with open(citations_path, 'r') as f:
    citations = json.load(f)

# Find the paper(s) that match criteria
matching_papers = []

for doc in paper_docs:
    filename = doc.get('filename', '')
    title = filename.replace('.txt', '') if filename else ''
    full_text = doc.get('text', '')
    
    # Extract year
    year_match = re.search(r'(20[0-2][0-9])', full_text[:2000])
    year = int(year_match.group(1)) if year_match else None
    
    # Check for empirical contribution
    text_lower = full_text.lower()
    has_empirical = bool(re.search(r'empirical|study|survey|interview|experiment|evaluation', text_lower))
    
    if year and year > 2016 and has_empirical:
        # Calculate total citations
        title_lower = title.lower()
        total_citations = 0
        for citation in citations:
            if citation.get('title', '').lower() == title_lower:
                total_citations += int(citation.get('citation_count', 0))
        
        matching_papers.append({
            'title': title,
            'year': year,
            'total_citations': total_citations
        })

print('__RESULT__:')
print(json.dumps(matching_papers))"""

env_args = {'var_functions.list_db:0': ['paper_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.list_db:6': ['Citations', 'sqlite_sequence'], 'var_functions.execute_python:16': [{'title': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App', 'total_citations': 0}], 'var_functions.execute_python:22': [{'title': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App', 'total_citations': 266}], 'var_functions.execute_python:24': {'total_papers': 5, 'papers_with_year': 2, 'empirical_papers': 2, 'years_distribution': {'2015': 1, '2019': 1}, 'papers_after_2016': 1, 'citations_count': 1405, 'unique_cited_papers': 259}}

exec(code, env_args)
