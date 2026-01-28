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

# normalize
for p in projinfo:
    if 'Project_Information' not in p:
        p['Project_Information'] = ''

# function to extract stars from a project_info string
def extract_stars(pi):
    if not pi:
        return None
    # Try several patterns
    patterns = [r'([0-9,]+) stars', r'stars count of ([0-9,]+)', r'has a total of ([0-9,]+) stars', r'has garnered a total of ([0-9,]+) stars', r'has currently [0-9,]+ open issues, ([0-9,]+) stars']
    for pat in patterns:
        m = re.search(pat, pi)
        if m:
            try:
                return int(m.group(1).replace(',',''))
            except:
                pass
    return None

# For each mapping entry, find matching project_info entries where Project_Information contains the exact repo string
records = []
for m in mapping:
    repo = m.get('ProjectName')
    if not repo:
        continue
    matched_stars = []
    for p in projinfo:
        pi = p.get('Project_Information') or ''
        if repo in pi:
            s = extract_stars(pi)
            if s is not None:
                matched_stars.append(s)
    if matched_stars:
        # take max
        stars = max(matched_stars)
        records.append({'Name': m.get('Name'), 'Version': m.get('Version'), 'ProjectName': repo, 'Stars': stars})

# sort and top5
records_sorted = sorted(records, key=lambda x: x['Stars'], reverse=True)
top5 = records_sorted[:5]

print('__RESULT__:')
print(json.dumps(top5))"""

env_args = {'var_call_wTx4WUlrMN0IMwtp8pOPhILg': 'file_storage/call_wTx4WUlrMN0IMwtp8pOPhILg.json', 'var_call_dFPubGgWvKq7qBzs9pPNNtw9': 'file_storage/call_dFPubGgWvKq7qBzs9pPNNtw9.json', 'var_call_Zgu0dlOfqao34ryZI7bLTHJA': 'file_storage/call_Zgu0dlOfqao34ryZI7bLTHJA.json', 'var_call_iEEmLfxD9Rf5lxvvk0JlBkg4': 'file_storage/call_iEEmLfxD9Rf5lxvvk0JlBkg4.json', 'var_call_DGJ043ob5YIr5XE6gfKQH2bj': [], 'var_call_0uy0Tkzqh0NidXKmHVpQ0p3C': {'num_mapping_projects': 72, 'num_projinfo_repos': 769, 'intersection_count': 0, 'intersection_sample': [], 'mapping_sample': ['0x1ance/wishport', 'asteriskzuo/react-native-create-thumbnail', 'danielusupov/ui-layer', 'dxatscale/sfpowerscripts', 'dxc-technology/halstack-react-hal', 'dxfeed/dxlink', 'dxfrontier/cds-ts-dispatcher', 'dxfrontier/cds-ts-repository', 'dxos/dxos', 'dydxfoundation/governance-contracts', 'dydxprotocol/v4-clients', 'dydxprotocol/v4-localization', 'dynamic-labs/dynamicauth', 'dynamic-labs/iconic', 'dynamicabot/signales', 'dynamicdevs/ai-assistant-ui-core', 'dynamicmapper/dynamicmapper', 'dynamicpdf-api/nodejs-client', 'dynamicweb/cli', 'dynamods/hig', 'dynamods/notificationcenter', 'dynamods/splashscreen', 'dyte-in/dyte-utils', 'dyte-in/react-native-core', 'dyte-in/react-native-ui-kit', 'dyte-in/ui-kit', 'dzangolab/fastify', 'dzeiocom/libs', 'e-conomic/taco', 'e-is/ngx-material-table', 'e-labs-io/commoncomponents', 'e-labs-io/web3provider', 'e-trias/woonplan-types', 'e2b-dev/e2b', 'e2n/validators', 'ealmansi/jagger', 'easegram/easegram-framework-nodejs', 'easy-ds-bot/framework', 'easyfe/admin-component', 'easyops-cn/brick-next-pipes', 'easyops-cn/docusaurus-search-local', 'eavfw/eavfw', 'ebay/ebayui-core-react', 'ebury/chameleon', 'ec-europa/europa-component-library', 'eccenca/gui-elements', 'eckhardt-d/dow-sdk', 'eclipse-che/che-devfile-registry', 'eclipse-glsp/glsp', 'eclipse-glsp/glsp-client'], 'projinfo_sample': ['lberrocal/npm-packages-template', 'leaflet/leaflet', 'leaflet/leaflet.fullscreen', 'leaflet/leaflet.markercluster', 'leandrowd/react-responsive-carousel', 'learnfrontend-dc/product-cart', 'ledgerproject/keypairoom', 'leebyron/jasmine-check', 'leebyron/testcheck-js', 'leecade/react-native-swiper', 'legendjaden/aftablecolumn', 'lekoarts/gatsby-themes', 'lenconda/dollie', 'leo-ran/easy-node-reflect', 'leo-ran/easy-node-server', 'leofelix077/bunchofnothing', 'leoilab/react-native-analytics-segment-io', 'leonardparisi/easy-express-server', 'leoroese/template-cli', 'letrungdo/react-ui-component-lib', 'levelkdev/dxswap-sdk', 'leviticusmb/divine-amd-loader', 'leviticusmb/divine-synchronization', 'leviticusmb/esxx-2', 'leviticusmb/ghostly', 'leviticusmb/sysconsole', 'lfujiwara/dnausp-core', 'libertydsnp/activity-content', 'libertydsnp/contracts', 'libertydsnp/parquetjs', 'libertydsnp/sdk-ts', 'libertydsnp/test-generators', 'libertyequalitydata/dynamic-data', 'liivevideo/react-native-web-webrtc', 'linkshare/service-container', 'lisiadito/checksslcertificate', 'litejs/natural-compare-lite', 'ljharb/define-properties', 'ljharb/has-symbols', 'ljharb/object-keys', 'ljharb/object.assign', 'ljharb/qs', 'ln-zap/node-lnd-grpc', 'locize/fluent_conv', 'lodash/lodash', 'logflare/winston-logflare', 'lohfu/dom-append-to', 'lohfu/dom-children', 'lohfu/dom-closest', 'lohfu/dom-insert-after']}, 'var_call_QxIAthLcRvrqsBtHvk44LMs7': {'lodash/lodash': {'in_mapping': False, 'in_projinfo': True, 'mapping_index': None, 'projinfo_index': 44, 'repr_map': '[]', 'repr_projinfo': "['lodash/lodash']"}, 'dxos/dxos': {'in_mapping': True, 'in_projinfo': False, 'mapping_index': 8, 'projinfo_index': None, 'repr_map': "['dxos/dxos']", 'repr_projinfo': '[]'}, 'dynamic-labs/iconic': {'in_mapping': True, 'in_projinfo': False, 'mapping_index': 13, 'projinfo_index': None, 'repr_map': "['dynamic-labs/iconic']", 'repr_projinfo': '[]'}}}

exec(code, env_args)
