code = """import json, pandas as pd

# Load full results from files
with open(var_call_uftyPqYc1gi2yOLindNNkhPJ, 'r') as f:
    packageinfo = json.load(f)
with open(var_call_FLgVZuWzRVn5Bmob9mPxxi5T, 'r') as f:
    project_package = json.load(f)

pkg_df = pd.DataFrame(packageinfo)
proj_pkg_df = pd.DataFrame(project_package)

pkg_df['IsRelease'] = pkg_df['VersionInfo'].apply(lambda x: json.loads(x).get('IsRelease') if isinstance(x, str) else None)
pkg_df['HasMIT'] = pkg_df['Licenses'].apply(lambda x: 'MIT' in json.loads(x) if isinstance(x, str) and x.strip() else False)

filtered_pkg = pkg_df[(pkg_df['IsRelease'] == True) & (pkg_df['HasMIT'])][['System','Name','Version']]

merged = filtered_pkg.merge(proj_pkg_df, on=['System','Name','Version'], how='inner')

# project_info only has Project_Information and Homepage; ProjectName is embedded in Project_Information text.
# We still need fork counts which we assume appear like "Forks: <number>" in Project_Information.

proj_info = query_db_result_placeholder"""

env_args = {'var_call_uftyPqYc1gi2yOLindNNkhPJ': 'file_storage/call_uftyPqYc1gi2yOLindNNkhPJ.json', 'var_call_FLgVZuWzRVn5Bmob9mPxxi5T': 'file_storage/call_FLgVZuWzRVn5Bmob9mPxxi5T.json'}

exec(code, env_args)
