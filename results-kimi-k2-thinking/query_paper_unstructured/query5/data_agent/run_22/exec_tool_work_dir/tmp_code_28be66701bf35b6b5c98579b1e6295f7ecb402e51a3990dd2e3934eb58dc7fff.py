code = """import json
import re

# Load the citations data (this is stored as a file path for large results)
citations_file = locals()['var_functions.query_db:5']
print(f"Citations file path: {citations_file}")

# Load the paper documents data
paper_docs_file = locals()['var_functions.query_db:6']
print(f"Paper docs file path: {paper_docs_file}")

# Try to load the data
try:
    with open(citations_file, 'r') as f:
        citations_data = json.load(f)
    print(f"Loaded {len(citations_data)} citation records")
    
    with open(paper_docs_file, 'r') as f:
        paper_docs_data = json.load(f)
    print(f"Loaded {len(paper_docs_data)} paper documents")
    
    # Extract CHI papers
    chi_papers = []
    for paper in paper_docs_data:
        text = paper.get('text', '')
        if 'CHI' in text.upper():
            filename = paper.get('filename', '')
            title = filename.replace('.txt', '') if filename else ''
            chi_papers.append(title)
    
    print(f"Found {len(chi_papers)} CHI papers")
    
    # Create a set for fast lookup
    chi_titles = set(chi_papers)
    
    # Find citations for CHI papers in 2020
    total_citations = 0
    chi_citations = []
    
    for citation in citations_data:
        title = citation.get('title', '')
        if title in chi_titles:
            count = int(citation.get('citation_count', 0))
            total_citations += count
            chi_citations.append({'title': title, 'citation_count': count})
    
    print(f"Total citations for CHI papers in 2020: {total_citations}")
    print(f"Number of CHI papers cited in 2020: {len(chi_citations)}")
    
    # Sort by citation count
    chi_citations.sort(key=lambda x: x['citation_count'], reverse=True)
    
    # Print top 10
    print("\nTop CHI papers by citations in 2020:")
    for i, paper in enumerate(chi_citations[:10], 1):
        print(f"{i}. {paper['title']}: {paper['citation_count']} citations")
    
    result = {
        'total_citations': total_citations,
        'num_papers': len(chi_citations),
        'papers': chi_citations
    }
    
    print("__RESULT__:")
    print(json.dumps(result))
    
except Exception as e:
    print(f"Error loading data: {e}")"""

env_args = {'var_functions.list_db:0': ['paper_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json'}

exec(code, env_args)
