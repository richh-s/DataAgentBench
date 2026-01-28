code = """import json, re
# load project_info full result file
with open(var_call_teg9e46LHWmd7wysPNzNB3PI, 'r', encoding='utf-8') as f:
    proj_info_list = json.load(f)
# load matches output file
with open(var_call_aJ7VxIkb4SFDJCLleMPKVPkO, 'r', encoding='utf-8') as f:
    matches_out = json.load(f)
matches = matches_out.get('all_matches', [])
project_set = {m['ProjectName'] for m in matches if m.get('ProjectName')}

# parse project_info entries
repo_map = {}
for entry in proj_info_list:
    s = entry.get('Project_Information') or entry.get('Project_Information')
    if not s:
        continue
    # find repo pattern owner/repo
    repo_match = re.search(r'([A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+)', s)
    if not repo_match:
        continue
    repo = repo_match.group(1)
    # find forks number via several patterns
    forks = None
    patterns = [r'forks count of (\d+)', r'forks count of (\d+)', r'(\d{1,7}) forks', r'forked (\d+) times', r'been forked (\d+) times', r'has been forked (\d+) times', r'forked (\d+)', r'has (\d+) forks']
    for p in patterns:
        m = re.search(p, s)
        if m:
            try:
                forks = int(m.group(1))
            except:
                forks = None
            break
    if forks is None:
        # sometimes phrasing like 'and 5782 forks' or ', and 5782 forks'
        m = re.search(r'[,\sand]+(\d{1,7}) forks', s)
        if m:
            forks = int(m.group(1))
    if forks is None:
        # fallback: find all numbers and maybe last number is forks, but risky. skip.
        continue
    repo_map[repo] = {'Forks': forks, 'Project_Information': s}

# filter to project_set
filtered = []
for repo, info in repo_map.items():
    if repo in project_set:
        filtered.append({'ProjectName': repo, 'Forks': info['Forks'], 'Project_Information': info['Project_Information']})
# sort by forks desc
filtered_sorted = sorted(filtered, key=lambda x: x['Forks'], reverse=True)
Top5 = filtered_sorted[:5]
print('__RESULT__:')
print(json.dumps(Top5))"""

env_args = {'var_call_ahEJxFjLRUBjBFLTYlcUqhv9': 'file_storage/call_ahEJxFjLRUBjBFLTYlcUqhv9.json', 'var_call_Z57R3AfceTnrp6dzF88dKyq7': 'file_storage/call_Z57R3AfceTnrp6dzF88dKyq7.json', 'var_call_gmD6KL9wxLcbQjG56WLSSqvS': {'count': 85158, 'sample_first_50_names': ['@discue/ui-components', '@dvcol/web-extension-utils', '@eclipsejs/cli', '@ebot7/edem-react', '@e4a/irmaseal-wasm-bindings', '@ebury/chameleon-components', '@e-group/material-form', '@e-group/material-layout', '@dspworkplace/ui', '@ditojs/router', '@ditojs/ui', '@ditojs/admin', '@dsrv/kms', '@domojs/rfx-parsers', '@dnvgl/playwright-live-recorder', '@ditojs/router', '@ditojs/router', '@draftbit/ui', '@draftbit/ui', '@dr.cash/components', '@dotdev/sanity-plugin-structure-helpers', '@dspworkplace/ui', '@easyops-cn/docusaurus-search-local', '@dwelle/excalidraw', '@dxos/crypto', '@dxos/aurora-table', '@dxos/debug', '@dxos/cli', '@dxos/react-appkit', '@dxos/react-uikit', '@dxos/hypercore', '@dxos/echo-typegen', '@dxos/plate', '@dxos/create-tasks', '@dxos/util', '@dxos/aurora', '@dxos/react-list', '@dxos/model-factory', '@dxos/testutils', '@dxos/messaging', '@dxos/object-model', '@dxos/document-model', '@dxos/node-std', '@dxos/context', '@dxos/react-uikit', '@dxos/teleport-extension-object-sync', '@dxos/client-services', '@dxos/messenger-model', '@dxos/messenger-model', '@dxos/network-manager']}, 'var_call_dfmxrw0uxUUaNGwJEX5x2u64': ['project_info', 'project_packageversion'], 'var_call_hfRUXBKifNfL89HhYiygnKud': 'file_storage/call_hfRUXBKifNfL89HhYiygnKud.json', 'var_call_SVaaigrJgbTgFXIwYyvA6qJA': [{'Project_Information': 'The project lberrocal/npm-packages-template is hosted on GitHub and currently has 0 open issues, 0 stars, and 0 forks.'}, {'Project_Information': 'The project leaflet/leaflet on GitHub is a popular open-source library that currently has 521 open issues, 38715 stars, and 5782 forks, making it a widely recognized tool in the developer community.'}, {'Project_Information': 'The project leaflet/leaflet.fullscreen on GitHub currently has 29 open issues, 417 stars, and 118 forks, making it a noteworthy contribution to the Leaflet ecosystem.'}, {'Project_Information': 'The project leaflet/leaflet.markercluster is hosted on GitHub and currently has an open issues count of 130, along with a stars count of 3761 and forks count of 988.'}, {'Project_Information': 'The project leandrowd/react-responsive-carousel on GitHub has garnered significant attention, with a total of 2,534 stars and 636 forks, while currently having 23 open issues.'}, {'Project_Information': 'The project is hosted on GitHub under the name learnfrontend-dc/product-cart, and it currently has 2 open issues. It has garnered a total of 11 stars and has been forked 12 times.'}, {'Project_Information': 'The GitHub project ledgerproject/keypairoom currently has 3 open issues, 3 stars, and 0 forks.'}, {'Project_Information': 'The project leebyron/jasmine-check is hosted on GitHub and currently has 0 open issues, 11 stars, and 3 forks.'}, {'Project_Information': 'The project leebyron/testcheck-js on GitHub has an open issues count of 29, a stars count of 1185, and a forks count of 58, making it a notable repository in the community.'}, {'Project_Information': 'The project leecade/react-native-swiper is hosted on GitHub and has a total of 786 open issues, along with an impressive 10,249 stars and 2,392 forks, making it a popular choice among developers for implementing swiping functionality in React Native applications.'}, {'Project_Information': 'The project legendjaden/aftablecolumn on GitHub currently has an open issues count of 35, a stars count of 136, and a forks count of 29.'}, {'Project_Information': 'The project lekoarts/gatsby-themes on GitHub currently has 11 open issues, 1836 stars, and 568 forks, making it a popular choice among developers looking for Gatsby themes.'}, {'Project_Information': 'The GitHub project lenconda/dollie currently has 0 open issues, 12 stars, and 3 forks, making it a noteworthy repository in its category.'}, {'Project_Information': 'The project leo-ran/easy-node-reflect is hosted on GitHub and currently has 0 open issues, 0 stars, and 0 forks, indicating that it may be in its early stages or not yet widely recognized within the GitHub community.'}, {'Project_Information': 'The project named leo-ran/easy-node-server is hosted on GitHub and currently has an open issues count of 0, stars count of 0, and forks count of 0.'}, {'Project_Information': 'The project named leofelix077/bunchofnothing on GitHub currently has 40 open issues, 0 stars, and 0 forks.'}, {'Project_Information': 'The project leoilab/react-native-analytics-segment-io on GitHub currently has 26 open issues, 71 stars, and 36 forks, making it a notable repository for those interested in integrating analytics into React Native applications.'}, {'Project_Information': 'The project on GitHub, named leonardparisi/easy-express-server, currently has an open issues count of 0, a stars count of 0, and a forks count of 0.'}, {'Project_Information': 'The project leoroese/template-cli is hosted on GitHub and currently has 1 open issue, along with a total of 17 stars and 13 forks.'}, {'Project_Information': 'The project is a GitHub repository named letrungdo/react-ui-component-lib, which currently has 0 open issues, 4 stars, and 0 forks.'}], 'var_call_aJ7VxIkb4SFDJCLleMPKVPkO': 'file_storage/call_aJ7VxIkb4SFDJCLleMPKVPkO.json', 'var_call_teg9e46LHWmd7wysPNzNB3PI': 'file_storage/call_teg9e46LHWmd7wysPNzNB3PI.json'}

exec(code, env_args)
