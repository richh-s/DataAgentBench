code = """import json
import math

with open(locals()['var_function-call-14780723483787250948'], 'r') as f:
    repo_names_data = json.load(f)

repo_names_list = [repo['repo_name'] for repo in repo_names_data]

# Split the list into chunks to avoid overly long SQL queries
chunk_size = 500  # Adjust chunk size as needed
repo_name_chunks = [repo_names_list[i:i + chunk_size] for i in range(0, len(repo_names_list), chunk_size)]

# Generate queries for each chunk
queries = []
for chunk in repo_name_chunks:
    repo_names_in_clause = ', '.join([f"'{repo}'" for repo in chunk])
    query = f"SELECT COUNT(message) AS commit_count FROM commits WHERE repo_name IN ({repo_names_in_clause}) AND message IS NOT NULL AND LENGTH(message) < 1000 AND NOT (LOWER(message) LIKE 'merge%' OR LOWER(message) LIKE 'update%' OR LOWER(message) LIKE 'test%');"
    queries.append(query)

print("__RESULT__:")
print(json.dumps(queries))"""

env_args = {'var_function-call-16630310231902441811': 'file_storage/function-call-16630310231902441811.json', 'var_function-call-14457107682505315983': 'file_storage/function-call-14457107682505315983.json', 'var_function-call-2790894637291042964': 'file_storage/function-call-2790894637291042964.json', 'var_function-call-14780723483787250948': 'file_storage/function-call-14780723483787250948.json', 'var_function-call-9386416734928850965': 'file_storage/function-call-9386416734928850965.json', 'var_function-call-12455657995538882406': 'file_storage/function-call-12455657995538882406.json', 'var_function-call-15305257313604863453': 'file_storage/function-call-15305257313604863453.json', 'var_function-call-2146303464074031221': 'file_storage/function-call-2146303464074031221.json'}

exec(code, env_args)
