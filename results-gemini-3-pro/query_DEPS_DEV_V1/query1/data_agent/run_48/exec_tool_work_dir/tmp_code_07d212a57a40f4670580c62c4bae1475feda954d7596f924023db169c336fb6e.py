code = """import json
import re
import pandas as pd

# Load project_info
file_path = locals()['var_function-call-720738556870625539']
with open(file_path, 'r') as f:
    project_info = json.load(f)

projects = []

for entry in project_info:
    text = entry.get('Project_Information', '')
    
    # Extract Name
    # Patterns observed:
    # "The project lberrocal/npm-packages-template is hosted..."
    # "The project on GitHub, named leonardparisi/easy-express-server, currently..."
    # "The GitHub project named leviticusmb/divine-synchronization..."
    # "The project is hosted on GitHub under the name learnfrontend-dc/product-cart..."
    
    name_match = re.search(r'(?:project|named|name)\s+([a-zA-Z0-9\-_]+/[a-zA-Z0-9\-_.]+)', text)
    if not name_match:
        # Try finding just the slash pattern if context fails, but be careful
        # Maybe look for "named " followed by anything?
        pass
    
    # Extract Stars
    # "0 stars", "38,715 stars", "stars count of 3761"
    stars_match = re.search(r'([0-9,]+)\s+stars', text)
    if not stars_match:
        stars_match = re.search(r'stars count of\s+([0-9,]+)', text)
        
    if name_match and stars_match:
        name = name_match.group(1)
        # Remove trailing punctuation if captured (regex should be tight but...)
        name = name.rstrip(',.')
        
        stars_str = stars_match.group(1).replace(',', '')
        try:
            stars = int(stars_str)
            projects.append({'ProjectName': name, 'Stars': stars})
        except:
            pass

# Sort by Stars DESC
df = pd.DataFrame(projects)
if not df.empty:
    df = df.sort_values(by='Stars', ascending=False)
    top_projects = df.head(50).to_dict(orient='records')
else:
    top_projects = []

print("__RESULT__:")
print(json.dumps(top_projects))"""

env_args = {'var_function-call-2628886420893491648': ['packageinfo'], 'var_function-call-2628886420893494295': ['project_info', 'project_packageversion'], 'var_function-call-1048771457595593400': [{'Project_Information': 'The project lberrocal/npm-packages-template is hosted on GitHub and currently has 0 open issues, 0 stars, and 0 forks.', 'Licenses': '[]', 'Description': 'Template for npm package library configured to be used with CI/CD', 'Homepage': 'None', 'OSSFuzz': 'nan'}], 'var_function-call-1048771457595592751': [{'System': 'NPM', 'Name': '@dms/io', 'Version': '0.9.0', 'ProjectType': 'GITHUB', 'ProjectName': 'dataminingsupply/dms-io', 'RelationProvenance': 'UNVERIFIED_METADATA', 'RelationType': 'SOURCE_REPO_TYPE'}], 'var_function-call-1048771457595596198': [{'System': 'NPM', 'Name': '@ecl/twig-component-carousel', 'Version': '3.11.1', 'Licenses': '[\n  "EUPL-1.2"\n]', 'Links': '[\n  {\n    "Label": "ORIGIN",\n    "URL": "https://registry.npmjs.org/@ecl%2Ftwig-component-carousel/3.11.1"\n  }\n]', 'Advisories': '[]', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 29\n}', 'Hashes': '[\n  {\n    "Hash": "vH5da6eUZ94i1AcOsrC6VjSV88cMUe5A1w+CDHAt2aYXldR9sBNRCse27cIx51GnUjnj7dSe3o5A81TjraJ0Lw==",\n    "Type": "SHA512"\n  },\n  {\n    "Hash": "WZUWPp1jVp6nrUZ0n7vmthbB4OrtnLFNDOPPBBNp15I=",\n    "Type": "SHA256"\n  },\n  {\n    "Hash": "JbFslb4AeqQVI+LCXFeZKFrWmHI=",\n    "Type": "SHA1"\n  },\n  {\n    "Hash": "zBm5Qvg5p2bQwUTcg6hZYA==",\n    "Type": "MD5"\n  }\n]', 'DependenciesProcessed': '1', 'DependencyError': '0', 'UpstreamPublishedAt': '1699345351000000.0', 'Registries': '[]', 'SLSAProvenance': 'None', 'UpstreamIdentifiers': '[]', 'Purl': 'None'}], 'var_function-call-1440536270160794377': [{'COUNT(*)': '661372'}], 'var_function-call-1440536270160795854': [{'count_star()': '597602'}], 'var_function-call-1440536270160797331': [{'count_star()': '770'}], 'var_function-call-720738556870625539': 'file_storage/function-call-720738556870625539.json'}

exec(code, env_args)
