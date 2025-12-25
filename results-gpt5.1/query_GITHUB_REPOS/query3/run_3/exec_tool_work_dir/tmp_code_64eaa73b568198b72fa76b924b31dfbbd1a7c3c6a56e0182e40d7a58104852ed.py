code = """import json, pandas as pd
from pathlib import Path

# Load full repo_name list
path = Path(var_call_wlFciQHnNGBs0lLfiNB1DK5H)
repos = json.loads(path.read_text())
repo_names = [r['repo_name'] for r in repos]

# Build an IN clause chunked to avoid overly large queries
chunks = []
chunk_size = 900
for i in range(0, len(repo_names), chunk_size):
    chunk = repo_names[i:i+chunk_size]
    in_list = ",".join(["'" + r.replace("'","''") + "'" for r in chunk])
    chunks.append(f"SELECT COUNT(*) AS cnt FROM commits WHERE repo_name IN ({in_list}) AND message IS NOT NULL AND LENGTH(message) < 1000 AND LOWER(TRIM(message)) NOT LIKE 'merge%' AND LOWER(TRIM(message)) NOT LIKE 'update%' AND LOWER(TRIM(message)) NOT LIKE 'test%'")

# Combine chunks with UNION ALL to sum later
queries = " UNION ALL ".join(chunks)

result = queries

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_wlFciQHnNGBs0lLfiNB1DK5H': 'file_storage/call_wlFciQHnNGBs0lLfiNB1DK5H.json', 'var_call_RYbLG2SWqb0ENBietbpbsnQj': [{'cnt': '15016'}]}

exec(code, env_args)
