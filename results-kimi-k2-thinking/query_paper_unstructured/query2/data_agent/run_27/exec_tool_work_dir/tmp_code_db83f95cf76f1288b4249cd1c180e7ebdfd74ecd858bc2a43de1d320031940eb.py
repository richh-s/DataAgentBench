code = """import json
import re

# Access the stored results using locals()
citations_result = locals()['var_functions.query_db:0']
papers_result = locals()['var_functions.query_db:2']

# Load the JSON data
citations_data = json.load(open(citations_result))
papers_data = json.load(open(papers_result))

# Create a dictionary to store paper title to source mapping
paper_sources = {}

# Extract source from each paper document
for paper in papers_data:
    filename = paper['filename']
    title = filename.replace('.txt', '')
    text = paper['text']
    
    source = None
    
    # Check for ACM patterns - case insensitive
    if re.search(r'ACM', text, re.IGNORECASE):
        source = 'ACM'
    elif re.search(r'IEEE', text, re.IGNORECASE):
        source = 'IEEE'
    elif re.search(r'PubMed', text, re.IGNORECASE):
        source = 'PubMed'
    
    if source:
        paper_sources[title] = source

# Create a mapping of titles to citation counts for 2018
citation_counts = {}
for citation in citations_data:
    title = citation['title']
    count = int(citation['citation_count'])
    citation_counts[title] = count

# Find papers published by ACM that have citation data in 2018
acm_citations = []
matched_papers = []

for title, source in paper_sources.items():
    if source == 'ACM' and title in citation_counts:
        acm_citations.append(citation_counts[title])
        matched_papers.append({
            'title': title,
            'citation_count': citation_counts[title]
        })

# Calculate average citation count for ACM papers
if acm_citations:
    avg_citation = sum(acm_citations) / len(acm_citations)
    result = {
        'average_citation_count': round(avg_citation, 2),
        'total_acm_papers_matched': len(acm_citations),
        'total_citations': sum(acm_citations)
    }
else:
    result = {
        'average_citation_count': 0,
        'total_acm_papers_matched': 0,
        'total_citations': 0
    }

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json'}

exec(code, env_args)
