code = """import json
# Load the repo list from the stored file path
path = var_call_Jvt6w3g9w3RbuxM50OUt8gLe
with open(path, 'r', encoding='utf-8') as f:
    repos = json.load(f)

# Ensure unique, lowercased
repos = sorted(list({r.lower() for r in repos}))

# Escape single quotes
def esc(s):
    return s.replace("'", "''")

chunk_size = 500
queries = []
for i in range(0, len(repos), chunk_size):
    chunk = repos[i:i+chunk_size]
    items = ["'" + esc(r) + "'" for r in chunk]
    in_list = ",".join(items)
    q = (
        "SELECT COUNT(*) AS cnt FROM commits WHERE lower(repo_name) IN (" + in_list + ") "
        "AND message IS NOT NULL AND message <> '' "
        "AND length(message) < 1000 "
        "AND NOT lower(message) LIKE 'merge%' "
        "AND NOT lower(message) LIKE 'update%' "
        "AND NOT lower(message) LIKE 'test%';"
    )
    queries.append(q)

print("__RESULT__:")
print(json.dumps(queries))"""

env_args = {'var_call_6aN3CzElB6ohUyLRkF7mru3h': 'file_storage/call_6aN3CzElB6ohUyLRkF7mru3h.json', 'var_call_Jvt6w3g9w3RbuxM50OUt8gLe': 'file_storage/call_Jvt6w3g9w3RbuxM50OUt8gLe.json', 'var_call_IWU1n8w8gXnYc3cI6cSaHeTg': "SELECT COUNT(*) AS cnt FROM commits WHERE lower(repo_name) IN ('f','i','l','e','_','s','t','o','r','a','g','e','/','c','a','l','l','_','j','v','t','6','w','3','g','9','w','3','r','b','u','x','m','5','0','o','u','t','8','g','l','e','.','j','s','o','n') AND message IS NOT NULL AND message <> '' AND length(message) < 1000 AND NOT lower(message) LIKE 'merge%' AND NOT lower(message) LIKE 'update%' AND NOT lower(message) LIKE 'test%';"}

exec(code, env_args)
