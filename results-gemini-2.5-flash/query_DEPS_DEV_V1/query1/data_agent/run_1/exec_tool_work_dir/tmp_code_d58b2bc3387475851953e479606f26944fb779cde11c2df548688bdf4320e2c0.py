code = """import pandas as pd
import json
import re

latest_releases_with_project_df = pd.read_json(locals()['var_function-call-13599132215489228585'])
project_info_df = pd.read_json(locals()['var_function-call-7140646661957748403'])

# Extract ProjectName and Stars from Project_Information
def extract_project_info(project_info_str):
    project_name_match = re.search(r"The project (.+?) on GitHub", project_info_str)
    stars_match = re.search(r"(\d{1,3}(?:,\d{3})*|\d+) stars", project_info_str)
    project_name = project_name_match.group(1).strip().replace('named ', '') if project_name_match else None
    stars = int(stars_match.group(1).replace(',', '')) if stars_match else 0
    return project_name, stars

project_info_df[['ExtractedProjectName', 'Stars']] = project_info_df['Project_Information'].apply(lambda x: pd.Series(extract_project_info(x)))

# Filter out rows where ExtractedProjectName is None
project_info_df_cleaned = project_info_df.dropna(subset=['ExtractedProjectName'])

# Merge with the latest releases DataFrame
final_df = pd.merge(latest_releases_with_project_df,
                    project_info_df_cleaned[['ExtractedProjectName', 'Stars']],
                    left_on='ProjectName',
                    right_on='ExtractedProjectName',
                    how='inner')

# Sort by Stars in descending order and get the top 5
top_5_packages = final_df.sort_values(by='Stars', ascending=False).drop_duplicates(subset = ['Name']).head(5)

# Format the result
result = top_5_packages[['Name', 'Version', 'Stars']].to_json(orient='records')

print('__RESULT__:')
print(result)"""

env_args = {'var_function-call-2495042024869739884': 'file_storage/function-call-2495042024869739884.json', 'var_function-call-2823689990461768366': 'file_storage/function-call-2823689990461768366.json', 'var_function-call-17895442689244187363': 'file_storage/function-call-17895442689244187363.json', 'var_function-call-13599132215489228585': 'file_storage/function-call-13599132215489228585.json', 'var_function-call-7140646661957748403': 'file_storage/function-call-7140646661957748403.json'}

exec(code, env_args)
