code = """import json

# Load data from the stored file paths
citations_path = var_functions.query_db:34
papers_path = var_functions.query_db:14

with open(citations_path, 'r') as f:
    citations_2018 = json.load(f)

with open(papers_path, 'r') as f:
    paper_docs = json.load(f)

# Function to check if text contains ACM publisher info
def is_acm_published(text):
    if not text:
        return False
    text_lower = text.lower()
    # Check for ACM indicators
    acm_indicators = ['acm', 'association for computing machinery', 'copyright © acm']
    for indicator in acm_indicators:
        if indicator in text_lower:
            return True
    return False

# Function to extract title from filename
def extract_title(filename):
    if filename.endswith('.txt'):
        return filename[:-4]
    return filename

# Create mapping of paper titles to ACM status
paper_acm_status = {}
for doc in paper_docs:
    filename = doc.get('filename', '')
    text = doc.get('text', '')
    title = extract_title(filename)
    paper_acm_status[title] = is_acm_published(text)

# Match citations with ACM papers
acm_citation_counts = []
matched_papers = 0

for citation in citations_2018:
    title = citation['title']
    citation_count = int(citation['citation_count'])
    
    if title in paper_acm_status and paper_acm_status[title]:
        acm_citation_counts.append(citation_count)
        matched_papers += 1

# Calculate average
total_acm_citations = sum(acm_citation_counts)
average_citations = total_acm_citations / len(acm_citation_counts) if acm_citation_counts else 0

print('__RESULT__:')
print(json.dumps({
    'total_citations_2018': len(citations_2018),
    'acm_papers_matched': len(acm_citation_counts),
    'average_citation_count': round(average_citations, 2),
    'acm_citation_counts': acm_citation_counts,
    'paper_docs_available': len(paper_docs)
}))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json', 'var_functions.query_db:14': 'file_storage/functions.query_db:14.json', 'var_functions.list_db:20': ['paper_docs'], 'var_functions.query_db:24': 'file_storage/functions.query_db:24.json', 'var_functions.query_db:28': 'file_storage/functions.query_db:28.json', 'var_functions.query_db:32': [{'total_2018': '158'}], 'var_functions.query_db:34': 'file_storage/functions.query_db:34.json', 'var_functions.execute_python:38': 'file_storage/functions.execute_python:38.json'}

exec(code, env_args)
