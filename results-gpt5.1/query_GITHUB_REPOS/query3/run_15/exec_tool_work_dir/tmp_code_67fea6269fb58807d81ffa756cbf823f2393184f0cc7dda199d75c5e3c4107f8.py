code = """import json

with open(var_call_KOdNwcDiXipxbYeYFwhiDLWP, 'r') as f:
    chunks = json.load(f)

# Build WHERE clause for repo_name IN (...) across chunks
where_clauses = []
for chunk in chunks:
    escaped = ["'" + r.replace("'", "''") + "'" for r in chunk]
    where_clauses.append("repo_name IN (" + ",".join(escaped) + ")")

full_where = " OR ".join(where_clauses)

query = f"SELECT COUNT(*) AS cnt FROM commits WHERE ({full_where}) AND message IS NOT NULL AND LENGTH(message) < 1000 AND LOWER(SUBSTR(TRIM(message), 1, 5)) NOT IN ('merge', 'updat', 'test');"

print("__RESULT__:")
print(json.dumps(query))"""

env_args = {'var_call_SNrQ0slpUKEPQAUhUt13enxt': 'file_storage/call_SNrQ0slpUKEPQAUhUt13enxt.json', 'var_call_Zu74SkUXnHb5xmQ91HiBBHEC': [{'cnt': '15019'}], 'var_call_KOdNwcDiXipxbYeYFwhiDLWP': 'file_storage/call_KOdNwcDiXipxbYeYFwhiDLWP.json'}

exec(code, env_args)
