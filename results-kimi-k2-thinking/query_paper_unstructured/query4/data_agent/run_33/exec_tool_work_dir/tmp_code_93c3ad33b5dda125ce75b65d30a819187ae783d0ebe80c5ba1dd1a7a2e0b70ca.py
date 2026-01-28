code = """import json

# Load the second query results which should have papers with physical activity and 2016
paper_data_path = locals()['var_functions.query_db:4'].strip()
print("Data path:", paper_data_path)

with open(paper_data_path, 'r') as f:
    papers = json.load(f)

print(f"Number of papers loaded: {len(papers)}")
print("Sample paper:", papers[0].get('filename') if papers else "No papers")"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json'}

exec(code, env_args)
