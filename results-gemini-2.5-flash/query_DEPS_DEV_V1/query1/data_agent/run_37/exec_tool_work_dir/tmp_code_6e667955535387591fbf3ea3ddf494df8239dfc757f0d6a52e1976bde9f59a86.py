code = """import json
import pandas as pd
import re

df_latest_releases = pd.read_json(locals()['var_function-call-3659017771143639660'])
project_packageversion_data = pd.read_json(locals()['var_function-call-11794616991749621324'])
df_project_packageversion = pd.DataFrame(project_packageversion_data)

# Read the full project_info data from the JSON file
with open(locals()['var_function-call-12597064572185373823'], 'r') as f:
    project_info_full_data = json.load(f)
df_project_info = pd.DataFrame(project_info_full_data)

# Merge to get ProjectName for the latest release versions
df_merged = pd.merge(
    df_latest_releases,
    df_project_packageversion,
    on=['Name', 'Version'],
    how='inner'
)

# Extract ProjectName and stars from Project_Information
def extract_github_info(info):
    project_name_match = re.search(r'The project ([^\\s]+/[^\\s]+) (?:on GitHub )?is hosted on GitHub', info)
    stars_match = re.search(r'stars(?: count)? of (\d+,?\d*)', info)
    project_name = project_name_match.group(1) if project_name_match else None
    stars = int(stars_match.group(1).replace(',', '')) if stars_match else 0
    return project_name, stars

df_project_info[['ProjectName', 'Stars']] = df_project_info['Project_Information'].apply(lambda x: pd.Series(extract_github_info(x)))

# Merge with the latest releases to get star counts
df_final_merged = pd.merge(
    df_merged,
    df_project_info[['ProjectName', 'Stars']],
    on='ProjectName',
    how='inner'
)

# Group by package name to get distinct packages and their latest versions with max stars
# In case of multiple project names for a single package version, we will take the max stars
df_final_merged = df_final_merged.loc[df_final_merged.groupby('Name')['Stars'].idxmax()]

# Sort by stars and get the top 5
df_top5_packages = df_final_merged.sort_values(by='Stars', ascending=False).head(5)

print("__RESULT__:")
print(df_top5_packages[['Name', 'Version', 'Stars']].to_json(orient='records'))"""

env_args = {'var_function-call-10276716253468333046': 'file_storage/function-call-10276716253468333046.json', 'var_function-call-4732325282894234512': 'file_storage/function-call-4732325282894234512.json', 'var_function-call-3659017771143639660': 'file_storage/function-call-3659017771143639660.json', 'var_function-call-11794616991749621324': 'file_storage/function-call-11794616991749621324.json', 'var_function-call-2336050334430510316': 'file_storage/function-call-2336050334430510316.json', 'var_function-call-11053164319625339069': ['project_info', 'project_packageversion'], 'var_function-call-3111109347744898566': [{'Project_Information': 'The project lberrocal/npm-packages-template is hosted on GitHub and currently has 0 open issues, 0 stars, and 0 forks.'}, {'Project_Information': 'The project leaflet/leaflet on GitHub is a popular open-source library that currently has 521 open issues, 38715 stars, and 5782 forks, making it a widely recognized tool in the developer community.'}, {'Project_Information': 'The project leaflet/leaflet.fullscreen on GitHub currently has 29 open issues, 417 stars, and 118 forks, making it a noteworthy contribution to the Leaflet ecosystem.'}, {'Project_Information': 'The project leaflet/leaflet.markercluster is hosted on GitHub and currently has an open issues count of 130, along with a stars count of 3761 and forks count of 988.'}, {'Project_Information': 'The project leandrowd/react-responsive-carousel on GitHub has garnered significant attention, with a total of 2,534 stars and 636 forks, while currently having 23 open issues.'}, {'Project_Information': 'The project is hosted on GitHub under the name learnfrontend-dc/product-cart, and it currently has 2 open issues. It has garnered a total of 11 stars and has been forked 12 times.'}, {'Project_Information': 'The GitHub project ledgerproject/keypairoom currently has 3 open issues, 3 stars, and 0 forks.'}, {'Project_Information': 'The project leebyron/jasmine-check is hosted on GitHub and currently has 0 open issues, 11 stars, and 3 forks.'}, {'Project_Information': 'The project leebyron/testcheck-js on GitHub has an open issues count of 29, a stars count of 1185, and a forks count of 58, making it a notable repository in the community.'}, {'Project_Information': 'The project leecade/react-native-swiper is hosted on GitHub and has a total of 786 open issues, along with an impressive 10,249 stars and 2,392 forks, making it a popular choice among developers for implementing swiping functionality in React Native applications.'}], 'var_function-call-12597064572185373823': 'file_storage/function-call-12597064572185373823.json', 'var_function-call-8392644207533064250': [{'Name': '@dwarvesf/react-scripts>0.7.0>rx-lite', 'Version': '3.1.2', 'Stars': 19496.0}, {'Name': '@duik/container-vertical', 'Version': '0.4.0', 'Stars': 201.0}, {'Name': '@duik/top-bar-title', 'Version': '0.1.7', 'Stars': 201.0}, {'Name': '@duik/create-simple-component', 'Version': '0.5.3', 'Stars': 201.0}, {'Name': '@duik/base-input', 'Version': '0.5.3', 'Stars': 201.0}]}

exec(code, env_args)
