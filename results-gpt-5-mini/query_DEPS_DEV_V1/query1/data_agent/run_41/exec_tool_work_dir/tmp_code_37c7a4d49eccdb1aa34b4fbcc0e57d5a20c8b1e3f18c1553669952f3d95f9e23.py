code = """import json, re

def load(v):
    if isinstance(v, str):
        with open(v, 'r', encoding='utf-8') as f:
            return json.load(f)
    return v

pkg_latest = load(var_call_Wmn4ZjaNEt1MylUS4b0rwr1y)
proj_pkg = load(var_call_CM29JjO0yMg1zMvvvwhYjq5L)
proj_info = load(var_call_wYMLSMTL4oICfXSaKQLWVcUO)

# Build set of latest package keys
keys = set()
for rec in pkg_latest:
    keys.add((rec.get('System'), rec.get('Name'), rec.get('Version')))

# Collect mappings from package to project names
mappings = []
for rec in proj_pkg:
    key = (rec.get('System'), rec.get('Name'), rec.get('Version'))
    if key in keys:
        mappings.append({'System': rec.get('System'), 'Name': rec.get('Name'), 'Version': rec.get('Version'), 'ProjectName': rec.get('ProjectName')})

# Parse project_info to extract repo -> stars
repo_stars = {}
repo_pattern = re.compile(r"project\s+([A-Za-z0-9_.\-]+/[A-Za-z0-9_.\-]+)", re.IGNORECASE)
stars_pattern = re.compile(r"([0-9][0-9,]*)\s+stars", re.IGNORECASE)

for rec in proj_info:
    text = rec.get('Project_Information')
    if not isinstance(text, str):
        continue
    repo = None
    m = repo_pattern.search(text)
    if m:
        repo = m.group(1)
    if not repo:
        m2 = re.search(r"named\s+([A-Za-z0-9_.\-]+/[A-Za-z0-9_.\-]+)", text, re.IGNORECASE)
        if m2:
            repo = m2.group(1)
    if not repo:
        m3 = re.search(r"on\s+GitHub\s+under\s+the\s+name\s+([A-Za-z0-9_.\-]+/[A-Za-z0-9_.\-]+)", text, re.IGNORECASE)
        if m3:
            repo = m3.group(1)
    stars = None
    mstar = stars_pattern.findall(text)
    if mstar:
        try:
            stars = int(mstar[-1].replace(',', ''))
        except:
            stars = None
    if repo and stars is not None:
        prev = repo_stars.get(repo)
        if prev is None or stars > prev:
            repo_stars[repo] = stars

# Attach stars to mappings
results = []
for m in mappings:
    pname = m.get('ProjectName')
    stars = 0
    if isinstance(pname, str) and pname in repo_stars:
        stars = repo_stars[pname]
    else:
        if isinstance(pname, str):
            short = pname.split('/')[-1]
            for repo, s in repo_stars.items():
                if repo.endswith('/' + short):
                    stars = s
                    break
    results.append({'Name': m.get('Name'), 'Version': m.get('Version'), 'ProjectName': pname, 'Stars': int(stars)})

# For each package Name keep the record with highest stars
best = {}
for r in results:
    name = r['Name']
    if name not in best or r['Stars'] > best[name]['Stars']:
        best[name] = r

best_list = list(best.values())
best_list.sort(key=lambda x: x['Stars'], reverse=True)

top5 = best_list[:5]

# Prepare output
lines = []
for i, it in enumerate(top5, start=1):
    lines.append(str(i) + '. ' + str(it['Name']) + ' ' + str(it['Version']) + ' — ' + str(it['Stars']) + ' stars (' + str(it['ProjectName']) + ')')
answer_text = '\n'.join(lines)
output = {'text': answer_text, 'records': top5}
print('__RESULT__:')
print(json.dumps(output))"""

env_args = {'var_call_E8TbuKKRyBtdFCb4DZqm7pZI': ['packageinfo'], 'var_call_2xc9qu26NUq4fx2UNbpxve99': ['project_info', 'project_packageversion'], 'var_call_Wmn4ZjaNEt1MylUS4b0rwr1y': 'file_storage/call_Wmn4ZjaNEt1MylUS4b0rwr1y.json', 'var_call_CM29JjO0yMg1zMvvvwhYjq5L': 'file_storage/call_CM29JjO0yMg1zMvvvwhYjq5L.json', 'var_call_wYMLSMTL4oICfXSaKQLWVcUO': 'file_storage/call_wYMLSMTL4oICfXSaKQLWVcUO.json', 'var_call_ilbKEsM79khpKPMvJgTK2F5A': {'len_a': 22146, 'len_b': 597602, 'len_c': 770}, 'var_call_1weIKGjvkjiGFHP8hR66Kab9': 'file_storage/call_1weIKGjvkjiGFHP8hR66Kab9.json', 'var_call_5X4UrX9kkWzH74s659jRh4bF': [['mui-org/material-ui', 89398], ['sveltejs/svelte', 73499], ['tailwindcss/tailwindcss', 73464], ['strapi/strapi', 57236], ['quilljs/quill', 42407], ['styled-components/styled-components', 39660], ['leaflet/leaflet', 38715], ['microsoft/monaco-editor', 36025], ['mobxjs/mobx', 26802], ['react-native-elements/react-native-elements', 24814], ['svg/svgo', 19768], ['tmpvar/jsdom', 19356], ['theia-ide/theia', 18526], ['motdotla/dotenv', 17836], ['thejameskyle/react-loadable', 16576], ['mjmlio/mjml', 15829], ['shelljs/shelljs', 14202], ['rjsf-team/react-jsonschema-form', 13923], ['mozilla-services/react-jsonschema-form', 13134], ['tj/co', 11862], ['matt-esch/virtual-dom', 11564], ['react-icons/react-icons', 11295], ['mono/mono', 10630], ['leecade/react-native-swiper', 10249], ['rebilly/redoc', 9951], ['marmelab/gremlins.js', 8973], ['sass/node-sass', 8498], ['sockjs/sockjs-client', 8401], ['terkelg/prompts', 8357], ['ljharb/qs', 8073], ['sveltejs/sapper', 7056], ['shaka-project/shaka-player', 6949], ['react-native-community/react-native-webview', 6345], ['mapbox/node-sqlite3', 5917], ['microsoft/web-build-tools', 5338], ['react-native-community/react-native-tab-view', 5137], ['request/request-promise', 4769], ['supasate/connected-react-router', 4737], ['remaxjs/remax', 4569], ['react-native-webrtc/react-native-webrtc', 4546], ['mikemcl/big.js', 4519], ['serverless-nextjs/serverless-next.js', 4418], ['thejameskyle/spectacle-code-slide', 4178], ['securingsincity/react-ace', 4005], ['mpetroff/pannellum', 3927], ['rrag/react-stockcharts', 3843], ['marcbachmann/node-html-pdf', 3523], ['sindresorhus/meow', 3519], ['mbrn/material-table', 3464], ['mozilla/source-map', 3400]]}

exec(code, env_args)
