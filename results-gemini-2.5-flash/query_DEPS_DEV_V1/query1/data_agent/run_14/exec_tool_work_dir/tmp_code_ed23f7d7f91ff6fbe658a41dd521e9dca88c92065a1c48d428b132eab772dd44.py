code = """import pandas as pd

merged_df = pd.read_json(locals()['var_function-call-15902394642716762254'])
project_stars_df = pd.read_json(locals()['var_function-call-14480788834966941430'])

# Merge to get stars for each project
final_df = pd.merge(merged_df, project_stars_df, on='ProjectName', how='inner')

# Group by package name and version, taking the maximum stars (in case of duplicate ProjectName for a package version)
final_df = final_df.groupby(['Name', 'Version', 'ProjectName'])['Stars'].max().reset_index()

# Sort by stars and get the top 5
top_5_packages = final_df.sort_values(by='Stars', ascending=False).head(5)

result = top_5_packages[['Name', 'Version', 'Stars']].to_json(orient='records')

print("__RESULT__:")
print(result)"""

env_args = {'var_function-call-18442683985073922078': 'file_storage/function-call-18442683985073922078.json', 'var_function-call-15828687765445895216': 'file_storage/function-call-15828687765445895216.json', 'var_function-call-17954856618360052339': 'file_storage/function-call-17954856618360052339.json', 'var_function-call-15902394642716762254': 'file_storage/function-call-15902394642716762254.json', 'var_function-call-16578664634641431138': ['project_info', 'project_packageversion'], 'var_function-call-962002978812241716': [{'Project_Information': 'The project lberrocal/npm-packages-template is hosted on GitHub and currently has 0 open issues, 0 stars, and 0 forks.', 'Licenses': '[]', 'Description': 'Template for npm package library configured to be used with CI/CD', 'Homepage': 'None', 'OSSFuzz': 'nan'}], 'var_function-call-7004063310327144851': 'file_storage/function-call-7004063310327144851.json', 'var_function-call-14480788834966941430': 'file_storage/function-call-14480788834966941430.json'}

exec(code, env_args)
