code = """import json

pkg_latest = json.load(open(var_call_Wmn4ZjaNEt1MylUS4b0rwr1y, 'r', encoding='utf-8'))
proj_pkg = json.load(open(var_call_CM29JjO0yMg1zMvvvwhYjq5L, 'r', encoding='utf-8'))
proj_info = json.load(open(var_call_wYMLSMTL4oICfXSaKQLWVcUO, 'r', encoding='utf-8'))

# Build set of latest package keys
keys = set((r.get('System'), r.get('Name'), r.get('Version')) for r in pkg_latest)

# Build mapping Name->ProjectName for latest versions
name_to_projects = {}
for r in proj_pkg:
    key = (r.get('System'), r.get('Name'), r.get('Version'))
    if key in keys:
        name_to_projects.setdefault(r.get('Name'), set()).add(r.get('ProjectName'))

# build repo->stars from proj_info
import re
repo_pattern = re.compile(r"project\s+([A-Za-z0-9_.\-]+/[A-Za-z0-9_.\-]+)", re.IGNORECASE)
stars_pattern = re.compile(r"([0-9][0-9,]*)\s+stars", re.IGNORECASE)
repo_stars = {}
for rec in proj_info:
    text = rec.get('Project_Information')
    if not isinstance(text, str):
        continue
    m = repo_pattern.search(text)
    repo = None
    if m:
        repo = m.group(1)
    else:
        m2 = re.search(r"named\s+([A-Za-z0-9_.\-]+/[A-Za-z0-9_.\-]+)", text, re.IGNORECASE)
        if m2:
            repo = m2.group(1)
    if not repo:
        m3 = re.search(r"on\s+GitHub\s+under\s+the\s+name\s+([A-Za-z0-9_.\-]+/[A-Za-z0-9_.\-]+)", text, re.IGNORECASE)
        if m3:
            repo = m3.group(1)
    if not repo:
        continue
    mstar = stars_pattern.findall(text)
    if not mstar:
        continue
    stars = int(mstar[-1].replace(',', ''))
    if repo in repo_stars:
        repo_stars[repo] = max(repo_stars[repo], stars)
    else:
        repo_stars[repo] = stars

# For each package name, find best matching project repo stars
results = []
for name, projects in name_to_projects.items():
    best = {'Name': name, 'Version': None, 'ProjectName': None, 'Stars': 0}
    # find version from pkg_latest
    for p in pkg_latest:
        if p.get('Name') == name:
            best['Version'] = p.get('Version')
            break
    for proj in projects:
        if proj in repo_stars:
            s = repo_stars[proj]
        else:
            # try short name match
            short = proj.split('/')[-1]
            s = 0
            for repo, val in repo_stars.items():
                if repo.endswith('/' + short):
                    s = val
                    break
        if s > best['Stars']:
            best['Stars'] = s
            best['ProjectName'] = proj
    results.append(best)

# sort
results.sort(key=lambda x: x['Stars'], reverse=True)
top5 = results[:5]

print('__RESULT__:')
print(json.dumps({'top5': top5}))"""

env_args = {'var_call_E8TbuKKRyBtdFCb4DZqm7pZI': ['packageinfo'], 'var_call_2xc9qu26NUq4fx2UNbpxve99': ['project_info', 'project_packageversion'], 'var_call_Wmn4ZjaNEt1MylUS4b0rwr1y': 'file_storage/call_Wmn4ZjaNEt1MylUS4b0rwr1y.json', 'var_call_CM29JjO0yMg1zMvvvwhYjq5L': 'file_storage/call_CM29JjO0yMg1zMvvvwhYjq5L.json', 'var_call_wYMLSMTL4oICfXSaKQLWVcUO': 'file_storage/call_wYMLSMTL4oICfXSaKQLWVcUO.json', 'var_call_ilbKEsM79khpKPMvJgTK2F5A': {'len_a': 22146, 'len_b': 597602, 'len_c': 770}, 'var_call_1weIKGjvkjiGFHP8hR66Kab9': 'file_storage/call_1weIKGjvkjiGFHP8hR66Kab9.json', 'var_call_5X4UrX9kkWzH74s659jRh4bF': [['mui-org/material-ui', 89398], ['sveltejs/svelte', 73499], ['tailwindcss/tailwindcss', 73464], ['strapi/strapi', 57236], ['quilljs/quill', 42407], ['styled-components/styled-components', 39660], ['leaflet/leaflet', 38715], ['microsoft/monaco-editor', 36025], ['mobxjs/mobx', 26802], ['react-native-elements/react-native-elements', 24814], ['svg/svgo', 19768], ['tmpvar/jsdom', 19356], ['theia-ide/theia', 18526], ['motdotla/dotenv', 17836], ['thejameskyle/react-loadable', 16576], ['mjmlio/mjml', 15829], ['shelljs/shelljs', 14202], ['rjsf-team/react-jsonschema-form', 13923], ['mozilla-services/react-jsonschema-form', 13134], ['tj/co', 11862], ['matt-esch/virtual-dom', 11564], ['react-icons/react-icons', 11295], ['mono/mono', 10630], ['leecade/react-native-swiper', 10249], ['rebilly/redoc', 9951], ['marmelab/gremlins.js', 8973], ['sass/node-sass', 8498], ['sockjs/sockjs-client', 8401], ['terkelg/prompts', 8357], ['ljharb/qs', 8073], ['sveltejs/sapper', 7056], ['shaka-project/shaka-player', 6949], ['react-native-community/react-native-webview', 6345], ['mapbox/node-sqlite3', 5917], ['microsoft/web-build-tools', 5338], ['react-native-community/react-native-tab-view', 5137], ['request/request-promise', 4769], ['supasate/connected-react-router', 4737], ['remaxjs/remax', 4569], ['react-native-webrtc/react-native-webrtc', 4546], ['mikemcl/big.js', 4519], ['serverless-nextjs/serverless-next.js', 4418], ['thejameskyle/spectacle-code-slide', 4178], ['securingsincity/react-ace', 4005], ['mpetroff/pannellum', 3927], ['rrag/react-stockcharts', 3843], ['marcbachmann/node-html-pdf', 3523], ['sindresorhus/meow', 3519], ['mbrn/material-table', 3464], ['mozilla/source-map', 3400]], 'var_call_K3xsJYqG9IUrssHSG593hUHh': [{'System': 'NPM', 'Name': '@edgarai/strapi-provider-upload-local', 'Version': '3.6.3-devgar-fork.1', 'ProjectName': 'strapi/strapi'}, {'System': 'NPM', 'Name': '@docly/web', 'Version': '0.1.381', 'ProjectName': 'mui-org/material-ui'}, {'System': 'NPM', 'Name': '@docly/web', 'Version': '0.1.371', 'ProjectName': 'mui-org/material-ui'}, {'System': 'NPM', 'Name': '@docly/web', 'Version': '0.0.2', 'ProjectName': 'mui-org/material-ui'}, {'System': 'NPM', 'Name': '@docly/web', 'Version': '0.2.0', 'ProjectName': 'mui-org/material-ui'}, {'System': 'NPM', 'Name': '@docly/web', 'Version': '0.0.1', 'ProjectName': 'mui-org/material-ui'}, {'System': 'NPM', 'Name': '@docly/web', 'Version': '0.1.362', 'ProjectName': 'mui-org/material-ui'}, {'System': 'NPM', 'Name': '@dylanvann/svelte', 'Version': '3.25.2', 'ProjectName': 'sveltejs/svelte'}, {'System': 'NPM', 'Name': '@edgarai/strapi-provider-upload-local', 'Version': '3.6.3-devgar-fork.2', 'ProjectName': 'strapi/strapi'}, {'System': 'NPM', 'Name': '@docly/web', 'Version': '0.1.381', 'ProjectName': 'mui-org/material-ui'}, {'System': 'NPM', 'Name': '@dylanvann/svelte', 'Version': '3.25.3', 'ProjectName': 'sveltejs/svelte'}, {'System': 'NPM', 'Name': '@docly/web', 'Version': '0.1.362', 'ProjectName': 'mui-org/material-ui'}, {'System': 'NPM', 'Name': '@docly/web', 'Version': '0.0.1', 'ProjectName': 'mui-org/material-ui'}, {'System': 'NPM', 'Name': '@dylanvann/svelte', 'Version': '3.25.0', 'ProjectName': 'sveltejs/svelte'}, {'System': 'NPM', 'Name': '@edgarai/strapi-provider-upload-local', 'Version': '3.6.3-devgar-fork.2', 'ProjectName': 'strapi/strapi'}, {'System': 'NPM', 'Name': '@dumc11/tailwindcss', 'Version': '0.4.0', 'ProjectName': 'tailwindcss/tailwindcss'}, {'System': 'NPM', 'Name': '@dman777/shadow-dom-quill-temp', 'Version': '1.0.0', 'ProjectName': 'quilljs/quill'}, {'System': 'NPM', 'Name': '@docly/web', 'Version': '0.0.2', 'ProjectName': 'mui-org/material-ui'}, {'System': 'NPM', 'Name': '@dylanvann/svelte', 'Version': '3.25.0', 'ProjectName': 'sveltejs/svelte'}, {'System': 'NPM', 'Name': '@edgarai/strapi-provider-upload-local', 'Version': '3.6.3-devgar-fork.1', 'ProjectName': 'strapi/strapi'}, {'System': 'NPM', 'Name': '@docly/web', 'Version': '0.0.362', 'ProjectName': 'mui-org/material-ui'}, {'System': 'NPM', 'Name': '@dylanvann/svelte', 'Version': '3.25.3', 'ProjectName': 'sveltejs/svelte'}, {'System': 'NPM', 'Name': '@dylanvann/svelte', 'Version': '3.25.1', 'ProjectName': 'sveltejs/svelte'}, {'System': 'NPM', 'Name': '@docly/web', 'Version': '0.2.0', 'ProjectName': 'mui-org/material-ui'}, {'System': 'NPM', 'Name': '@dylanvann/svelte', 'Version': '3.25.4', 'ProjectName': 'sveltejs/svelte'}, {'System': 'NPM', 'Name': '@dylanvann/svelte', 'Version': '3.25.1', 'ProjectName': 'sveltejs/svelte'}, {'System': 'NPM', 'Name': '@dumc11/tailwindcss', 'Version': '0.4.0', 'ProjectName': 'tailwindcss/tailwindcss'}, {'System': 'NPM', 'Name': '@docly/web', 'Version': '0.2.1', 'ProjectName': 'mui-org/material-ui'}, {'System': 'NPM', 'Name': '@dylanvann/svelte', 'Version': '3.25.4', 'ProjectName': 'sveltejs/svelte'}, {'System': 'NPM', 'Name': '@docly/web', 'Version': '0.2.1', 'ProjectName': 'mui-org/material-ui'}, {'System': 'NPM', 'Name': '@docly/web', 'Version': '0.0.362', 'ProjectName': 'mui-org/material-ui'}, {'System': 'NPM', 'Name': '@docly/web', 'Version': '0.1.371', 'ProjectName': 'mui-org/material-ui'}, {'System': 'NPM', 'Name': '@dylanvann/svelte', 'Version': '3.25.2', 'ProjectName': 'sveltejs/svelte'}], 'var_call_P9X0u4X8yzp04aeHfnYTSw7I': [{'System': 'NPM', 'Name': '@dman777/shadow-dom-quill-temp', 'Version': '1.0.0'}, {'System': 'NPM', 'Name': '@docly/web', 'Version': '0.2.3'}, {'System': 'NPM', 'Name': '@dumc11/tailwindcss', 'Version': '0.4.0'}, {'System': 'NPM', 'Name': '@dylanvann/svelte', 'Version': '3.25.4'}, {'System': 'NPM', 'Name': '@edgarai/strapi-provider-upload-local', 'Version': '3.6.3-devgar-fork.2'}]}

exec(code, env_args)
