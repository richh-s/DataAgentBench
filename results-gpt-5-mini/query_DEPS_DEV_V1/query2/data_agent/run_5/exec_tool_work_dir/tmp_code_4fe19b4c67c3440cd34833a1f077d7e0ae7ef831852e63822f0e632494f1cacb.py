code = """import json
import re

# Load mapping of package to project
mapping_path = var_call_Jk6uPPy5uSFPQDeh4DmIsxXL
with open(mapping_path, 'r', encoding='utf-8') as f:
    mappings = json.load(f)
project_names = sorted({r['ProjectName'] for r in mappings if r.get('ProjectName')})

# Load project_info
projinfo_path = var_call_dzlLeQmV4zwL14SNAEQQZdbW
with open(projinfo_path, 'r', encoding='utf-8') as f:
    projinfos = json.load(f)

# Build repo -> forks mapping by parsing Project_Information
repo_forks = {}
repo_infos = {}
repo_regex = re.compile(r'([A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+)')
# patterns for forks
fork_patterns = [
    re.compile(r'([0-9,]+)\s+forks'),
    re.compile(r'forks count of\s*([0-9,]+)'),
    re.compile(r'forked\s+([0-9,]+)\s+times'),
    re.compile(r'been forked\s+([0-9,]+)\s+times'),
    re.compile(r'and\s+([0-9,]{1,3}(?:,[0-9]{3})*)\s+forks')
]

for rec in projinfos:
    pi = rec.get('Project_Information') or ''
    if not pi:
        continue
    # find repo
    m = repo_regex.search(pi)
    if not m:
        continue
    repo = m.group(1)
    # extract forks
    forks = None
    for p in fork_patterns:
        fm = p.search(pi)
        if fm:
            try:
                forks = int(fm.group(1).replace(',', ''))
                break
            except:
                pass
    # Some strings may have "has been forked X times" caught above; or "X forks" caught.
    if forks is None:
        # try another heuristic: find all numbers and take one near 'fork'
        words = pi.split()
        # if 'fork' or 'forks' in text, take number just before it
        tokens = re.findall(r"\d{1,3}(?:,\d{3})*|\d+", pi)
        # fallback: set forks to 0
        forks = 0
    repo_forks[repo] = forks
    repo_infos[repo] = pi

# For our project_names, pick forks if available
results = []
for pn in project_names:
    if pn in repo_forks:
        results.append({'ProjectName': pn, 'Forks': repo_forks[pn]})

# If none matched directly, try to match case-insensitively or with leading/trailing slashes
if len(results) < 5:
    # build lowercase map
    lower_map = {k.lower(): k for k in repo_forks.keys()}
    for pn in project_names:
        if any(r['ProjectName'] == pn for r in results):
            continue
        key = pn.lower()
        if key in lower_map:
            rk = lower_map[key]
            results.append({'ProjectName': rk, 'Forks': repo_forks[rk]})
        else:
            # try strip leading slash
            stripped = pn.lstrip('/')
            if stripped.lower() in lower_map:
                rk = lower_map[stripped.lower()]
                results.append({'ProjectName': rk, 'Forks': repo_forks[rk]})

# Sort by forks desc
results_sorted = sorted(results, key=lambda x: x['Forks'], reverse=True)
top5 = results_sorted[:5]

print("__RESULT__:")
print(json.dumps(top5))"""

env_args = {'var_call_SPpf6OTIy2suP5I0T2HqEXjg': ['packageinfo'], 'var_call_i6hRKgFEWzpOJz5Z6LugaNNc': ['project_info', 'project_packageversion'], 'var_call_4QBHnENUNKnmttDHTGhGVb3H': 'file_storage/call_4QBHnENUNKnmttDHTGhGVb3H.json', 'var_call_0WCxbMuTxQGRvEiIxdI5oYtN': 'file_storage/call_0WCxbMuTxQGRvEiIxdI5oYtN.json', 'var_call_j0C5oPHpfXCyprf5Yum5tvPX': 'file_storage/call_j0C5oPHpfXCyprf5Yum5tvPX.json', 'var_call_Jk6uPPy5uSFPQDeh4DmIsxXL': 'file_storage/call_Jk6uPPy5uSFPQDeh4DmIsxXL.json', 'var_call_SZIO9aOUgv3xJGHCzyw21vx4': {'total_mappings': 5477, 'unique_projects': 5477, 'sample_projects': ['/crislin2046', '/robpethick', '0x1ance/soulbound', '0x1ance/wishport', '0xsalah/tete', '1394/manipula', '1728954833/project-manager', '20lives/scad-js', '286810/react-native-switch-box', '431910864/dumi-antd-components', '4catalyzer/theme', '4x-sas/create-react-app', '6km/minify-css', '776a0a/dus', '7rulnik/postcss-flexibility', 'a5hik/ng-sortable', 'a7650/vue3-draggable-resizable', 'a916856595/react-dropdown', 'aareksio/koa-history-api-fallback', 'aareksio/node-steam-client', 'aaronjwang/redux-websocket', 'abacritt/angularx-social-login', 'abrcdf1023/egroup-material', 'abrcdf1023/egroup-redux', 'abrcdf1023/egroup-utils', 'abuinitski/redux-bundler-async-resources', 'accenture/sfpowerscripts', 'actorapp/react-scroll', 'adamhalasz/uniqid', 'aduth/preact-jsx-runtime', 'adyatlov/behold', 'aeb-labs/graphql-weaver', 'aelbore/esbuild-jest', 'age-bijkaart/cbuf', 'agenciaed3/event-emitter', 'agenciaed3/helix-hooks', 'agenciaed3/helix-style', 'agenciaed3/utils', 'agenciaed3/vtex-api', 'agtenr/typescript-storagefactory', 'agustinramos/react-orgchart', 'aheckmann/mquery', 'aheissenberger/serverless-appsync-offline', 'ahmadnassri/node-har-validator', 'ahmadreza-s/dotlottie-player', 'ahmadreza-s/xmlparser', 'ahomu/grunt-data-uri', 'ahram-dolphin/cli', 'ai/audio-recorder-polyfill', 'ai/browserslist']}, 'var_call_dzlLeQmV4zwL14SNAEQQZdbW': 'file_storage/call_dzlLeQmV4zwL14SNAEQQZdbW.json'}

exec(code, env_args)
