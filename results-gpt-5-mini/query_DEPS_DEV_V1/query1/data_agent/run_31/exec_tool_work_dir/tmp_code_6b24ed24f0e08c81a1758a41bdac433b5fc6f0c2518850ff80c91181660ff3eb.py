code = """import json
import pandas as pd
import re

# Load the latest-release per package result from SQL query
with open(var_call_7eXbIb43YaPzp2GKC5pPonrL, 'r') as f:
    latest_records = json.load(f)

# Load project_packageversion and project_info fully (they were stored earlier)
with open(var_call_Sce4h7xh95295hbhOTw9J46q, 'r') as f:
    ppv_records = json.load(f)
with open(var_call_JCeuFVYZRs49WheFWkV3KOLV, 'r') as f:
    pinfo_records = json.load(f)

latest_df = pd.DataFrame(latest_records).drop_duplicates(subset=['Name'])
ppv_df = pd.DataFrame(ppv_records)
pinfo_df = pd.DataFrame(pinfo_records)

# Merge latest with project packageversion to get ProjectName
merged = pd.merge(latest_df, ppv_df, on=['System','Name','Version'], how='left')

# Helper to extract stars
def extract_stars_from_text(text):
    if not text or not isinstance(text, str):
        return None
    patterns = [r"([0-9]{1,3}(?:,[0-9]{3})*|[0-9]+)\s*stars",
                r"stars count of\s*([0-9]{1,3}(?:,[0-9]{3})*|[0-9]+)",
                r"a total of\s*([0-9]{1,3}(?:,[0-9]{3})*|[0-9]+)\s*stars",
                r"has garnered .* with a total of\s*([0-9]{1,3}(?:,[0-9]{3})*|[0-9]+)\s*stars",
                r"has\s*([0-9]{1,3}(?:,[0-9]{3})*|[0-9]+)\s*stars",
               ]
    for pat in patterns:
        m = re.search(pat, text, flags=re.IGNORECASE)
        if m:
            num = m.group(1).replace(',', '')
            try:
                return int(num)
            except:
                continue
    return None

rows = []
for _, r in merged.iterrows():
    pkg = r['Name']
    ver = r['Version']
    proj = r.get('ProjectName', None)
    stars = None
    if pd.notna(proj):
        matches = pinfo_df[pinfo_df['Project_Information'].fillna('').str.contains(proj, case=False, na=False)]
        if not matches.empty:
            stars = extract_stars_from_text(matches.iloc[0]['Project_Information'])
    # fallback: search project_info for package name
    if stars is None:
        matches2 = pinfo_df[pinfo_df['Project_Information'].fillna('').str.contains(pkg, case=False, na=False)]
        if not matches2.empty:
            stars = extract_stars_from_text(matches2.iloc[0]['Project_Information'])
    if stars is None:
        stars = 0
    rows.append({'Package': pkg, 'Version': ver, 'ProjectName': proj if pd.notna(proj) else None, 'Stars': int(stars)})

res_df = pd.DataFrame(rows)
# aggregate by package/version
res_df = res_df.groupby(['Package','Version'], as_index=False).agg({'ProjectName': lambda s: s.dropna().iloc[0] if s.dropna().any() else None, 'Stars': 'max'})

top5 = res_df.sort_values('Stars', ascending=False).head(5)
result = top5[['Package','Version','Stars']].to_dict(orient='records')

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_el6MM5aWzqKb4Z9twLYgRaMM': ['packageinfo'], 'var_call_zGKTK1Z3SS8arxTfaSI1LlQW': ['project_info', 'project_packageversion'], 'var_call_sA5pwg0elTXFpJFUpVNSK5Ck': [{'System': 'NPM', 'Name': '@ecl/twig-component-carousel', 'Version': '3.11.1', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 29\n}', 'UpstreamPublishedAt': '1699345351000000.0'}, {'System': 'NPM', 'Name': '@douganderson444/panzoom-node', 'Version': '1.1.5', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 18\n}', 'UpstreamPublishedAt': '1670271173000000.0'}, {'System': 'NPM', 'Name': '@douganderson444/panzoom-node', 'Version': '1.1.1', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 14\n}', 'UpstreamPublishedAt': '1654791421000000.0'}, {'System': 'NPM', 'Name': '@dreamworld/dw-select', 'Version': '3.1.2-fix-double-click-issue.1', 'VersionInfo': '{\n  "IsRelease": false,\n  "Ordinal": 129\n}', 'UpstreamPublishedAt': '1624260093000000.0'}, {'System': 'NPM', 'Name': '@discue/ui-components', 'Version': '0.13.0', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 12\n}', 'UpstreamPublishedAt': '1656518476000000.0'}, {'System': 'NPM', 'Name': '@dvcol/web-extension-utils', 'Version': '1.1.1', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 7\n}', 'UpstreamPublishedAt': '1651424462000000.0'}, {'System': 'NPM', 'Name': '@dxos/client', 'Version': '2.28.20-dev.a2e143d3', 'VersionInfo': '{\n  "IsRelease": false,\n  "Ordinal": 1514\n}', 'UpstreamPublishedAt': '1649368661000000.0'}, {'System': 'NPM', 'Name': '@dxos/client', 'Version': '2.28.20-dev.a2e143d3', 'VersionInfo': '{\n  "IsRelease": false,\n  "Ordinal": 1514\n}', 'UpstreamPublishedAt': '1649368661000000.0'}, {'System': 'NPM', 'Name': '@edgedev/firebase', 'Version': '1.0.12', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 13\n}', 'UpstreamPublishedAt': '1666049703000000.0'}, {'System': 'NPM', 'Name': '@eden-network/data', 'Version': '1.0.9-sev.5', 'VersionInfo': '{\n  "IsRelease": false,\n  "Ordinal": 14\n}', 'UpstreamPublishedAt': '1637610934000000.0'}, {'System': 'NPM', 'Name': '@dyoshikawa/mentor-php-env', 'Version': '0.0.11', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 10\n}', 'UpstreamPublishedAt': '1635682875000000.0'}, {'System': 'NPM', 'Name': '@eclipsejs/cli', 'Version': '1.0.0', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 13\n}', 'UpstreamPublishedAt': '1672532998000000.0'}, {'System': 'NPM', 'Name': '@dytesdk/electron-main', 'Version': '1.0.2', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 6\n}', 'UpstreamPublishedAt': '1664186899000000.0'}, {'System': 'NPM', 'Name': '@dxos/client', 'Version': '2.31.8-dev.dcd68d50', 'VersionInfo': '{\n  "IsRelease": false,\n  "Ordinal": 1605\n}', 'UpstreamPublishedAt': '1652053857000000.0'}, {'System': 'NPM', 'Name': '@dxos/client', 'Version': '2.31.8-dev.dcd68d50', 'VersionInfo': '{\n  "IsRelease": false,\n  "Ordinal": 1605\n}', 'UpstreamPublishedAt': '1652053857000000.0'}, {'System': 'NPM', 'Name': '@ebot7/edem-react', 'Version': '0.18.8', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 55\n}', 'UpstreamPublishedAt': '1618309268000000.0'}, {'System': 'NPM', 'Name': '@e4a/irmaseal-wasm-bindings', 'Version': '0.0.1', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 1\n}', 'UpstreamPublishedAt': '1614248966000000.0'}, {'System': 'NPM', 'Name': '@ebury/chameleon-components', 'Version': '0.1.46', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 46\n}', 'UpstreamPublishedAt': '1578921588000000.0'}, {'System': 'NPM', 'Name': '@dxos/console-app', 'Version': '1.0.0-beta.4', 'VersionInfo': '{\n  "IsRelease": false,\n  "Ordinal": 4\n}', 'UpstreamPublishedAt': '1592022730000000.0'}, {'System': 'NPM', 'Name': '@dxos/console-app', 'Version': '1.0.0-beta.4', 'VersionInfo': '{\n  "IsRelease": false,\n  "Ordinal": 4\n}', 'UpstreamPublishedAt': '1592022730000000.0'}, {'System': 'NPM', 'Name': '@eddeee888/gcg-typescript-resolver-files', 'Version': '0.0.0-pr9-run20-1-20221027114308', 'VersionInfo': '{\n  "IsRelease": false,\n  "Ordinal": 60\n}', 'UpstreamPublishedAt': '1666870996000000.0'}, {'System': 'NPM', 'Name': '@dxos/broadcast', 'Version': '2.19.4-dev.54bbea97', 'VersionInfo': '{\n  "IsRelease": false,\n  "Ordinal": 147\n}', 'UpstreamPublishedAt': '1640693007000000.0'}, {'System': 'NPM', 'Name': '@dxos/broadcast', 'Version': '2.19.4-dev.54bbea97', 'VersionInfo': '{\n  "IsRelease": false,\n  "Ordinal": 147\n}', 'UpstreamPublishedAt': '1640693007000000.0'}, {'System': 'NPM', 'Name': '@dxos/client', 'Version': '2.1.2-beta.0', 'VersionInfo': '{\n  "IsRelease": false,\n  "Ordinal": 974\n}', 'UpstreamPublishedAt': '1602705180000000.0'}, {'System': 'NPM', 'Name': '@dxos/client', 'Version': '2.1.2-beta.0', 'VersionInfo': '{\n  "IsRelease": false,\n  "Ordinal": 974\n}', 'UpstreamPublishedAt': '1602705180000000.0'}, {'System': 'NPM', 'Name': '@e-group/material-form', 'Version': '3.13.9', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 29\n}', 'UpstreamPublishedAt': '1576120808000000.0'}, {'System': 'NPM', 'Name': '@e-group/material-layout', 'Version': '3.4.5', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 6\n}', 'UpstreamPublishedAt': '1564554070000000.0'}, {'System': 'NPM', 'Name': '@dxos/client', 'Version': '2.7.17-alpha.0', 'VersionInfo': '{\n  "IsRelease": false,\n  "Ordinal": 1011\n}', 'UpstreamPublishedAt': '1606321225000000.0'}, {'System': 'NPM', 'Name': '@dxos/client', 'Version': '2.7.17-alpha.0', 'VersionInfo': '{\n  "IsRelease": false,\n  "Ordinal": 1011\n}', 'UpstreamPublishedAt': '1606321225000000.0'}, {'System': 'NPM', 'Name': '@dxos/broadcast', 'Version': '2.22.1-dev.e16cf8db', 'VersionInfo': '{\n  "IsRelease": false,\n  "Ordinal": 239\n}', 'UpstreamPublishedAt': '1642693979000000.0'}, {'System': 'NPM', 'Name': '@dxos/broadcast', 'Version': '2.22.1-dev.e16cf8db', 'VersionInfo': '{\n  "IsRelease": false,\n  "Ordinal": 239\n}', 'UpstreamPublishedAt': '1642693979000000.0'}, {'System': 'NPM', 'Name': '@edgeros/jsre-types', 'Version': '1.8.8', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 53\n}', 'UpstreamPublishedAt': '1661743833000000.0'}, {'System': 'NPM', 'Name': '@dxos/cli-chess', 'Version': '1.0.0-beta.84', 'VersionInfo': '{\n  "IsRelease": false,\n  "Ordinal": 25\n}', 'UpstreamPublishedAt': '1596462418000000.0'}, {'System': 'NPM', 'Name': '@dxos/cli-chess', 'Version': '1.0.0-beta.84', 'VersionInfo': '{\n  "IsRelease": false,\n  "Ordinal": 25\n}', 'UpstreamPublishedAt': '1596462418000000.0'}, {'System': 'NPM', 'Name': '@edgeros/jsre-types', 'Version': '1.8.12', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 57\n}', 'UpstreamPublishedAt': '1663140420000000.0'}, {'System': 'NPM', 'Name': '@dxos/client', 'Version': '2.18.1', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 1131\n}', 'UpstreamPublishedAt': '1637930080000000.0'}, {'System': 'NPM', 'Name': '@dxos/client', 'Version': '2.18.1', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 1131\n}', 'UpstreamPublishedAt': '1637930080000000.0'}, {'System': 'NPM', 'Name': '@edgeandnode/gds', 'Version': '3.0.0-global-header-1692827365828-fc1e4a1', 'VersionInfo': '{\n  "IsRelease": false,\n  "Ordinal": 287\n}', 'UpstreamPublishedAt': '1692827376000000.0'}, {'System': 'NPM', 'Name': '@edgeandnode/gds', 'Version': '3.0.0-global-header-1699370867138-33c8884', 'VersionInfo': '{\n  "IsRelease": false,\n  "Ordinal": 304\n}', 'UpstreamPublishedAt': '1699370897000000.0'}, {'System': 'NPM', 'Name': '@edgeandnode/components', 'Version': '1.0.135', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 146\n}', 'UpstreamPublishedAt': '1626116782000000.0'}, {'System': 'NPM', 'Name': '@edgeandnode/components', 'Version': '1.0.58', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 69\n}', 'UpstreamPublishedAt': '1621038170000000.0'}, {'System': 'NPM', 'Name': '@dkoerner/propertyui', 'Version': '0.0.18', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 18\n}', 'UpstreamPublishedAt': '1622769158000000.0'}, {'System': 'NPM', 'Name': '@dspworkplace/ui', 'Version': '1.0.3', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 4\n}', 'UpstreamPublishedAt': '1573240066000000.0'}, {'System': 'NPM', 'Name': '@dollarshaveclub/js-utils', 'Version': '7.6.0-rc.5', 'VersionInfo': '{\n  "IsRelease": false,\n  "Ordinal": 63\n}', 'UpstreamPublishedAt': '1526948328000000.0'}, {'System': 'NPM', 'Name': '@ditojs/router', 'Version': '0.125.0', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 87\n}', 'UpstreamPublishedAt': '1566494021000000.0'}, {'System': 'NPM', 'Name': '@ditojs/ui', 'Version': '0.113.0', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 107\n}', 'UpstreamPublishedAt': '1563894672000000.0'}, {'System': 'NPM', 'Name': '@ditojs/admin', 'Version': '0.155.0', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 164\n}', 'UpstreamPublishedAt': '1599720562000000.0'}, {'System': 'NPM', 'Name': '@dsrv/kms', 'Version': '0.2.2', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 29\n}', 'UpstreamPublishedAt': '1640062466000000.0'}, {'System': 'NPM', 'Name': '@domojs/rfx-parsers', 'Version': '1.5.9', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 23\n}', 'UpstreamPublishedAt': '1664111812000000.0'}, {'System': 'NPM', 'Name': '@dnvgl/playwright-live-recorder', 'Version': '2.0.14', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 15\n}', 'UpstreamPublishedAt': '1664221488000000.0'}], 'var_call_PgOvFYAeazgzBQffrmEm9gMB': 'file_storage/call_PgOvFYAeazgzBQffrmEm9gMB.json', 'var_call_Sce4h7xh95295hbhOTw9J46q': 'file_storage/call_Sce4h7xh95295hbhOTw9J46q.json', 'var_call_JCeuFVYZRs49WheFWkV3KOLV': 'file_storage/call_JCeuFVYZRs49WheFWkV3KOLV.json', 'var_call_7eXbIb43YaPzp2GKC5pPonrL': 'file_storage/call_7eXbIb43YaPzp2GKC5pPonrL.json'}

exec(code, env_args)
