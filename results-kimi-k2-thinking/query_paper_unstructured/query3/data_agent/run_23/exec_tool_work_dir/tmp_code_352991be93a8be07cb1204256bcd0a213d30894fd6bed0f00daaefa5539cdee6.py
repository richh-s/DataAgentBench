code = """# Read stored results - for large results, a file path is stored
import json

# The result is too large and stored as a file path
file_path = "/tmp/tmp_mongo_result_zwqu5g2w.json"

with open(file_path, 'r') as f:
    papers = json.load(f)

print(f"Loaded {len(papers)} papers from MongoDB")

# Save to local variable
result_data = papers
print('__RESULT__:')
print(json.dumps(f"Loaded {len(papers)} papers"))"""

env_args = {'var_functions.list_db:0': ['paper_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json'}

exec(code, env_args)
