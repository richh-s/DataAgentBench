code = """import json

# Load the paper data from the first query
paper_data_path = var_functions.query_db:0
with open(paper_data_path, 'r') as f:
    papers = json.load(f)

print(f"Number of papers loaded: {len(papers)}")
print("\nFirst few papers:")
for i, paper in enumerate(papers[:3]):
    print(f"\nPaper {i+1}:")
    print(f"Filename: {paper.get('filename')}")
    print(f"Text preview: {paper.get('text', '')[:200]}...")"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json'}

exec(code, env_args)
