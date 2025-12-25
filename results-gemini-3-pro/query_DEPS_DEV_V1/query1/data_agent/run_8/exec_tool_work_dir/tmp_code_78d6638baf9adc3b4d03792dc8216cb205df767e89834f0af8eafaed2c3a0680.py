code = """# Same setup as before to get top 5
import json
import pandas as pd
import re

with open(locals()['var_function-call-5064586497231711022'], 'r') as f:
    packages_data = json.load(f)
df_packages = pd.DataFrame(packages_data)
df_packages['UpstreamPublishedAt'] = pd.to_numeric(df_packages['UpstreamPublishedAt'], errors='coerce')
df_packages = df_packages.sort_values(by=['Name', 'UpstreamPublishedAt'], ascending=[True, False])
df_latest = df_packages.drop_duplicates(subset=['Name'], keep='first')

with open(locals()['var_function-call-7159053233744676591'], 'r') as f:
    mapping_data = json.load(f)
df_mapping = pd.DataFrame(mapping_data)
df_mapping = df_mapping.drop_duplicates(subset=['Name', 'Version', 'ProjectName'])

df_merged = pd.merge(df_latest, df_mapping, on=['Name', 'Version'], how='inner')

with open(locals()['var_function-call-12549605067623195085'], 'r') as f:
    info_data = json.load(f)

project_infos = []
for entry in info_data:
    text = entry.get('Project_Information', '')
    name = None
    name_patterns = [
        r"The project ([a-zA-Z0-9-._]+/[a-zA-Z0-9-._]+)",
        r"The GitHub project ([a-zA-Z0-9-._]+/[a-zA-Z0-9-._]+)",
        r"The project named ([a-zA-Z0-9-._]+/[a-zA-Z0-9-._]+)",
        r"GitHub project named ([a-zA-Z0-9-._]+/[a-zA-Z0-9-._]+)",
        r"under the name ([a-zA-Z0-9-._]+/[a-zA-Z0-9-._]+)",
        r"repository named ([a-zA-Z0-9-._]+/[a-zA-Z0-9-._]+)"
    ]
    for pat in name_patterns:
        m = re.search(pat, text)
        if m:
            name = m.group(1)
            if name.endswith(',') or name.endswith('.'):
                name = name[:-1]
            break
            
    stars = 0
    star_patterns = [
        r"(\d+(?:,\d+)*) stars",
        r"stars count of (\d+(?:,\d+)*)",
        r"total of (\d+(?:,\d+)*) stars"
    ]
    for pat in star_patterns:
        m = re.search(pat, text)
        if m:
            s_str = m.group(1).replace(',', '')
            stars = int(s_str)
            break
            
    if name:
        project_infos.append({'ProjectName': name, 'Stars': stars})

df_info = pd.DataFrame(project_infos)
df_info = df_info.drop_duplicates(subset=['ProjectName'])

df_final = pd.merge(df_merged, df_info, on='ProjectName', how='inner')
df_final = df_final.drop_duplicates(subset=['Name'])
df_final = df_final.sort_values(by='Stars', ascending=False)
top_5 = df_final[['Name', 'Version', 'Stars', 'ProjectName']].head(5)

print("__RESULT__:")
print(top_5.to_json(orient='records'))"""

env_args = {'var_function-call-16346607828030946301': ['project_info', 'project_packageversion'], 'var_function-call-4586612903755575240': [{'Project_Information': 'The project lberrocal/npm-packages-template is hosted on GitHub and currently has 0 open issues, 0 stars, and 0 forks.', 'Licenses': '[]', 'Description': 'Template for npm package library configured to be used with CI/CD', 'Homepage': 'None', 'OSSFuzz': 'nan'}, {'Project_Information': 'The project leaflet/leaflet on GitHub is a popular open-source library that currently has 521 open issues, 38715 stars, and 5782 forks, making it a widely recognized tool in the developer community.', 'Licenses': '[\n  "non-standard"\n]', 'Description': '🍃 JavaScript library for mobile-friendly interactive maps 🇺🇦', 'Homepage': 'https://leafletjs.com', 'OSSFuzz': 'nan'}, {'Project_Information': 'The project leaflet/leaflet.fullscreen on GitHub currently has 29 open issues, 417 stars, and 118 forks, making it a noteworthy contribution to the Leaflet ecosystem.', 'Licenses': '[\n  "ISC"\n]', 'Description': 'A fullscreen control for Leaflet', 'Homepage': 'http://leaflet.github.io/Leaflet.fullscreen/', 'OSSFuzz': 'nan'}], 'var_function-call-5064586497231711022': 'file_storage/function-call-5064586497231711022.json', 'var_function-call-7159053233744676591': 'file_storage/function-call-7159053233744676591.json', 'var_function-call-5226446723810651635': 7843, 'var_function-call-17151931996028791556': [{'count_star()': '770'}], 'var_function-call-12549605067623195085': 'file_storage/function-call-12549605067623195085.json', 'var_function-call-11825773633354340323': [{'Name': '@dmrvos/infrajs>0.0.6>typescript', 'Version': '2.6.2', 'Stars': 94931, 'ProjectName': 'microsoft/typescript'}, {'Name': '@dmrvos/infrajs>0.0.6>typescript', 'Version': '2.6.2', 'Stars': 94931, 'ProjectName': 'microsoft/typescript'}, {'Name': '@dmrvos/infrajs>0.0.5>typescript', 'Version': '2.6.2', 'Stars': 94931, 'ProjectName': 'microsoft/typescript'}, {'Name': '@dmrvos/infrajs>0.0.5>typescript', 'Version': '2.6.2', 'Stars': 94931, 'ProjectName': 'microsoft/typescript'}, {'Name': '@dylanvann/svelte', 'Version': '3.25.4', 'Stars': 73499, 'ProjectName': 'sveltejs/svelte'}], 'var_function-call-2743529436280323138': [{'Name': '@dmrvos/infrajs>0.0.5>typescript', 'Version': '2.6.2', 'Stars': 94931, 'ProjectName': 'microsoft/typescript'}, {'Name': '@dmrvos/infrajs>0.0.6>typescript', 'Version': '2.6.2', 'Stars': 94931, 'ProjectName': 'microsoft/typescript'}, {'Name': '@dylanvann/svelte', 'Version': '3.25.4', 'Stars': 73499, 'ProjectName': 'sveltejs/svelte'}, {'Name': '@dumc11/tailwindcss', 'Version': '0.4.0', 'Stars': 73464, 'ProjectName': 'tailwindcss/tailwindcss'}, {'Name': '@dollarshaveclub/cli>1.11.4>lodash', 'Version': '4.17.11', 'Stars': 57779, 'ProjectName': 'lodash/lodash'}]}

exec(code, env_args)
