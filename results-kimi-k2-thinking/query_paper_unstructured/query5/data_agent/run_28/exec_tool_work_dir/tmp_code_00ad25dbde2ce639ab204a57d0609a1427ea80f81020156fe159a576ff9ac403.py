code = """import json
import re

# Read the 2020 citations data
citations_path = var_functions.query_db:0
with open(citations_path, 'r') as f:
    citations_2020 = json.load(f)

# Read the paper documents data
papers_path = var_functions.query_db:6
with open(papers_path, 'r') as f:
    paper_docs = json.load(f)

# Debug: Check basic info
print('Total 2020 citations:', len(citations_2020))
print('Total paper docs:', len(paper_docs))

# Check sample data
sample_citation = citations_2020[0]
print('Sample citation keys:', list(sample_citation.keys()))
print('Sample citation:', sample_citation)

sample_paper = paper_docs[0]
print('Sample paper keys:', list(sample_paper.keys()))
print('Sample paper filename:', sample_paper.get('filename'))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.list_db:2': ['paper_docs'], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json'}

exec(code, env_args)
