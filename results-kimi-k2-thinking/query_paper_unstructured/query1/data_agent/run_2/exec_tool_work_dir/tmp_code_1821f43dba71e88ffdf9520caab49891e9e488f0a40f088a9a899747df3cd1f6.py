code = """import json
import os

# Get the paths from the stored variables
papers_result = locals().get('var_functions.query_db:2', '')
citations_result = locals().get('var_functions.query_db:9', '')

print("Paper docs DB result type:", type(papers_result))
print("Citations DB result type:", type(citations_result))

if isinstance(papers_result, str) and os.path.exists(papers_result):
    with open(papers_result, 'r') as f:
        papers = json.load(f)
    print(f"Papers: {len(papers)} records")
    if papers:
        print("Sample paper:", papers[0].get('filename', 'N/A'))
else:
    print("Papers result is not a valid file path or is empty")
    papers = []

if isinstance(citations_result, str) and os.path.exists(citations_result):
    with open(citations_result, 'r') as f:
        citations = json.load(f)
    print(f"Citations: {len(citations)} records")
    if citations:
        print("Sample citation:", citations[0].get('title', 'N/A'))
else:
    print("Citations result is not a valid file path or is empty")
    citations = []

print('__RESULT__:')
print(json.dumps({"papers": len(papers), "citations": len(citations)}))"""

env_args = {'var_functions.list_db:0': ['paper_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.list_db:5': ['Citations', 'sqlite_sequence'], 'var_functions.query_db:9': 'file_storage/functions.query_db:9.json'}

exec(code, env_args)
