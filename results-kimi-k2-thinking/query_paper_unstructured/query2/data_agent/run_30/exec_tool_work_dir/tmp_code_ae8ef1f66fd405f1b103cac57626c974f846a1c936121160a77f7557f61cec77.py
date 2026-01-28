code = """import json

# Load citation data from 2018
citations_data_json = locals()['var_functions.query_db:0']
if isinstance(citations_data_json, str) and citations_data_json.endswith('.json'):
    with open(citations_data_json, 'r') as f:
        citations_2018 = json.load(f)
else:
    citations_2018 = citations_data_json

# Load paper documents
papers_data_json = locals()['var_functions.query_db:2']
if isinstance(papers_data_json, str) and papers_data_json.endswith('.json'):
    with open(papers_data_json, 'r') as f:
        paper_docs = json.load(f)
else:
    paper_docs = papers_data_json

print('Number of citation records in 2018:', len(citations_2018))
print('Number of paper documents:', len(paper_docs))

# Extract title from filename for paper documents
paper_titles = []
for doc in paper_docs:
    filename = doc.get('filename', '')
    if filename.endswith('.txt'):
        title = filename[:-4]  # Remove .txt extension
        paper_titles.append(title)

print('Sample paper titles:', paper_titles[:5])
print('Sample citation titles:', [c['title'] for c in citations_2018[:5]])"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json'}

exec(code, env_args)
