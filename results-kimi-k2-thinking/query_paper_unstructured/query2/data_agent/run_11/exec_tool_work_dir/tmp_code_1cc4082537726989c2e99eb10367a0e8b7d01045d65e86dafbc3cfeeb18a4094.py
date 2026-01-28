code = """import json

# Get the file paths from the variables dictionary
vars_dict = dict(locals())

# Find the file paths
citations_file = None
papers_file = None

for key, value in vars_dict.items():
    if 'query_db' in key and ':70' in str(value):
        citations_file = value
    elif 'query_db' in key and ':74' in str(value):
        papers_file = value

# Load the data
with open(citations_file, 'r') as f:
    citations_2018 = json.load(f)

with open(papers_file, 'r') as f:
    paper_docs = json.load(f)

# Helper functions
def extract_title(filename):
    return filename[:-4] if filename.endswith('.txt') else filename

def is_acm_published(text):
    if not text:
        return False
    text = text.lower()
    indicators = ['acm', 'association for computing machinery', 'copyright © acm']
    return any(indicator in text for indicator in indicators)

# Map papers to ACM status
acm_map = {}
for doc in paper_docs:
    title = extract_title(doc.get('filename', ''))
    acm_map[title] = is_acm_published(doc.get('text', ''))

# Count ACM paper citations
acm_citations = []
for citation in citations_2018:
    title = citation['title']
    if title in acm_map and acm_map[title]:
        acm_citations.append(int(citation['citation_count']))

# Calculate average
avg = sum(acm_citations) / len(acm_citations) if acm_citations else 0

result = {
    'total_citations_2018': len(citations_2018),
    'acm_papers_count': len(acm_citations),
    'average_citation_count': round(avg, 2),
    'acm_citations_list': acm_citations
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json', 'var_functions.query_db:14': 'file_storage/functions.query_db:14.json', 'var_functions.list_db:20': ['paper_docs'], 'var_functions.query_db:24': 'file_storage/functions.query_db:24.json', 'var_functions.query_db:28': 'file_storage/functions.query_db:28.json', 'var_functions.query_db:32': [{'total_2018': '158'}], 'var_functions.query_db:34': 'file_storage/functions.query_db:34.json', 'var_functions.execute_python:38': 'file_storage/functions.execute_python:38.json', 'var_functions.query_db:48': 'file_storage/functions.query_db:48.json', 'var_functions.execute_python:52': {'total_2018': 158, 'acm_papers': 2, 'avg_citations': 68.5, 'sample_counts': [50, 87]}, 'var_functions.query_db:54': 'file_storage/functions.query_db:54.json', 'var_functions.query_db:56': 'file_storage/functions.query_db:56.json', 'var_functions.query_db:60': [], 'var_functions.query_db:62': 'file_storage/functions.query_db:62.json', 'var_functions.query_db:64': 'file_storage/functions.query_db:64.json', 'var_functions.query_db:70': 'file_storage/functions.query_db:70.json', 'var_functions.query_db:74': 'file_storage/functions.query_db:74.json'}

exec(code, env_args)
