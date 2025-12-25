code = """import json
import pandas as pd

# Load data
with open(locals()['var_function-call-17936320984994100568'], 'r') as f:
    package_data = json.load(f)
with open(locals()['var_function-call-5171920729111271395'], 'r') as f:
    project_package_data = json.load(f)

df_pkg = pd.DataFrame(package_data)
df_pp = pd.DataFrame(project_package_data)

# Check Typescript
ts_pkgs = df_pkg[df_pkg['Name'] == 'typescript']
ts_projs = df_pp[df_pp['ProjectName'] == 'microsoft/typescript']

# Check Svelte
svelte_pkgs = df_pkg[df_pkg['Name'] == 'svelte']
svelte_projs = df_pp[df_pp['ProjectName'] == 'sveltejs/svelte']

print("Typescript Pkg Latest:")
if not ts_pkgs.empty:
    ts_pkgs['UpstreamPublishedAt'] = pd.to_numeric(ts_pkgs['UpstreamPublishedAt'], errors='coerce')
    latest_ts = ts_pkgs.loc[ts_pkgs['UpstreamPublishedAt'].idxmax()]
    print(latest_ts[['Name', 'Version']])
else:
    print("None")

print("\nTypescript Project Mappings:")
print(ts_projs[['Name', 'Version']].head())

print("\nSvelte Pkg Latest:")
if not svelte_pkgs.empty:
    svelte_pkgs['UpstreamPublishedAt'] = pd.to_numeric(svelte_pkgs['UpstreamPublishedAt'], errors='coerce')
    latest_svelte = svelte_pkgs.loc[svelte_pkgs['UpstreamPublishedAt'].idxmax()]
    print(latest_svelte[['Name', 'Version']])
else:
    print("None")

print("\nSvelte Project Mappings:")
print(svelte_projs[['Name', 'Version']].head())"""

env_args = {'var_function-call-15265893695332558738': ['packageinfo'], 'var_function-call-1015005864724100337': ['project_info', 'project_packageversion'], 'var_function-call-297498087076333845': [{'Project_Information': 'The project lberrocal/npm-packages-template is hosted on GitHub and currently has 0 open issues, 0 stars, and 0 forks.', 'Licenses': '[]', 'Description': 'Template for npm package library configured to be used with CI/CD', 'Homepage': 'None', 'OSSFuzz': 'nan'}], 'var_function-call-2551278673153472772': [{'column_name': 'Project_Information', 'column_type': 'VARCHAR', 'null': 'YES', 'key': 'None', 'default': 'None', 'extra': 'None'}, {'column_name': 'Licenses', 'column_type': 'VARCHAR', 'null': 'YES', 'key': 'None', 'default': 'None', 'extra': 'None'}, {'column_name': 'Description', 'column_type': 'VARCHAR', 'null': 'YES', 'key': 'None', 'default': 'None', 'extra': 'None'}, {'column_name': 'Homepage', 'column_type': 'VARCHAR', 'null': 'YES', 'key': 'None', 'default': 'None', 'extra': 'None'}, {'column_name': 'OSSFuzz', 'column_type': 'DOUBLE', 'null': 'YES', 'key': 'None', 'default': 'None', 'extra': 'None'}], 'var_function-call-3158966555197872046': [{'count(*)': '661372'}], 'var_function-call-17992344091215332840': [{'count_star()': '597602'}], 'var_function-call-13934852242877722428': [{'count_star()': '770'}], 'var_function-call-13695207813627073106': 'file_storage/function-call-13695207813627073106.json', 'var_function-call-5171920729111271395': 'file_storage/function-call-5171920729111271395.json', 'var_function-call-17936320984994100568': 'file_storage/function-call-17936320984994100568.json', 'var_function-call-15119832055290009601': [{'Name': '@dylanvann/svelte', 'Version': '3.25.4'}, {'Name': '@dylanvann/svelte', 'Version': '3.25.4'}, {'Name': '@dumc11/tailwindcss', 'Version': '0.4.0'}, {'Name': '@dumc11/tailwindcss', 'Version': '0.4.0'}, {'Name': '@edgarai/strapi-provider-upload-local', 'Version': '3.6.3-devgar-fork.2'}], 'var_function-call-9165310766928041281': [{'Name': '@dylanvann/svelte', 'Version': '3.25.4'}, {'Name': '@dumc11/tailwindcss', 'Version': '0.4.0'}, {'Name': '@edgarai/strapi-provider-upload-local', 'Version': '3.6.3-devgar-fork.2'}, {'Name': '@dreampie/semantic-ui', 'Version': '2.2.11'}, {'Name': '@dongls/pdfjs-dist', 'Version': '3.2.72'}], 'var_function-call-994738237734338444': {'top_projects_debug': [{'ProjectName': 'microsoft/typescript', 'Stars': 94931}, {'ProjectName': 'mui-org/material-ui', 'Stars': 89398}, {'ProjectName': 'sveltejs/svelte', 'Stars': 73499}, {'ProjectName': 'tailwindcss/tailwindcss', 'Stars': 73464}, {'ProjectName': 'lodash/lodash', 'Stars': 57779}, {'ProjectName': 'strapi/strapi', 'Stars': 57236}, {'ProjectName': 'semantic-org/semantic-ui', 'Stars': 51069}, {'ProjectName': 'moment/moment', 'Stars': 47549}, {'ProjectName': 'mozilla/pdf.js', 'Stars': 44231}, {'ProjectName': 'quilljs/quill', 'Stars': 42407}], 'top_packages': [{'Name': '@dylanvann/svelte', 'Version': '3.25.4', 'ProjectName': 'sveltejs/svelte', 'Stars': 73499}, {'Name': '@dumc11/tailwindcss', 'Version': '0.4.0', 'ProjectName': 'tailwindcss/tailwindcss', 'Stars': 73464}, {'Name': '@edgarai/strapi-provider-upload-local', 'Version': '3.6.3-devgar-fork.2', 'ProjectName': 'strapi/strapi', 'Stars': 57236}, {'Name': '@dreampie/semantic-ui', 'Version': '2.2.11', 'ProjectName': 'semantic-org/semantic-ui', 'Stars': 51069}, {'Name': '@dongls/pdfjs-dist', 'Version': '3.2.72', 'ProjectName': 'mozilla/pdf.js', 'Stars': 44231}]}}

exec(code, env_args)
