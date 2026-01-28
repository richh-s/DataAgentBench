code = """import json
import pandas as pd
import re

def load_var(v):
    if isinstance(v, str):
        with open(v, 'r', encoding='utf-8') as f:
            return json.load(f)
    return v

pkg = load_var(var_call_pNIjHE3o9a3zDzMzhZUv0Ubj)
ppv = load_var(var_call_OZHgFr7rS1jFcpaDCTB9gmFv)
pinfo = load_var(var_call_X1oS1P9R1bSZllGgiXvtHyNr)

df_pkg = pd.DataFrame(pkg)
df_ppv = pd.DataFrame(ppv)
df_pinfo = pd.DataFrame(pinfo)
merged = pd.merge(df_pkg, df_ppv[['System','Name','Version','ProjectName']], on=['System','Name','Version'], how='left')
projects = sorted(merged['ProjectName'].dropna().unique())

# build mapping project -> forks
proj_forks = {}
for proj in projects:
    # find project_info rows where Project_Information contains the proj string
    matches = [rec for rec in pinfo if rec.get('Project_Information') and proj in rec.get('Project_Information')]
    max_forks = None
    for rec in matches:
        pi = rec.get('Project_Information')
        # parse forks
        m = re.search(r"([0-9][0-9,]*)\s*(?:forks|fork)\b", pi)
        if m:
            forks = int(m.group(1).replace(',',''))
            if max_forks is None or forks > max_forks:
                max_forks = forks
    if max_forks is not None:
        proj_forks[proj] = max_forks

# get top 5
items = sorted(proj_forks.items(), key=lambda x: x[1], reverse=True)[:5]
out = [{'ProjectName': k, 'Forks': v} for k,v in items]
print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_pNIjHE3o9a3zDzMzhZUv0Ubj': 'file_storage/call_pNIjHE3o9a3zDzMzhZUv0Ubj.json', 'var_call_OZHgFr7rS1jFcpaDCTB9gmFv': 'file_storage/call_OZHgFr7rS1jFcpaDCTB9gmFv.json', 'var_call_X1oS1P9R1bSZllGgiXvtHyNr': 'file_storage/call_X1oS1P9R1bSZllGgiXvtHyNr.json', 'var_call_4SAyhtKDfcKh241BBlj6wlI3': [], 'var_call_uJf69QDCRQ3YWny9CUJxnOEH': {'merged_head': [{'System': 'NPM', 'Name': '@discue/ui-components', 'Version': '0.13.0', 'Licenses': '[\n  "MIT"\n]', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 12\n}', 'ProjectName': 'discue/ui-components'}, {'System': 'NPM', 'Name': '@dvcol/web-extension-utils', 'Version': '1.1.1', 'Licenses': '[\n  "MIT"\n]', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 7\n}', 'ProjectName': 'dvcol/web-extension-utils'}, {'System': 'NPM', 'Name': '@eclipsejs/cli', 'Version': '1.0.0', 'Licenses': '[\n  "MIT"\n]', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 13\n}', 'ProjectName': 'dlesage25/eclipse-cli'}, {'System': 'NPM', 'Name': '@ebot7/edem-react', 'Version': '0.18.8', 'Licenses': '[\n  "MIT"\n]', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 55\n}', 'ProjectName': 'ebot7/edem'}, {'System': 'NPM', 'Name': '@e4a/irmaseal-wasm-bindings', 'Version': '0.0.1', 'Licenses': '[\n  "MIT"\n]', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 1\n}', 'ProjectName': 'encryption4all/irmaseal'}, {'System': 'NPM', 'Name': '@ebury/chameleon-components', 'Version': '0.1.46', 'Licenses': '[\n  "MIT"\n]', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 46\n}', 'ProjectName': 'ebury/chameleon'}, {'System': 'NPM', 'Name': '@e-group/material-form', 'Version': '3.13.9', 'Licenses': '[\n  "MIT"\n]', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 29\n}', 'ProjectName': 'egroupai/egroup-material'}, {'System': 'NPM', 'Name': '@e-group/material-layout', 'Version': '3.4.5', 'Licenses': '[\n  "MIT"\n]', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 6\n}', 'ProjectName': 'egroupai/egroup-material'}, {'System': 'NPM', 'Name': '@dspworkplace/ui', 'Version': '1.0.3', 'Licenses': '[\n  "MIT"\n]', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 4\n}', 'ProjectName': 'dsp-workplace/dsp-npm'}, {'System': 'NPM', 'Name': '@ditojs/router', 'Version': '0.125.0', 'Licenses': '[\n  "MIT"\n]', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 87\n}', 'ProjectName': 'ditojs/dito'}, {'System': 'NPM', 'Name': '@ditojs/ui', 'Version': '0.113.0', 'Licenses': '[\n  "MIT"\n]', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 107\n}', 'ProjectName': 'ditojs/dito'}, {'System': 'NPM', 'Name': '@ditojs/admin', 'Version': '0.155.0', 'Licenses': '[\n  "MIT"\n]', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 164\n}', 'ProjectName': 'ditojs/dito'}, {'System': 'NPM', 'Name': '@dsrv/kms', 'Version': '0.2.2', 'Licenses': '[\n  "MIT"\n]', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 29\n}', 'ProjectName': 'dsrvlabs/kms'}, {'System': 'NPM', 'Name': '@domojs/rfx-parsers', 'Version': '1.5.9', 'Licenses': '[\n  "MIT"\n]', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 23\n}', 'ProjectName': 'npenin/rfx'}, {'System': 'NPM', 'Name': '@dnvgl/playwright-live-recorder', 'Version': '2.0.14', 'Licenses': '[\n  "MIT"\n]', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 15\n}', 'ProjectName': 'dnv-opensource/playwright-live-recorder'}, {'System': 'NPM', 'Name': '@ditojs/router', 'Version': '0.43.0', 'Licenses': '[\n  "MIT"\n]', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 5\n}', 'ProjectName': 'ditojs/dito'}, {'System': 'NPM', 'Name': '@ditojs/router', 'Version': '0.96.0', 'Licenses': '[\n  "MIT"\n]', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 58\n}', 'ProjectName': 'ditojs/dito'}, {'System': 'NPM', 'Name': '@draftbit/ui', 'Version': '0.1.14', 'Licenses': '[\n  "MIT"\n]', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 31\n}', 'ProjectName': 'draftbit/react-native-jigsaw'}, {'System': 'NPM', 'Name': '@draftbit/ui', 'Version': '0.14.3', 'Licenses': '[\n  "MIT"\n]', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 65\n}', 'ProjectName': 'draftbit/react-native-jigsaw'}, {'System': 'NPM', 'Name': '@dr.cash/components', 'Version': '1.1.1', 'Licenses': '[\n  "MIT"\n]', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 7\n}', 'ProjectName': 'drcash/drcash_components'}], 'projects_sample': ['discue/ui-components', 'dvcol/web-extension-utils', 'dlesage25/eclipse-cli', 'ebot7/edem', 'encryption4all/irmaseal', 'ebury/chameleon', 'egroupai/egroup-material', 'dsp-workplace/dsp-npm', 'ditojs/dito', 'dsrvlabs/kms', 'npenin/rfx', 'dnv-opensource/playwright-live-recorder', 'draftbit/react-native-jigsaw', 'drcash/drcash_components', 'dotdevv/packages', 'easyops-cn/docusaurus-search-local', 'dwelle/excalidraw', 'dxos/dxos', 'taixw2/dx', 'e-conomic/gaudi'], 'repo_sample': [], 'intersection_sample': [], 'counts': {'num_pkg_rows': 176998, 'num_ppv_rows': 597602, 'num_pinfo_rows': 770, 'num_projects_from_pkg': 5477}}}

exec(code, env_args)
