code = """import json, pandas as pd

# Load swift repos list from the sqlite query result file
path = var_call_nozFEbqmS9STd9jfyiCfvxay
with open(path, 'r', encoding='utf-8') as f:
    swift_repos = [r['repo_name'] for r in json.load(f)]

# Format for SQL IN clause
# Escape single quotes just in case
swift_repos_escaped = [s.replace("'","''") for s in swift_repos]

# Chunk to avoid huge IN lists
chunks = [swift_repos_escaped[i:i+500] for i in range(0, len(swift_repos_escaped), 500)]

queries = []
for ch in chunks:
    in_list = ",".join([f"'{x}'" for x in ch])
    q = f"""
    SELECT id,
           any_value(sample_repo_name) AS repo_name,
           max(try_cast(regexp_extract(repo_data_description, 'copies\\s*:\\s*([0-9]+)', 1) AS BIGINT)) AS copies
    FROM contents
    WHERE lower(sample_path) LIKE '%.swift'
      AND sample_repo_name IN ({in_list})
      AND lower(coalesce(repo_data_description,'')) NOT LIKE '%binary%: true%'
      AND lower(coalesce(repo_data_description,'')) NOT LIKE '%binary: true%'
    GROUP BY id
    """
    queries.append(q)

out = {"swift_repo_count": len(swift_repos), "chunk_queries": queries}
print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_MaspD0JKWxcVqwqMJs8pP4ei': ['languages', 'repos', 'licenses'], 'var_call_S7eIxS0Nz9UmVkBjf3Y4aT7A': ['commits', 'contents', 'files'], 'var_call_nozFEbqmS9STd9jfyiCfvxay': 'file_storage/call_nozFEbqmS9STd9jfyiCfvxay.json'}

exec(code, env_args)
