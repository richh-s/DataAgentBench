code = """import pandas as pd
import json
import re

# Load the merged data containing package name, version, and project name
merged_package_project_df = pd.DataFrame(json.loads(open(locals()['var_function-call-3216871092368004526'], 'r').read()))

# Load project information with star counts
project_info_data = json.loads(open(locals()['var_function-call-7701970117348726494'], 'r').read())

# Create a list to store parsed project info
parsed_project_info = []

for project in project_info_data:
    info = project['Project_Information']
    
    # Extract ProjectName using regex
    project_name_match = re.search(r'The project (.+?) on GitHub', info)
    if not project_name_match:
        project_name_match = re.search(r'The GitHub project named (.+?) currently', info)
    if not project_name_match:
        project_name_match = re.search(r'The project is hosted on GitHub under the name (.+?), and it currently has', info)
    if not project_name_match:
        project_name_match = re.search(r'The project named (.+?) is hosted on GitHub', info)
    
    project_name = project_name_match.group(1).strip() if project_name_match else None

    # Extract stars using regex
    stars_match = re.search(r'(\d{1,3}(?:,\d{3})*|\d+) stars', info)
    stars = int(stars_match.group(1).replace(',', '')) if stars_match else 0
    
    if project_name:
        parsed_project_info.append({'ProjectName': project_name, 'Stars': stars})

# Create a DataFrame for parsed project info
project_stars_df = pd.DataFrame(parsed_project_info)

# Merge the dataframes to combine package info with stars
final_df = pd.merge(merged_package_project_df, project_stars_df, on='ProjectName', how='inner')

# Sort by stars and get the top 5 unique packages based on name
top_5_packages = final_df.sort_values(by='Stars', ascending=False).drop_duplicates(subset=['Name']).head(5)

# Select the required columns for the final output
result = top_5_packages[['Name', 'Version', 'Stars']]

print("__RESULT__:")
print(result.to_json(orient='records'))"""

env_args = {'var_function-call-13869052368742656528': 'file_storage/function-call-13869052368742656528.json', 'var_function-call-4179847827954287643': 'file_storage/function-call-4179847827954287643.json', 'var_function-call-12412451248896417788': 'file_storage/function-call-12412451248896417788.json', 'var_function-call-3216871092368004526': 'file_storage/function-call-3216871092368004526.json', 'var_function-call-7701970117348726494': 'file_storage/function-call-7701970117348726494.json'}

exec(code, env_args)
