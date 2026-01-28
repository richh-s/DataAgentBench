code = """import json
import re
import pandas as pd

# Load all datasets
with open(locals()['var_functions.query_db:8'], 'r') as f:
    release_packages = json.load(f)

with open(locals()['var_functions.query_db:20'], 'r') as f:
    project_mappings = json.load(f)

with open(locals()['var_functions.query_db:24'], 'r') as f:
    project_info = json.load(f)

# Step 1: Find latest release version for each NPM package
latest_packages = {}
for pkg in release_packages:
    try:
        version_info = json.loads(pkg['VersionInfo'])
        if version_info.get('IsRelease', False):
            name = pkg['Name']
            ordinal = version_info.get('Ordinal', 0)
            
            if name not in latest_packages or ordinal > latest_packages[name]['ordinal']:
                latest_packages[name] = {
                    'name': name,
                    'version': pkg['Version'],
                    'ordinal': ordinal
                }
    except:
        continue

# Step 2: Create mapping from package name+version to GitHub repo
latest_pkg_lookup = {pkg['name']: pkg for pkg in latest_packages.values()}

# Filter mappings to only include NPM system mappings
npm_mappings = [m for m in project_mappings if m.get('System') == 'NPM']

# Create package to repo mapping for latest versions only
package_to_repo = {}
for mapping in npm_mappings:
    pkg_name = mapping.get('Name')
    pkg_version = mapping.get('Version')
    project_name = mapping.get('ProjectName')
    
    if pkg_name in latest_pkg_lookup and latest_pkg_lookup[pkg_name]['version'] == pkg_version:
        package_to_repo[pkg_name] = project_name

# Step 3: Get star counts for repos from project_info
repo_star_counts = {}
for info in project_info:
    project_text = info.get('Project_Information', '')
    
    # Extract repo name from project text
    match = re.search(r'The project\s+(\S+)\s+(?:is hosted on|on)', project_text)
    if match:
        repo_name = match.group(1)
        
        # Extract star count
        stars_match = re.search(r'(\d+(?:,\d+)*)\s+stars?', project_text)
        if stars_match:
            stars_str = stars_match.group(1).replace(',', '')
            stars = int(stars_str)
            repo_star_counts[repo_name] = stars

# Step 4: Merge and find top packages
packages_with_stars = []
for pkg_name, repo_name in package_to_repo.items():
    if repo_name in repo_star_counts:
        packages_with_stars.append({
            'package_name': pkg_name,
            'version': latest_pkg_lookup[pkg_name]['version'],
            'github_repo': repo_name,
            'stars': repo_star_counts[repo_name]
        })

# Step 5: Sort by stars and get top 5
top_5_packages = sorted(packages_with_stars, key=lambda x: x['stars'], reverse=True)[:5]

print('__RESULT__:')
print(json.dumps(top_5_packages))"""

env_args = {'var_functions.query_db:0': [{'Name': '@ecl/twig-component-carousel', 'Version': '3.11.1', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 29\n}'}, {'Name': '@douganderson444/panzoom-node', 'Version': '1.1.5', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 18\n}'}, {'Name': '@douganderson444/panzoom-node', 'Version': '1.1.1', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 14\n}'}, {'Name': '@dreamworld/dw-select', 'Version': '3.1.2-fix-double-click-issue.1', 'VersionInfo': '{\n  "IsRelease": false,\n  "Ordinal": 129\n}'}, {'Name': '@discue/ui-components', 'Version': '0.13.0', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 12\n}'}, {'Name': '@dvcol/web-extension-utils', 'Version': '1.1.1', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 7\n}'}, {'Name': '@dxos/client', 'Version': '2.28.20-dev.a2e143d3', 'VersionInfo': '{\n  "IsRelease": false,\n  "Ordinal": 1514\n}'}, {'Name': '@dxos/client', 'Version': '2.28.20-dev.a2e143d3', 'VersionInfo': '{\n  "IsRelease": false,\n  "Ordinal": 1514\n}'}, {'Name': '@edgedev/firebase', 'Version': '1.0.12', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 13\n}'}, {'Name': '@eden-network/data', 'Version': '1.0.9-sev.5', 'VersionInfo': '{\n  "IsRelease": false,\n  "Ordinal": 14\n}'}], 'var_functions.query_db:2': [{'Name': '@douganderson444/panzoom-node', 'Version': '1.0.11', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 9\n}'}, {'Name': '@douganderson444/panzoom-node', 'Version': '1.0.10', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 8\n}'}, {'Name': '@douganderson444/panzoom-node', 'Version': '1.0.9', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 7\n}'}, {'Name': '@douganderson444/panzoom-node', 'Version': '1.0.8', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 6\n}'}, {'Name': '@douganderson444/panzoom-node', 'Version': '1.0.7', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 5\n}'}], 'var_functions.query_db:5': [{'Name': '@ecl/twig-component-carousel'}, {'Name': '@douganderson444/panzoom-node'}, {'Name': '@dreamworld/dw-select'}, {'Name': '@discue/ui-components'}, {'Name': '@dvcol/web-extension-utils'}, {'Name': '@dxos/client'}, {'Name': '@edgedev/firebase'}, {'Name': '@eden-network/data'}, {'Name': '@dyoshikawa/mentor-php-env'}, {'Name': '@eclipsejs/cli'}, {'Name': '@dytesdk/electron-main'}, {'Name': '@ebot7/edem-react'}, {'Name': '@e4a/irmaseal-wasm-bindings'}, {'Name': '@ebury/chameleon-components'}, {'Name': '@dxos/console-app'}, {'Name': '@eddeee888/gcg-typescript-resolver-files'}, {'Name': '@dxos/broadcast'}, {'Name': '@e-group/material-form'}, {'Name': '@e-group/material-layout'}, {'Name': '@edgeros/jsre-types'}, {'Name': '@dxos/cli-chess'}, {'Name': '@edgeandnode/gds'}, {'Name': '@edgeandnode/components'}, {'Name': '@dkoerner/propertyui'}, {'Name': '@dspworkplace/ui'}, {'Name': '@dollarshaveclub/js-utils'}, {'Name': '@ditojs/router'}, {'Name': '@ditojs/ui'}, {'Name': '@ditojs/admin'}, {'Name': '@dsrv/kms'}, {'Name': '@domojs/rfx-parsers'}, {'Name': '@dnvgl/playwright-live-recorder'}, {'Name': '@draftbit/ui'}, {'Name': '@docusaurus/lqip-loader'}, {'Name': '@dr.cash/components'}, {'Name': '@docusaurus/utils'}, {'Name': '@docusaurus/theme-live-codeblock'}, {'Name': '@dpc-sdp/ripple-campaign-primary'}, {'Name': '@dotdev/sanity-plugin-structure-helpers'}, {'Name': '@dithercat/servitor'}, {'Name': '@dpc-sdp/ripple-sitemap'}, {'Name': '@docbrasil/api-systemmanager'}, {'Name': '@dpc-sdp/ripple-whats-next'}, {'Name': '@e4web/charts'}, {'Name': '@easyops-cn/docusaurus-search-local'}, {'Name': '@dxos/text-model'}, {'Name': '@dxos/util'}, {'Name': '@dxos/rpc'}, {'Name': '@dxos/echo-db'}, {'Name': '@doodlincorp/doodlin-ui'}, {'Name': '@dso-toolkit/react'}, {'Name': '@doodl/ss-react-forms'}, {'Name': '@dpc-sdp/ripple-search'}, {'Name': '@dpc-sdp/ripple-document-link'}, {'Name': '@dpc-sdp/ripple-card'}, {'Name': '@dpc-sdp/ripple-event'}, {'Name': '@dpc-sdp/ripple-share-this'}, {'Name': '@dpc-sdp/ripple-timeline'}, {'Name': '@dpc-sdp/ripple-list-group'}, {'Name': '@dpc-sdp/ripple-button'}, {'Name': '@dpc-sdp/ripple-link'}, {'Name': '@dpc-sdp/ripple-breadcrumbs'}, {'Name': '@dpc-sdp/ripple-news'}, {'Name': '@dpc-sdp/ripple-figure'}, {'Name': '@dpc-sdp/ripple-site-header'}, {'Name': '@dpc-sdp/ripple-site-section-navigation'}, {'Name': '@dwelle/excalidraw'}, {'Name': '@dpc-sdp/ripple-grid'}, {'Name': '@dpc-sdp/ripple-call-to-action'}, {'Name': '@dpc-sdp/ripple-list'}, {'Name': '@disploy/ws'}, {'Name': '@disploy/rest'}, {'Name': '@dpc-sdp/ripple-contact'}, {'Name': '@dpc-sdp/ripple-image-gallery'}, {'Name': '@dpc-sdp/ripple-description-list'}, {'Name': '@dpc-sdp/ripple-meta-tag'}, {'Name': '@dpc-sdp/ripple-global'}, {'Name': '@dpc-sdp/ripple-anchor-links'}, {'Name': '@dpc-sdp/ripple-form'}, {'Name': '@dpc-sdp/ripple-publish-date-and-author'}, {'Name': '@dpc-sdp/ripple-layout'}, {'Name': '@dpc-sdp/ripple-alert'}, {'Name': '@dpc-sdp/ripple-updated-date'}, {'Name': '@dpc-sdp/ripple-embedded-video'}, {'Name': '@dxos/debug'}, {'Name': '@dpc-sdp/ripple-data-table'}, {'Name': '@dxos/async'}, {'Name': '@dxos/context'}, {'Name': '@dxos/functions'}, {'Name': '@dxos/model-factory'}, {'Name': '@dxos/document-model'}, {'Name': '@dxos/crypto'}, {'Name': '@dxos/timeframe'}, {'Name': '@dxos/feed-store'}, {'Name': '@dxos/aurora-table'}, {'Name': '@dxos/codec-protobuf'}, {'Name': '@dxos/sentry'}, {'Name': '@dxos/node-std'}, {'Name': '@dxos/invariant'}, {'Name': '@dxos/react-hooks'}], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.execute_python:12': 'Loaded 337844 release packages', 'var_functions.query_db:14': [{'System': 'NPM', 'Name': '@dms/io', 'Version': '0.9.0', 'ProjectType': 'GITHUB', 'ProjectName': 'dataminingsupply/dms-io', 'RelationProvenance': 'UNVERIFIED_METADATA', 'RelationType': 'SOURCE_REPO_TYPE'}, {'System': 'NPM', 'Name': '@dvo/fc', 'Version': '0.0.4', 'ProjectType': 'GITHUB', 'ProjectName': 'isacvale/fc', 'RelationProvenance': 'UNVERIFIED_METADATA', 'RelationType': 'SOURCE_REPO_TYPE'}, {'System': 'NPM', 'Name': '@djie/ui', 'Version': '1.0.17', 'ProjectType': 'GITHUB', 'ProjectName': 'laihaojie/jie', 'RelationProvenance': 'UNVERIFIED_METADATA', 'RelationType': 'SOURCE_REPO_TYPE'}, {'System': 'NPM', 'Name': '@djie/ui', 'Version': '1.0.16', 'ProjectType': 'GITHUB', 'ProjectName': 'laihaojie/jie', 'RelationProvenance': 'UNVERIFIED_METADATA', 'RelationType': 'SOURCE_REPO_TYPE'}, {'System': 'NPM', 'Name': '@djie/ws', 'Version': '1.0.8', 'ProjectType': 'GITHUB', 'ProjectName': 'laihaojie/jie', 'RelationProvenance': 'UNVERIFIED_METADATA', 'RelationType': 'SOURCE_REPO_TYPE'}], 'var_functions.query_db:16': [{'Project_Information': 'The project lberrocal/npm-packages-template is hosted on GitHub and currently has 0 open issues, 0 stars, and 0 forks.', 'Licenses': '[]', 'Description': 'Template for npm package library configured to be used with CI/CD', 'Homepage': 'None', 'OSSFuzz': 'nan'}, {'Project_Information': 'The project leaflet/leaflet on GitHub is a popular open-source library that currently has 521 open issues, 38715 stars, and 5782 forks, making it a widely recognized tool in the developer community.', 'Licenses': '[\n  "non-standard"\n]', 'Description': '🍃 JavaScript library for mobile-friendly interactive maps 🇺🇦', 'Homepage': 'https://leafletjs.com', 'OSSFuzz': 'nan'}, {'Project_Information': 'The project leaflet/leaflet.fullscreen on GitHub currently has 29 open issues, 417 stars, and 118 forks, making it a noteworthy contribution to the Leaflet ecosystem.', 'Licenses': '[\n  "ISC"\n]', 'Description': 'A fullscreen control for Leaflet', 'Homepage': 'http://leaflet.github.io/Leaflet.fullscreen/', 'OSSFuzz': 'nan'}, {'Project_Information': 'The project leaflet/leaflet.markercluster is hosted on GitHub and currently has an open issues count of 130, along with a stars count of 3761 and forks count of 988.', 'Licenses': '[\n  "MIT"\n]', 'Description': 'Marker Clustering plugin for Leaflet', 'Homepage': 'None', 'OSSFuzz': 'nan'}, {'Project_Information': 'The project leandrowd/react-responsive-carousel on GitHub has garnered significant attention, with a total of 2,534 stars and 636 forks, while currently having 23 open issues.', 'Licenses': '[\n  "MIT"\n]', 'Description': 'React.js Responsive Carousel (with Swipe)', 'Homepage': 'http://leandrowd.github.io/react-responsive-carousel/', 'OSSFuzz': 'nan'}], 'var_functions.execute_python:18': 'Loaded 337844 release packages from NPM', 'var_functions.query_db:20': 'file_storage/functions.query_db:20.json', 'var_functions.execute_python:22': 'Loaded 337844 packages and 597602 mappings', 'var_functions.query_db:24': 'file_storage/functions.query_db:24.json', 'var_functions.execute_python:26': 'Found 15811 packages with latest release versions', 'var_functions.execute_python:28': 'Found 15811 latest release versions', 'var_functions.execute_python:30': 'Step 1: Found 15811 latest release versions', 'var_functions.execute_python:32': 'Step 2: Found 7537 repos with latest packages, Step 3: Found 530 repos with star info'}

exec(code, env_args)
