code = """import json

# Load all citations from 2018
citations_file = var_functions.query_db:62
with open(citations_file, 'r') as f:
    citations_2018 = json.load(f)

# Load all paper documents
papers_file = var_functions.query_db:64
with open(papers_file, 'r') as f:
    paper_docs = json.load(f)

# Helper functions
def extract_title_from_filename(filename):
    return filename[:-4] if filename.endswith('.txt') else filename

def is_acm_published(text):
    if not text:
        return False
    text_lower = text.lower()
    acm_indicators = [
        'acm',
        'association for computing machinery', 
        'copyright © acm',
        'permission to make digital or hard copies',
        'acm classification keywords'
    ]
    return any(indicator in text_lower for indicator in acm_indicators)

# Create mapping of paper titles to ACM status
paper_acm_map = {}
for doc in paper_docs:
    filename = doc.get('filename', '')
    text = doc.get('text', '')
    title = extract_title_from_filename(filename)
    paper_acm_map[title] = is_acm_published(text)

# Match citations with ACM papers and collect citation counts
acm_citation_data = []
for citation in citations_2018:
    title = citation['title']
    citation_count = int(citation['citation_count'])
    
    if title in paper_acm_map and paper_acm_map[title]:
        acm_citation_data.append({
            'title': title,
            'citation_count': citation_count
        })

# Calculate average
total_citations = sum(item['citation_count'] for item in acm_citation_data)
total_papers = len(acm_citation_data)
average_citations = total_citations / total_papers if total_papers > 0 else 0

# Prepare comprehensive result
result = {
    'total_citations_2018': len(citations_2018),
    'acm_papers_identified': total_papers,
    'average_citation_count': round(average_citations, 2),
    'acm_papers_details': acm_citation_data,
    'total_acm_citations': total_citations
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json', 'var_functions.query_db:14': 'file_storage/functions.query_db:14.json', 'var_functions.list_db:20': ['paper_docs'], 'var_functions.query_db:24': 'file_storage/functions.query_db:24.json', 'var_functions.query_db:28': 'file_storage/functions.query_db:28.json', 'var_functions.query_db:32': [{'total_2018': '158'}], 'var_functions.query_db:34': 'file_storage/functions.query_db:34.json', 'var_functions.execute_python:38': 'file_storage/functions.execute_python:38.json', 'var_functions.query_db:48': 'file_storage/functions.query_db:48.json', 'var_functions.execute_python:52': {'total_2018': 158, 'acm_papers': 2, 'avg_citations': 68.5, 'sample_counts': [50, 87]}, 'var_functions.query_db:54': 'file_storage/functions.query_db:54.json', 'var_functions.query_db:56': 'file_storage/functions.query_db:56.json', 'var_functions.query_db:60': [], 'var_functions.query_db:62': 'file_storage/functions.query_db:62.json', 'var_functions.query_db:64': 'file_storage/functions.query_db:64.json'}

exec(code, env_args)
