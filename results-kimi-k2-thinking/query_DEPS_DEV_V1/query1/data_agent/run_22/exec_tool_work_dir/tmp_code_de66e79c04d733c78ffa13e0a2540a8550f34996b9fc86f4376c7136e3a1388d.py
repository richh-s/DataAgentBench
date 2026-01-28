code = """import json
import re

# Load all matched packages from our earlier analysis
matched_path = locals()['var_functions.execute_python:40']
with open(matched_path, 'r') as f:
    matched_data = json.load(f)

matched_packages = matched_data['matched']
print('Total package-project matches:', len(matched_packages))

# Create lookup: project_name -> list of packages
project_packages = {}
for pkg in matched_packages:
    project = pkg['project']
    if project not in project_packages:
        project_packages[project] = []
    project_packages[project].append(pkg)

print('Unique projects:', len(project_packages))

# Load all project info records to get star counts
projects_file = locals()['var_functions.query_db:46']
with open(projects_file, 'r') as f:
    all_project_records = json.load(f)

print('Total project info records:', len(all_project_records))

# Extract star counts for all projects we care about
project_stars = {}
for record in all_project_records:
    info = record['Project_Information']
    
    # Try to extract project name and stars
    # Pattern: "The project X on GitHub"
    proj_match = re.search(r'The project\s+([\w\-\.]+/[\w\-\.]+)\s+on\s+GitHub', info)
    if proj_match:
        project_name = proj_match.group(1)
        
        # Extract stars
        stars_match = re.search(r'(\d+(?:,\d+)*)\s+stars?', info, re.IGNORECASE)
        if stars_match:
            try:
                stars = int(stars_match.group(1).replace(',', ''))
                project_stars[project_name] = stars
            except:
                pass

print('Projects with extracted star counts:', len(project_stars))

# Now find which of our matched projects have stars
matched_projects_with_stars = []
for project, packages in project_packages.items():
    if project in project_stars:
        stars = project_stars[project]
        matched_projects_with_stars.append({
            'project': project,
            'stars': stars,
            'package_count': len(packages)
        })

print('Matched projects with stars:', len(matched_projects_with_stars))

# Sort by stars and get top 5
top_5_projects = sorted(matched_projects_with_stars, key=lambda x: x['stars'], reverse=True)[:10]
print('Top 5 projects by stars:', top_5_projects[:5])

# For top 5, get the actual packages
result = []
for project_info in top_5_projects[:5]:
    project = project_info['project']
    packages = project_packages[project]
    result.append({
        'project': project,
        'stars': project_info['stars'],
        'packages': packages
    })

print('Top 5 with packages:', json.dumps(result, indent=2)[:500])

output = {'top_5': result}
print('__RESULT__:')
print(json.dumps(output))"""

env_args = {'var_functions.list_db:0': ['packageinfo'], 'var_functions.list_db:2': ['project_info', 'project_packageversion'], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:8': [{'System': 'NPM', 'Name': '@dms/io', 'Version': '0.9.0', 'ProjectType': 'GITHUB', 'ProjectName': 'dataminingsupply/dms-io', 'RelationProvenance': 'UNVERIFIED_METADATA', 'RelationType': 'SOURCE_REPO_TYPE'}, {'System': 'NPM', 'Name': '@dvo/fc', 'Version': '0.0.4', 'ProjectType': 'GITHUB', 'ProjectName': 'isacvale/fc', 'RelationProvenance': 'UNVERIFIED_METADATA', 'RelationType': 'SOURCE_REPO_TYPE'}, {'System': 'NPM', 'Name': '@djie/ui', 'Version': '1.0.17', 'ProjectType': 'GITHUB', 'ProjectName': 'laihaojie/jie', 'RelationProvenance': 'UNVERIFIED_METADATA', 'RelationType': 'SOURCE_REPO_TYPE'}, {'System': 'NPM', 'Name': '@djie/ui', 'Version': '1.0.16', 'ProjectType': 'GITHUB', 'ProjectName': 'laihaojie/jie', 'RelationProvenance': 'UNVERIFIED_METADATA', 'RelationType': 'SOURCE_REPO_TYPE'}, {'System': 'NPM', 'Name': '@djie/ws', 'Version': '1.0.8', 'ProjectType': 'GITHUB', 'ProjectName': 'laihaojie/jie', 'RelationProvenance': 'UNVERIFIED_METADATA', 'RelationType': 'SOURCE_REPO_TYPE'}, {'System': 'NPM', 'Name': '@djie/ws', 'Version': '1.0.10', 'ProjectType': 'GITHUB', 'ProjectName': 'laihaojie/jie', 'RelationProvenance': 'UNVERIFIED_METADATA', 'RelationType': 'SOURCE_REPO_TYPE'}, {'System': 'NPM', 'Name': '@djie/ws', 'Version': '1.0.17', 'ProjectType': 'GITHUB', 'ProjectName': 'laihaojie/jie', 'RelationProvenance': 'UNVERIFIED_METADATA', 'RelationType': 'SOURCE_REPO_TYPE'}, {'System': 'NPM', 'Name': '@dlcs/ng', 'Version': '1.0.0', 'ProjectType': 'GITHUB', 'ProjectName': 'winup/dlcs-ng', 'RelationProvenance': 'UNVERIFIED_METADATA', 'RelationType': 'SOURCE_REPO_TYPE'}, {'System': 'NPM', 'Name': '@dms/cli', 'Version': '1.0.1', 'ProjectType': 'GITHUB', 'ProjectName': 'dataminingsupply/dms-cli', 'RelationProvenance': 'UNVERIFIED_METADATA', 'RelationType': 'SOURCE_REPO_TYPE'}, {'System': 'NPM', 'Name': '@dms/cli', 'Version': '1.0.0', 'ProjectType': 'GITHUB', 'ProjectName': 'dataminingsupply/dms-cli', 'RelationProvenance': 'UNVERIFIED_METADATA', 'RelationType': 'SOURCE_REPO_TYPE'}, {'System': 'NPM', 'Name': '@dms/cli', 'Version': '0.8.0', 'ProjectType': 'GITHUB', 'ProjectName': 'dataminingsupply/dms-cli', 'RelationProvenance': 'UNVERIFIED_METADATA', 'RelationType': 'SOURCE_REPO_TYPE'}, {'System': 'NPM', 'Name': '@dms/cli', 'Version': '0.9.3', 'ProjectType': 'GITHUB', 'ProjectName': 'dataminingsupply/dms-cli', 'RelationProvenance': 'UNVERIFIED_METADATA', 'RelationType': 'SOURCE_REPO_TYPE'}, {'System': 'NPM', 'Name': '@dms/cli', 'Version': '0.2.0', 'ProjectType': 'GITHUB', 'ProjectName': 'dataminingsupply/dms-cli', 'RelationProvenance': 'UNVERIFIED_METADATA', 'RelationType': 'SOURCE_REPO_TYPE'}, {'System': 'NPM', 'Name': '@domp/fp', 'Version': '0.0.1', 'ProjectType': 'GITHUB', 'ProjectName': 'dom-packages/fp', 'RelationProvenance': 'UNVERIFIED_METADATA', 'RelationType': 'SOURCE_REPO_TYPE'}, {'System': 'NPM', 'Name': '@domp/is', 'Version': '0.2.0', 'ProjectType': 'GITHUB', 'ProjectName': 'lohfu/domp-is', 'RelationProvenance': 'UNVERIFIED_METADATA', 'RelationType': 'SOURCE_REPO_TYPE'}, {'System': 'NPM', 'Name': '@domp/is', 'Version': '0.1.3', 'ProjectType': 'GITHUB', 'ProjectName': 'lohfu/domp-is', 'RelationProvenance': 'UNVERIFIED_METADATA', 'RelationType': 'SOURCE_REPO_TYPE'}, {'System': 'NPM', 'Name': '@dosy/ws', 'Version': '8.11.1', 'ProjectType': 'GITHUB', 'ProjectName': 'dosyago/ws', 'RelationProvenance': 'UNVERIFIED_METADATA', 'RelationType': 'SOURCE_REPO_TYPE'}, {'System': 'NPM', 'Name': '@dosy/ws', 'Version': '8.11.4', 'ProjectType': 'GITHUB', 'ProjectName': 'dosyago/ws', 'RelationProvenance': 'UNVERIFIED_METADATA', 'RelationType': 'SOURCE_REPO_TYPE'}, {'System': 'NPM', 'Name': '@dot/cdk', 'Version': '2.1.0', 'ProjectType': 'GITHUB', 'ProjectName': 'shellscape/dot', 'RelationProvenance': 'UNVERIFIED_METADATA', 'RelationType': 'SOURCE_REPO_TYPE'}, {'System': 'NPM', 'Name': '@dot/cdk', 'Version': '0.1.0', 'ProjectType': 'GITHUB', 'ProjectName': 'shellscape/dot', 'RelationProvenance': 'UNVERIFIED_METADATA', 'RelationType': 'SOURCE_REPO_TYPE'}], 'var_functions.execute_python:20': {'packages_loaded': 100}, 'var_functions.query_db:24': [{'Project_Information': 'The project lberrocal/npm-packages-template is hosted on GitHub and currently has 0 open issues, 0 stars, and 0 forks.', 'Licenses': '[]', 'Description': 'Template for npm package library configured to be used with CI/CD', 'Homepage': 'None', 'OSSFuzz': 'nan'}, {'Project_Information': 'The project leaflet/leaflet on GitHub is a popular open-source library that currently has 521 open issues, 38715 stars, and 5782 forks, making it a widely recognized tool in the developer community.', 'Licenses': '[\n  "non-standard"\n]', 'Description': '🍃 JavaScript library for mobile-friendly interactive maps 🇺🇦', 'Homepage': 'https://leafletjs.com', 'OSSFuzz': 'nan'}, {'Project_Information': 'The project leaflet/leaflet.fullscreen on GitHub currently has 29 open issues, 417 stars, and 118 forks, making it a noteworthy contribution to the Leaflet ecosystem.', 'Licenses': '[\n  "ISC"\n]', 'Description': 'A fullscreen control for Leaflet', 'Homepage': 'http://leaflet.github.io/Leaflet.fullscreen/', 'OSSFuzz': 'nan'}, {'Project_Information': 'The project leaflet/leaflet.markercluster is hosted on GitHub and currently has an open issues count of 130, along with a stars count of 3761 and forks count of 988.', 'Licenses': '[\n  "MIT"\n]', 'Description': 'Marker Clustering plugin for Leaflet', 'Homepage': 'None', 'OSSFuzz': 'nan'}, {'Project_Information': 'The project leandrowd/react-responsive-carousel on GitHub has garnered significant attention, with a total of 2,534 stars and 636 forks, while currently having 23 open issues.', 'Licenses': '[\n  "MIT"\n]', 'Description': 'React.js Responsive Carousel (with Swipe)', 'Homepage': 'http://leandrowd.github.io/react-responsive-carousel/', 'OSSFuzz': 'nan'}], 'var_functions.query_db:26': 'file_storage/functions.query_db:26.json', 'var_functions.execute_python:30': {'count': 15811, 'sample': [{'name': '@ecl/twig-component-carousel', 'version': '3.11.1', 'ts': 1699345351000000.0}, {'name': '@douganderson444/panzoom-node', 'version': '1.2.2', 'ts': 1674844413000000.0}, {'name': '@discue/ui-components', 'version': '0.38.2', 'ts': 1682020735000000.0}]}, 'var_functions.query_db:32': 'file_storage/functions.query_db:32.json', 'var_functions.execute_python:36': {'matched': [{'name': '@ecl/twig-component-carousel', 'version': '3.11.1', 'project': 'ec-europa/europa-component-library'}, {'name': '@douganderson444/panzoom-node', 'version': '1.2.2', 'project': 'douganderson444/panzoom-node'}, {'name': '@discue/ui-components', 'version': '0.38.2', 'project': 'discue/ui-components'}]}, 'var_functions.execute_python:40': 'file_storage/functions.execute_python:40.json', 'var_functions.execute_python:44': {'projects': ['cryptocoinjs/ripemd160', 'magnusdanielson/au-fluent-ui', 'duckduckgo/eslint-config-duckduckgo', 'duncanwalter/spider-web', 'visma-draftit/pdf-js-fork', 'dynamicdevs/ai-assistant-ui-core', 'dock365/refield', 'dolomite-exchange/dolomite-margin', 'easylogic/image-filter', 'djforth/jest-matchers', 'dopt/odopt', 'dmnd/dedent', 'browserify/resolve', 'draswap/redux-multicall', 'dolittle-tools/boilerplates-discoverer', 'dr-wade/drwade-cli', 'dk1a/solecslib', 'amadousysada/easypay_sdk', 'djencks/asciidoctor-antora-indexer', 'duacom/dua-icons']}, 'var_functions.query_db:46': 'file_storage/functions.query_db:46.json', 'var_functions.execute_python:48': 'file_storage/functions.execute_python:48.json', 'var_functions.execute_python:50': {'project_stars': {'leaflet/leaflet': 38715, 'leaflet/leaflet.fullscreen': 417, 'leandrowd/react-responsive-carousel': 2534, 'lekoarts/gatsby-themes': 1836, 'leoilab/react-native-analytics-segment-io': 71, 'levelkdev/dxswap-sdk': 8, 'leviticusmb/ghostly': 2, 'libertydsnp/contracts': 2, 'libertydsnp/parquetjs': 21, 'litejs/natural-compare-lite': 100, 'ljharb/define-properties': 20, 'ljharb/has-symbols': 14, 'ljharb/object.assign': 105, 'ljharb/qs': 8073, 'ln-zap/node-lnd-grpc': 41, 'logflare/winston-logflare': 2, 'lohfu/dom-closest': 0, 'lohfu/domp': 2, 'lohfu/domp-create-many': 0, 'ltsfran/dreamtec-ui': 2, 'lucasferreira/react-native-flash-message': 1292, 'luehang/react-native-masonry-list': 237, 'luzzif/ethereum-contacts-registry': 5, 'lydell/js-tokens': 410, 'maddijoyce/serverless-ses-mjml': 4, 'mafintosh/generate-object-property': 25, 'mafintosh/tar-fs': 342, 'magnusdanielson/au-fluent-ui': 7, 'magnusdanielson/aureactwrapper': 2, 'malte-wessel/react-custom-scrollbars': 3161, 'mapbox/node-sqlite3': 5917, 'marcbachmann/node-html-pdf': 3523, 'marijnh/moduleserve': 68, 'marmelab/gremlins.js': 8973, 'martinpagesaal/ngx-ace-editor-wrapper': 8}, 'top_5': [['leaflet/leaflet', 38715], ['marmelab/gremlins.js', 8973], ['ljharb/qs', 8073], ['mapbox/node-sqlite3', 5917], ['marcbachmann/node-html-pdf', 3523]]}}

exec(code, env_args)
