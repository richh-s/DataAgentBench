code = """import json
import pandas as pd
import re

# Load packageinfo
with open(locals()['var_function-call-16088444697966514014'], 'r') as f:
    packages_data = json.load(f)
df_packages = pd.DataFrame(packages_data)

# Filter for latest version
# Convert UpstreamPublishedAt to float
df_packages['UpstreamPublishedAt'] = pd.to_numeric(df_packages['UpstreamPublishedAt'], errors='coerce')
# Sort by Name and UpstreamPublishedAt desc
df_packages = df_packages.sort_values(['Name', 'UpstreamPublishedAt'], ascending=[True, False])
# Drop duplicates keeping first (latest)
df_latest_packages = df_packages.drop_duplicates(subset=['Name'], keep='first')

# Load project_packageversion
with open(locals()['var_function-call-1945020110919878754'], 'r') as f:
    ppv_data = json.load(f)
df_ppv = pd.DataFrame(ppv_data)

# Join packages with ppv
# df_latest_packages: Name, Version
# df_ppv: Name, Version, ProjectName
# Inner join to get ProjectName for latest packages
df_merged = pd.merge(df_latest_packages, df_ppv, on=['Name', 'Version'], how='inner')

# Load project_info
with open(locals()['var_function-call-1113074479373272055'], 'r') as f:
    pinfo_data = json.load(f)
df_pinfo = pd.DataFrame(pinfo_data)

# Parse Project_Information
def parse_info(text):
    # Extract Stars
    # Patterns like: "38715 stars", "stars count of 3761", "total of 2,534 stars", "1 star", "0 stars"
    # Regex to capture number before "star" or "stars", possibly with "count of" or "total of" in between?
    # Actually, usually "X stars" or "stars count of X".
    
    stars = 0
    # Try finding "X stars" where X is number
    # Handle commas in numbers
    # Pattern: number followed by "stars"
    # \b([\d,]+)\s+stars\b
    
    # Also "stars count of X"
    # stars\s+count\s+of\s+([\d,]+)
    
    star_match = re.search(r'(\d[\d,]*)\s+stars\b', text)
    if not star_match:
        star_match = re.search(r'stars\s+count\s+of\s+(\d[\d,]*)', text)
        
    if star_match:
        stars_str = star_match.group(1).replace(',', '')
        try:
            stars = int(stars_str)
        except:
            stars = 0
            
    # Extract Project Name
    # Patterns based on observation
    name = None
    # 1. "The project X is hosted"
    # 2. "The project X on GitHub"
    # 3. "The project named X on GitHub"
    # 4. "The GitHub project X currently"
    # 5. "The GitHub project named X currently"
    # 6. "under the name X," or "under the name X and"
    
    # Heuristic: Look for "owner/repo" pattern?
    # Regex: [\w.-]+/[\w.-]+
    # But text might not contain slash if it just says name? 
    # The samples showed "lberrocal/npm-packages-template", "leaflet/leaflet", etc.
    # So looking for "word/word" might be effective.
    
    name_match = re.search(r'\b([\w\.-]+/[\w\.-]+)\b', text)
    if name_match:
        # Check if it looks like a repo (has slash)
        possible_name = name_match.group(1)
        if '/' in possible_name:
            name = possible_name
    
    return name, stars

parsed_data = []
for text in df_pinfo['Project_Information']:
    pname, stars = parse_info(text)
    if pname:
        parsed_data.append({'ProjectName': pname, 'Stars': stars})

df_stars = pd.DataFrame(parsed_data)
# There might be duplicates in parsed data if multiple project_info rows refer to same project (unlikely but possible)
# Or if my regex picked up same name multiple times.
df_stars = df_stars.drop_duplicates(subset=['ProjectName'])

# Join merged packages with stars
# df_merged: Name, Version, ProjectName
# df_stars: ProjectName, Stars
final_df = pd.merge(df_merged, df_stars, on='ProjectName', how='inner')

# Sort by Stars desc
top_5 = final_df.sort_values('Stars', ascending=False).head(5)

# Output Name, Version, Stars (and ProjectName just for checking)
result = top_5[['Name', 'Version', 'Stars', 'ProjectName']].to_dict(orient='records')
print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_function-call-2228285167515106346': ['packageinfo'], 'var_function-call-13917252462233452231': ['project_info', 'project_packageversion'], 'var_function-call-277263438303744630': [{'Project_Information': 'The project lberrocal/npm-packages-template is hosted on GitHub and currently has 0 open issues, 0 stars, and 0 forks.', 'Licenses': '[]', 'Description': 'Template for npm package library configured to be used with CI/CD', 'Homepage': 'None', 'OSSFuzz': 'nan'}], 'var_function-call-190737393126830296': [{'column_name': 'Project_Information', 'column_type': 'VARCHAR', 'null': 'YES', 'key': 'None', 'default': 'None', 'extra': 'None'}, {'column_name': 'Licenses', 'column_type': 'VARCHAR', 'null': 'YES', 'key': 'None', 'default': 'None', 'extra': 'None'}, {'column_name': 'Description', 'column_type': 'VARCHAR', 'null': 'YES', 'key': 'None', 'default': 'None', 'extra': 'None'}, {'column_name': 'Homepage', 'column_type': 'VARCHAR', 'null': 'YES', 'key': 'None', 'default': 'None', 'extra': 'None'}, {'column_name': 'OSSFuzz', 'column_type': 'DOUBLE', 'null': 'YES', 'key': 'None', 'default': 'None', 'extra': 'None'}], 'var_function-call-14868772338267612134': [{'COUNT(*)': '661372'}], 'var_function-call-12747696014607391844': [{'Name': '@ecl/twig-component-carousel', 'Version': '3.11.1', 'UpstreamPublishedAt': '1699345351000000.0'}, {'Name': '@douganderson444/panzoom-node', 'Version': '1.1.5', 'UpstreamPublishedAt': '1670271173000000.0'}, {'Name': '@douganderson444/panzoom-node', 'Version': '1.1.1', 'UpstreamPublishedAt': '1654791421000000.0'}, {'Name': '@dreamworld/dw-select', 'Version': '3.1.2-fix-double-click-issue.1', 'UpstreamPublishedAt': '1624260093000000.0'}, {'Name': '@discue/ui-components', 'Version': '0.13.0', 'UpstreamPublishedAt': '1656518476000000.0'}], 'var_function-call-9759696769129836495': [{'count_star()': '597602'}], 'var_function-call-6437638699816300697': [{'count_star()': '770'}], 'var_function-call-10251858433506105411': [{'Project_Information': 'The project lberrocal/npm-packages-template is hosted on GitHub and currently has 0 open issues, 0 stars, and 0 forks.'}, {'Project_Information': 'The project leaflet/leaflet on GitHub is a popular open-source library that currently has 521 open issues, 38715 stars, and 5782 forks, making it a widely recognized tool in the developer community.'}, {'Project_Information': 'The project leaflet/leaflet.fullscreen on GitHub currently has 29 open issues, 417 stars, and 118 forks, making it a noteworthy contribution to the Leaflet ecosystem.'}, {'Project_Information': 'The project leaflet/leaflet.markercluster is hosted on GitHub and currently has an open issues count of 130, along with a stars count of 3761 and forks count of 988.'}, {'Project_Information': 'The project leandrowd/react-responsive-carousel on GitHub has garnered significant attention, with a total of 2,534 stars and 636 forks, while currently having 23 open issues.'}, {'Project_Information': 'The project is hosted on GitHub under the name learnfrontend-dc/product-cart, and it currently has 2 open issues. It has garnered a total of 11 stars and has been forked 12 times.'}, {'Project_Information': 'The GitHub project ledgerproject/keypairoom currently has 3 open issues, 3 stars, and 0 forks.'}, {'Project_Information': 'The project leebyron/jasmine-check is hosted on GitHub and currently has 0 open issues, 11 stars, and 3 forks.'}, {'Project_Information': 'The project leebyron/testcheck-js on GitHub has an open issues count of 29, a stars count of 1185, and a forks count of 58, making it a notable repository in the community.'}, {'Project_Information': 'The project leecade/react-native-swiper is hosted on GitHub and has a total of 786 open issues, along with an impressive 10,249 stars and 2,392 forks, making it a popular choice among developers for implementing swiping functionality in React Native applications.'}], 'var_function-call-16088444697966514014': 'file_storage/function-call-16088444697966514014.json', 'var_function-call-1945020110919878754': 'file_storage/function-call-1945020110919878754.json', 'var_function-call-1113074479373272055': 'file_storage/function-call-1113074479373272055.json'}

exec(code, env_args)
