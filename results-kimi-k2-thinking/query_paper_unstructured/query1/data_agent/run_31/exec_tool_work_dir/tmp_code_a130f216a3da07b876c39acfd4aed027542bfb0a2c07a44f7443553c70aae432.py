code = """import json, os

# Find and list all JSON result files
result_dir = 'storage/result'
print('Files in storage/result:')
for file in sorted(os.listdir(result_dir)):
    print('  ' + file)

# Load citations data
citations_path = os.path.join(result_dir, 'query_Citations_citations_database_12.json')
print('\nLoading citations from: ' + citations_path)
with open(citations_path) as f:
    citations = json.load(f)

# Load papers data
papers_path = os.path.join(result_dir, 'query_paper_docs_paper_docs_database_11.json')
print('Loading papers from: ' + papers_path)
with open(papers_path) as f:
    papers = json.load(f)

print('\nData loaded successfully!')
print('Citations count: ' + str(len(citations)))
print('Papers count: ' + str(len(papers)))

# Show some food-related citation titles to verify
print('\nSample food-related citations:')
food_citation_count = 0
for c in citations[15:30]:  # sample of citations
    title_lower = c['title'].lower()
    if 'food' in title_lower or 'diet' in title_lower:
        print('  ' + c['title'] + ' (' + c['total_citations'] + ')')
        food_citation_count += 1

print('\nTotal food-related citations in sample: ' + str(food_citation_count))"""

env_args = {'var_functions.list_db:0': ['paper_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.list_db:14': ['Citations', 'sqlite_sequence'], 'var_functions.query_db:16': 'file_storage/functions.query_db:16.json', 'var_functions.query_db:18': 'file_storage/functions.query_db:18.json', 'var_functions.query_db:22': 'file_storage/functions.query_db:22.json', 'var_functions.query_db:24': 'file_storage/functions.query_db:24.json', 'var_functions.query_db:28': 'file_storage/functions.query_db:28.json', 'var_functions.execute_python:52': {'total_citations': 0}}

exec(code, env_args)
