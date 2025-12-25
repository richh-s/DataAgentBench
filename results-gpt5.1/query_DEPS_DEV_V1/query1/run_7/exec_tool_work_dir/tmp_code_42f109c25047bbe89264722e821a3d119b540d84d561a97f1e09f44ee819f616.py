code = """import pandas as pd, json
import os

# Load full NPM packageinfo result
file_path = var_call_nyrbYaNUMrfMgO7qvjkRDmMK
with open(file_path, 'r') as f:
    package_rows = json.load(f)

pkg_df = pd.DataFrame(package_rows)

# Keep only latest version per (System, Name) using UpstreamPublishedAt if available, else VersionInfo Ordinal, else max Version lexicographically
# Need more fields, so re-query not possible here; instead, just dedupe by Name taking the last occurrence (approximation)
# To improve, we should actually requery needed cols later; for now, compute distinct NPM names list.

npm_names = pkg_df['Name'].unique().tolist()

result = json.dumps(npm_names[:1000])
print("__RESULT__:")
print(result)"""

env_args = {'var_call_nyrbYaNUMrfMgO7qvjkRDmMK': 'file_storage/call_nyrbYaNUMrfMgO7qvjkRDmMK.json', 'var_call_TjSktaNgsJRC5SF2Yh2OGJ33': ['project_info', 'project_packageversion'], 'var_call_4DklVgFjNvduTbppym443oOc': 'file_storage/call_4DklVgFjNvduTbppym443oOc.json', 'var_call_QaAMedsQtcFkDP9W52BRQOuz': 'file_storage/call_QaAMedsQtcFkDP9W52BRQOuz.json'}

exec(code, env_args)
