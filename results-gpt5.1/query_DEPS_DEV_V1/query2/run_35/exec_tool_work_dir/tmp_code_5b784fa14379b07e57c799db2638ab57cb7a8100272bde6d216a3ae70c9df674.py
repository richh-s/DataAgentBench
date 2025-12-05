code = """import pandas as pd, json
from pathlib import Path

path = Path(var_call_gxTgALSTKBiZ55pCkLghy7It)
records = json.loads(path.read_text())
pkg_df = pd.DataFrame(records)[['System','Name','Version']].drop_duplicates()

values = []
for _, row in pkg_df.iterrows():
    s = row['System'].replace("'", "''")
    n = row['Name'].replace("'", "''")
    v = row['Version'].replace("'", "''")
    values.append(f"('{s}','{n}','{v}')")

values_sql = ",".join(values)

join_query = "CREATE TEMP TABLE npm_mit_release AS SELECT * FROM (VALUES " + values_sql + ") AS t(System, Name, Version); " \
    + "SELECT p.System, p.Name, p.Version, pp.ProjectName FROM npm_mit_release p JOIN project_packageversion pp ON p.System = pp.System AND p.Name = pp.Name AND p.Version = pp.Version WHERE pp.ProjectType = 'GITHUB';"

print("__RESULT__:")
print(json.dumps(join_query))"""

env_args = {'var_call_gxTgALSTKBiZ55pCkLghy7It': 'file_storage/call_gxTgALSTKBiZ55pCkLghy7It.json', 'var_call_u3qdge9zUQ9XFwgqchhnKAjQ': ['project_info', 'project_packageversion']}

exec(code, env_args)
