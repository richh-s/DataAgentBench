code = """import json
repos = var_call_Jvt6w3g9w3RbuxM50OUt8gLe
# repos is a list of repo_name strings
# Build SQL IN list, escaping single quotes
def esc(s):
    return s.replace("'", "''")
items = ["'" + esc(r.lower()) + "'" for r in repos]
# chunk size to avoid extremely long single query? We'll attempt single query
in_list = ",".join(items)
sql = (
    "SELECT COUNT(*) AS cnt FROM commits WHERE lower(repo_name) IN (" + in_list + ") "
    "AND message IS NOT NULL AND message <> '' "
    "AND length(message) < 1000 "
    "AND NOT lower(message) LIKE 'merge%' "
    "AND NOT lower(message) LIKE 'update%' "
    "AND NOT lower(message) LIKE 'test%';"
)
print("__RESULT__:")
print(json.dumps(sql))"""

env_args = {'var_call_6aN3CzElB6ohUyLRkF7mru3h': 'file_storage/call_6aN3CzElB6ohUyLRkF7mru3h.json', 'var_call_Jvt6w3g9w3RbuxM50OUt8gLe': 'file_storage/call_Jvt6w3g9w3RbuxM50OUt8gLe.json'}

exec(code, env_args)
