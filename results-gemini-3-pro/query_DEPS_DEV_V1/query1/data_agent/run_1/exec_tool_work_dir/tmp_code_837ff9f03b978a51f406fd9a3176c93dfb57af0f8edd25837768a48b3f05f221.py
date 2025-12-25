code = """import json
import re
import pandas as pd

# Load data
with open(locals()['var_function-call-17936320984994100568'], 'r') as f:
    package_data = json.load(f)
with open(locals()['var_function-call-5171920729111271395'], 'r') as f:
    project_package_data = json.load(f)
with open(locals()['var_function-call-13695207813627073106'], 'r') as f:
    project_info_data = json.load(f)

# Parse Project Info for Stars
project_star_map = {}

def parse_stars(text):
    if not text: return 0
    patterns = [
        r"currently has.*?\s([\d,]+)\s+stars",
        r"stars count of\s*([\d,]+)",
        r"total of\s*([\d,]+)\s+stars",
        r"garnered.*?total of\s*([\d,]+)\s+stars",
        r"([\d,]+)\s+stars"
    ]
    for pat in patterns:
        m = re.search(pat, text, re.IGNORECASE)
        if m:
            try:
                return int(m.group(1).replace(',', ''))
            except:
                pass
    return 0

def parse_project_name(text):
    m = re.search(r"project\s+(?:named\s+)?([a-zA-Z0-9\-_\.]+/[a-zA-Z0-9\-_\.]+)", text, re.IGNORECASE)
    if m:
        return m.group(1)
    m = re.search(r"The project ([a-zA-Z0-9\-_\.]+/[a-zA-Z0-9\-_\.]+)", text, re.IGNORECASE)
    if m:
        return m.group(1)
    # Fallback to just finding owner/repo at start?
    # "The project lberrocal/npm-packages-template..."
    return None

parsed_projects = []
for entry in project_info_data:
    info = entry.get('Project_Information', '')
    p_name = parse_project_name(info)
    stars = parse_stars(info)
    if p_name:
        parsed_projects.append({'ProjectName': p_name, 'Stars': stars})
        project_star_map[p_name] = stars
        project_star_map[p_name.lower()] = stars

# Top projects by stars
df_projects = pd.DataFrame(parsed_projects)
if not df_projects.empty:
    top_projects = df_projects.sort_values('Stars', ascending=False).head(10).to_dict(orient='records')
else:
    top_projects = []

# Process Packages
df_pkg = pd.DataFrame(package_data)
df_pkg['UpstreamPublishedAt'] = pd.to_numeric(df_pkg['UpstreamPublishedAt'], errors='coerce')
df_pkg = df_pkg.dropna(subset=['UpstreamPublishedAt'])
latest_idx = df_pkg.groupby('Name')['UpstreamPublishedAt'].idxmax()
df_latest = df_pkg.loc[latest_idx, ['Name', 'Version']]

df_pp = pd.DataFrame(project_package_data)
df_pp = df_pp[['Name', 'Version', 'ProjectName']].drop_duplicates()

merged = pd.merge(df_latest, df_pp, on=['Name', 'Version'], how='inner')

def get_stars(p_name):
    return project_star_map.get(p_name, project_star_map.get(str(p_name).lower()))

merged['Stars'] = merged['ProjectName'].apply(get_stars)
merged = merged.dropna(subset=['Stars'])
merged['Stars'] = merged['Stars'].astype(int)

top5 = merged.sort_values(by=['Stars', 'Name'], ascending=[False, True]).head(5)

result = {
    "top_projects_debug": top_projects,
    "top_packages": top5[['Name', 'Version', 'ProjectName', 'Stars']].to_dict(orient='records')
}

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_function-call-15265893695332558738': ['packageinfo'], 'var_function-call-1015005864724100337': ['project_info', 'project_packageversion'], 'var_function-call-297498087076333845': [{'Project_Information': 'The project lberrocal/npm-packages-template is hosted on GitHub and currently has 0 open issues, 0 stars, and 0 forks.', 'Licenses': '[]', 'Description': 'Template for npm package library configured to be used with CI/CD', 'Homepage': 'None', 'OSSFuzz': 'nan'}], 'var_function-call-2551278673153472772': [{'column_name': 'Project_Information', 'column_type': 'VARCHAR', 'null': 'YES', 'key': 'None', 'default': 'None', 'extra': 'None'}, {'column_name': 'Licenses', 'column_type': 'VARCHAR', 'null': 'YES', 'key': 'None', 'default': 'None', 'extra': 'None'}, {'column_name': 'Description', 'column_type': 'VARCHAR', 'null': 'YES', 'key': 'None', 'default': 'None', 'extra': 'None'}, {'column_name': 'Homepage', 'column_type': 'VARCHAR', 'null': 'YES', 'key': 'None', 'default': 'None', 'extra': 'None'}, {'column_name': 'OSSFuzz', 'column_type': 'DOUBLE', 'null': 'YES', 'key': 'None', 'default': 'None', 'extra': 'None'}], 'var_function-call-3158966555197872046': [{'count(*)': '661372'}], 'var_function-call-17992344091215332840': [{'count_star()': '597602'}], 'var_function-call-13934852242877722428': [{'count_star()': '770'}], 'var_function-call-13695207813627073106': 'file_storage/function-call-13695207813627073106.json', 'var_function-call-5171920729111271395': 'file_storage/function-call-5171920729111271395.json', 'var_function-call-17936320984994100568': 'file_storage/function-call-17936320984994100568.json', 'var_function-call-15119832055290009601': [{'Name': '@dylanvann/svelte', 'Version': '3.25.4'}, {'Name': '@dylanvann/svelte', 'Version': '3.25.4'}, {'Name': '@dumc11/tailwindcss', 'Version': '0.4.0'}, {'Name': '@dumc11/tailwindcss', 'Version': '0.4.0'}, {'Name': '@edgarai/strapi-provider-upload-local', 'Version': '3.6.3-devgar-fork.2'}], 'var_function-call-9165310766928041281': [{'Name': '@dylanvann/svelte', 'Version': '3.25.4'}, {'Name': '@dumc11/tailwindcss', 'Version': '0.4.0'}, {'Name': '@edgarai/strapi-provider-upload-local', 'Version': '3.6.3-devgar-fork.2'}, {'Name': '@dreampie/semantic-ui', 'Version': '2.2.11'}, {'Name': '@dongls/pdfjs-dist', 'Version': '3.2.72'}]}

exec(code, env_args)
