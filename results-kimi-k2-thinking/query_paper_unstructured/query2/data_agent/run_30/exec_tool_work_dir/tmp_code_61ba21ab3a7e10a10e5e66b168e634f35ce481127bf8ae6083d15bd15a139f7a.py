code = """import json

# Load citation data from 2018
citations_data_json = locals()['var_functions.query_db:0']
if isinstance(citations_data_json, str) and citations_data_json.endswith('.json'):
    with open(citations_data_json, 'r') as f:
        citations_2018 = json.load(f)
else:
    citations_2018 = citations_data_json

# Load paper documents
papers_data_json = locals()['var_functions.query_db:2']
if isinstance(papers_data_json, str) and papers_data_json.endswith('.json'):
    with open(papers_data_json, 'r') as f:
        paper_docs = json.load(f)
else:
    paper_docs = papers_data_json

# Create mapping of titles to ACM status
acm_papers = {}

for doc in paper_docs:
    text = doc.get('text', '')
    filename = doc.get('filename', '')
    
    # Extract title from filename
    if filename.endswith('.txt'):
        title = filename[:-4]  # Remove .txt
    else:
        title = filename
    
    # Check if paper is from ACM
    # Look for ACM references in the text
    is_acm = 'ACM' in text or 'acm' in text or 'acm.org' in text
    
    # Also check for ACM conference mentions
    if not is_acm:
        # Common ACM venues mentioned
        acm_venues = ['UBICOMP', 'CHI', 'CSCW', 'DIS', 'UIST', 'ISS']
        for venue in acm_venues:
            if venue in text and 'ACM' in text:
                is_acm = True
                break
    
    acm_papers[title] = is_acm

# Find citation counts for ACM papers in 2018
acm_citation_counts = []
matched_titles = []

for citation in citations_2018:
    cite_title = citation.get('title', '')
    cite_count = int(citation.get('citation_count', 0))
    
    # Check if this title is in our ACM papers
    for paper_title, is_acm in acm_papers.items():
        if is_acm and cite_title.lower() == paper_title.lower():
            acm_citation_counts.append(cite_count)
            matched_titles.append(cite_title)
            break

# Calculate average
if acm_citation_counts:
    avg_citations = sum(acm_citation_counts) / len(acm_citation_counts)
    result = {
        'avg_citation_count': avg_citations,
        'num_acm_papers': len(acm_citation_counts),
        'total_citations': sum(acm_citation_counts)
    }
else:
    result = {
        'avg_citation_count': 0,
        'num_acm_papers': 0,
        'total_citations': 0,
        'message': 'No ACM papers found or no matches'
    }

print('__RESULT__:')
print(json.dumps(result, indent=2))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json'}

exec(code, env_args)
