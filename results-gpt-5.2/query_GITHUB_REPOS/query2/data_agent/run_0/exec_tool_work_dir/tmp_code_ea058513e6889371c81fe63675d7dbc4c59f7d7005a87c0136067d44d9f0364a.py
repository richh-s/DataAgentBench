code = """import json, pandas as pd

# load swift repos from sqlite result file
path = var_call_fS4uahqT4P6iZ6uDsshFgnIU
with open(path, 'r') as f:
    swift_repos = json.load(f)
repos = [r['repo_name'] for r in swift_repos]

# chunk repos to query duckdb contents
chunks = [repos[i:i+500] for i in range(0, len(repos), 500)]
rows = []
for ch in chunks:
    in_list = ','.join(["'" + x.replace("'","''") + "'" for x in ch])
    q = f"""
    SELECT DISTINCT id, sample_repo_name
    FROM contents
    WHERE lower(sample_path) LIKE '%.swift'
      AND sample_repo_name IN ({in_list})
      AND (repo_data_description IS NULL OR lower(repo_data_description) NOT LIKE '%binary%')
    """
    # query_db tool not available inside python; instead, accumulate queries to run outside
    rows.append(q)

result = {'repo_chunks': len(chunks), 'first_query': rows[0], 'last_query': rows[-1]}
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_myApm1BQz0AfqlS9o7qy2OWn': ['languages', 'repos', 'licenses'], 'var_call_qtxP5Juz9RSuJU0gpJ2hBc6N': ['commits', 'contents', 'files'], 'var_call_fS4uahqT4P6iZ6uDsshFgnIU': 'file_storage/call_fS4uahqT4P6iZ6uDsshFgnIU.json'}

exec(code, env_args)
