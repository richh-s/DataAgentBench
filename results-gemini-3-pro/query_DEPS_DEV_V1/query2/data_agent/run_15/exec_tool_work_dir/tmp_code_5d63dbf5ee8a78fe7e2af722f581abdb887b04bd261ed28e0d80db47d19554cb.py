code = """import json
import re

# Load data files
# var_function-call-9978821279046557838: packageinfo (Name, Version)
# var_function-call-8003098710851808412: project_info (Project_Information)
# var_function-call-7590661337522328408: project_packageversion (Name, Version, ProjectName)

with open(locals()['var_function-call-9978821279046557838'], 'r') as f:
    package_data = json.load(f)

with open(locals()['var_function-call-8003098710851808412'], 'r') as f:
    project_info_data = json.load(f)

with open(locals()['var_function-call-7590661337522328408'], 'r') as f:
    ppv_data = json.load(f)

# 1. Parse project_info
project_metrics = {}

def parse_project_info(text):
    # Extract Project Name
    # Patterns based on observations
    name_patterns = [
        r"The project ([\w\-\.\/]+) is hosted on GitHub",
        r"The project ([\w\-\.\/]+) on GitHub",
        r"The GitHub project ([\w\-\.\/]+) currently",
        r"The GitHub project named ([\w\-\.\/]+) currently",
        r"The project is hosted on GitHub under the name ([\w\-\.\/]+),",
        r"The project named ([\w\-\.\/]+) on GitHub",
        r"The project named ([\w\-\.\/]+) is hosted",
        r"The project ([\w\-\.\/]+) is a GitHub repository"
    ]
    
    project_name = None
    for pat in name_patterns:
        m = re.search(pat, text, re.IGNORECASE)
        if m:
            project_name = m.group(1)
            break
            
    if not project_name:
        # Fallback: maybe just the second word? But "The project is hosted..."
        pass

    # Extract Forks
    # Patterns: "X forks", "forks count of X"
    forks = 0
    fork_patterns = [
        r"and ([0-9,]+) forks",
        r"forks count of ([0-9,]+)",
        r"([0-9,]+) forks"
    ]
    
    for pat in fork_patterns:
        m = re.search(pat, text)
        if m:
            num_str = m.group(1).replace(',', '')
            try:
                forks = int(num_str)
                break # Take the first match
            except:
                continue
                
    return project_name, forks

for row in project_info_data:
    info = row.get('Project_Information', '')
    p_name, p_forks = parse_project_info(info)
    if p_name:
        project_metrics[p_name] = p_forks

# 2. Create set of valid packages (Name, Version)
valid_packages = set()
for pkg in package_data:
    valid_packages.add((pkg['Name'], pkg['Version']))

# 3. Join with project_packageversion
# We want: distinct projects that have at least one valid package, sorted by forks.
matched_projects = {} # ProjectName -> Forks

for row in ppv_data:
    p_name = row.get('ProjectName')
    if not p_name:
        continue
    
    # Check if this project is in our metrics (otherwise we don't know its fork count)
    if p_name in project_metrics:
        # Check if this row is a valid package
        pkg_key = (row.get('Name'), row.get('Version'))
        if pkg_key in valid_packages:
            matched_projects[p_name] = project_metrics[p_name]

# 4. Sort and take top 5
sorted_projects = sorted(matched_projects.items(), key=lambda x: x[1], reverse=True)
top_5 = sorted_projects[:5]

print("__RESULT__:")
print(json.dumps(top_5))"""

env_args = {'var_function-call-12867843472110857426': ['packageinfo'], 'var_function-call-12867843472110857625': ['project_info', 'project_packageversion'], 'var_function-call-10984041455623859307': [{'System': 'NPM', 'Name': '@ecl/twig-component-carousel', 'Version': '3.11.1', 'Licenses': '[\n  "EUPL-1.2"\n]', 'Links': '[\n  {\n    "Label": "ORIGIN",\n    "URL": "https://registry.npmjs.org/@ecl%2Ftwig-component-carousel/3.11.1"\n  }\n]', 'Advisories': '[]', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 29\n}', 'Hashes': '[\n  {\n    "Hash": "vH5da6eUZ94i1AcOsrC6VjSV88cMUe5A1w+CDHAt2aYXldR9sBNRCse27cIx51GnUjnj7dSe3o5A81TjraJ0Lw==",\n    "Type": "SHA512"\n  },\n  {\n    "Hash": "WZUWPp1jVp6nrUZ0n7vmthbB4OrtnLFNDOPPBBNp15I=",\n    "Type": "SHA256"\n  },\n  {\n    "Hash": "JbFslb4AeqQVI+LCXFeZKFrWmHI=",\n    "Type": "SHA1"\n  },\n  {\n    "Hash": "zBm5Qvg5p2bQwUTcg6hZYA==",\n    "Type": "MD5"\n  }\n]', 'DependenciesProcessed': '1', 'DependencyError': '0', 'UpstreamPublishedAt': '1699345351000000.0', 'Registries': '[]', 'SLSAProvenance': 'None', 'UpstreamIdentifiers': '[]', 'Purl': 'None'}], 'var_function-call-10984041455623856674': [{'Project_Information': 'The project lberrocal/npm-packages-template is hosted on GitHub and currently has 0 open issues, 0 stars, and 0 forks.', 'Licenses': '[]', 'Description': 'Template for npm package library configured to be used with CI/CD', 'Homepage': 'None', 'OSSFuzz': 'nan'}], 'var_function-call-10984041455623858137': [{'System': 'NPM', 'Name': '@dms/io', 'Version': '0.9.0', 'ProjectType': 'GITHUB', 'ProjectName': 'dataminingsupply/dms-io', 'RelationProvenance': 'UNVERIFIED_METADATA', 'RelationType': 'SOURCE_REPO_TYPE'}], 'var_function-call-15460082337333858862': [{'Project_Information': 'The project lberrocal/npm-packages-template is hosted on GitHub and currently has 0 open issues, 0 stars, and 0 forks.'}, {'Project_Information': 'The project leaflet/leaflet on GitHub is a popular open-source library that currently has 521 open issues, 38715 stars, and 5782 forks, making it a widely recognized tool in the developer community.'}, {'Project_Information': 'The project leaflet/leaflet.fullscreen on GitHub currently has 29 open issues, 417 stars, and 118 forks, making it a noteworthy contribution to the Leaflet ecosystem.'}, {'Project_Information': 'The project leaflet/leaflet.markercluster is hosted on GitHub and currently has an open issues count of 130, along with a stars count of 3761 and forks count of 988.'}, {'Project_Information': 'The project leandrowd/react-responsive-carousel on GitHub has garnered significant attention, with a total of 2,534 stars and 636 forks, while currently having 23 open issues.'}], 'var_function-call-9978821279046557838': 'file_storage/function-call-9978821279046557838.json', 'var_function-call-1937016187943461082': [{'count_star()': '597602'}], 'var_function-call-16694617714043807106': [{'count_star()': '770'}], 'var_function-call-8003098710851808412': 'file_storage/function-call-8003098710851808412.json', 'var_function-call-7590661337522328408': 'file_storage/function-call-7590661337522328408.json'}

exec(code, env_args)
