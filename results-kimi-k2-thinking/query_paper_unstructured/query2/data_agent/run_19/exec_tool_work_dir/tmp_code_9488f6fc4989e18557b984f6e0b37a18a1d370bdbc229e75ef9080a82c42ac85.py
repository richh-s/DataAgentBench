code = """import json
import re
from collections import defaultdict

# Load the data
citations_file_path = locals()['var_functions.query_db:2']
papers_file_path = locals()['var_functions.query_db:4']

with open(citations_file_path, 'r') as f:
    citations_data = json.load(f)

with open(papers_file_path, 'r') as f:
    papers_data = json.load(f)

# Build comprehensive paper metadata
paper_metadata = {}
for paper in papers_data:
    filename = paper['filename']
    title = filename.replace('.txt', '')
    text = paper['text']
    
    # Detect source/publisher
    source = None
    if 'ACM' in text or 'acm' in text:
        source = 'ACM'
    elif 'IEEE' in text or 'ieee' in text:
        source = 'IEEE'
    elif 'PubMed' in text or 'pubmed' in text:
        source = 'PubMed'
    
    # Also check copyright notices and conference headers more carefully
    text_lower = text.lower()
    if 'proceedings of the acm' in text_lower or 'acm conference' in text_lower:
        source = 'ACM'
    
    paper_metadata[title] = {
        'source': source,
        'filename': filename
    }

# Create a mapping for flexible matching
def normalize_title(title):
    """Normalize titles for better matching"""
    # Remove common words, convert to lowercase, remove punctuation
    title = title.lower()
    title = re.sub(r'[^a-z0-9\s]', '', title)
    # Remove common stop words
    stop_words = {'the', 'a', 'an', 'and', 'or', 'but', 'in', 'on', 'at', 'to', 'for', 'of', 'with', 'by', 'from'}
    words = [w for w in title.split() if w not in stop_words]
    return ' '.join(words)

# Create normalized versions of paper titles
paper_normalized = {}
for title, meta in paper_metadata.items():
    if meta['source'] == 'ACM':
        paper_normalized[normalize_title(title)] = title

# Match citations with ACM papers
acm_citation_counts = []
matched_citations = []

for citation in citations_data:
    cit_title = citation['title']
    cit_count = int(citation['citation_count'])
    
    # Try exact match first
    if cit_title in paper_metadata:
        if paper_metadata[cit_title]['source'] == 'ACM':
            acm_citation_counts.append(cit_count)
            matched_citations.append(cit_title)
            continue
    
    # Try normalized match
    cit_normalized = normalize_title(cit_title)
    if cit_normalized in paper_normalized:
        acm_citation_counts.append(cit_count)
        matched_citations.append(cit_title)
    else:
        # Try partial matching for longer titles
        for paper_norm, paper_orig in paper_normalized.items():
            if len(cit_normalized) > 15 and cit_normalized in paper_norm:
                acm_citation_counts.append(cit_count)
                matched_citations.append(cit_title)
                break
            elif len(paper_norm) > 15 and paper_norm in cit_normalized:
                acm_citation_counts.append(cit_count)
                matched_citations.append(cit_title)
                break

# Calculate average
if acm_citation_counts:
    avg_citations = sum(acm_citation_counts) / len(acm_citation_counts)
else:
    avg_citations = 0

result = {
    'total_citations_2018': len(citations_data),
    'acm_papers_found': len([p for p in paper_metadata.values() if p['source'] == 'ACM']),
    'matched_acm_papers': len(acm_citation_counts),
    'average_citation_count': round(avg_citations, 2),
    'matched_titles_sample': matched_citations[:5]
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['paper_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json', 'var_functions.execute_python:10': {'total_citations_2018': 158, 'acm_papers_count': 2, 'average_citation_count': 68.5, 'acm_citations_list': [50, 87]}, 'var_functions.execute_python:14': {'total_citations_2018': 158, 'acm_papers_in_corpus': 5, 'exact_matches': 2, 'close_matches': 2}}

exec(code, env_args)
