code = """import pandas as pd
import json
import re

# Load data
# df_packages
with open('var_function-call-9768801032224537016.json', 'r') as f:
    packages_data = json.load(f)
df_packages = pd.DataFrame(packages_data)

# df_mappings
with open('var_function-call-6268189373222231529.json', 'r') as f:
    mappings_data = json.load(f)
df_mappings = pd.DataFrame(mappings_data)

# df_project_info
with open('var_function-call-7577034226740686034.json', 'r') as f:
    project_info_data = json.load(f)
df_project_info = pd.DataFrame(project_info_data)

# Filter mappings by valid packages
# We need to match on Name and Version.
# Create a set of tuples for fast lookup
valid_pkg_set = set(zip(df_packages['Name'], df_packages['Version']))

# Filter mappings
# This might be slow if we iterate. Let's use merge.
# df_packages only has Name, Version.
df_valid_mappings = df_mappings.merge(df_packages, on=['Name', 'Version'])

# Get unique valid ProjectNames
valid_project_names = set(df_valid_mappings['ProjectName'].unique())

# Parse Project Information
parsed_projects = []

for text in df_project_info['Project_Information']:
    if not isinstance(text, str):
        continue
        
    # Find which project name is in the text
    # Heuristic: the project name usually contains a slash "owner/repo"
    # Iterate through valid_project_names? No, that's too slow (592k mappings, but maybe unique projects is smaller?)
    # Let's see how many unique projects we have in valid_mappings.
    pass

# Check number of unique projects
print(f"Unique valid projects: {len(valid_project_names)}")

# If unique valid projects is small, we can iterate.
# If it's large, we need to extract from text first.
# Given only 770 rows in project_info, we can iterate over project_info rows and extract the name.
# The name usually looks like "owner/repo". Regex: [\w\-\.]+ / [\w\-\.]+
# Let's define a regex for project name in text.

name_pattern = re.compile(r'project (?:named |is |on GitHub, named |is a GitHub repository named |is hosted on GitHub under the name )?([a-zA-Z0-9\-\._]+/[a-zA-Z0-9\-\._]+)')
forks_pattern_1 = re.compile(r'(\d+) forks')
forks_pattern_2 = re.compile(r'forks count of (\d+)')
forks_pattern_3 = re.compile(r'forked (\d+) times')

def extract_info(text):
    if not isinstance(text, str):
        return None, 0
    
    # Extract Name
    name_match = name_pattern.search(text)
    if name_match:
        name = name_match.group(1)
        # Clean up trailing punctuation if any (regex might grab it if careless)
        name = name.rstrip(',.')
    else:
        # Fallback: check if any valid_project_name is in text
        # Only feasible if we have the valid list in scope. 
        # But we can try to extract potential "owner/repo" pattern generally.
        # general pattern: word/word
        # But let's stick to what we saw.
        return None, 0

    # Extract Forks
    forks = 0
    f_match = forks_pattern_1.search(text)
    if f_match:
        forks = int(f_match.group(1).replace(',', ''))
    else:
        f_match = forks_pattern_2.search(text)
        if f_match:
            forks = int(f_match.group(1).replace(',', ''))
        else:
            f_match = forks_pattern_3.search(text)
            if f_match:
                forks = int(f_match.group(1).replace(',', ''))
    
    return name, forks

extracted_data = []
for text in df_project_info['Project_Information']:
    p_name, p_forks = extract_info(text)
    if p_name:
        extracted_data.append({'ProjectName': p_name, 'Forks': p_forks})

df_extracted = pd.DataFrame(extracted_data)

# Filter extracted projects by valid_project_names
# This ensures we only count projects that are linked to valid packages
df_final = df_extracted[df_extracted['ProjectName'].isin(valid_project_names)].copy()

# Sort by Forks
df_final = df_final.sort_values(by='Forks', ascending=False)

# Get top 5
top_5 = df_final.head(5).to_dict(orient='records')

print("__RESULT__:")
print(json.dumps(top_5))"""

env_args = {'var_function-call-8306285842551339484': ['project_info', 'project_packageversion'], 'var_function-call-15205586733890660752': [{'Project_Information': 'The project lberrocal/npm-packages-template is hosted on GitHub and currently has 0 open issues, 0 stars, and 0 forks.', 'Licenses': '[]', 'Description': 'Template for npm package library configured to be used with CI/CD', 'Homepage': 'None', 'OSSFuzz': 'nan'}, {'Project_Information': 'The project leaflet/leaflet on GitHub is a popular open-source library that currently has 521 open issues, 38715 stars, and 5782 forks, making it a widely recognized tool in the developer community.', 'Licenses': '[\n  "non-standard"\n]', 'Description': '🍃 JavaScript library for mobile-friendly interactive maps 🇺🇦', 'Homepage': 'https://leafletjs.com', 'OSSFuzz': 'nan'}, {'Project_Information': 'The project leaflet/leaflet.fullscreen on GitHub currently has 29 open issues, 417 stars, and 118 forks, making it a noteworthy contribution to the Leaflet ecosystem.', 'Licenses': '[\n  "ISC"\n]', 'Description': 'A fullscreen control for Leaflet', 'Homepage': 'http://leaflet.github.io/Leaflet.fullscreen/', 'OSSFuzz': 'nan'}], 'var_function-call-2825709360015694910': [{'column_name': 'Project_Information', 'column_type': 'VARCHAR', 'null': 'YES', 'key': 'None', 'default': 'None', 'extra': 'None'}, {'column_name': 'Licenses', 'column_type': 'VARCHAR', 'null': 'YES', 'key': 'None', 'default': 'None', 'extra': 'None'}, {'column_name': 'Description', 'column_type': 'VARCHAR', 'null': 'YES', 'key': 'None', 'default': 'None', 'extra': 'None'}, {'column_name': 'Homepage', 'column_type': 'VARCHAR', 'null': 'YES', 'key': 'None', 'default': 'None', 'extra': 'None'}, {'column_name': 'OSSFuzz', 'column_type': 'DOUBLE', 'null': 'YES', 'key': 'None', 'default': 'None', 'extra': 'None'}], 'var_function-call-13208554681068482386': [{'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 29\n}'}, {'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 18\n}'}, {'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 14\n}'}, {'VersionInfo': '{\n  "IsRelease": false,\n  "Ordinal": 129\n}'}, {'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 12\n}'}], 'var_function-call-12495672928513731532': [{'count(*)': '176998'}], 'var_function-call-9768801032224537016': 'file_storage/function-call-9768801032224537016.json', 'var_function-call-11972509971105772543': [{'count_star()': '591699'}], 'var_function-call-6472062802415353313': [{'count_star()': '770'}], 'var_function-call-6268189373222231529': 'file_storage/function-call-6268189373222231529.json', 'var_function-call-5874452534023789954': 'file_storage/function-call-5874452534023789954.json', 'var_function-call-7577034226740686034': 'file_storage/function-call-7577034226740686034.json'}

exec(code, env_args)
