code = """import json
import re

# Load project_info
with open(locals()['var_function-call-2774435484611140585'], 'r') as f:
    project_info = json.load(f)

project_data = {} # ProjectName -> Forks
names = []

# Regex patterns
name_patterns = [
    r"The project ([^\s]+) is hosted on GitHub",
    r"The project ([^\s]+) on GitHub",
    r"The GitHub project ([^\s]+) currently",
    r"The GitHub project named ([^\s]+) has",
    r"The GitHub project named ([^\s]+) currently",
    r"The project named ([^\s]+) is hosted",
    r"The project named ([^\s]+) on GitHub",
    r"The project is hosted on GitHub under the name ([^\s,]+)",
    r"The project is a GitHub repository named ([^\s,]+)",
    r"The project ([^\s]+) has an open issues count" # fallback
]

fork_patterns = [
    r"([\d,]+) forks",
    r"forks count of ([\d,]+)",
    r"has been forked ([\d,]+) times"
]

for row in project_info:
    text = row.get('Project_Information', '')
    if not text:
        continue
    
    # Extract Name
    p_name = None
    for pat in name_patterns:
        m = re.search(pat, text)
        if m:
            p_name = m.group(1).rstrip(',')
            # Validate format owner/repo
            if '/' in p_name:
                break
            else:
                p_name = None # false match?
    
    if not p_name:
        # Try finding anything that looks like owner/repo
        # This is risky but might work if patterns fail
        m = re.search(r"\b([a-zA-Z0-9_-]+/[a-zA-Z0-9_-]+)\b", text)
        if m:
            p_name = m.group(1)

    if not p_name:
        continue

    # Extract Forks
    forks = 0
    for pat in fork_patterns:
        m = re.search(pat, text)
        if m:
            num = m.group(1).replace(',', '')
            forks = int(num)
            break
            
    project_data[p_name] = forks
    names.append(p_name)

print(f"Extracted {len(project_data)} projects.")
print(f"Sample: {list(project_data.items())[:5]}")

print("__RESULT__:")
print(json.dumps(names))"""

env_args = {'var_function-call-11620772436885148255': [{'System': 'NPM', 'Name': '@ecl/twig-component-carousel', 'Version': '3.11.1', 'Licenses': '[\n  "EUPL-1.2"\n]', 'Links': '[\n  {\n    "Label": "ORIGIN",\n    "URL": "https://registry.npmjs.org/@ecl%2Ftwig-component-carousel/3.11.1"\n  }\n]', 'Advisories': '[]', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 29\n}', 'Hashes': '[\n  {\n    "Hash": "vH5da6eUZ94i1AcOsrC6VjSV88cMUe5A1w+CDHAt2aYXldR9sBNRCse27cIx51GnUjnj7dSe3o5A81TjraJ0Lw==",\n    "Type": "SHA512"\n  },\n  {\n    "Hash": "WZUWPp1jVp6nrUZ0n7vmthbB4OrtnLFNDOPPBBNp15I=",\n    "Type": "SHA256"\n  },\n  {\n    "Hash": "JbFslb4AeqQVI+LCXFeZKFrWmHI=",\n    "Type": "SHA1"\n  },\n  {\n    "Hash": "zBm5Qvg5p2bQwUTcg6hZYA==",\n    "Type": "MD5"\n  }\n]', 'DependenciesProcessed': '1', 'DependencyError': '0', 'UpstreamPublishedAt': '1699345351000000.0', 'Registries': '[]', 'SLSAProvenance': 'None', 'UpstreamIdentifiers': '[]', 'Purl': 'None'}], 'var_function-call-11620772436885151118': [{'System': 'NPM', 'Name': '@dms/io', 'Version': '0.9.0', 'ProjectType': 'GITHUB', 'ProjectName': 'dataminingsupply/dms-io', 'RelationProvenance': 'UNVERIFIED_METADATA', 'RelationType': 'SOURCE_REPO_TYPE'}], 'var_function-call-11620772436885149885': [{'Project_Information': 'The project lberrocal/npm-packages-template is hosted on GitHub and currently has 0 open issues, 0 stars, and 0 forks.', 'Licenses': '[]', 'Description': 'Template for npm package library configured to be used with CI/CD', 'Homepage': 'None', 'OSSFuzz': 'nan'}], 'var_function-call-5856525573606195906': [{'Project_Information': 'The project lberrocal/npm-packages-template is hosted on GitHub and currently has 0 open issues, 0 stars, and 0 forks.'}, {'Project_Information': 'The project leaflet/leaflet on GitHub is a popular open-source library that currently has 521 open issues, 38715 stars, and 5782 forks, making it a widely recognized tool in the developer community.'}, {'Project_Information': 'The project leaflet/leaflet.fullscreen on GitHub currently has 29 open issues, 417 stars, and 118 forks, making it a noteworthy contribution to the Leaflet ecosystem.'}, {'Project_Information': 'The project leaflet/leaflet.markercluster is hosted on GitHub and currently has an open issues count of 130, along with a stars count of 3761 and forks count of 988.'}, {'Project_Information': 'The project leandrowd/react-responsive-carousel on GitHub has garnered significant attention, with a total of 2,534 stars and 636 forks, while currently having 23 open issues.'}], 'var_function-call-11015933483321329327': [{'column_name': 'Project_Information', 'column_type': 'VARCHAR', 'null': 'YES', 'key': 'None', 'default': 'None', 'extra': 'None'}, {'column_name': 'Licenses', 'column_type': 'VARCHAR', 'null': 'YES', 'key': 'None', 'default': 'None', 'extra': 'None'}, {'column_name': 'Description', 'column_type': 'VARCHAR', 'null': 'YES', 'key': 'None', 'default': 'None', 'extra': 'None'}, {'column_name': 'Homepage', 'column_type': 'VARCHAR', 'null': 'YES', 'key': 'None', 'default': 'None', 'extra': 'None'}, {'column_name': 'OSSFuzz', 'column_type': 'DOUBLE', 'null': 'YES', 'key': 'None', 'default': 'None', 'extra': 'None'}], 'var_function-call-17699413025534137838': [{'COUNT(*)': '661372'}], 'var_function-call-17699413025534140353': [{'count_star()': '770'}], 'var_function-call-2774435484611140585': 'file_storage/function-call-2774435484611140585.json'}

exec(code, env_args)
