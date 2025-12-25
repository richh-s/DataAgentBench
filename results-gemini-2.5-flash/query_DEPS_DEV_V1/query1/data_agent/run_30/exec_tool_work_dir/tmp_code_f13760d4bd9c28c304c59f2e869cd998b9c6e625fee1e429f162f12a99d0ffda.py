code = """import pandas as pd

latest_releases = pd.read_json(locals()['var_function-call-14792413543603152937'])
project_packageversion_data = pd.read_json(locals()['var_function-call-11276087383552559208'])

# Merge to get ProjectName for latest releases
merged_data = pd.merge(latest_releases,
                       project_packageversion_data[['Name', 'Version', 'ProjectName']],
                       on=['Name', 'Version'],
                       how='inner')

# Get unique project names to query project_info
unique_project_names = merged_data['ProjectName'].unique().tolist()

print('__RESULT__:')
print(pd.DataFrame({'ProjectName': unique_project_names}).to_json(orient='records'))"""

env_args = {'var_function-call-17052421974825312040': 'file_storage/function-call-17052421974825312040.json', 'var_function-call-14792413543603152937': 'file_storage/function-call-14792413543603152937.json', 'var_function-call-11276087383552559208': 'file_storage/function-call-11276087383552559208.json'}

exec(code, env_args)
