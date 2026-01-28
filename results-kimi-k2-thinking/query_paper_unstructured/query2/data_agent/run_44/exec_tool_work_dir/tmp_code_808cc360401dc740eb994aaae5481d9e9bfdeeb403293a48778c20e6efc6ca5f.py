code = """import json
import os

# Load citation data for 2018
citation_file = locals()['var_functions.query_db:0']
citation_data = []
with open(citation_file, 'r') as f:
    for line in f:
        if line.strip():
            citation_data.append(json.loads(line))

# Load paper documents
paper_file = locals()['var_functions.query_db:2']
paper_data = []
with open(paper_file, 'r') as f:
    for line in f:
        if line.strip():
            paper_data.append(json.loads(line))

print("__RESULT__:")
print(json.dumps({
    'citation_records': len(citation_data),
    'paper_documents': len(paper_data)
}))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json'}

exec(code, env_args)
