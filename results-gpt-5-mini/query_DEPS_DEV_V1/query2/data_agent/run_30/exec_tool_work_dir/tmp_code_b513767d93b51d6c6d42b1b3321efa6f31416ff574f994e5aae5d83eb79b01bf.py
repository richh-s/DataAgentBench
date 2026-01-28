code = """import json
# load package pairs (Name, Version) from earlier unique list
with open(var_call_Z57R3AfceTnrp6dzF88dKyq7, 'r', encoding='utf-8') as f:
    pkg_pairs = json.load(f)
# load project_packageversion data
with open(var_call_hfRUXBKifNfL89HhYiygnKud, 'r', encoding='utf-8') as f:
    proj_pkg = json.load(f)
# Build map from (Name,Version) to list of ProjectName
pp_map = {}
for r in proj_pkg:
    if r['System']!='NPM':
        continue
    key = (r['Name'], r['Version'])
    pp_map.setdefault(key, []).append(r.get('ProjectName'))
# For each package pair, get associated ProjectName(s)
matches = []
for p in pkg_pairs:
    key = (p['Name'], p['Version'])
    if key in pp_map:
        for pn in set(pp_map[key]):
            matches.append({'Name': p['Name'], 'Version': p['Version'], 'ProjectName': pn})
# write matches to file
out_path = '/tmp/matches.json'
with open(out_path, 'w', encoding='utf-8') as f:
    json.dump(matches, f)
print('__RESULT__:')
print(out_path)"""

env_args = {'var_call_ahEJxFjLRUBjBFLTYlcUqhv9': 'file_storage/call_ahEJxFjLRUBjBFLTYlcUqhv9.json', 'var_call_Z57R3AfceTnrp6dzF88dKyq7': 'file_storage/call_Z57R3AfceTnrp6dzF88dKyq7.json', 'var_call_gmD6KL9wxLcbQjG56WLSSqvS': {'count': 85158, 'sample_first_50_names': ['@discue/ui-components', '@dvcol/web-extension-utils', '@eclipsejs/cli', '@ebot7/edem-react', '@e4a/irmaseal-wasm-bindings', '@ebury/chameleon-components', '@e-group/material-form', '@e-group/material-layout', '@dspworkplace/ui', '@ditojs/router', '@ditojs/ui', '@ditojs/admin', '@dsrv/kms', '@domojs/rfx-parsers', '@dnvgl/playwright-live-recorder', '@ditojs/router', '@ditojs/router', '@draftbit/ui', '@draftbit/ui', '@dr.cash/components', '@dotdev/sanity-plugin-structure-helpers', '@dspworkplace/ui', '@easyops-cn/docusaurus-search-local', '@dwelle/excalidraw', '@dxos/crypto', '@dxos/aurora-table', '@dxos/debug', '@dxos/cli', '@dxos/react-appkit', '@dxos/react-uikit', '@dxos/hypercore', '@dxos/echo-typegen', '@dxos/plate', '@dxos/create-tasks', '@dxos/util', '@dxos/aurora', '@dxos/react-list', '@dxos/model-factory', '@dxos/testutils', '@dxos/messaging', '@dxos/object-model', '@dxos/document-model', '@dxos/node-std', '@dxos/context', '@dxos/react-uikit', '@dxos/teleport-extension-object-sync', '@dxos/client-services', '@dxos/messenger-model', '@dxos/messenger-model', '@dxos/network-manager']}, 'var_call_dfmxrw0uxUUaNGwJEX5x2u64': ['project_info', 'project_packageversion'], 'var_call_hfRUXBKifNfL89HhYiygnKud': 'file_storage/call_hfRUXBKifNfL89HhYiygnKud.json'}

exec(code, env_args)
