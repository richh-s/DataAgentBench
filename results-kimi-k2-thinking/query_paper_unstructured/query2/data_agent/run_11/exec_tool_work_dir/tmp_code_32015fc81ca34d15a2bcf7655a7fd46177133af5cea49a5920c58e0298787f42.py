code = """import json

# Load the citations data for 2018
citations_file = var_functions.query_db:12
with open(citations_file, 'r') as f:
    citations_2018 = json.load(f)

# Load the paper documents data
papers_file = var_functions.query_db:14
with open(papers_file, 'r') as f:
    paper_docs = json.load(f)

# Create a mapping from title to citation count for 2018
title_to_citations = {item['title']: int(item['citation_count']) for item in citations_2018}

# Function to extract ACM publisher information from text
def is_acm_paper(text):
    if not text:
        return False
    text_lower = text.lower()
    # Look for ACM indicators
    indicators = ['acm', 'association for computing machinery']
    for indicator in indicators:
        if indicator in text_lower:
            return True
    return False

# Function to extract title from filename
def get_title_from_filename(filename):
    if filename.endswith('.txt'):
        return filename[:-4]
    return filename

# Create mapping from title to paper info
paper_info = {}
for doc in paper_docs:
    filename = doc.get('filename', '')
    text = doc.get('text', '')
    title = get_title_from_filename(filename)
    paper_info[title] = {
        'is_acm': is_acm_paper(text),
        'filename': filename
    }

# Match 2018 citations with ACM papers
acm_citation_counts = []
missing_papers = []
non_acm_papers = []

for title, citation_count in title_to_citations.items():
    if title in paper_info:
        if paper_info[title]['is_acm']:
            acm_citation_counts.append(citation_count)
        else:
            non_acm_papers.append(title)
    else:
        missing_papers.append(title)

print('__RESULT__:')
print(json.dumps({
    'total_2018_citations': len(citations_2018),
    'acm_papers_found': len(acm_citation_counts),
    'non_acm_papers_found': len(non_acm_papers),
    'missing_papers': len(missing_papers),
    'average_citation_count': sum(acm_citation_counts) / len(acm_citation_counts) if acm_citation_counts else 0,
    'acm_citation_stats': {
        'min': min(acm_citation_counts) if acm_citation_counts else None,
        'max': max(acm_citation_counts) if acm_citation_counts else None,
        'median': sorted(acm_citation_counts)[len(acm_citation_counts)//2] if acm_citation_counts else None
    }
}))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json', 'var_functions.query_db:14': 'file_storage/functions.query_db:14.json'}

exec(code, env_args)
