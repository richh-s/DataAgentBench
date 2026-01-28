code = """import json, os, re

def load_var(v):
    if isinstance(v, str) and v.endswith('.json') and os.path.exists(v):
        with open(v, 'r') as f:
            return json.load(f)
    return v

var_mapping = load_var(var_call_Zgu0dlOfqao34ryZI7bLTHJA)
var_projinfo = load_var(var_call_iEEmLfxD9Rf5lxvvk0JlBkg4)
mapping = var_mapping.get('mapping') if isinstance(var_mapping, dict) else var_mapping
projinfo = var_projinfo
map_projects = sorted(list({m['ProjectName'] for m in mapping if m.get('ProjectName')}))
projinfo_repos = set()
for entry in projinfo:
    pi = entry.get('Project_Information') or ''
    m = re.search(r'([A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+)', pi)
    if m:
        projinfo_repos.add(m.group(1))
projinfo_repos = sorted(list(projinfo_repos))

checks = ['lodash/lodash','dxos/dxos','dynamic-labs/iconic']
res = {}
for c in checks:
    res[c] = {
        'in_mapping': c in map_projects,
        'in_projinfo': c in projinfo_repos,
        'mapping_index': map_projects.index(c) if c in map_projects else None,
        'projinfo_index': projinfo_repos.index(c) if c in projinfo_repos else None,
        'repr_map': repr([p for p in map_projects if c in p][:3]),
        'repr_projinfo': repr([p for p in projinfo_repos if c in p][:3])
    }

print('__RESULT__:')
print(json.dumps(res))"""

env_args = {'var_call_wTx4WUlrMN0IMwtp8pOPhILg': 'file_storage/call_wTx4WUlrMN0IMwtp8pOPhILg.json', 'var_call_dFPubGgWvKq7qBzs9pPNNtw9': 'file_storage/call_dFPubGgWvKq7qBzs9pPNNtw9.json', 'var_call_Zgu0dlOfqao34ryZI7bLTHJA': 'file_storage/call_Zgu0dlOfqao34ryZI7bLTHJA.json', 'var_call_iEEmLfxD9Rf5lxvvk0JlBkg4': 'file_storage/call_iEEmLfxD9Rf5lxvvk0JlBkg4.json', 'var_call_DGJ043ob5YIr5XE6gfKQH2bj': [], 'var_call_0uy0Tkzqh0NidXKmHVpQ0p3C': {'num_mapping_projects': 72, 'num_projinfo_repos': 769, 'intersection_count': 0, 'intersection_sample': [], 'mapping_sample': ['0x1ance/wishport', 'asteriskzuo/react-native-create-thumbnail', 'danielusupov/ui-layer', 'dxatscale/sfpowerscripts', 'dxc-technology/halstack-react-hal', 'dxfeed/dxlink', 'dxfrontier/cds-ts-dispatcher', 'dxfrontier/cds-ts-repository', 'dxos/dxos', 'dydxfoundation/governance-contracts', 'dydxprotocol/v4-clients', 'dydxprotocol/v4-localization', 'dynamic-labs/dynamicauth', 'dynamic-labs/iconic', 'dynamicabot/signales', 'dynamicdevs/ai-assistant-ui-core', 'dynamicmapper/dynamicmapper', 'dynamicpdf-api/nodejs-client', 'dynamicweb/cli', 'dynamods/hig', 'dynamods/notificationcenter', 'dynamods/splashscreen', 'dyte-in/dyte-utils', 'dyte-in/react-native-core', 'dyte-in/react-native-ui-kit', 'dyte-in/ui-kit', 'dzangolab/fastify', 'dzeiocom/libs', 'e-conomic/taco', 'e-is/ngx-material-table', 'e-labs-io/commoncomponents', 'e-labs-io/web3provider', 'e-trias/woonplan-types', 'e2b-dev/e2b', 'e2n/validators', 'ealmansi/jagger', 'easegram/easegram-framework-nodejs', 'easy-ds-bot/framework', 'easyfe/admin-component', 'easyops-cn/brick-next-pipes', 'easyops-cn/docusaurus-search-local', 'eavfw/eavfw', 'ebay/ebayui-core-react', 'ebury/chameleon', 'ec-europa/europa-component-library', 'eccenca/gui-elements', 'eckhardt-d/dow-sdk', 'eclipse-che/che-devfile-registry', 'eclipse-glsp/glsp', 'eclipse-glsp/glsp-client'], 'projinfo_sample': ['lberrocal/npm-packages-template', 'leaflet/leaflet', 'leaflet/leaflet.fullscreen', 'leaflet/leaflet.markercluster', 'leandrowd/react-responsive-carousel', 'learnfrontend-dc/product-cart', 'ledgerproject/keypairoom', 'leebyron/jasmine-check', 'leebyron/testcheck-js', 'leecade/react-native-swiper', 'legendjaden/aftablecolumn', 'lekoarts/gatsby-themes', 'lenconda/dollie', 'leo-ran/easy-node-reflect', 'leo-ran/easy-node-server', 'leofelix077/bunchofnothing', 'leoilab/react-native-analytics-segment-io', 'leonardparisi/easy-express-server', 'leoroese/template-cli', 'letrungdo/react-ui-component-lib', 'levelkdev/dxswap-sdk', 'leviticusmb/divine-amd-loader', 'leviticusmb/divine-synchronization', 'leviticusmb/esxx-2', 'leviticusmb/ghostly', 'leviticusmb/sysconsole', 'lfujiwara/dnausp-core', 'libertydsnp/activity-content', 'libertydsnp/contracts', 'libertydsnp/parquetjs', 'libertydsnp/sdk-ts', 'libertydsnp/test-generators', 'libertyequalitydata/dynamic-data', 'liivevideo/react-native-web-webrtc', 'linkshare/service-container', 'lisiadito/checksslcertificate', 'litejs/natural-compare-lite', 'ljharb/define-properties', 'ljharb/has-symbols', 'ljharb/object-keys', 'ljharb/object.assign', 'ljharb/qs', 'ln-zap/node-lnd-grpc', 'locize/fluent_conv', 'lodash/lodash', 'logflare/winston-logflare', 'lohfu/dom-append-to', 'lohfu/dom-children', 'lohfu/dom-closest', 'lohfu/dom-insert-after']}}

exec(code, env_args)
