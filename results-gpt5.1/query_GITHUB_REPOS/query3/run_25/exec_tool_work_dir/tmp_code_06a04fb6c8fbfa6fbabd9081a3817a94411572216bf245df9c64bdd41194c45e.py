code = """import json, pandas as pd
from pathlib import Path

path = Path(var_call_go05Wk3xvJMfmFUt9HSgvM1G)
repos = pd.read_json(path).repo_name.unique().tolist()
# To keep query size reasonable, we'll pass repos as a temp table via VALUES
values = ",".join([f"('{r.replace("'","''")}')" for r in repos])
query = f"SELECT COUNT(*) AS cnt FROM commits WHERE repo_name IN (SELECT column1 AS repo_name FROM (VALUES {values})) AND message IS NOT NULL AND length(message) < 1000 AND lower(message) NOT LIKE 'merge%' AND lower(message) NOT LIKE 'update%' AND lower(message) NOT LIKE 'test%';"

result = json.dumps(query)
print("__RESULT__:")
print(result)"""

env_args = {'var_call_go05Wk3xvJMfmFUt9HSgvM1G': 'file_storage/call_go05Wk3xvJMfmFUt9HSgvM1G.json'}

exec(code, env_args)
