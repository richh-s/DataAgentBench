code = """import json
import re

# Load project_info
file_path = locals()['var_function-call-3255179192108180976']
with open(file_path, 'r') as f:
    project_info_list = json.load(f)

project_stars = {}

for entry in project_info_list:
    text = entry.get('Project_Information', '')
    # Regex to find project name and stars
    # "The project owner/repo ..." or "The project is hosted on GitHub under the name owner/repo ..."
    # "The GitHub project named owner/repo ..."
    # "The project named owner/repo ..."
    
    # Try multiple patterns for name
    name_match = re.search(r'project (?:is hosted on GitHub under the name |named |is a GitHub repository named |is hosted on GITHUB and currently has an open issues count of \d+, a stars count of \d+, and a forks count of \d+, making it a notable resource for developers looking to integrate )?([a-zA-Z0-9_.-]+/[a-zA-Z0-9_.-]+)', text)
    
    # Try a simpler extraction if complex one fails
    if not name_match:
         name_match = re.search(r'project ([a-zA-Z0-9_.-]+/[a-zA-Z0-9_.-]+)', text)

    # Stars
    # "stars count of X" or "X stars"
    stars_match = re.search(r'stars count of ([\d,]+)', text)
    if not stars_match:
        stars_match = re.search(r'([\d,]+) stars', text)
        
    if name_match and stars_match:
        name = name_match.group(1)
        stars_str = stars_match.group(1).replace(',', '')
        try:
            stars = int(stars_str)
            project_stars[name] = stars
        except:
            pass

# Sort by stars desc
sorted_projects = sorted(project_stars.items(), key=lambda x: x[1], reverse=True)

# Let's keep all identified projects
project_names = [p[0] for p in sorted_projects]

result = {
    "project_stars": project_stars,
    "project_names": project_names
}

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_function-call-16868295410973434380': [{'Project_Information': 'The project lberrocal/npm-packages-template is hosted on GitHub and currently has 0 open issues, 0 stars, and 0 forks.', 'Licenses': '[]', 'Description': 'Template for npm package library configured to be used with CI/CD', 'Homepage': 'None', 'OSSFuzz': 'nan'}, {'Project_Information': 'The project leaflet/leaflet on GitHub is a popular open-source library that currently has 521 open issues, 38715 stars, and 5782 forks, making it a widely recognized tool in the developer community.', 'Licenses': '[\n  "non-standard"\n]', 'Description': '🍃 JavaScript library for mobile-friendly interactive maps 🇺🇦', 'Homepage': 'https://leafletjs.com', 'OSSFuzz': 'nan'}, {'Project_Information': 'The project leaflet/leaflet.fullscreen on GitHub currently has 29 open issues, 417 stars, and 118 forks, making it a noteworthy contribution to the Leaflet ecosystem.', 'Licenses': '[\n  "ISC"\n]', 'Description': 'A fullscreen control for Leaflet', 'Homepage': 'http://leaflet.github.io/Leaflet.fullscreen/', 'OSSFuzz': 'nan'}], 'var_function-call-16868295410973434277': [{'System': 'NPM', 'Name': '@ecl/twig-component-carousel', 'Version': '3.11.1', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 29\n}', 'UpstreamPublishedAt': '1699345351000000.0'}, {'System': 'NPM', 'Name': '@douganderson444/panzoom-node', 'Version': '1.1.5', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 18\n}', 'UpstreamPublishedAt': '1670271173000000.0'}, {'System': 'NPM', 'Name': '@douganderson444/panzoom-node', 'Version': '1.1.1', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 14\n}', 'UpstreamPublishedAt': '1654791421000000.0'}], 'var_function-call-4178620871579730136': [{'column_name': 'Project_Information', 'column_type': 'VARCHAR', 'null': 'YES', 'key': 'None', 'default': 'None', 'extra': 'None'}, {'column_name': 'Licenses', 'column_type': 'VARCHAR', 'null': 'YES', 'key': 'None', 'default': 'None', 'extra': 'None'}, {'column_name': 'Description', 'column_type': 'VARCHAR', 'null': 'YES', 'key': 'None', 'default': 'None', 'extra': 'None'}, {'column_name': 'Homepage', 'column_type': 'VARCHAR', 'null': 'YES', 'key': 'None', 'default': 'None', 'extra': 'None'}, {'column_name': 'OSSFuzz', 'column_type': 'DOUBLE', 'null': 'YES', 'key': 'None', 'default': 'None', 'extra': 'None'}], 'var_function-call-4178620871579733381': [{'COUNT(*)': '661372'}], 'var_function-call-5834658971357262038': [{'count_star()': '770'}], 'var_function-call-5834658971357262757': [{'count_star()': '597602'}], 'var_function-call-5834658971357263476': [{'COUNT(DISTINCT Name)': '16614'}], 'var_function-call-3255179192108180976': 'file_storage/function-call-3255179192108180976.json', 'var_function-call-8543107306348249679': 'file_storage/function-call-8543107306348249679.json'}

exec(code, env_args)
