code = """import json
import re

# Read the full paper data
with open('/tmp/tmpld3w_0o1.json', 'r') as f:
    papers = json.load(f)

print('Number of papers loaded:', len(papers))

# Let's examine the structure
first_paper = papers[0]
print('Keys:', list(first_paper.keys()))
print('Filename:', first_paper['filename'])
print('\nFirst 500 chars of text:')
print(first_paper['text'][:500])"""

env_args = {'var_functions.list_db:0': ['paper_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.list_db:5': ['Citations', 'sqlite_sequence'], 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json'}

exec(code, env_args)
