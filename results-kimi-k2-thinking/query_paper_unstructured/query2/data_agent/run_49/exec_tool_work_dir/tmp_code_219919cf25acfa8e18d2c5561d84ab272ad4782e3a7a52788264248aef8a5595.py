code = """import json
import re

# Load the 2018 citations data
citations_file = locals()['var_functions.query_db:0']
if isinstance(citations_file, str):
    with open(citations_file, 'r') as f:
        citations_data = json.load(f)
else:
    citations_data = citations_file

# Load the paper documents
papers_file = locals()['var_functions.query_db:5']
if isinstance(papers_file, str):
    with open(papers_file, 'r') as f:
        papers_data = json.load(f)
else:
    papers_data = papers_file

# Let's examine the structure more carefully
print("Examining citation titles structure:")
for i in range(min(5, len(citations_data))):
    print(f"  {i}: '{citations_data[i]['title']}'")

print("\nExamining paper document structure:")
for i in range(min(3, len(papers_data))):
    paper = papers_data[i]
    filename = paper.get('filename', 'NO FILENAME')
    has_text = 'text' in paper
    print(f"  {i}: filename='{filename}', has_text={has_text}")

# Let's try to extract title from the text content itself
print("\nTrying to extract titles from text content:")
for i in range(min(3, len(papers_data))):
    paper = papers_data[i]
    text = paper.get('text', '')
    
    # Try to find title patterns
    # Usually titles are at the beginning, in uppercase, and separated from authors
    lines = text.split('\n')
    potential_title = []
    
    for line in lines[:20]:  # Check first 20 lines
        stripped = line.strip()
        if stripped and not stripped.startswith('Permission') and not stripped.startswith('Author Keywords'):
            # Look for all caps or title case patterns
            if len(stripped) > 10 and (stripped.isupper() or (stripped[0].isupper() and len(stripped.split()) > 2)):
                potential_title.append(stripped)
                break
    
    print(f"  {i}: potential_title='{potential_title[0] if potential_title else 'NOT FOUND'}'")

# Let's also check for ACM patterns
print("\nChecking for ACM patterns in first paper:")
first_paper_text = papers_data[0].get('text', '').lower()
acm_indicators = []

if 'acm' in first_paper_text:
    acm_indicators.append("'acm' found")
    
if 'association for computing machinery' in first_paper_text:
    acm_indicators.append("'association for computing machinery' found")
    
# Check for copyright patterns
copyright_patterns = ['copyright', 'acm', 'association for computing machinery']
found_patterns = []
for pattern in copyright_patterns:
    if pattern in first_paper_text:
        found_patterns.append(pattern)

print(f"  Found patterns: {found_patterns}")

result = {
    'sample_citation_titles': [c['title'] for c in citations_data[:5]],
    'sample_paper_filenames': [p.get('filename') for p in papers_data[:5]],
    'total_citations': len(citations_data),
    'total_papers': len(papers_data)
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.list_db:2': ['paper_docs'], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.execute_python:18': {'acm_papers_count': 2, 'total_2018_citations': 158, 'missing_papers': 156, 'average_citations': 68.5, 'total_citations_for_acm_papers': 137}}

exec(code, env_args)
