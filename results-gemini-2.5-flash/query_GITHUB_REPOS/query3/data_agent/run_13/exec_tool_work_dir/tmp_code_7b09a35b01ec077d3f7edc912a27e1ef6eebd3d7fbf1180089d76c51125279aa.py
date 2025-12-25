code = """import json

with open(locals()['var_function-call-8063691937234990429'], 'r') as f:
    repo_names_data = json.load(f)

repo_names = [repo['repo_name'] for repo in repo_names_data['results']]

batch_size = 100
repo_name_batches = [repo_names[i:i + batch_size] for i in range(0, len(repo_names), batch_size)]

queries = []
for batch in repo_name_batches:
    repo_name_in_clause = ', '.join([f"'{repo}'" for repo in batch])
    query = f"""SELECT COUNT(message) AS commit_count
        FROM commits
        WHERE
            repo_name IN ({repo_name_in_clause}) AND
            message IS NOT NULL AND
            LENGTH(message) < 1000 AND
            NOT (message LIKE 'merge%' OR message LIKE 'update%' OR message LIKE 'test%');"""
    queries.append(query)

print("__RESULT__:")
print(json.dumps(queries))"""

env_args = {'var_function-call-8063691937234990429': 'file_storage/function-call-8063691937234990429.json'}

exec(code, env_args)
