code = """import json
import re

# Load the citations data for 2018
citations_data = var_functions.query_db:2

# Load the paper documents data
papers_data = var_functions.query_db:5

# Create a dictionary to store paper titles and their sources
paper_sources = {}

for paper in papers_data:
    # Extract title from filename
    filename = paper.get('filename', '')
    if filename.endswith('.txt'):
        title = filename[:-4]  # Remove .txt extension
    else:
        title = filename
    
    # Extract source (publisher) from text
    text = paper.get('text', '')
    
    # Look for ACM mentions in the text
    source = []
    
    # Check for ACM
    if re.search(r'ACM', text):
        source.append('ACM')
    
    # Check for IEEE
    if re.search(r'IEEE', text):
        source.append('IEEE')
    
    # Check for PubMed
    if re.search(r'PubMed', text, re.IGNORECASE):
        source.append('PubMed')
    
    # Store the sources for this paper
    if source:
        paper_sources[title] = source

# Join citations with paper sources and filter for ACM papers
acm_citations = []
all_citation_counts = []

for citation in citations_data:
    title = citation.get('title', '')
    citation_count = int(citation.get('citation_count', 0))
    
    all_citation_counts.append(citation_count)
    
    # Check if this paper is in our paper_sources and if it has ACM
    if title in paper_sources and 'ACM' in paper_sources[title]:
        acm_citations.append(citation_count)

# Calculate statistics
total_citations = len(citations_data)
acm_citations_count = len(acm_citations)

if acm_citations_count > 0:
    avg_acm_citations = sum(acm_citations) / acm_citations_count
else:
    avg_acm_citations = 0

avg_all_citations = sum(all_citation_counts) / len(all_citation_counts) if all_citation_counts else 0

# Prepare result
result = {
    "total_papers_cited_in_2018": total_citations,
    "acm_papers_identified": acm_citations_count,
    "average_citation_count_acm_papers": round(avg_acm_citations, 2) if avg_acm_citations else 0,
    "average_citation_count_all_papers": round(avg_all_citations, 2)
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json'}

exec(code, env_args)
