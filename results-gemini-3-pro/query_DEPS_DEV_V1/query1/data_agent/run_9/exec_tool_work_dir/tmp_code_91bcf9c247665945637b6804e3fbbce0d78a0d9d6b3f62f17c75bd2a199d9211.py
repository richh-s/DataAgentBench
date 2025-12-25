code = """import json
import pandas as pd
import re

# Load packageinfo
with open(locals()['var_function-call-16088444697966514014'], 'r') as f:
    packages_data = json.load(f)
df_packages = pd.DataFrame(packages_data)

df_packages['UpstreamPublishedAt'] = pd.to_numeric(df_packages['UpstreamPublishedAt'], errors='coerce')
df_packages = df_packages.sort_values(['Name', 'UpstreamPublishedAt'], ascending=[True, False])
df_latest_packages = df_packages.drop_duplicates(subset=['Name'], keep='first')

# Load project_packageversion
with open(locals()['var_function-call-1945020110919878754'], 'r') as f:
    ppv_data = json.load(f)
df_ppv = pd.DataFrame(ppv_data)

# Join packages with ppv
df_merged = pd.merge(df_latest_packages, df_ppv, on=['Name', 'Version'], how='inner')
print(f"df_merged shape: {df_merged.shape}")
if not df_merged.empty:
    print("df_merged cols:", df_merged.columns)
    print(df_merged.head(2).to_dict())

# Load project_info
with open(locals()['var_function-call-1113074479373272055'], 'r') as f:
    pinfo_data = json.load(f)
df_pinfo = pd.DataFrame(pinfo_data)

# Parse Project_Information
def parse_info(text):
    stars = 0
    star_match = re.search(r'(\d[\d,]*)\s+stars\b', text)
    if not star_match:
        star_match = re.search(r'stars\s+count\s+of\s+(\d[\d,]*)', text)
        
    if star_match:
        stars_str = star_match.group(1).replace(',', '')
        try:
            stars = int(stars_str)
        except:
            stars = 0
            
    name = None
    # Looking for owner/repo
    # Be more permissive?
    name_matches = re.findall(r'\b([\w\.-]+/[\w\.-]+)\b', text)
    if name_matches:
        # Filter out false positives if any? 
        # Usually the first one is the project name
        # But sometimes "is hosted on GitHub under the name X"
        # Let's take the one that is most likely the repo name.
        # Check against df_merged['ProjectName']? No that's circular if I want to join.
        # Just take the first one that looks like owner/repo
        for m in name_matches:
            if '/' in m and not m.startswith('http'):
                name = m
                break
    
    return name, stars

parsed_data = []
for text in df_pinfo['Project_Information']:
    pname, stars = parse_info(text)
    if pname:
        parsed_data.append({'ProjectName': pname, 'Stars': stars})

df_stars = pd.DataFrame(parsed_data)
print(f"df_stars shape: {df_stars.shape}")
if not df_stars.empty:
    print("df_stars cols:", df_stars.columns)
    print(df_stars.head(2).to_dict())
else:
    print("df_stars is empty. Sample text:", df_pinfo['Project_Information'].iloc[0])

# Join merged packages with stars
if not df_stars.empty and 'ProjectName' in df_stars.columns:
    final_df = pd.merge(df_merged, df_stars, on='ProjectName', how='inner')
    top_5 = final_df.sort_values('Stars', ascending=False).head(5)
    result = top_5[['Name', 'Version', 'Stars']].to_dict(orient='records')
    print("__RESULT__:")
    print(json.dumps(result))
else:
    print("__RESULT__:")
    print("[]")"""

env_args = {'var_function-call-2228285167515106346': ['packageinfo'], 'var_function-call-13917252462233452231': ['project_info', 'project_packageversion'], 'var_function-call-277263438303744630': [{'Project_Information': 'The project lberrocal/npm-packages-template is hosted on GitHub and currently has 0 open issues, 0 stars, and 0 forks.', 'Licenses': '[]', 'Description': 'Template for npm package library configured to be used with CI/CD', 'Homepage': 'None', 'OSSFuzz': 'nan'}], 'var_function-call-190737393126830296': [{'column_name': 'Project_Information', 'column_type': 'VARCHAR', 'null': 'YES', 'key': 'None', 'default': 'None', 'extra': 'None'}, {'column_name': 'Licenses', 'column_type': 'VARCHAR', 'null': 'YES', 'key': 'None', 'default': 'None', 'extra': 'None'}, {'column_name': 'Description', 'column_type': 'VARCHAR', 'null': 'YES', 'key': 'None', 'default': 'None', 'extra': 'None'}, {'column_name': 'Homepage', 'column_type': 'VARCHAR', 'null': 'YES', 'key': 'None', 'default': 'None', 'extra': 'None'}, {'column_name': 'OSSFuzz', 'column_type': 'DOUBLE', 'null': 'YES', 'key': 'None', 'default': 'None', 'extra': 'None'}], 'var_function-call-14868772338267612134': [{'COUNT(*)': '661372'}], 'var_function-call-12747696014607391844': [{'Name': '@ecl/twig-component-carousel', 'Version': '3.11.1', 'UpstreamPublishedAt': '1699345351000000.0'}, {'Name': '@douganderson444/panzoom-node', 'Version': '1.1.5', 'UpstreamPublishedAt': '1670271173000000.0'}, {'Name': '@douganderson444/panzoom-node', 'Version': '1.1.1', 'UpstreamPublishedAt': '1654791421000000.0'}, {'Name': '@dreamworld/dw-select', 'Version': '3.1.2-fix-double-click-issue.1', 'UpstreamPublishedAt': '1624260093000000.0'}, {'Name': '@discue/ui-components', 'Version': '0.13.0', 'UpstreamPublishedAt': '1656518476000000.0'}], 'var_function-call-9759696769129836495': [{'count_star()': '597602'}], 'var_function-call-6437638699816300697': [{'count_star()': '770'}], 'var_function-call-10251858433506105411': [{'Project_Information': 'The project lberrocal/npm-packages-template is hosted on GitHub and currently has 0 open issues, 0 stars, and 0 forks.'}, {'Project_Information': 'The project leaflet/leaflet on GitHub is a popular open-source library that currently has 521 open issues, 38715 stars, and 5782 forks, making it a widely recognized tool in the developer community.'}, {'Project_Information': 'The project leaflet/leaflet.fullscreen on GitHub currently has 29 open issues, 417 stars, and 118 forks, making it a noteworthy contribution to the Leaflet ecosystem.'}, {'Project_Information': 'The project leaflet/leaflet.markercluster is hosted on GitHub and currently has an open issues count of 130, along with a stars count of 3761 and forks count of 988.'}, {'Project_Information': 'The project leandrowd/react-responsive-carousel on GitHub has garnered significant attention, with a total of 2,534 stars and 636 forks, while currently having 23 open issues.'}, {'Project_Information': 'The project is hosted on GitHub under the name learnfrontend-dc/product-cart, and it currently has 2 open issues. It has garnered a total of 11 stars and has been forked 12 times.'}, {'Project_Information': 'The GitHub project ledgerproject/keypairoom currently has 3 open issues, 3 stars, and 0 forks.'}, {'Project_Information': 'The project leebyron/jasmine-check is hosted on GitHub and currently has 0 open issues, 11 stars, and 3 forks.'}, {'Project_Information': 'The project leebyron/testcheck-js on GitHub has an open issues count of 29, a stars count of 1185, and a forks count of 58, making it a notable repository in the community.'}, {'Project_Information': 'The project leecade/react-native-swiper is hosted on GitHub and has a total of 786 open issues, along with an impressive 10,249 stars and 2,392 forks, making it a popular choice among developers for implementing swiping functionality in React Native applications.'}], 'var_function-call-16088444697966514014': 'file_storage/function-call-16088444697966514014.json', 'var_function-call-1945020110919878754': 'file_storage/function-call-1945020110919878754.json', 'var_function-call-1113074479373272055': 'file_storage/function-call-1113074479373272055.json'}

exec(code, env_args)
