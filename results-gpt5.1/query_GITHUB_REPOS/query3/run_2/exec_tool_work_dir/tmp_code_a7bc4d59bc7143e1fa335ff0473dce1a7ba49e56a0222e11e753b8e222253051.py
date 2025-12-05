code = """import json
import pandas as pd

shell_file = var_call_nsdnsY64nTLM6HkDsGGv4ma5
apache_file = var_call_Ks0miRyJj8YOp4CjnjwuQir3

shell_df = pd.read_json(shell_file)
apache_df = pd.read_json(apache_file)

shell_repos = set(shell_df['repo_name'])
apache_repos = set(apache_df['repo_name'])

eligible_repos = shell_repos & apache_repos

# Build an IN clause chunked query for DuckDB
eligible_list = sorted(eligible_repos)

chunks = []
chunk_size = 900
for i in range(0, len(eligible_list), chunk_size):
    chunk = eligible_list[i:i+chunk_size]
    in_list = ",".join("'" + r.replace("'", "''") + "'" for r in chunk)
    clause = f"repo_name IN ({in_list})"
    chunks.append(clause)

where_clause = " OR ".join(chunks)

query = "SELECT COUNT(*) AS cnt FROM commits WHERE (" + where_clause + ") AND message IS NOT NULL AND LENGTH(message) < 1000 AND LOWER(message) NOT LIKE 'merge%' AND LOWER(message) NOT LIKE 'update%' AND LOWER(message) NOT LIKE 'test%';"

print("__RESULT__:")
print(json.dumps(query))"""

env_args = {'var_call_nsdnsY64nTLM6HkDsGGv4ma5': 'file_storage/call_nsdnsY64nTLM6HkDsGGv4ma5.json', 'var_call_Ks0miRyJj8YOp4CjnjwuQir3': 'file_storage/call_Ks0miRyJj8YOp4CjnjwuQir3.json', 'var_call_jGvDcnjLClszrgfL2xsSAG22': [{'cnt': '15016'}], 'var_call_Np8uFfNNWcdKtzcoj7jSdpcL': 114972}

exec(code, env_args)
