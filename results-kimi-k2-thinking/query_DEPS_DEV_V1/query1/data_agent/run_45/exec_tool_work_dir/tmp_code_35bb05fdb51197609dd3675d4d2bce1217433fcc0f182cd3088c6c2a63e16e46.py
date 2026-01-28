code = """import json

# Read package data
pkg_file = "file_storage/functions.query_db:26.json"
with open(pkg_file, 'r') as f:
    packages = json.load(f)

print(f'Total packages loaded: {len(packages)}')

# Parse and filter NPM packages
npm_packages = []
for pkg in packages:
    try:
        version_info_str = pkg['VersionInfo']
        version_info = json.loads(version_info_str)
        
        # Extract repository info from Links
        repo_url = None
        links_str = pkg.get('Links', '[]')
        if links_str:
            try:
                links = json.loads(links_str)
                for link in links:
                    if link.get('Label') == 'SOURCE_REPO':
                        repo_url = link.get('URL', '')
                        # Clean up git+ URLs
                        if repo_url.startswith('git+'):
                            repo_url = repo_url[4:]
                        if repo_url.endswith('.git'):
                            repo_url = repo_url[:-4]
                        break
            except:
                pass
        
        npm_packages.append({
            'Name': pkg['Name'],
            'Version': pkg['Version'],
            'IsRelease': version_info.get('IsRelease', False),
            'Ordinal': version_info.get('Ordinal', 0),
            'PublishedAt': float(pkg.get('UpstreamPublishedAt') or 0),
            'RepoURL': repo_url
        })
    except Exception as e:
        print(f"Error processing: {e}")

print(f'NPM packages parsed: {len(npm_packages)}')
print('First few entries:', npm_packages[:3])

# Find latest release for each package
from collections import defaultdict

latest_releases = {}
for pkg in npm_packages:
    name = pkg['Name']
    if pkg['IsRelease']:  # Only consider release versions
        if name not in latest_releases or pkg['Ordinal'] > latest_releases[name]['Ordinal']:
            latest_releases[name] = pkg

print(f'Latest releases found: {len(latest_releases)}')

# Get packages with their latest release data
latest_packages = list(latest_releases.values())
print('Sample latest releases:', latest_packages[:3])"""

env_args = {'var_functions.list_db:0': ['packageinfo'], 'var_functions.list_db:2': ['project_info', 'project_packageversion'], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:6': [{'System': 'NPM', 'Name': '@dxos/client', 'Version': '2.28.20-dev.a2e143d3', 'VersionInfo': '{\n  "IsRelease": false,\n  "Ordinal": 1514\n}'}, {'System': 'NPM', 'Name': '@dxos/client', 'Version': '2.28.20-dev.a2e143d3', 'VersionInfo': '{\n  "IsRelease": false,\n  "Ordinal": 1514\n}'}, {'System': 'NPM', 'Name': '@dxos/client', 'Version': '2.31.8-dev.dcd68d50', 'VersionInfo': '{\n  "IsRelease": false,\n  "Ordinal": 1605\n}'}, {'System': 'NPM', 'Name': '@dxos/client', 'Version': '2.31.8-dev.dcd68d50', 'VersionInfo': '{\n  "IsRelease": false,\n  "Ordinal": 1605\n}'}, {'System': 'NPM', 'Name': '@dxos/client', 'Version': '2.1.2-beta.0', 'VersionInfo': '{\n  "IsRelease": false,\n  "Ordinal": 974\n}'}], 'var_functions.query_db:8': [{'System': 'NPM', 'Name': '@dms/io', 'Version': '0.9.0', 'ProjectType': 'GITHUB', 'ProjectName': 'dataminingsupply/dms-io', 'RelationProvenance': 'UNVERIFIED_METADATA', 'RelationType': 'SOURCE_REPO_TYPE'}, {'System': 'NPM', 'Name': '@dvo/fc', 'Version': '0.0.4', 'ProjectType': 'GITHUB', 'ProjectName': 'isacvale/fc', 'RelationProvenance': 'UNVERIFIED_METADATA', 'RelationType': 'SOURCE_REPO_TYPE'}, {'System': 'NPM', 'Name': '@djie/ui', 'Version': '1.0.17', 'ProjectType': 'GITHUB', 'ProjectName': 'laihaojie/jie', 'RelationProvenance': 'UNVERIFIED_METADATA', 'RelationType': 'SOURCE_REPO_TYPE'}, {'System': 'NPM', 'Name': '@djie/ui', 'Version': '1.0.16', 'ProjectType': 'GITHUB', 'ProjectName': 'laihaojie/jie', 'RelationProvenance': 'UNVERIFIED_METADATA', 'RelationType': 'SOURCE_REPO_TYPE'}, {'System': 'NPM', 'Name': '@djie/ws', 'Version': '1.0.8', 'ProjectType': 'GITHUB', 'ProjectName': 'laihaojie/jie', 'RelationProvenance': 'UNVERIFIED_METADATA', 'RelationType': 'SOURCE_REPO_TYPE'}], 'var_functions.query_db:10': [{'System': 'NPM', 'Name': '@ecl/twig-component-carousel', 'Version': '3.11.1', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 29\n}'}, {'System': 'NPM', 'Name': '@douganderson444/panzoom-node', 'Version': '1.1.5', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 18\n}'}, {'System': 'NPM', 'Name': '@douganderson444/panzoom-node', 'Version': '1.1.1', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 14\n}'}, {'System': 'NPM', 'Name': '@discue/ui-components', 'Version': '0.13.0', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 12\n}'}, {'System': 'NPM', 'Name': '@dvcol/web-extension-utils', 'Version': '1.1.1', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 7\n}'}, {'System': 'NPM', 'Name': '@edgedev/firebase', 'Version': '1.0.12', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 13\n}'}, {'System': 'NPM', 'Name': '@dyoshikawa/mentor-php-env', 'Version': '0.0.11', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 10\n}'}, {'System': 'NPM', 'Name': '@eclipsejs/cli', 'Version': '1.0.0', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 13\n}'}, {'System': 'NPM', 'Name': '@dytesdk/electron-main', 'Version': '1.0.2', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 6\n}'}, {'System': 'NPM', 'Name': '@ebot7/edem-react', 'Version': '0.18.8', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 55\n}'}], 'var_functions.query_db:12': [{'cnt': '597602'}], 'var_functions.query_db:14': [{'Project_Information': 'The project lberrocal/npm-packages-template is hosted on GitHub and currently has 0 open issues, 0 stars, and 0 forks.', 'Licenses': '[]', 'Description': 'Template for npm package library configured to be used with CI/CD', 'Homepage': 'None', 'OSSFuzz': 'nan'}, {'Project_Information': 'The project leaflet/leaflet on GitHub is a popular open-source library that currently has 521 open issues, 38715 stars, and 5782 forks, making it a widely recognized tool in the developer community.', 'Licenses': '[\n  "non-standard"\n]', 'Description': '🍃 JavaScript library for mobile-friendly interactive maps 🇺🇦', 'Homepage': 'https://leafletjs.com', 'OSSFuzz': 'nan'}, {'Project_Information': 'The project leaflet/leaflet.fullscreen on GitHub currently has 29 open issues, 417 stars, and 118 forks, making it a noteworthy contribution to the Leaflet ecosystem.', 'Licenses': '[\n  "ISC"\n]', 'Description': 'A fullscreen control for Leaflet', 'Homepage': 'http://leaflet.github.io/Leaflet.fullscreen/', 'OSSFuzz': 'nan'}, {'Project_Information': 'The project leaflet/leaflet.markercluster is hosted on GitHub and currently has an open issues count of 130, along with a stars count of 3761 and forks count of 988.', 'Licenses': '[\n  "MIT"\n]', 'Description': 'Marker Clustering plugin for Leaflet', 'Homepage': 'None', 'OSSFuzz': 'nan'}, {'Project_Information': 'The project leandrowd/react-responsive-carousel on GitHub has garnered significant attention, with a total of 2,534 stars and 636 forks, while currently having 23 open issues.', 'Licenses': '[\n  "MIT"\n]', 'Description': 'React.js Responsive Carousel (with Swipe)', 'Homepage': 'http://leandrowd.github.io/react-responsive-carousel/', 'OSSFuzz': 'nan'}, {'Project_Information': 'The project is hosted on GitHub under the name learnfrontend-dc/product-cart, and it currently has 2 open issues. It has garnered a total of 11 stars and has been forked 12 times.', 'Licenses': '[]', 'Description': 'None', 'Homepage': 'None', 'OSSFuzz': 'nan'}, {'Project_Information': 'The GitHub project ledgerproject/keypairoom currently has 3 open issues, 3 stars, and 0 forks.', 'Licenses': '[\n  "AGPL-3.0"\n]', 'Description': 'Component to generate and regenerate a keypair, in a deterministic and private way', 'Homepage': 'None', 'OSSFuzz': 'nan'}, {'Project_Information': 'The project leebyron/jasmine-check is hosted on GitHub and currently has 0 open issues, 11 stars, and 3 forks.', 'Licenses': '[]', 'Description': 'Generative property testing for Jasmine', 'Homepage': 'None', 'OSSFuzz': 'nan'}, {'Project_Information': 'The project leebyron/testcheck-js on GitHub has an open issues count of 29, a stars count of 1185, and a forks count of 58, making it a notable repository in the community.', 'Licenses': '[\n  "non-standard"\n]', 'Description': 'Generative testing for JavaScript', 'Homepage': 'http://leebyron.com/testcheck-js', 'OSSFuzz': 'nan'}, {'Project_Information': 'The project leecade/react-native-swiper is hosted on GitHub and has a total of 786 open issues, along with an impressive 10,249 stars and 2,392 forks, making it a popular choice among developers for implementing swiping functionality in React Native applications.', 'Licenses': '[\n  "MIT"\n]', 'Description': 'The best Swiper component for React Native.', 'Homepage': 'None', 'OSSFuzz': 'nan'}], 'var_functions.execute_python:20': 'file_storage/functions.query_db:5.json', 'var_functions.execute_python:22': {'total_packages': 100, 'npm_packages': 100, 'sample': [{'System': 'NPM', 'Name': '@ecl/twig-component-carousel', 'Version': '3.11.1', 'IsRelease': True, 'Ordinal': 29, 'PublishedAt': 1699345351000000.0}, {'System': 'NPM', 'Name': '@douganderson444/panzoom-node', 'Version': '1.1.5', 'IsRelease': True, 'Ordinal': 18, 'PublishedAt': 1670271173000000.0}, {'System': 'NPM', 'Name': '@douganderson444/panzoom-node', 'Version': '1.1.1', 'IsRelease': True, 'Ordinal': 14, 'PublishedAt': 1654791421000000.0}]}, 'var_functions.query_db:24': [{'Project_Information': 'The project lberrocal/npm-packages-template is hosted on GitHub and currently has 0 open issues, 0 stars, and 0 forks.'}, {'Project_Information': 'The project leaflet/leaflet on GitHub is a popular open-source library that currently has 521 open issues, 38715 stars, and 5782 forks, making it a widely recognized tool in the developer community.'}, {'Project_Information': 'The project leaflet/leaflet.fullscreen on GitHub currently has 29 open issues, 417 stars, and 118 forks, making it a noteworthy contribution to the Leaflet ecosystem.'}, {'Project_Information': 'The project leaflet/leaflet.markercluster is hosted on GitHub and currently has an open issues count of 130, along with a stars count of 3761 and forks count of 988.'}, {'Project_Information': 'The project leandrowd/react-responsive-carousel on GitHub has garnered significant attention, with a total of 2,534 stars and 636 forks, while currently having 23 open issues.'}, {'Project_Information': 'The project is hosted on GitHub under the name learnfrontend-dc/product-cart, and it currently has 2 open issues. It has garnered a total of 11 stars and has been forked 12 times.'}, {'Project_Information': 'The GitHub project ledgerproject/keypairoom currently has 3 open issues, 3 stars, and 0 forks.'}, {'Project_Information': 'The project leebyron/jasmine-check is hosted on GitHub and currently has 0 open issues, 11 stars, and 3 forks.'}, {'Project_Information': 'The project leebyron/testcheck-js on GitHub has an open issues count of 29, a stars count of 1185, and a forks count of 58, making it a notable repository in the community.'}, {'Project_Information': 'The project leecade/react-native-swiper is hosted on GitHub and has a total of 786 open issues, along with an impressive 10,249 stars and 2,392 forks, making it a popular choice among developers for implementing swiping functionality in React Native applications.'}, {'Project_Information': 'The project legendjaden/aftablecolumn on GitHub currently has an open issues count of 35, a stars count of 136, and a forks count of 29.'}, {'Project_Information': 'The project lekoarts/gatsby-themes on GitHub currently has 11 open issues, 1836 stars, and 568 forks, making it a popular choice among developers looking for Gatsby themes.'}, {'Project_Information': 'The GitHub project lenconda/dollie currently has 0 open issues, 12 stars, and 3 forks, making it a noteworthy repository in its category.'}, {'Project_Information': 'The project leo-ran/easy-node-reflect is hosted on GitHub and currently has 0 open issues, 0 stars, and 0 forks, indicating that it may be in its early stages or not yet widely recognized within the GitHub community.'}, {'Project_Information': 'The project named leo-ran/easy-node-server is hosted on GitHub and currently has an open issues count of 0, stars count of 0, and forks count of 0.'}], 'var_functions.query_db:26': 'file_storage/functions.query_db:26.json'}

exec(code, env_args)
