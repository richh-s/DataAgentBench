code = """import json
import os

# Load citation data for 2018
citation_file = locals()['var_functions.query_db:0']
print(f"Citation file path: {citation_file}")

# Check file size and first few lines
if os.path.exists(citation_file):
    with open(citation_file, 'r') as f:
        preview = f.read(500)
        print(f"File preview: {preview[:200]}")
else:
    print("Citation file not found")

# Load paper documents
paper_file = locals()['var_functions.query_db:2']
print(f"Paper file path: {paper_file}")

if os.path.exists(paper_file):
    with open(paper_file, 'r') as f:
        preview = f.read(500)
        print(f"File preview: {preview[:200]}")
else:
    print("Paper file not found")

print("__RESULT__:")
print(json.dumps({"status": "files_checked"}))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json'}

exec(code, env_args)
