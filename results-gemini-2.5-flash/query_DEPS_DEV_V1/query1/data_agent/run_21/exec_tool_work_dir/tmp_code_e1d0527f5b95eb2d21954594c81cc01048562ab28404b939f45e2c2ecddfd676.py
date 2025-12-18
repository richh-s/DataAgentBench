code = """import json
import pandas as pd
import re

# Load the full result from the file
with open(locals()['var_function-call-16043436952945545173'], 'r') as f:
    merged_data = json.load(f)

df_merged_unique_projects = pd.DataFrame(merged_data)

# Load the full result from the file
with open(locals()['var_function-call-6386257081514175875'], 'r') as f:
    project_info_data = json.load(f)

df_project_info = pd.DataFrame(project_info_data)

# Function to parse Project_Information
def parse_project_info(info_string):
    project_name_match = re.search(r'The project (?:named )?([a-zA-Z0-9_-]+/[a-zA-Z0-9_.-]+) (?:is hosted on GitHub and )?currently has.*?, (\d+(?:,\d{3})*) stars(?:, and)?', info_string)
    if project_name_match:
        project_name = project_name_match.group(1)
        stars_str = project_name_match.group(2).replace(',', '')
        stars = int(stars_str)
        return {'ProjectName': project_name, 'Stars': stars}
    project_name_match_alt = re.search(r'The GitHub project (?:named )?([a-zA-Z0-9_-]+/[a-zA-Z0-9_.-]+) (?:is an open-source library that )?currently has.*?, (\d+(?:,\d{3})*) stars(?:, and)?', info_string)
    if project_name_match_alt:
        project_name = project_name_match_alt.group(1)
        stars_str = project_name_match_alt.group(2).replace(',', '')
        stars = int(stars_str)
        return {'ProjectName': project_name, 'Stars': stars}
    return None

# Apply the parsing function
parsed_project_info = df_project_info['Project_Information'].apply(parse_project_info)

# Filter out None values and convert to DataFrame
parsed_project_info = [item for item in parsed_project_info if item is not None]
df_parsed_project_info = pd.DataFrame(parsed_project_info)

# Merge with the latest releases data
df_final = pd.merge(df_merged_unique_projects,
                    df_parsed_project_info,
                    on='ProjectName',
                    how='inner')

# Sort by Stars and get top 5
top_5_packages = df_final.sort_values(by='Stars', ascending=False).head(5)

# Select desired columns and format output
result = top_5_packages[['Name', 'Version', 'Stars']].to_json(orient='records')
print('__RESULT__:')
print(result)"""

env_args = {'var_function-call-16890172847440563023': 'file_storage/function-call-16890172847440563023.json', 'var_function-call-13524775630133408629': 'file_storage/function-call-13524775630133408629.json', 'var_function-call-5327434771699848945': 'file_storage/function-call-5327434771699848945.json', 'var_function-call-16043436952945545173': 'file_storage/function-call-16043436952945545173.json', 'var_function-call-4616950896943763102': 'file_storage/function-call-4616950896943763102.json', 'var_function-call-6386257081514175875': 'file_storage/function-call-6386257081514175875.json'}

exec(code, env_args)
