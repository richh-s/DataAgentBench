code = """import json
import re
from collections import defaultdict

# Load latest-release per package records
with open(var_call_7eXbIb43YaPzp2GKC5pPonrL, 'r') as f:
    latest_records = json.load(f)

# Load project_packageversion and project_info
with open(var_call_Sce4h7xh95295hbhOTw9J46q, 'r') as f:
    ppv_records = json.load(f)
with open(var_call_JCeuFVYZRs49WheFWkV3KOLV, 'r') as f:
    pinfo_records = json.load(f)

# Build mapping repo -> stars from project_info
repo_stars = {}
# patterns to extract repo and stars
repo_pattern = re.compile(r"(?:project\s+)?([A-Za-z0-9_.-]+\/[A-Za-z0-9_.-]+)", re.IGNORECASE)
star_patterns = [re.compile(r"([0-9]{1,3}(?:,[0-9]{3})*|[0-9]+)\s*stars", re.IGNORECASE),
                 re.compile(r"stars count of\s*([0-9]{1,3}(?:,[0-9]{3})*|[0-9]+)", re.IGNORECASE),
                 re.compile(r"a total of\s*([0-9]{1,3}(?:,[0-9]{3})*|[0-9]+)\s*stars", re.IGNORECASE)]

for rec in pinfo_records:
    info = rec.get('Project_Information', '')
    if not info:
        continue
    # find repo occurrences
    repo_match = repo_pattern.search(info)
    if not repo_match:
        continue
    repo = repo_match.group(1)
    # extract stars
    stars = None
    for pat in star_patterns:
        m = pat.search(info)
        if m:
            try:
                stars = int(m.group(1).replace(',', ''))
                break
            except:
                continue
    if stars is None:
        # try other phrase patterns
        m = re.search(r"has\s*([0-9]{1,3}(?:,[0-9]{3})*|[0-9]+)\s*stars", info, re.IGNORECASE)
        if m:
            stars = int(m.group(1).replace(',', ''))
    if stars is None:
        # default 0
        stars = 0
    # store if not present or keep max
    if repo in repo_stars:
        if stars > repo_stars[repo]:
            repo_stars[repo] = stars
    else:
        repo_stars[repo] = stars

# Build mapping from (Name,Version) -> list of ProjectName from project_packageversion
ppv_map = defaultdict(list)
for rec in ppv_records:
    if rec.get('System') != 'NPM':
        continue
    key = (rec.get('Name'), rec.get('Version'))
    proj = rec.get('ProjectName')
    if proj:
        ppv_map[key].append(proj)

# For each latest record, find ProjectNames and stars
rows = []
seen = set()
for rec in latest_records:
    if rec.get('System') != 'NPM':
        continue
    name = rec.get('Name')
    version = rec.get('Version')
    key = (name, version)
    if key in seen:
        continue
    seen.add(key)
    proj_list = ppv_map.get(key, [])
    stars = 0
    matched_proj = None
    # check each proj for stars
    for proj in proj_list:
        if proj in repo_stars:
            s = repo_stars[proj]
            if s > stars:
                stars = s
                matched_proj = proj
    # fallback: try to find any repo that contains the owner/repo pattern matching part of proj
    if stars == 0 and proj_list:
        for proj in proj_list:
            # try variations: sometimes project_info repo stored like 'leaflet/leaflet' etc; check keys with case-insensitive
            for repo_key, s in repo_stars.items():
                if repo_key.lower() == proj.lower():
                    if s > stars:
                        stars = s
                        matched_proj = repo_key
    rows.append({'Package': name, 'Version': version, 'ProjectName': matched_proj, 'Stars': stars})

# Now select top 5 by Stars
rows_sorted = sorted(rows, key=lambda x: x['Stars'], reverse=True)
top5 = rows_sorted[:5]

print('__RESULT__:')
print(json.dumps(top5))"""

env_args = {'var_call_el6MM5aWzqKb4Z9twLYgRaMM': ['packageinfo'], 'var_call_zGKTK1Z3SS8arxTfaSI1LlQW': ['project_info', 'project_packageversion'], 'var_call_sA5pwg0elTXFpJFUpVNSK5Ck': [{'System': 'NPM', 'Name': '@ecl/twig-component-carousel', 'Version': '3.11.1', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 29\n}', 'UpstreamPublishedAt': '1699345351000000.0'}, {'System': 'NPM', 'Name': '@douganderson444/panzoom-node', 'Version': '1.1.5', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 18\n}', 'UpstreamPublishedAt': '1670271173000000.0'}, {'System': 'NPM', 'Name': '@douganderson444/panzoom-node', 'Version': '1.1.1', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 14\n}', 'UpstreamPublishedAt': '1654791421000000.0'}, {'System': 'NPM', 'Name': '@dreamworld/dw-select', 'Version': '3.1.2-fix-double-click-issue.1', 'VersionInfo': '{\n  "IsRelease": false,\n  "Ordinal": 129\n}', 'UpstreamPublishedAt': '1624260093000000.0'}, {'System': 'NPM', 'Name': '@discue/ui-components', 'Version': '0.13.0', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 12\n}', 'UpstreamPublishedAt': '1656518476000000.0'}, {'System': 'NPM', 'Name': '@dvcol/web-extension-utils', 'Version': '1.1.1', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 7\n}', 'UpstreamPublishedAt': '1651424462000000.0'}, {'System': 'NPM', 'Name': '@dxos/client', 'Version': '2.28.20-dev.a2e143d3', 'VersionInfo': '{\n  "IsRelease": false,\n  "Ordinal": 1514\n}', 'UpstreamPublishedAt': '1649368661000000.0'}, {'System': 'NPM', 'Name': '@dxos/client', 'Version': '2.28.20-dev.a2e143d3', 'VersionInfo': '{\n  "IsRelease": false,\n  "Ordinal": 1514\n}', 'UpstreamPublishedAt': '1649368661000000.0'}, {'System': 'NPM', 'Name': '@edgedev/firebase', 'Version': '1.0.12', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 13\n}', 'UpstreamPublishedAt': '1666049703000000.0'}, {'System': 'NPM', 'Name': '@eden-network/data', 'Version': '1.0.9-sev.5', 'VersionInfo': '{\n  "IsRelease": false,\n  "Ordinal": 14\n}', 'UpstreamPublishedAt': '1637610934000000.0'}, {'System': 'NPM', 'Name': '@dyoshikawa/mentor-php-env', 'Version': '0.0.11', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 10\n}', 'UpstreamPublishedAt': '1635682875000000.0'}, {'System': 'NPM', 'Name': '@eclipsejs/cli', 'Version': '1.0.0', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 13\n}', 'UpstreamPublishedAt': '1672532998000000.0'}, {'System': 'NPM', 'Name': '@dytesdk/electron-main', 'Version': '1.0.2', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 6\n}', 'UpstreamPublishedAt': '1664186899000000.0'}, {'System': 'NPM', 'Name': '@dxos/client', 'Version': '2.31.8-dev.dcd68d50', 'VersionInfo': '{\n  "IsRelease": false,\n  "Ordinal": 1605\n}', 'UpstreamPublishedAt': '1652053857000000.0'}, {'System': 'NPM', 'Name': '@dxos/client', 'Version': '2.31.8-dev.dcd68d50', 'VersionInfo': '{\n  "IsRelease": false,\n  "Ordinal": 1605\n}', 'UpstreamPublishedAt': '1652053857000000.0'}, {'System': 'NPM', 'Name': '@ebot7/edem-react', 'Version': '0.18.8', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 55\n}', 'UpstreamPublishedAt': '1618309268000000.0'}, {'System': 'NPM', 'Name': '@e4a/irmaseal-wasm-bindings', 'Version': '0.0.1', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 1\n}', 'UpstreamPublishedAt': '1614248966000000.0'}, {'System': 'NPM', 'Name': '@ebury/chameleon-components', 'Version': '0.1.46', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 46\n}', 'UpstreamPublishedAt': '1578921588000000.0'}, {'System': 'NPM', 'Name': '@dxos/console-app', 'Version': '1.0.0-beta.4', 'VersionInfo': '{\n  "IsRelease": false,\n  "Ordinal": 4\n}', 'UpstreamPublishedAt': '1592022730000000.0'}, {'System': 'NPM', 'Name': '@dxos/console-app', 'Version': '1.0.0-beta.4', 'VersionInfo': '{\n  "IsRelease": false,\n  "Ordinal": 4\n}', 'UpstreamPublishedAt': '1592022730000000.0'}, {'System': 'NPM', 'Name': '@eddeee888/gcg-typescript-resolver-files', 'Version': '0.0.0-pr9-run20-1-20221027114308', 'VersionInfo': '{\n  "IsRelease": false,\n  "Ordinal": 60\n}', 'UpstreamPublishedAt': '1666870996000000.0'}, {'System': 'NPM', 'Name': '@dxos/broadcast', 'Version': '2.19.4-dev.54bbea97', 'VersionInfo': '{\n  "IsRelease": false,\n  "Ordinal": 147\n}', 'UpstreamPublishedAt': '1640693007000000.0'}, {'System': 'NPM', 'Name': '@dxos/broadcast', 'Version': '2.19.4-dev.54bbea97', 'VersionInfo': '{\n  "IsRelease": false,\n  "Ordinal": 147\n}', 'UpstreamPublishedAt': '1640693007000000.0'}, {'System': 'NPM', 'Name': '@dxos/client', 'Version': '2.1.2-beta.0', 'VersionInfo': '{\n  "IsRelease": false,\n  "Ordinal": 974\n}', 'UpstreamPublishedAt': '1602705180000000.0'}, {'System': 'NPM', 'Name': '@dxos/client', 'Version': '2.1.2-beta.0', 'VersionInfo': '{\n  "IsRelease": false,\n  "Ordinal": 974\n}', 'UpstreamPublishedAt': '1602705180000000.0'}, {'System': 'NPM', 'Name': '@e-group/material-form', 'Version': '3.13.9', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 29\n}', 'UpstreamPublishedAt': '1576120808000000.0'}, {'System': 'NPM', 'Name': '@e-group/material-layout', 'Version': '3.4.5', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 6\n}', 'UpstreamPublishedAt': '1564554070000000.0'}, {'System': 'NPM', 'Name': '@dxos/client', 'Version': '2.7.17-alpha.0', 'VersionInfo': '{\n  "IsRelease": false,\n  "Ordinal": 1011\n}', 'UpstreamPublishedAt': '1606321225000000.0'}, {'System': 'NPM', 'Name': '@dxos/client', 'Version': '2.7.17-alpha.0', 'VersionInfo': '{\n  "IsRelease": false,\n  "Ordinal": 1011\n}', 'UpstreamPublishedAt': '1606321225000000.0'}, {'System': 'NPM', 'Name': '@dxos/broadcast', 'Version': '2.22.1-dev.e16cf8db', 'VersionInfo': '{\n  "IsRelease": false,\n  "Ordinal": 239\n}', 'UpstreamPublishedAt': '1642693979000000.0'}, {'System': 'NPM', 'Name': '@dxos/broadcast', 'Version': '2.22.1-dev.e16cf8db', 'VersionInfo': '{\n  "IsRelease": false,\n  "Ordinal": 239\n}', 'UpstreamPublishedAt': '1642693979000000.0'}, {'System': 'NPM', 'Name': '@edgeros/jsre-types', 'Version': '1.8.8', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 53\n}', 'UpstreamPublishedAt': '1661743833000000.0'}, {'System': 'NPM', 'Name': '@dxos/cli-chess', 'Version': '1.0.0-beta.84', 'VersionInfo': '{\n  "IsRelease": false,\n  "Ordinal": 25\n}', 'UpstreamPublishedAt': '1596462418000000.0'}, {'System': 'NPM', 'Name': '@dxos/cli-chess', 'Version': '1.0.0-beta.84', 'VersionInfo': '{\n  "IsRelease": false,\n  "Ordinal": 25\n}', 'UpstreamPublishedAt': '1596462418000000.0'}, {'System': 'NPM', 'Name': '@edgeros/jsre-types', 'Version': '1.8.12', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 57\n}', 'UpstreamPublishedAt': '1663140420000000.0'}, {'System': 'NPM', 'Name': '@dxos/client', 'Version': '2.18.1', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 1131\n}', 'UpstreamPublishedAt': '1637930080000000.0'}, {'System': 'NPM', 'Name': '@dxos/client', 'Version': '2.18.1', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 1131\n}', 'UpstreamPublishedAt': '1637930080000000.0'}, {'System': 'NPM', 'Name': '@edgeandnode/gds', 'Version': '3.0.0-global-header-1692827365828-fc1e4a1', 'VersionInfo': '{\n  "IsRelease": false,\n  "Ordinal": 287\n}', 'UpstreamPublishedAt': '1692827376000000.0'}, {'System': 'NPM', 'Name': '@edgeandnode/gds', 'Version': '3.0.0-global-header-1699370867138-33c8884', 'VersionInfo': '{\n  "IsRelease": false,\n  "Ordinal": 304\n}', 'UpstreamPublishedAt': '1699370897000000.0'}, {'System': 'NPM', 'Name': '@edgeandnode/components', 'Version': '1.0.135', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 146\n}', 'UpstreamPublishedAt': '1626116782000000.0'}, {'System': 'NPM', 'Name': '@edgeandnode/components', 'Version': '1.0.58', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 69\n}', 'UpstreamPublishedAt': '1621038170000000.0'}, {'System': 'NPM', 'Name': '@dkoerner/propertyui', 'Version': '0.0.18', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 18\n}', 'UpstreamPublishedAt': '1622769158000000.0'}, {'System': 'NPM', 'Name': '@dspworkplace/ui', 'Version': '1.0.3', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 4\n}', 'UpstreamPublishedAt': '1573240066000000.0'}, {'System': 'NPM', 'Name': '@dollarshaveclub/js-utils', 'Version': '7.6.0-rc.5', 'VersionInfo': '{\n  "IsRelease": false,\n  "Ordinal": 63\n}', 'UpstreamPublishedAt': '1526948328000000.0'}, {'System': 'NPM', 'Name': '@ditojs/router', 'Version': '0.125.0', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 87\n}', 'UpstreamPublishedAt': '1566494021000000.0'}, {'System': 'NPM', 'Name': '@ditojs/ui', 'Version': '0.113.0', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 107\n}', 'UpstreamPublishedAt': '1563894672000000.0'}, {'System': 'NPM', 'Name': '@ditojs/admin', 'Version': '0.155.0', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 164\n}', 'UpstreamPublishedAt': '1599720562000000.0'}, {'System': 'NPM', 'Name': '@dsrv/kms', 'Version': '0.2.2', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 29\n}', 'UpstreamPublishedAt': '1640062466000000.0'}, {'System': 'NPM', 'Name': '@domojs/rfx-parsers', 'Version': '1.5.9', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 23\n}', 'UpstreamPublishedAt': '1664111812000000.0'}, {'System': 'NPM', 'Name': '@dnvgl/playwright-live-recorder', 'Version': '2.0.14', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 15\n}', 'UpstreamPublishedAt': '1664221488000000.0'}], 'var_call_PgOvFYAeazgzBQffrmEm9gMB': 'file_storage/call_PgOvFYAeazgzBQffrmEm9gMB.json', 'var_call_Sce4h7xh95295hbhOTw9J46q': 'file_storage/call_Sce4h7xh95295hbhOTw9J46q.json', 'var_call_JCeuFVYZRs49WheFWkV3KOLV': 'file_storage/call_JCeuFVYZRs49WheFWkV3KOLV.json', 'var_call_7eXbIb43YaPzp2GKC5pPonrL': 'file_storage/call_7eXbIb43YaPzp2GKC5pPonrL.json'}

exec(code, env_args)
