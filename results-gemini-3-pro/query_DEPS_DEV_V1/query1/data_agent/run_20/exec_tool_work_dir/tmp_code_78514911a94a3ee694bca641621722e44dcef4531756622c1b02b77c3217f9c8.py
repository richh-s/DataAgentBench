code = """import json

# Load files
project_stars_file = locals()['var_function-call-15329664476362592078']
latest_packages_file = locals()['var_function-call-8543107306348249679']
mappings_file = locals()['var_function-call-16853993012680595200']

with open(project_stars_file, 'r') as f:
    project_data = json.load(f)
    project_stars = project_data['project_stars'] # Dict[ProjectName, Stars]

with open(latest_packages_file, 'r') as f:
    latest_pkgs_list = json.load(f)
    # Create a set for fast lookup: (Name, Version)
    latest_pkgs_set = set()
    for item in latest_pkgs_list:
        latest_pkgs_set.add((item['Name'], item['Version']))

with open(mappings_file, 'r') as f:
    mappings = json.load(f)

# Join
package_star_list = []

for m in mappings:
    pkg_name = m['Name']
    pkg_ver = m['Version']
    proj_name = m['ProjectName']
    
    if (pkg_name, pkg_ver) in latest_pkgs_set:
        # Check if project has stars info
        if proj_name in project_stars:
            stars = project_stars[proj_name]
            package_star_list.append({
                'Package': pkg_name,
                'Version': pkg_ver,
                'Project': proj_name,
                'Stars': stars
            })

# Sort by Stars desc
# Break ties with Package Name asc
package_star_list.sort(key=lambda x: (-x['Stars'], x['Package']))

# Get top 5
top_5 = package_star_list[:5]

print("__RESULT__:")
print(json.dumps(top_5))"""

env_args = {'var_function-call-16868295410973434380': [{'Project_Information': 'The project lberrocal/npm-packages-template is hosted on GitHub and currently has 0 open issues, 0 stars, and 0 forks.', 'Licenses': '[]', 'Description': 'Template for npm package library configured to be used with CI/CD', 'Homepage': 'None', 'OSSFuzz': 'nan'}, {'Project_Information': 'The project leaflet/leaflet on GitHub is a popular open-source library that currently has 521 open issues, 38715 stars, and 5782 forks, making it a widely recognized tool in the developer community.', 'Licenses': '[\n  "non-standard"\n]', 'Description': '🍃 JavaScript library for mobile-friendly interactive maps 🇺🇦', 'Homepage': 'https://leafletjs.com', 'OSSFuzz': 'nan'}, {'Project_Information': 'The project leaflet/leaflet.fullscreen on GitHub currently has 29 open issues, 417 stars, and 118 forks, making it a noteworthy contribution to the Leaflet ecosystem.', 'Licenses': '[\n  "ISC"\n]', 'Description': 'A fullscreen control for Leaflet', 'Homepage': 'http://leaflet.github.io/Leaflet.fullscreen/', 'OSSFuzz': 'nan'}], 'var_function-call-16868295410973434277': [{'System': 'NPM', 'Name': '@ecl/twig-component-carousel', 'Version': '3.11.1', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 29\n}', 'UpstreamPublishedAt': '1699345351000000.0'}, {'System': 'NPM', 'Name': '@douganderson444/panzoom-node', 'Version': '1.1.5', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 18\n}', 'UpstreamPublishedAt': '1670271173000000.0'}, {'System': 'NPM', 'Name': '@douganderson444/panzoom-node', 'Version': '1.1.1', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 14\n}', 'UpstreamPublishedAt': '1654791421000000.0'}], 'var_function-call-4178620871579730136': [{'column_name': 'Project_Information', 'column_type': 'VARCHAR', 'null': 'YES', 'key': 'None', 'default': 'None', 'extra': 'None'}, {'column_name': 'Licenses', 'column_type': 'VARCHAR', 'null': 'YES', 'key': 'None', 'default': 'None', 'extra': 'None'}, {'column_name': 'Description', 'column_type': 'VARCHAR', 'null': 'YES', 'key': 'None', 'default': 'None', 'extra': 'None'}, {'column_name': 'Homepage', 'column_type': 'VARCHAR', 'null': 'YES', 'key': 'None', 'default': 'None', 'extra': 'None'}, {'column_name': 'OSSFuzz', 'column_type': 'DOUBLE', 'null': 'YES', 'key': 'None', 'default': 'None', 'extra': 'None'}], 'var_function-call-4178620871579733381': [{'COUNT(*)': '661372'}], 'var_function-call-5834658971357262038': [{'count_star()': '770'}], 'var_function-call-5834658971357262757': [{'count_star()': '597602'}], 'var_function-call-5834658971357263476': [{'COUNT(DISTINCT Name)': '16614'}], 'var_function-call-3255179192108180976': 'file_storage/function-call-3255179192108180976.json', 'var_function-call-8543107306348249679': 'file_storage/function-call-8543107306348249679.json', 'var_function-call-15329664476362592078': 'file_storage/function-call-15329664476362592078.json', 'var_function-call-16853993012680595200': 'file_storage/function-call-16853993012680595200.json'}

exec(code, env_args)
