code = """import json
import re

# Load the 2018 citations
citations_2018_path = locals()['var_functions.query_db:0']
with open(citations_2018_path, 'r') as f:
    citations_2018 = json.load(f)

# Load the paper documents  
paper_docs_path = locals()['var_functions.query_db:2']
with open(paper_docs_path, 'r') as f:
    paper_docs = json.load(f)

# Create paper title to document mapping
paper_map = {}
for doc in paper_docs:
    if 'filename' in doc:
        title = doc['filename'].replace('.txt', '')
        paper_map[title] = doc

# Extract publisher source from paper text
def extract_source(text):
    text_upper = text.upper()
    
    # Check for ACM first (most common in this dataset)
    if 'ACM' in text_upper:
        return 'ACM'
    elif 'IEEE' in text_upper:
        return 'IEEE'
    elif 'PUBMED' in text_upper or 'NCBI' in text_upper:
        return 'PubMed'
    else:
        # Check for conference indicators
        if any(conf in text_upper for conf in ['UBICOMP', 'CHI ', 'CSCW', 'DIS', 'TEI', 'IUI']):
            return 'ACM'
        return 'Unknown'

# Get source for each paper
paper_sources = {}
for title, doc in paper_map.items():
    if 'text' in doc:
        paper_sources[title] = extract_source(doc['text'])

# Find ACM papers cited in 2018
acm_citation_counts = []
for citation in citations_2018:
    title = citation['title']
    if title in paper_sources and paper_sources[title] == 'ACM':
        acm_citation_counts.append(int(citation['citation_count']))

# Calculate average
total_acm_papers = len(acm_citation_counts)
if total_acm_papers > 0:
    avg_citations = sum(acm_citation_counts) / total_acm_papers
    result = {
        'average_citation_count': round(avg_citations, 2),
        'total_acm_papers': total_acm_papers,
        'total_citations': sum(acm_citation_counts)
    }
else:
    result = {
        'average_citation_count': 0,
        'total_acm_papers': 0,
        'total_citations': 0
    }

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json'}

exec(code, env_args)
