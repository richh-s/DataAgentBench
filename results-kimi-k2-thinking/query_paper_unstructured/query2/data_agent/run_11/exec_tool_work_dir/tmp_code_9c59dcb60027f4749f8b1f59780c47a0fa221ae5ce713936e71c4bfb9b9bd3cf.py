code = """import json

# Get file paths from locals() without using colon syntax
citations_key = [k for k in locals().keys() if 'query_db' in k and '48' in str(locals()[k])][0]
papers_key = [k for k in locals().keys() if 'query_db' in k and '14' in str(locals()[k])][0]

citations_file = locals()[citations_key]
papers_file = locals()[papers_key]

# Load data
with open(citations_file) as f:
    citations_2018 = json.load(f)

with open(papers_file) as f:
    paper_docs = json.load(f)

# Helper functions
def extract_title(filename):
    return filename[:-4] if filename.endswith('.txt') else filename

def is_acm(text):
    if not text:
        return False
    text = text.lower()
    indicators = ['acm', 'association for computing machinery', 'copyright © acm']
    return any(indicator in text for indicator in indicators)

# Map papers to ACM status
paper_map = {}
for doc in paper_docs:
    title = extract_title(doc.get('filename', ''))
    paper_map[title] = is_acm(doc.get('text', ''))

# Find ACM paper citations
acm_counts = [int(c['citation_count']) for c in citations_2018 
              if c['title'] in paper_map and paper_map[c['title']]]

avg = sum(acm_counts) / len(acm_counts) if acm_counts else 0

result = {
    'total_2018': len(citations_2018),
    'acm_papers': len(acm_counts),
    'avg_citations': round(avg, 2),
    'sample_counts': acm_counts[:10]
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json', 'var_functions.query_db:14': 'file_storage/functions.query_db:14.json', 'var_functions.list_db:20': ['paper_docs'], 'var_functions.query_db:24': 'file_storage/functions.query_db:24.json', 'var_functions.query_db:28': 'file_storage/functions.query_db:28.json', 'var_functions.query_db:32': [{'total_2018': '158'}], 'var_functions.query_db:34': 'file_storage/functions.query_db:34.json', 'var_functions.execute_python:38': 'file_storage/functions.execute_python:38.json', 'var_functions.query_db:48': 'file_storage/functions.query_db:48.json'}

exec(code, env_args)
