code = """import json
import pandas as pd

repos_file = var_call_HiJCbap0dySGavBqOT20aiEe
repos = pd.read_json(repos_file, typ='series').tolist()

# To avoid excessively long SQL, limit the number of repos per chunk
chunk_size = 900
chunks = [repos[i:i+chunk_size] for i in range(0, len(repos), chunk_size)]

conditions = []
for chunk in chunks:
    escaped = ["'" + r.replace("'", "''") + "'" for r in chunk]
    conditions.append("LOWER(repo_name) IN (" + ",".join(escaped) + ")")

where_clause = "(" + " OR ".join(conditions) + ")"

query = "SELECT COUNT(*) AS cnt FROM commits WHERE " + where_clause + " AND message IS NOT NULL AND LENGTH(message) < 1000 AND LOWER(subject) NOT LIKE 'merge%' AND LOWER(subject) NOT LIKE 'update%' AND LOWER(subject) NOT LIKE 'test%';"

print("__RESULT__:")
print(json.dumps(query))"""

env_args = {'var_call_2D46pc7KBPHkqvEf40mUTLaN': 'file_storage/call_2D46pc7KBPHkqvEf40mUTLaN.json', 'var_call_X1iywMlQtF1evGiqmGnWDDQy': 'file_storage/call_X1iywMlQtF1evGiqmGnWDDQy.json', 'var_call_HiJCbap0dySGavBqOT20aiEe': 'file_storage/call_HiJCbap0dySGavBqOT20aiEe.json'}

exec(code, env_args)
