code = """import json

# Load data
citations_path = "var_functions.query_db:16"
try:
    with open(citations_path, 'r') as f:
        citations_2020 = json.load(f)
except Exception as e:
    print('Error loading citations', e)
    citations_2020 = []

papers_path = "var_functions.query_db:2"
try:
    with open(papers_path, 'r') as f:
        papers = json.load(f)
except Exception as e:
    print('Error loading papers', e)
    papers = []

# Debug: Print sample of data
print('Number of citation records for 2020:', len(citations_2020))
print('Number of paper documents:', len(papers))

# Show sample citations
if citations_2020:
    print('\nSample citation titles:')
    for i, cite in enumerate(citations_2020[:5]):
        print(f"  {i+1}. '{cite.get('title')}'")

# Show sample paper filenames
if papers:
    print('\nSample paper filenames:')
    for i, paper in enumerate(papers[:5]):
        print(f"  {i+1}. '{paper.get('filename')}'")

result = {
    'citation_records_2020': len(citations_2020),
    'paper_documents': len(papers)
}

print('\n__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:16': 'file_storage/functions.query_db:16.json', 'var_functions.execute_python:20': {'total_citations_from_chi_papers_in_2020': 0}, 'var_functions.execute_python:24': {'total_citation_count_for_chi_papers in 2020': 0, 'number_of_chi_papers_with_citations': 0, 'total_chi_papers_identified': 0}}

exec(code, env_args)
