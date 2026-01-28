code = """import json
import re
import pandas as pd

proj_list = var_call_qWXkNkFixzsMjOcBXYKfZr3B
path_projinfo = var_call_2xZRCVHbTg6SGSD7Pa7Ku5g0

with open(path_projinfo, 'r') as f:
    projinfo_records = json.load(f)

df_info = pd.DataFrame(projinfo_records)

pattern = re.compile(r'([0-9][0-9,]*)\s*(?:forks|fork)', re.I)

results = []

for proj in proj_list:
    # try exact owner/repo
    matches = df_info[df_info['Project_Information'].fillna('').str.contains(proj, case=False, na=False)]
    best = None
    best_text = None
    if not matches.empty:
        for text in matches['Project_Information'].fillna(''):
            m = pattern.search(text)
            if m:
                num = int(m.group(1).replace(',',''))
                if best is None or num > best:
                    best = num
                    best_text = text
    # try repo-only
    if best is None:
        repo = proj.split('/')[-1]
        matches2 = df_info[df_info['Project_Information'].fillna('').str.contains('/'+repo, case=False, na=False) | df_info['Project_Information'].fillna('').str.contains(repo+' on GitHub', case=False, na=False) | df_info['Project_Information'].fillna('').str.contains(' '+repo+' ', case=False, na=False)]
        if not matches2.empty:
            for text in matches2['Project_Information'].fillna(''):
                m = pattern.search(text)
                if m:
                    num = int(m.group(1).replace(',',''))
                    if best is None or num > best:
                        best = num
                        best_text = text
    if best is not None:
        results.append({'ProjectName': proj, 'Forks': best, 'Project_Information': best_text})

# If still less than 5, consider adding projects with forks==0 from matches without explicit forks
if len(results) < 5:
    for proj in proj_list:
        if any(r['ProjectName']==proj for r in results):
            continue
        repo = proj.split('/')[-1]
        matches = df_info[df_info['Project_Information'].fillna('').str.contains(proj, case=False, na=False) | df_info['Project_Information'].fillna('').str.contains('/'+repo, case=False, na=False) | df_info['Project_Information'].fillna('').str.contains(repo+' on GitHub', case=False, na=False)]
        if not matches.empty:
            # assign 0 if no forks found
            results.append({'ProjectName': proj, 'Forks': 0, 'Project_Information': matches.iloc[0]['Project_Information']})
        if len(results) >= 5:
            break

results_sorted = sorted(results, key=lambda x: x['Forks'], reverse=True)[:5]

out = [{'ProjectName': r['ProjectName'], 'Forks': r['Forks']} for r in results_sorted]

print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_Ynihs5S7g9dRrvzFs4lsKAop': ['packageinfo'], 'var_call_yfgJV2CWFhqmptLhP2gg9379': ['project_info', 'project_packageversion'], 'var_call_Dt1jep51h0je3AQG3K8y5sM7': 'file_storage/call_Dt1jep51h0je3AQG3K8y5sM7.json', 'var_call_cnnhcBTvzreBOELoPOM90KVp': 'file_storage/call_cnnhcBTvzreBOELoPOM90KVp.json', 'var_call_qWXkNkFixzsMjOcBXYKfZr3B': ['astridlyre/fp', 'discue/ui-components', 'ditojs/dito', 'dlesage25/eclipse-cli', 'dnv-opensource/playwright-live-recorder', 'dotdevv/packages', 'dotnetautor/easm', 'draftbit/react-native-jigsaw', 'dsrvlabs/kms', 'dvcol/web-extension-utils', 'dwelle/excalidraw', 'dxatscale/sfpowerscripts', 'dxcli/dev', 'dxcli/loader', 'dxos/dxos', 'dxos/halo', 'dxos/protocol', 'dynamic-labs/dynamicauth', 'dynamicmsw/dynamic-msw', 'dynatrace/serverless-oneagent', 'dzakh/rescript-ava', 'dzangolab/pulumi', 'dzangolab/vue-cli-plugin-dzango', 'dzangolab/vue-layout', 'dzangolab/vue-locale-switcher', 'dzeiocom/libs', 'dzervoudakes/dztools', 'e-conomic/gaudi', 'e2b-dev/e2b', 'eagletrt/telemetria-postprocessing', 'ealmansi/jagger', 'earth-association/assets', 'easylogic/editor', 'easyops-cn/docusaurus-search-local', 'eaze/danger-plugin-eslint', 'ebay/ebayui-core', 'ebay/nice-dag', 'ebay/skin', 'ebot7/edem', 'ebury/chameleon', 'ecency/ecency-render-helper', 'eclass/ui-kit', 'ecodev/natural', 'ecomclub/storefront-twbs', 'ecomclub/widget-minicart', 'ecomclub/widget-tag-manager', 'ecomplus/storefront', 'eddo81/webpack-5-boilerplate', 'edenhealth/eve', 'edgar0011/e1011-es-kit', 'egroupai/egroup-material', 'encryption4all/irmaseal', 'hurleyinnovations/econsult-storybook', 'lulucodes/easy-front-core-sdk', 'luzzif/ethereum-contacts-registry', 'n43/easyapp', 'npenin/rfx', 'taixw2/dx', 'yuhongda/echarts-readymade'], 'var_call_2xZRCVHbTg6SGSD7Pa7Ku5g0': 'file_storage/call_2xZRCVHbTg6SGSD7Pa7Ku5g0.json', 'var_call_xNIcODpX4jNmkvlZ6P1DXHbL': [{'ProjectName': 'dxcli/loader', 'Forks': 128}, {'ProjectName': 'taixw2/dx', 'Forks': 14}, {'ProjectName': 'luzzif/ethereum-contacts-registry', 'Forks': 0}, {'ProjectName': 'n43/easyapp', 'Forks': 0}]}

exec(code, env_args)
