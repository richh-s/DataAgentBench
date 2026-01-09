code = """import json
import pandas as pd

# Load repo list from file path
path = var_call_XgSDe5Ce6OMsj82l8GW6iy1y
with open(path, 'r', encoding='utf-8') as f:
    repos = json.load(f)
repo_names = [r['repo_name'] for r in repos]

# Build duckdb IN list safely by JSON dumping each string
# but for SQL we need single quotes doubled
def sql_quote(s):
    return "'" + s.replace("'","''") + "'"

# If empty, result is 0
if not repo_names:
    result = json.dumps(0)
else:
    # Chunk to avoid overly long queries
    chunks = [repo_names[i:i+500] for i in range(0, len(repo_names), 500)]
    counts = []
    for ch in chunks:
        in_list = ','.join(sql_quote(x) for x in ch)
        q = f"""
        SELECT COUNT(*)::BIGINT AS cnt
        FROM commits
        WHERE repo_name IN ({in_list})
          AND message IS NOT NULL
          AND length(message) < 1000
          AND lower(message) NOT LIKE 'merge%'
          AND lower(message) NOT LIKE 'update%'
          AND lower(message) NOT LIKE 'test%'
        """
        counts.append(q)
    out = json.dumps({'queries': counts})

print('__RESULT__:')
print(out)"""

env_args = {'var_call_XgSDe5Ce6OMsj82l8GW6iy1y': 'file_storage/call_XgSDe5Ce6OMsj82l8GW6iy1y.json', 'var_call_ErqNY2aK18MkyRAfvm5kGJgR': [{'cnt': '15016'}]}

exec(code, env_args)
