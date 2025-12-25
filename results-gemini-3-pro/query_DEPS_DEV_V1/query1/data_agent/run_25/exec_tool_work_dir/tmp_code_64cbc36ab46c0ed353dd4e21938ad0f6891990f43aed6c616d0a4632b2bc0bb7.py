code = """import json
import pandas as pd
import re

# Load data again
with open(locals()['var_function-call-6533266665392833605'], 'r') as f:
    latest_pkgs = json.load(f)
    
with open(locals()['var_function-call-2594427622717481590'], 'r') as f:
    pkg_mappings = json.load(f)

with open(locals()['var_function-call-11249593111119486648'], 'r') as f:
    proj_info = json.load(f)

# Convert to DataFrames
df_latest = pd.DataFrame(latest_pkgs)
df_map = pd.DataFrame(pkg_mappings)
df_info = pd.DataFrame(proj_info)

# Check for lodash
print("Lodash in latest packages:", 'lodash' in df_latest['Name'].values)
print("Lodash in mappings:", 'lodash' in df_map['Name'].values)

# Re-run the join process
df_latest['key'] = df_latest['Name'] + "@@" + df_latest['Version']
df_map['key'] = df_map['Name'] + "@@" + df_map['Version']
df_map_filtered = df_map[df_map['key'].isin(df_latest['key'])]

def parse_info(text):
    # Regex for Project Name
    name_regexes = [
        r"The project ([^\s]+) is hosted on GitHub",
        r"The project ([^\s]+) on GitHub",
        r"The GitHub project ([^\s]+) currently",
        r"The project is hosted on GitHub under the name ([^\s]+),",
        r"The project named ([^\s]+) on GitHub",
        r"The GitHub project named ([^\s]+) currently",
        r"The project ([^\s]+) has an open issues",
        r"The project ([^\s]+) currently has" # fallback
    ]
    p_name = None
    for r in name_regexes:
        m = re.search(r, text)
        if m:
            candidate = m.group(1)
            candidate = candidate.rstrip(",.")
            if "/" in candidate:
                p_name = candidate
                break
    
    stars = 0
    m_star = re.search(r"(\d+(?:,\d+)*) stars", text)
    if m_star:
        stars_str = m_star.group(1).replace(",", "")
        stars = int(stars_str)
    return p_name, stars

parsed_data = []
for entry in proj_info:
    text = entry.get('Project_Information', '')
    name, stars = parse_info(text)
    if name:
        parsed_data.append({'ProjectName': name, 'Stars': stars})

df_parsed_info = pd.DataFrame(parsed_data)

print("Parsed info sample:", df_parsed_info[df_parsed_info['ProjectName'] == 'lodash/lodash'].to_dict('records'))

df_final = pd.merge(df_map_filtered, df_parsed_info, on='ProjectName', how='inner')
df_final = df_final.sort_values(by='Stars', ascending=False)
df_final = df_final.drop_duplicates(subset=['Name'])

print("__RESULT__:")
print(df_final.head(10).to_json(orient='records'))"""

env_args = {'var_function-call-2400554470036027377': ['project_info', 'project_packageversion'], 'var_function-call-7826454399859203854': [{'Project_Information': 'The project lberrocal/npm-packages-template is hosted on GitHub and currently has 0 open issues, 0 stars, and 0 forks.', 'Licenses': '[]', 'Description': 'Template for npm package library configured to be used with CI/CD', 'Homepage': 'None', 'OSSFuzz': 'nan'}], 'var_function-call-16313167936421178255': [{'System': 'NPM', 'Name': '@dms/io', 'Version': '0.9.0', 'ProjectType': 'GITHUB', 'ProjectName': 'dataminingsupply/dms-io', 'RelationProvenance': 'UNVERIFIED_METADATA', 'RelationType': 'SOURCE_REPO_TYPE'}], 'var_function-call-17095951221475461517': [{'COUNT(*)': '661372'}], 'var_function-call-9493649555037983030': [{'COUNT(DISTINCT Name)': '16614'}], 'var_function-call-10744671647180174986': [{'count_star()': '597602'}], 'var_function-call-14411249742618821086': [{'count_star()': '770'}], 'var_function-call-6533266665392833605': 'file_storage/function-call-6533266665392833605.json', 'var_function-call-2594427622717481590': 'file_storage/function-call-2594427622717481590.json', 'var_function-call-11249593111119486648': 'file_storage/function-call-11249593111119486648.json', 'var_function-call-11380674343270437097': [{'Name': '@dylanvann/svelte', 'Version': '3.25.4', 'Stars': 73499}, {'Name': '@dumc11/tailwindcss', 'Version': '0.4.0', 'Stars': 73464}, {'Name': '@dman777/shadow-dom-quill-temp', 'Version': '1.0.0', 'Stars': 42407}, {'Name': '@dothq/styled-components', 'Version': '6.0.2-prealpha-dot', 'Stars': 39660}, {'Name': '@dynasty/styled-components', 'Version': '3.2.1', 'Stars': 39660}]}

exec(code, env_args)
