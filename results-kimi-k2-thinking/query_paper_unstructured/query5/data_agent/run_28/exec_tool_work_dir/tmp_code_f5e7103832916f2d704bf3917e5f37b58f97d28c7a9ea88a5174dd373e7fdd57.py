code = """import json

# Read the data from files
with open('var_functions.query_db:0', 'r') as f:
    citations_2020 = json.load(f)

with open('var_functions.query_db:6', 'r') as f:
    paper_docs = json.load(f)

# Create a mapping of paper titles to their data
paper_lookup = {}
for paper in paper_docs:
    title = paper['filename'].replace('.txt', '')
    paper_lookup[title] = paper
    
print('Loaded', len(citations_2020), '2020 citations')
print('Loaded', len(paper_docs), 'paper documents')
print('Created lookup for', len(paper_lookup), 'papers')

# Check first entry
print('First citation:', citations_2020[0])
print('First paper:', paper_docs[0]['filename'])"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.list_db:2': ['paper_docs'], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json'}

exec(code, env_args)
