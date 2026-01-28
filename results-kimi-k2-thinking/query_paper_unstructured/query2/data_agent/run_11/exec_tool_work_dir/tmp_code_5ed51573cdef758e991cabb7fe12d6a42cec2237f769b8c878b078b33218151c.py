code = """import json

# Load the citations data
citations_result = var_functions.query_db:34
with open(citations_result, 'r') as f:
    citations_2018 = json.load(f)

# Load the paper documents
papers_result = var_functions.query_db:14
with open(papers_result, 'r') as f:
    paper_docs = json.load(f)

# Function to extract title from filename
def extract_title_from_filename(filename):
    if filename.endswith('.txt'):
        return filename[:-4]
    return filename

# Function to check if paper is ACM published
def is_acm_paper(text):
    if not text:
        return False
    text_lower = text.lower()
    # Look for ACM indicators
    acm_indicators = [
        'acm',
        'association for computing machinery',
        'copyright © acm',
        'permission to make digital or hard copies',
        'acm classification keywords'
    ]
    for indicator in acm_indicators:
        if indicator in text_lower:
            return True
    return False

# Build dictionary of papers with ACM status
paper_acm_map = {}
for doc in paper_docs:
    filename = doc.get('filename', '')
    text = doc.get('text', '')
    title = extract_title_from_filename(filename)
    paper_acm_map[title] = is_acm_paper(text)

# Match citations with ACM papers and collect citation counts
acm_citation_counts = []
acm_paper_titles = []

for citation in citations_2018:
    title = citation['title']
    citation_count = int(citation['citation_count'])
    
    if title in paper_acm_map and paper_acm_map[title]:
        acm_citation_counts.append(citation_count)
        acm_paper_titles.append(title)

# Calculate average
total_citations = sum(acm_citation_counts)
count = len(acm_citation_counts)
average = total_citations / count if count > 0 else 0

# Prepare result
result = {
    'total_papers_cited_2018': len(citations_2018),
    'acm_papers_identified': count,
    'acm_citation_counts': acm_citation_counts,
    'average_citation_count': round(average, 2),
    'acm_paper_sample': acm_paper_titles[:5]
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json', 'var_functions.query_db:14': 'file_storage/functions.query_db:14.json', 'var_functions.list_db:20': ['paper_docs'], 'var_functions.query_db:24': 'file_storage/functions.query_db:24.json', 'var_functions.query_db:28': 'file_storage/functions.query_db:28.json', 'var_functions.query_db:32': [{'total_2018': '158'}], 'var_functions.query_db:34': 'file_storage/functions.query_db:34.json', 'var_functions.execute_python:38': 'file_storage/functions.execute_python:38.json'}

exec(code, env_args)
