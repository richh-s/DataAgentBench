code = """import json
import os

# Load the full result from the file
file_path = locals()['var_functions.query_db:10']
print(f"Loading from: {file_path}")

if os.path.exists(file_path):
    with open(file_path, 'r') as f:
        food_papers = json.load(f)
    print(f"Total food-related papers loaded: {len(food_papers)}")
    print("\nSample papers:")
    for i, paper in enumerate(food_papers[:10]):
        print(f"{i+1}. {paper['filename']}")
else:
    print("File not found")"""

env_args = {'var_functions.list_db:0': ['paper_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json'}

exec(code, env_args)
