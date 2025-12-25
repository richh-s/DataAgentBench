code = """import json
import math
import pandas as pd

batches_file = var_call_LizeJlgeDbiRxaEqiU09tB2j
with open(batches_file) as f:
    data = json.load(f)

batches = data['batches']

queries = []
for batch in batches:
    if not batch:
        continue
    in_list = ','.join("'" + r.replace("'", "''") + "'" for r in batch)
    q = f"SELECT COUNT(*) AS cnt FROM commits WHERE repo_name IN ({in_list}) AND message IS NOT NULL AND LENGTH(message) < 1000 AND LOWER(TRIM(subject)) NOT LIKE 'merge%' AND LOWER(TRIM(subject)) NOT LIKE 'update%' AND LOWER(TRIM(subject)) NOT LIKE 'test%';"
    queries.append(q)

result = json.dumps(queries)

print("__RESULT__:")
print(result)"""

env_args = {'var_call_FbyMTaA1aM1pmMdc8aEKy8IY': 'file_storage/call_FbyMTaA1aM1pmMdc8aEKy8IY.json', 'var_call_g8AGlbliJV88hORIAk0q9D7U': 'file_storage/call_g8AGlbliJV88hORIAk0q9D7U.json', 'var_call_CXOtMW9Ov9JD7vUjxVzUcRw8': [{'cnt': '15014'}], 'var_call_LizeJlgeDbiRxaEqiU09tB2j': 'file_storage/call_LizeJlgeDbiRxaEqiU09tB2j.json'}

exec(code, env_args)
