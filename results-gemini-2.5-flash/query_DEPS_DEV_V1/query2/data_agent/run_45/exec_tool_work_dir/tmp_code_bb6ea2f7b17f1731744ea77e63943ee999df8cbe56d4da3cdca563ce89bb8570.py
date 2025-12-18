code = """import pandas as pd
import json
import re

merged_packages_projects_df = pd.read_json(locals()['var_function-call-4739559070795843551'])
project_info_df = pd.read_json(locals()['var_function-call-16343587294783752181'])

# Extract ProjectName and fork count from Project_Information
project_info_data = []
for index, row in project_info_df.iterrows():
    project_info_text = row['Project_Information']
    project_name_match = re.search(r'The project (\S+/\S+) is hosted on GitHub', project_info_text)
    if not project_name_match:
        project_name_match = re.search(r'The GitHub project named (\S+/\S+)', project_info_text)
    if not project_name_match:
        project_name_match = re.search(r'The project named (\S+/\S+) on GitHub', project_info_text)
    if not project_name_match:
        project_name_match = re.search(r'The project on GitHub, named (\S+/\S+), ', project_info_text)
    if not project_name_match:
        project_name_match = re.search(r'The project (\S+/\S+) on GitHub', project_info_text)
    
    project_name = project_name_match.group(1) if project_name_match else None
    forks_match = re.search(r'and (\d+,?\d*) forks', project_info_text)
    forks_count = int(forks_match.group(1).replace(',', '')) if forks_match else 0
    if project_name:
        project_info_data.append({'ProjectName': project_name, 'Forks': forks_count})

project_forks_df = pd.DataFrame(project_info_data)

# Merge with the combined package and project_packageversion data
final_merged_df = pd.merge(merged_packages_projects_df, project_forks_df, on='ProjectName', how='inner')

# Drop duplicate ProjectName entries, keeping the one with the highest fork count (if any duplicates exist)
final_merged_df = final_merged_df.sort_values(by='Forks', ascending=False).drop_duplicates(subset=['ProjectName'])

# Sort by Forks in descending order and get the top 5
top_5_projects = final_merged_df.sort_values(by='Forks', ascending=False).head(5)

result = top_5_projects[['ProjectName', 'Forks']].to_json(orient='records')
print('__RESULT__:')
print(result)"""

env_args = {'var_function-call-9752221296848005442': 'file_storage/function-call-9752221296848005442.json', 'var_function-call-1506412339707267862': 'file_storage/function-call-1506412339707267862.json', 'var_function-call-5731134246569357444': 'file_storage/function-call-5731134246569357444.json', 'var_function-call-4739559070795843551': 'file_storage/function-call-4739559070795843551.json', 'var_function-call-1664029801454547131': [{'Project_Information': 'The project lberrocal/npm-packages-template is hosted on GitHub and currently has 0 open issues, 0 stars, and 0 forks.'}, {'Project_Information': 'The project leaflet/leaflet on GitHub is a popular open-source library that currently has 521 open issues, 38715 stars, and 5782 forks, making it a widely recognized tool in the developer community.'}, {'Project_Information': 'The project leaflet/leaflet.fullscreen on GitHub currently has 29 open issues, 417 stars, and 118 forks, making it a noteworthy contribution to the Leaflet ecosystem.'}, {'Project_Information': 'The project leaflet/leaflet.markercluster is hosted on GitHub and currently has an open issues count of 130, along with a stars count of 3761 and forks count of 988.'}, {'Project_Information': 'The project leandrowd/react-responsive-carousel on GitHub has garnered significant attention, with a total of 2,534 stars and 636 forks, while currently having 23 open issues.'}, {'Project_Information': 'The project is hosted on GitHub under the name learnfrontend-dc/product-cart, and it currently has 2 open issues. It has garnered a total of 11 stars and has been forked 12 times.'}, {'Project_Information': 'The GitHub project ledgerproject/keypairoom currently has 3 open issues, 3 stars, and 0 forks.'}, {'Project_Information': 'The project leebyron/jasmine-check is hosted on GitHub and currently has 0 open issues, 11 stars, and 3 forks.'}, {'Project_Information': 'The project leebyron/testcheck-js on GitHub has an open issues count of 29, a stars count of 1185, and a forks count of 58, making it a notable repository in the community.'}, {'Project_Information': 'The project leecade/react-native-swiper is hosted on GitHub and has a total of 786 open issues, along with an impressive 10,249 stars and 2,392 forks, making it a popular choice among developers for implementing swiping functionality in React Native applications.'}], 'var_function-call-16343587294783752181': 'file_storage/function-call-16343587294783752181.json'}

exec(code, env_args)
