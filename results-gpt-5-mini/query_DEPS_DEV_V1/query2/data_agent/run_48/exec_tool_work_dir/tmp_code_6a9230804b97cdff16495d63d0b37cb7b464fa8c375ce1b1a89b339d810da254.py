code = """import json
import re
import pandas as pd

proj_list = var_call_qWXkNkFixzsMjOcBXYKfZr3B
path_projinfo = var_call_2xZRCVHbTg6SGSD7Pa7Ku5g0

with open(path_projinfo, 'r') as f:
    projinfo_records = json.load(f)

df_info = pd.DataFrame(projinfo_records)

# Helper to extract forks
def extract_forks(text):
    if not isinstance(text, str):
        return None
    # common patterns
    patterns = [r'([0-9,]+)\s+forks',
                r'forks count of\s+([0-9,]+)',
                r'forks count[:\s]+([0-9,]+)',
                r'forks[:\s]+([0-9,]+)']
    for p in patterns:
        m = re.search(p, text, re.I)
        if m:
            num = m.group(1)
            num = num.replace(',','')
            try:
                return int(num)
            except:
                continue
    # fallback: look for 'and 5782 forks' style: number before 'forks' covered by first
    return None

results = []

for proj in proj_list:
    # find rows where Project_Information contains proj
    matches = df_info[df_info['Project_Information'].fillna('').str.contains(proj, case=False, na=False)]
    best = None
    best_text = None
    if not matches.empty:
        for text in matches['Project_Information'].fillna(''):
            forks = extract_forks(text)
            if forks is not None:
                if best is None or forks > best:
                    best = forks
                    best_text = text
    if best is not None:
        results.append({'ProjectName': proj, 'Forks': best, 'Project_Information': best_text})

# If no results found in intersection, we may attempt looser matching by repo name only (part after /)
if len(results) < 5:
    # map repos by repo-only
    repo_only = [p.split('/')[-1] for p in proj_list]
    for proj, repo in zip(proj_list, repo_only):
        if any(r['ProjectName']==proj for r in results):
            continue
        matches = df_info[df_info['Project_Information'].fillna('').str.contains('/'+repo+' ', case=False, na=False) | df_info['Project_Information'].fillna('').str.contains('/'+repo+' on GitHub', case=False, na=False) | df_info['Project_Information'].fillna('').str.contains(repo+' on GitHub', case=False, na=False)]
        best = None
        best_text = None
        if not matches.empty:
            for text in matches['Project_Information'].fillna(''):
                forks = extract_forks(text)
                if forks is not None:
                    if best is None or forks > best:
                        best = forks
                        best_text = text
        if best is not None:
            results.append({'ProjectName': proj, 'Forks': best, 'Project_Information': best_text})

# sort and take top 5
results_sorted = sorted(results, key=lambda x: x['Forks'], reverse=True)[:5]

# prepare output (strip Project_Information to shorter snippet)
out = []
for r in results_sorted:
    out.append({'ProjectName': r['ProjectName'], 'Forks': r['Forks']})

print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_Ynihs5S7g9dRrvzFs4lsKAop': ['packageinfo'], 'var_call_yfgJV2CWFhqmptLhP2gg9379': ['project_info', 'project_packageversion'], 'var_call_Dt1jep51h0je3AQG3K8y5sM7': 'file_storage/call_Dt1jep51h0je3AQG3K8y5sM7.json', 'var_call_cnnhcBTvzreBOELoPOM90KVp': 'file_storage/call_cnnhcBTvzreBOELoPOM90KVp.json', 'var_call_qWXkNkFixzsMjOcBXYKfZr3B': ['astridlyre/fp', 'discue/ui-components', 'ditojs/dito', 'dlesage25/eclipse-cli', 'dnv-opensource/playwright-live-recorder', 'dotdevv/packages', 'dotnetautor/easm', 'draftbit/react-native-jigsaw', 'dsrvlabs/kms', 'dvcol/web-extension-utils', 'dwelle/excalidraw', 'dxatscale/sfpowerscripts', 'dxcli/dev', 'dxcli/loader', 'dxos/dxos', 'dxos/halo', 'dxos/protocol', 'dynamic-labs/dynamicauth', 'dynamicmsw/dynamic-msw', 'dynatrace/serverless-oneagent', 'dzakh/rescript-ava', 'dzangolab/pulumi', 'dzangolab/vue-cli-plugin-dzango', 'dzangolab/vue-layout', 'dzangolab/vue-locale-switcher', 'dzeiocom/libs', 'dzervoudakes/dztools', 'e-conomic/gaudi', 'e2b-dev/e2b', 'eagletrt/telemetria-postprocessing', 'ealmansi/jagger', 'earth-association/assets', 'easylogic/editor', 'easyops-cn/docusaurus-search-local', 'eaze/danger-plugin-eslint', 'ebay/ebayui-core', 'ebay/nice-dag', 'ebay/skin', 'ebot7/edem', 'ebury/chameleon', 'ecency/ecency-render-helper', 'eclass/ui-kit', 'ecodev/natural', 'ecomclub/storefront-twbs', 'ecomclub/widget-minicart', 'ecomclub/widget-tag-manager', 'ecomplus/storefront', 'eddo81/webpack-5-boilerplate', 'edenhealth/eve', 'edgar0011/e1011-es-kit', 'egroupai/egroup-material', 'encryption4all/irmaseal', 'hurleyinnovations/econsult-storybook', 'lulucodes/easy-front-core-sdk', 'luzzif/ethereum-contacts-registry', 'n43/easyapp', 'npenin/rfx', 'taixw2/dx', 'yuhongda/echarts-readymade'], 'var_call_2xZRCVHbTg6SGSD7Pa7Ku5g0': 'file_storage/call_2xZRCVHbTg6SGSD7Pa7Ku5g0.json'}

exec(code, env_args)
