code = """import json

# Load file paths
citations_path = var_functions.query_db:62
papers_path = var_functions.query_db:64

# Read citations data
with open(citations_path, 'r') as f:
    citations_data = json.load(f)

# Read papers data  
with open(papers_path, 'r') as f:
    papers_data = json.load(f)

# Helper functions
def get_title_from_filename(filename):
    return filename[:-4] if filename.endswith('.txt') else filename

def check_acm_publisher(text):
    if not text:
        return False
    text = text.lower()
    return 'acm' in text or 'association for computing machinery' in text

# Create ACM paper lookup
acm_papers = {}
for paper in papers_data:
    title = get_title_from_filename(paper.get('filename', ''))
    text = paper.get('text', '')
    acm_papers[title] = check_acm_publisher(text)

# Find ACM papers with 2018 citations
citation_counts = []
matched_titles = []

for citation in citations_data:
    title = citation['title']
    if title in acm_papers and acm_papers[title]:
        citation_counts.append(int(citation['citation_count']))
        matched_titles.append(title)

# Calculate average
if citation_counts:
    avg = sum(citation_counts) / len(citation_counts)
else:
    avg = 0

# Output result
output = {
    'total_2018_citations': len(citations_data),
    'acm_papers_with_citations': len(citation_counts),
    'average_citation_count': round(avg, 2),
    'total_citations_for_acm': sum(citation_counts),
    'acm_papers_sample': matched_titles[:3]
}

print('__RESULT__:')
print(json.dumps(output))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json', 'var_functions.query_db:14': 'file_storage/functions.query_db:14.json', 'var_functions.list_db:20': ['paper_docs'], 'var_functions.query_db:24': 'file_storage/functions.query_db:24.json', 'var_functions.query_db:28': 'file_storage/functions.query_db:28.json', 'var_functions.query_db:32': [{'total_2018': '158'}], 'var_functions.query_db:34': 'file_storage/functions.query_db:34.json', 'var_functions.execute_python:38': 'file_storage/functions.execute_python:38.json', 'var_functions.query_db:48': 'file_storage/functions.query_db:48.json', 'var_functions.execute_python:52': {'total_2018': 158, 'acm_papers': 2, 'avg_citations': 68.5, 'sample_counts': [50, 87]}, 'var_functions.query_db:54': 'file_storage/functions.query_db:54.json', 'var_functions.query_db:56': 'file_storage/functions.query_db:56.json', 'var_functions.query_db:60': [], 'var_functions.query_db:62': 'file_storage/functions.query_db:62.json', 'var_functions.query_db:64': 'file_storage/functions.query_db:64.json'}

exec(code, env_args)
