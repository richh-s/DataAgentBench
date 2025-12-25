code = """import pandas as pd
import re
import json

latest_releases_with_project = pd.read_json(locals()['var_function-call-4019896437681382581'])
project_info_raw = pd.read_json(locals()['var_function-call-9924848683352055014'])

# Extract ProjectName from Project_Information for merging
project_info_df = project_info_raw.copy()
project_info_df['ProjectName'] = project_info_df['Project_Information'].apply(lambda x: re.search(r'The project ([a-zA-Z0-9_-]+/[a-zA-Z0-9_.-]+) is hosted on GitHub', x) or re.search(r'The GitHub project ([a-zA-Z0-9_-]+/[a-zA-Z0-9_.-]+)', x))
project_info_df['ProjectName'] = project_info_df['ProjectName'].apply(lambda x: x.group(1) if x else None)

# Extract star count from Project_Information
project_info_df['Stars'] = project_info_df['Project_Information'].apply(lambda x: int(re.search(r'stars count of (\d+)', x).group(1)) if re.search(r'stars count of (\d+)', x) else 0)
project_info_df['Stars'] = project_info_df['Project_Information'].apply(lambda x: int(re.search(r'total of (\d+,?\d*) stars', x).group(1).replace(',', '')) if re.search(r'total of (\d+,?\d*) stars', x) else project_info_df['Stars'])
project_info_df['Stars'] = project_info_df['Project_Information'].apply(lambda x: int(re.search(r'(\d+) stars', x).group(1)) if re.search(r'(\d+) stars', x) and re.search(r'stars count of (\d+)', x) is None and re.search(r'total of (\d+,?\d*) stars', x) is None else project_info_df['Stars'])


# Merge the dataframes
final_df = pd.merge(latest_releases_with_project, project_info_df, on='ProjectName', how='inner')

# Group by package name and version to ensure distinct latest releases are considered
# Take the maximum stars in case a package version maps to multiple projects with different star counts
top_packages = final_df.groupby(['Name', 'Version'])['Stars'].max().reset_index()

# Sort by Stars and get the top 5
top_5_popular = top_packages.sort_values(by='Stars', ascending=False).head(5)

result = top_5_popular.to_json(orient='records')
print('__RESULT__:')
print(result)"""

env_args = {'var_function-call-11444979742191410607': ['packageinfo'], 'var_function-call-6475892482026271473': 'file_storage/function-call-6475892482026271473.json', 'var_function-call-1011998616401049187': ['project_info', 'project_packageversion'], 'var_function-call-9258655881987030810': 'file_storage/function-call-9258655881987030810.json', 'var_function-call-4019896437681382581': 'file_storage/function-call-4019896437681382581.json', 'var_function-call-9924848683352055014': 'file_storage/function-call-9924848683352055014.json'}

exec(code, env_args)
