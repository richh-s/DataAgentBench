code = """import json
import pandas as pd
import re

project_info_data = pd.read_json(locals()['var_function-call-7004063310327144851'])

def parse_project_info(info_string):
    project_name_match = re.search(r'The project ([a-zA-Z0-9_-]+/[a-zA-Z0-9_-]+) is hosted on GitHub', info_string) or \
                         re.search(r'The GitHub project ([a-zA-Z0-9_-]+/[a-zA-Z0-9_-]+) currently has', info_string) or \
                         re.search(r'The project named ([a-zA-Z0-9_-]+/[a-zA-Z0-9_-]+) on GitHub currently has', info_string) or \
                         re.search(r'The project ([a-zA-Z0-9_-]+/[a-zA-Z0-9_-]+) on GitHub has garnered', info_string) or \
                         re.search(r'The project on GitHub, named ([a-zA-Z0-9_-]+/[a-zA-Z0-9_-]+), currently has', info_string) or \
                         re.search(r'The project ([a-zA-Z0-9_-]+/[a-zA-Z0-9_-]+) is hosted on GITHUB and currently has', info_string)
    stars_match = re.search(r'(\\d{1,3}(?:,\\d{3})*|\\d+) stars', info_string)
    
    project_name = project_name_match.group(1) if project_name_match else None
    stars = int(stars_match.group(1).replace(',', '')) if stars_match else 0
    return project_name, stars

project_info_data[['ProjectName', 'Stars']] = project_info_data['Project_Information'].apply(lambda x: pd.Series(parse_project_info(x)))

# Filter out rows where ProjectName is None
project_info_data = project_info_data.dropna(subset=['ProjectName'])

result = project_info_data[['ProjectName', 'Stars']].to_json(orient='records')

print("__RESULT__:")
print(result)"""

env_args = {'var_function-call-18442683985073922078': 'file_storage/function-call-18442683985073922078.json', 'var_function-call-15828687765445895216': 'file_storage/function-call-15828687765445895216.json', 'var_function-call-17954856618360052339': 'file_storage/function-call-17954856618360052339.json', 'var_function-call-15902394642716762254': 'file_storage/function-call-15902394642716762254.json', 'var_function-call-16578664634641431138': ['project_info', 'project_packageversion'], 'var_function-call-962002978812241716': [{'Project_Information': 'The project lberrocal/npm-packages-template is hosted on GitHub and currently has 0 open issues, 0 stars, and 0 forks.', 'Licenses': '[]', 'Description': 'Template for npm package library configured to be used with CI/CD', 'Homepage': 'None', 'OSSFuzz': 'nan'}], 'var_function-call-7004063310327144851': 'file_storage/function-call-7004063310327144851.json'}

exec(code, env_args)
