code = """import json

# Load the data
citations_file_path = locals()['var_functions.query_db:2']
papers_file_path = locals()['var_functions.query_db:4']

with open(citations_file_path, 'r') as f:
    citations_data = json.load(f)

with open(papers_file_path, 'r') as f:
    papers_data = json.load(f)

# Create a more robust mapping
# First, let's explore what patterns indicate ACM papers in our data

# Sample some papers to see patterns
sample_papers = papers_data[:10]
for paper in sample_papers:
    filename = paper['filename']
    text_preview = paper['text'][:500]
    has_acm = 'ACM' in paper['text']
    print(f"File: {filename}, Has ACM: {has_acm}")
    if has_acm:
        # Show where ACM appears
        lines = paper['text'].split('\n')
        for i, line in enumerate(lines[:20]):
            if 'ACM' in line:
                print(f"  Line {i}: {line[:100]}")

result = {"sample_checked": True}
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['paper_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json', 'var_functions.execute_python:10': {'total_citations_2018': 158, 'acm_papers_count': 2, 'average_citation_count': 68.5, 'acm_citations_list': [50, 87]}}

exec(code, env_args)
