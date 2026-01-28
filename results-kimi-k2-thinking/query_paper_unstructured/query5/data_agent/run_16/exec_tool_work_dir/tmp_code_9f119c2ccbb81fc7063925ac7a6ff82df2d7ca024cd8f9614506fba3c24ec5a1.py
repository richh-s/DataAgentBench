code = """import json

# Access the stored results using the provided keys
citations_key = 'functions.query_db:6'
paper_docs_key = 'functions.query_db:2'

# Get the results from locals()
citations_result = locals().get(citations_key)
paper_docs_result = locals().get(paper_docs_key)

# Check if they're file paths
if isinstance(citations_result, str) and citations_result.endswith('.json'):
    with open(citations_result, 'r') as f:
        citations_data = json.load(f)
else:
    citations_data = citations_result

if isinstance(paper_docs_result, str) and paper_docs_result.endswith('.json'):
    with open(paper_docs_result, 'r') as f:
        paper_docs_data = json.load(f)
else:
    paper_docs_data = paper_docs_result

# Process data to extract CHI papers
citation_titles = [c['title'] for c in citations_data]

# Extract CHI papers from paper docs
chi_papers = []
for doc in paper_docs_data:
    text = doc.get('text', '')
    filename = doc.get('filename', '')
    # Check if this is a CHI paper
    if 'CHI' in text or 'chi' in filename.lower():
        title = filename.replace('.txt', '')
        chi_papers.append(title)

# Find CHI papers in citations data
chi_citations = []
for citation in citations_data:
    title = citation['title']
    if title in chi_papers:
        chi_citations.append({
            'title': title,
            'citation_count': int(citation['citation_count'])
        })

# Calculate total citations
total_citations = sum(c['citation_count'] for c in chi_citations)

# Print result in required format
result = {
    'total_citations': total_citations,
    'chi_papers_count': len(chi_citations)
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['paper_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json'}

exec(code, env_args)
