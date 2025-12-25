code = """import json, pandas as pd
from pathlib import Path

pkg_path = Path(var_call_gxTgALSTKBiZ55pCkLghy7It)
proj_path = Path(var_call_dg33ifVrAPTZ7q985JZueKb6)

pkg_df = pd.DataFrame(json.loads(pkg_path.read_text()))[['System','Name','Version']].drop_duplicates()
proj_df = pd.DataFrame(json.loads(proj_path.read_text()))[['System','Name','Version','ProjectName']].drop_duplicates()

merged = pkg_df.merge(proj_df, on=['System','Name','Version'], how='inner')
projects = merged['ProjectName'].dropna().unique().tolist()

result = {'project_count': len(projects), 'sample_projects': projects[:20]}

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_gxTgALSTKBiZ55pCkLghy7It': 'file_storage/call_gxTgALSTKBiZ55pCkLghy7It.json', 'var_call_u3qdge9zUQ9XFwgqchhnKAjQ': ['project_info', 'project_packageversion'], 'var_call_PxhJ3XdhqDrTLmDe1uEtHtoT': 'file_storage/call_PxhJ3XdhqDrTLmDe1uEtHtoT.json', 'var_call_usmK5gNxZ5zat4MLBzwMOgWD': [{'Count': '1'}], 'var_call_dg33ifVrAPTZ7q985JZueKb6': 'file_storage/call_dg33ifVrAPTZ7q985JZueKb6.json'}

exec(code, env_args)
