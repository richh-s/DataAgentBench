code = """import json, pandas as pd

# Load NPM packageinfo
file_path = var_call_Hbey6xNOqMjaSZ1IVysH5JaU
with open(file_path, 'r') as f:
    npm_packages = json.load(f)

pkg_df = pd.DataFrame(npm_packages)
# keep latest version per (System, Name) using UpstreamPublishedAt if available, else max Version lexicographically
# Need UpstreamPublishedAt so reload with that column

result = pkg_df[['System','Name','Version']].drop_duplicates().head(5).to_dict(orient='records')

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_Hbey6xNOqMjaSZ1IVysH5JaU': 'file_storage/call_Hbey6xNOqMjaSZ1IVysH5JaU.json', 'var_call_MdpyJgu8fAkYLLBHUPFCaQCZ': ['project_info', 'project_packageversion'], 'var_call_eZWUAUoRnlsdMSQHJozG19dk': 'file_storage/call_eZWUAUoRnlsdMSQHJozG19dk.json'}

exec(code, env_args)
