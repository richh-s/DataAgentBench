code = """# Read the MongoDB query results from the file
import json
result_file = var_functions.query_db:5
with open(result_file, 'r') as f:
    papers = json.load(f)

print(f"Found {len(papers)} papers mentioning 'physical activity'")

# Let's inspect the first paper to understand structure
print("Sample paper structure:")
first_paper = papers[0]
print(f"Filename: {first_paper['filename']}")
print(f"Text preview: {first_paper['text'][:500]}")"""

env_args = {'var_functions.list_db:0': ['paper_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.list_db:6': ['Citations', 'sqlite_sequence']}

exec(code, env_args)
