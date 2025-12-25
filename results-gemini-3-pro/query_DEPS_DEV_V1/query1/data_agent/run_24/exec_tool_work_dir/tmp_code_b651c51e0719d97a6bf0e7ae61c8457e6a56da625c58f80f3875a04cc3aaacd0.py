code = """import json
import re

# Load data
with open(locals()['var_function-call-14443527561838418530'], 'r') as f:
    latest_packages = json.load(f)

with open(locals()['var_function-call-2845906047691929764'], 'r') as f:
    project_mappings = json.load(f)

with open(locals()['var_function-call-14939796039816498915'], 'r') as f:
    project_infos = json.load(f)

# 1. Create set of latest packages
latest_pkg_set = set()
for pkg in latest_packages:
    latest_pkg_set.add((pkg['Name'], pkg['Version']))

# 2. Filter mappings
valid_mappings = []
seen_mappings = set()
for m in project_mappings:
    key = (m['Name'], m['Version'])
    if key in latest_pkg_set:
        # Avoid duplicate rows from the mapping table if any
        # But wait, a package might map to multiple projects?
        # If so, which one to pick? Usually 1:1.
        # If 1:N, we might get the same package with different stars.
        # But here the duplicate result showed same Name, Version, Stars.
        # So it's likely just duplicate rows or same project.
        # We can handle this by checking if we already processed this package.
        # Or better: collect all candidates, then deduplicate by Name?
        # The query asks "which packages". Distinct packages.
        # So I should have unique Name.
        # "Considering only the latest release versions for each distinct NPM package" -> Unique Name.
        # The 'latest_packages' list is already unique by Name.
        # So if I join, I should keep it unique by Name.
        if key not in seen_mappings:
            valid_mappings.append(m)
            seen_mappings.add(key)

# 3. Parse Project Info for Stars
project_stars = {}
name_pattern = re.compile(r"(?:project|name)\s+(?:named\s+)?(?:is\s+hosted\s+on\s+GitHub\s+under\s+the\s+name\s+)?([a-zA-Z0-9\-_]+/[a-zA-Z0-9\-_.]+)")
stars_pattern = re.compile(r"(\d+(?:,\d+)*)\s+stars")

for info in project_infos:
    text = info['Project_Information']
    match_name = name_pattern.search(text)
    match_stars = stars_pattern.search(text)
    
    if match_name and match_stars:
        project_name = match_name.group(1)
        stars = int(match_stars.group(1).replace(',', ''))
        project_stars[project_name] = stars

# 4. Join
results = []
# We want unique packages. valid_mappings should be unique by (Name, Version) now.
for m in valid_mappings:
    p_name = m['ProjectName']
    if p_name in project_stars:
        results.append({
            'Name': m['Name'],
            'Version': m['Version'],
            'Stars': project_stars[p_name]
        })

# 5. Sort and Top 5
results.sort(key=lambda x: x['Stars'], reverse=True)
top_5 = results[:5]

print("__RESULT__:")
print(json.dumps(top_5))"""

env_args = {'var_function-call-12019473054385977647': [{'Project_Information': 'The project lberrocal/npm-packages-template is hosted on GitHub and currently has 0 open issues, 0 stars, and 0 forks.', 'Licenses': '[]', 'Description': 'Template for npm package library configured to be used with CI/CD', 'Homepage': 'None', 'OSSFuzz': 'nan'}, {'Project_Information': 'The project leaflet/leaflet on GitHub is a popular open-source library that currently has 521 open issues, 38715 stars, and 5782 forks, making it a widely recognized tool in the developer community.', 'Licenses': '[\n  "non-standard"\n]', 'Description': '🍃 JavaScript library for mobile-friendly interactive maps 🇺🇦', 'Homepage': 'https://leafletjs.com', 'OSSFuzz': 'nan'}, {'Project_Information': 'The project leaflet/leaflet.fullscreen on GitHub currently has 29 open issues, 417 stars, and 118 forks, making it a noteworthy contribution to the Leaflet ecosystem.', 'Licenses': '[\n  "ISC"\n]', 'Description': 'A fullscreen control for Leaflet', 'Homepage': 'http://leaflet.github.io/Leaflet.fullscreen/', 'OSSFuzz': 'nan'}, {'Project_Information': 'The project leaflet/leaflet.markercluster is hosted on GitHub and currently has an open issues count of 130, along with a stars count of 3761 and forks count of 988.', 'Licenses': '[\n  "MIT"\n]', 'Description': 'Marker Clustering plugin for Leaflet', 'Homepage': 'None', 'OSSFuzz': 'nan'}, {'Project_Information': 'The project leandrowd/react-responsive-carousel on GitHub has garnered significant attention, with a total of 2,534 stars and 636 forks, while currently having 23 open issues.', 'Licenses': '[\n  "MIT"\n]', 'Description': 'React.js Responsive Carousel (with Swipe)', 'Homepage': 'http://leandrowd.github.io/react-responsive-carousel/', 'OSSFuzz': 'nan'}], 'var_function-call-5483379945343837933': [{'Name': '@ecl/twig-component-carousel', 'Version': '3.11.1', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 29\n}', 'UpstreamPublishedAt': '1699345351000000.0'}, {'Name': '@douganderson444/panzoom-node', 'Version': '1.1.5', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 18\n}', 'UpstreamPublishedAt': '1670271173000000.0'}, {'Name': '@douganderson444/panzoom-node', 'Version': '1.1.1', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 14\n}', 'UpstreamPublishedAt': '1654791421000000.0'}, {'Name': '@dreamworld/dw-select', 'Version': '3.1.2-fix-double-click-issue.1', 'VersionInfo': '{\n  "IsRelease": false,\n  "Ordinal": 129\n}', 'UpstreamPublishedAt': '1624260093000000.0'}, {'Name': '@discue/ui-components', 'Version': '0.13.0', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 12\n}', 'UpstreamPublishedAt': '1656518476000000.0'}], 'var_function-call-1142659303685043375': [{'COUNT(*)': '661372'}], 'var_function-call-3486770934197289607': [{'Name': '@discordx/music', 'Version': '6.0.2'}, {'Name': '@discordx/pagination', 'Version': '3.4.1'}, {'Name': '@discordx/utilities', 'Version': '5.2.1'}, {'Name': '@discoteam/vueify', 'Version': '1.0.0'}, {'Name': '@discourse/itsatrap', 'Version': '2.0.10'}, {'Name': '@discourse/moment-timezone-names-translations', 'Version': '1.0.0'}, {'Name': '@discoursegroup/commons-js', 'Version': '0.0.11'}, {'Name': '@discoursegroup/commons-test-js', 'Version': '0.0.4'}, {'Name': '@discoursegroup/relayrabbit-addons-js', 'Version': '0.0.384'}, {'Name': '@discoursegroup/relayrabbit-commons-js', 'Version': '0.0.7'}], 'var_function-call-10168844906737215568': [{'count(distinct Name)': '16614'}], 'var_function-call-5191022865534257296': [{'count_star()': '770'}], 'var_function-call-14443527561838418530': 'file_storage/function-call-14443527561838418530.json', 'var_function-call-2845906047691929764': 'file_storage/function-call-2845906047691929764.json', 'var_function-call-14939796039816498915': 'file_storage/function-call-14939796039816498915.json', 'var_function-call-12562208999251969595': [{'Name': '@dylanvann/svelte', 'Version': '3.25.4', 'Stars': 73499}, {'Name': '@dylanvann/svelte', 'Version': '3.25.4', 'Stars': 73499}, {'Name': '@dumc11/tailwindcss', 'Version': '0.4.0', 'Stars': 73464}, {'Name': '@dumc11/tailwindcss', 'Version': '0.4.0', 'Stars': 73464}, {'Name': '@dman777/shadow-dom-quill-temp', 'Version': '1.0.0', 'Stars': 42407}]}

exec(code, env_args)
