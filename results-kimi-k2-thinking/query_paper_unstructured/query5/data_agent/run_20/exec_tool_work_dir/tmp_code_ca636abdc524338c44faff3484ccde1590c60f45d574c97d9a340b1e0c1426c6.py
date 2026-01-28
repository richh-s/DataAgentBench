code = """import json

# Read the full citation data from the file
citation_file_path = var_functions.query_db:0
with open(citation_file_path, 'r') as f:
    citations_2020 = json.load(f)

print(f"Total citations in 2020: {len(citations_2020)}")
print(f"First few records: {citations_2020[:3]}")

# Extract all titles to query MongoDB
titles = [record['title'] for record in citations_2020]
print(f"Number of titles to query: {len(titles)}")
print(f"Sample titles: {titles[:5]}")"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json'}

exec(code, env_args)
