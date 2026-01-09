code = """import json, pandas as pd

# var_call_2YS6k9nzzOQ9o9HHjIzL6sGk is a file path with repo_name list
path = var_call_2YS6k9nzzOQ9o9HHjIzL6sGk
with open(path, 'r', encoding='utf-8') as f:
    repos = json.load(f)
repo_names = [r['repo_name'] for r in repos]

# Chunk repo_names to avoid very long IN clauses
chunks = [repo_names[i:i+500] for i in range(0, len(repo_names), 500)]
queries = []
for ch in chunks:
    in_list = ','.join(["'" + x.replace("'","''") + "'" for x in ch])
    q = f"""SELECT COUNT(*) AS cnt
            FROM commits
            WHERE repo_name IN ({in_list})
              AND message IS NOT NULL
              AND length(message) < 1000
              AND NOT regexp_matches(lower(message), '^(merge|update|test)');"""
    queries.append(q)

# Print queries as JSON array for sequential execution outside python isn't allowed,
# so instead compute by running each query via duckdb is not available here.
# We'll just output the list of queries to run.
result = json.dumps(queries)
print('__RESULT__:')
print(result)"""

env_args = {'var_call_2YS6k9nzzOQ9o9HHjIzL6sGk': 'file_storage/call_2YS6k9nzzOQ9o9HHjIzL6sGk.json', 'var_call_RXEbwrhEsMWYvmk9emYNy5Fo': [{'commit_message_count': '15016'}]}

exec(code, env_args)
