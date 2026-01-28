code = """import json, re
pkg_file = locals()['var_functions.query_db:26']
ver_file = locals()['var_functions.query_db:8']
info_file = locals()['var_functions.query_db:6']

packages = json.load(open(pkg_file))
versions = json.load(open(ver_file))
projects = json.load(open(info_file))

# Filter for MIT license and release status
mit_releases = []
for pkg in packages:
    try:
        if pkg['System'] == 'NPM':
            licenses = json.loads(pkg['Licenses'])
            ver_info = json.loads(pkg['VersionInfo'].replace('\n', '').strip())
            if 'MIT' in licenses and ver_info.get('IsRelease', False) == True:
                mit_releases.append(pkg)
    except:
        continue

print('MIT release packages:', len(mit_releases))

# Create lookup for versions
ver_map = {}
for ver in versions:
    key = (ver['System'], ver['Name'], ver['Version'])
    ver_map[key] = ver.get('ProjectName')

# Extract fork counts from project info
proj_forks = {}
for proj in projects:
    info = proj['Project_Information']
    match = re.search(r'(\d+)\s+forks', str(info), re.I)
    forks = int(match.group(1)) if match else 0
    proj_forks[info] = forks

# Map packages to projects and get fork counts
project_fork_counts = {}
processed_projects = set()

for pkg in mit_releases:
    key = (pkg['System'], pkg['Name'], pkg['Version'])
    proj_name = ver_map.get(key)
    
    if proj_name and proj_name not in processed_projects:
        processed_projects.add(proj_name)
        # Find project info matching this project name
        for proj_info, forks in proj_forks.items():
            if proj_name in proj_info and forks > 0:
                project_fork_counts[proj_name] = forks
                break

# Get top 5
top5 = sorted(project_fork_counts.items(), key=lambda x: x[1], reverse=True)[:5]

result = {'top5': top5, 'total_packages': len(mit_releases), 'projects_mapped': len(project_fork_counts)}
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['packageinfo'], 'var_functions.list_db:1': ['project_info', 'project_packageversion'], 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json', 'var_functions.query_db:6': [{'Project_Information': 'The project lberrocal/npm-packages-template is hosted on GitHub and currently has 0 open issues, 0 stars, and 0 forks.', 'Licenses': '[]', 'Description': 'Template for npm package library configured to be used with CI/CD', 'Homepage': 'None', 'OSSFuzz': 'nan'}, {'Project_Information': 'The project leaflet/leaflet on GitHub is a popular open-source library that currently has 521 open issues, 38715 stars, and 5782 forks, making it a widely recognized tool in the developer community.', 'Licenses': '[\n  "non-standard"\n]', 'Description': '🍃 JavaScript library for mobile-friendly interactive maps 🇺🇦', 'Homepage': 'https://leafletjs.com', 'OSSFuzz': 'nan'}, {'Project_Information': 'The project leaflet/leaflet.fullscreen on GitHub currently has 29 open issues, 417 stars, and 118 forks, making it a noteworthy contribution to the Leaflet ecosystem.', 'Licenses': '[\n  "ISC"\n]', 'Description': 'A fullscreen control for Leaflet', 'Homepage': 'http://leaflet.github.io/Leaflet.fullscreen/', 'OSSFuzz': 'nan'}, {'Project_Information': 'The project leaflet/leaflet.markercluster is hosted on GitHub and currently has an open issues count of 130, along with a stars count of 3761 and forks count of 988.', 'Licenses': '[\n  "MIT"\n]', 'Description': 'Marker Clustering plugin for Leaflet', 'Homepage': 'None', 'OSSFuzz': 'nan'}, {'Project_Information': 'The project leandrowd/react-responsive-carousel on GitHub has garnered significant attention, with a total of 2,534 stars and 636 forks, while currently having 23 open issues.', 'Licenses': '[\n  "MIT"\n]', 'Description': 'React.js Responsive Carousel (with Swipe)', 'Homepage': 'http://leandrowd.github.io/react-responsive-carousel/', 'OSSFuzz': 'nan'}, {'Project_Information': 'The project is hosted on GitHub under the name learnfrontend-dc/product-cart, and it currently has 2 open issues. It has garnered a total of 11 stars and has been forked 12 times.', 'Licenses': '[]', 'Description': 'None', 'Homepage': 'None', 'OSSFuzz': 'nan'}, {'Project_Information': 'The GitHub project ledgerproject/keypairoom currently has 3 open issues, 3 stars, and 0 forks.', 'Licenses': '[\n  "AGPL-3.0"\n]', 'Description': 'Component to generate and regenerate a keypair, in a deterministic and private way', 'Homepage': 'None', 'OSSFuzz': 'nan'}, {'Project_Information': 'The project leebyron/jasmine-check is hosted on GitHub and currently has 0 open issues, 11 stars, and 3 forks.', 'Licenses': '[]', 'Description': 'Generative property testing for Jasmine', 'Homepage': 'None', 'OSSFuzz': 'nan'}, {'Project_Information': 'The project leebyron/testcheck-js on GitHub has an open issues count of 29, a stars count of 1185, and a forks count of 58, making it a notable repository in the community.', 'Licenses': '[\n  "non-standard"\n]', 'Description': 'Generative testing for JavaScript', 'Homepage': 'http://leebyron.com/testcheck-js', 'OSSFuzz': 'nan'}, {'Project_Information': 'The project leecade/react-native-swiper is hosted on GitHub and has a total of 786 open issues, along with an impressive 10,249 stars and 2,392 forks, making it a popular choice among developers for implementing swiping functionality in React Native applications.', 'Licenses': '[\n  "MIT"\n]', 'Description': 'The best Swiper component for React Native.', 'Homepage': 'None', 'OSSFuzz': 'nan'}], 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.query_db:18': 'file_storage/functions.query_db:18.json', 'var_functions.query_db:20': 'file_storage/functions.query_db:20.json', 'var_functions.query_db:22': 'file_storage/functions.query_db:22.json', 'var_functions.query_db:26': 'file_storage/functions.query_db:26.json', 'var_functions.query_db:28': 'file_storage/functions.query_db:28.json', 'var_functions.query_db:34': []}

exec(code, env_args)
