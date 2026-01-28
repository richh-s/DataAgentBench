code = """import json

# Load data
citations_path = "var_functions.query_db:16"
try:
    with open(citations_path, 'r') as f:
        citations_2020 = json.load(f)
except Exception as e:
    print('Error loading citations:', e)
    citations_2020 = []

papers_path = "var_functions.query_db:2"
try:
    with open(papers_path, 'r') as f:
        papers = json.load(f)
except Exception as e:
    print('Error loading papers:', e)
    papers = []

# Find CHI papers by checking text content
chi_titles = set()
for paper in papers:
    text = paper.get('text', '')
    # Check if CHI appears in first 1000 chars (likely header)
    header = text[:1000].upper()
    # Look for CHI with year markers
    if 'CHI' in header and ('20' in header or "'" in header):
        # Additional check: look for common conference markers
        if any(marker in text[:1000] for marker in ['Proceedings', 'ACM', 'Conference', 'paper', 'Paper', 'ISBN']):
            filename = paper.get('filename', '')
            title = filename.replace('.txt', '')
            chi_titles.add(title.lower())

# Count citations
total_citations = 0
chi_citation_count = 0
for cite in citations_2020:
    cite_title = cite.get('title', '')
    if cite_title:
        if cite_title.lower() in chi_titles:
            total_citations += int(cite.get('citation_count', 0))
            chi_citation_count += 1

result = {
    'total_citation_count_for_chi_papers in 2020': total_citations,
    'number_of_chi_papers_with_citations': chi_citation_count,
    'total_chi_papers_identified': len(chi_titles)
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:16': 'file_storage/functions.query_db:16.json', 'var_functions.execute_python:20': {'total_citations_from_chi_papers_in_2020': 0}}

exec(code, env_args)
