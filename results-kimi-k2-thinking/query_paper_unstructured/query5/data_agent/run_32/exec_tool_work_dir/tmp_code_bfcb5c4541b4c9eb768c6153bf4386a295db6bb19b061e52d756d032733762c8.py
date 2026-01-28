code = """import json

# Load citations data
citations_path = "var_functions.query_db:16"
with open(citations_path, 'r') as f:
    citations_2020 = json.load(f)

# Load papers data  
papers_path = "var_functions.query_db:2"
with open(papers_path, 'r') as f:
    papers = json.load(f)

# Get all paper titles from citations
citation_titles = set()
for cite in citations_2020:
    title = cite.get('title', '')
    if title:
        citation_titles.add(title.lower())

# Find CHI papers from the documents
chi_papers = []
for paper in papers:
    filename = paper.get('filename', '')
    title = filename.replace('.txt', '')
    text = paper.get('text', '')
    
    # Check if this is a CHI paper by looking for CHI in text
    if 'CHI' in text[:2000]:
        chi_papers.append(title.lower())

# Calculate citations for CHI papers
total_citations = 0
for cite in citations_2020:
    cite_title = cite.get('title', '')
    if cite_title and cite_title.lower() in chi_papers:
        total_citations += int(cite.get('citation_count', 0))

result = {
    'total_citation_count': total_citations
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:16': 'file_storage/functions.query_db:16.json', 'var_functions.execute_python:20': {'total_citations_from_chi_papers_in_2020': 0}, 'var_functions.execute_python:24': {'total_citation_count_for_chi_papers in 2020': 0, 'number_of_chi_papers_with_citations': 0, 'total_chi_papers_identified': 0}}

exec(code, env_args)
