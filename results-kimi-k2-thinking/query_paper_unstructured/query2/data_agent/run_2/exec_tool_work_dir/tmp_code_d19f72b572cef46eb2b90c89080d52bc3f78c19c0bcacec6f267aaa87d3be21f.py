code = """import json

# Load the citations data for 2018
citations_path = locals()['var_functions.query_db:0']
with open(citations_path, 'r') as f:
    citations_2018 = json.load(f)

# Load the paper documents
paper_docs_path = locals()['var_functions.query_db:2']
with open(paper_docs_path, 'r') as f:
    paper_docs = json.load(f)

# Create a mapping of paper titles to source/publisher information
paper_source_mapping = {}
for doc in paper_docs:
    filename = doc.get('filename', '')
    if filename.endswith('.txt'):
        title = filename[:-4]  # Remove .txt extension
        text = doc.get('text', '')
        
        # Extract source/publisher from the text (look for ACM, IEEE, PubMed mentions)
        source = None
        if 'ACM' in text or 'ACM Classification' in text or 'permissions@acm.org' in text:
            source = 'ACM'
        elif 'IEEE' in text:
            source = 'IEEE'
        elif 'PubMed' in text:
            source = 'PubMed'
        
        if source:
            paper_source_mapping[title] = source

# Find papers published by ACM that were cited in 2018
acm_citations = []
for citation in citations_2018:
    title = citation.get('title', '')
    if title in paper_source_mapping and paper_source_mapping[title] == 'ACM':
        acm_citations.append(int(citation.get('citation_count', 0)))

# Calculate average citation count
average_citations = sum(acm_citations) / len(acm_citations) if acm_citations else 0

result = {
    'total_acm_papers_cited_in_2018': len(acm_citations),
    'average_citation_count': round(average_citations, 2),
    'acm_citation_counts': acm_citations
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json'}

exec(code, env_args)
