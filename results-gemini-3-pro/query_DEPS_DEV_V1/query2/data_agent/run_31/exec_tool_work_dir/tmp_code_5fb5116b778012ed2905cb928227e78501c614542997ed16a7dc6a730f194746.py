code = """import json
import re

# Same parsing logic
with open(locals()['var_function-call-1341069900202570123'], 'r') as f:
    project_info_list = json.load(f)

def parse_forks(text):
    text = text.replace(',', '')
    patterns = [
        r'(\d+)\s+forks',
        r'forks\s+count\s+of\s+(\d+)',
        r'forked\s+(\d+)\s+times'
    ]
    for pat in patterns:
        m = re.search(pat, text)
        if m:
            return int(m.group(1))
    return 0

def parse_name(text):
    matches = re.findall(r'([a-zA-Z0-9_\-\.]+)\/([a-zA-Z0-9_\-\.]+)', text)
    for owner, repo in matches:
        full = f"{owner}/{repo}"
        if owner.lower() in ['github.com', 'http:', 'https:', 'api.github.com']:
            continue
        return full
    return None

project_stats = {}
for entry in project_info_list:
    info = entry.get('Project_Information', '')
    name = parse_name(info)
    forks = parse_forks(info)
    if name:
        project_stats[name] = forks

# Load valid packages (Name, Version)
with open(locals()['var_function-call-15144337828498858295'], 'r') as f:
    pkgs = json.load(f)
    valid_pkg_set = set()
    for p in pkgs:
        valid_pkg_set.add((p['Name'], p['Version']))

# Load mapping
with open(locals()['var_function-call-15144337828498861948'], 'r') as f:
    mappings = json.load(f)

relevant_projects = set()
for m in mappings:
    if (m['Name'], m['Version']) in valid_pkg_set:
        pname = m.get('ProjectName')
        if pname:
            relevant_projects.add(pname)

# Compare
all_projects = sorted(project_stats.items(), key=lambda x: x[1], reverse=True)
top_20 = all_projects[:20]

print("__RESULT__:")
debug_list = []
for p, forks in top_20:
    is_relevant = p in relevant_projects
    debug_list.append({"project": p, "forks": forks, "relevant": is_relevant})
print(json.dumps(debug_list))"""

env_args = {'var_function-call-9453498204060445815': [{'Name': '@discue/ui-components', 'Version': '0.13.0', 'Licenses': '[\n  "MIT"\n]', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 12\n}'}, {'Name': '@dvcol/web-extension-utils', 'Version': '1.1.1', 'Licenses': '[\n  "MIT"\n]', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 7\n}'}, {'Name': '@dxos/client', 'Version': '2.28.20-dev.a2e143d3', 'Licenses': '[\n  "MIT"\n]', 'VersionInfo': '{\n  "IsRelease": false,\n  "Ordinal": 1514\n}'}, {'Name': '@dxos/client', 'Version': '2.28.20-dev.a2e143d3', 'Licenses': '[\n  "MIT"\n]', 'VersionInfo': '{\n  "IsRelease": false,\n  "Ordinal": 1514\n}'}, {'Name': '@eden-network/data', 'Version': '1.0.9-sev.5', 'Licenses': '[\n  "MIT"\n]', 'VersionInfo': '{\n  "IsRelease": false,\n  "Ordinal": 14\n}'}], 'var_function-call-9453498204060445988': [{'Project_Information': 'The project lberrocal/npm-packages-template is hosted on GitHub and currently has 0 open issues, 0 stars, and 0 forks.'}, {'Project_Information': 'The project leaflet/leaflet on GitHub is a popular open-source library that currently has 521 open issues, 38715 stars, and 5782 forks, making it a widely recognized tool in the developer community.'}, {'Project_Information': 'The project leaflet/leaflet.fullscreen on GitHub currently has 29 open issues, 417 stars, and 118 forks, making it a noteworthy contribution to the Leaflet ecosystem.'}, {'Project_Information': 'The project leaflet/leaflet.markercluster is hosted on GitHub and currently has an open issues count of 130, along with a stars count of 3761 and forks count of 988.'}, {'Project_Information': 'The project leandrowd/react-responsive-carousel on GitHub has garnered significant attention, with a total of 2,534 stars and 636 forks, while currently having 23 open issues.'}], 'var_function-call-6934230748163086369': [{'count(*)': '176998'}], 'var_function-call-9232261889426046384': [{'count_star()': '597602'}], 'var_function-call-14844971607820229659': [{'column_name': 'Project_Information', 'column_type': 'VARCHAR', 'null': 'YES', 'key': 'None', 'default': 'None', 'extra': 'None'}, {'column_name': 'Licenses', 'column_type': 'VARCHAR', 'null': 'YES', 'key': 'None', 'default': 'None', 'extra': 'None'}, {'column_name': 'Description', 'column_type': 'VARCHAR', 'null': 'YES', 'key': 'None', 'default': 'None', 'extra': 'None'}, {'column_name': 'Homepage', 'column_type': 'VARCHAR', 'null': 'YES', 'key': 'None', 'default': 'None', 'extra': 'None'}, {'column_name': 'OSSFuzz', 'column_type': 'DOUBLE', 'null': 'YES', 'key': 'None', 'default': 'None', 'extra': 'None'}], 'var_function-call-17935917694381846867': [{'count_star()': '770'}], 'var_function-call-1341069900202570123': 'file_storage/function-call-1341069900202570123.json', 'var_function-call-15144337828498858295': 'file_storage/function-call-15144337828498858295.json', 'var_function-call-15144337828498861948': 'file_storage/function-call-15144337828498861948.json', 'var_function-call-17605324698348961652': [], 'var_function-call-729150113041602230': {'extracted_sample': [], 'mapping_sample': ['easyflux/eslint-config', 'dkoerner/propertyui', 'dpa-connect/bootstrap-theme', 'yeikos/js.merge', 'alastairzotos/eco-client', 'supakornnellika/react-chat-widget', 'hueniverse/hawk', 'docchipl/pobieranie-anime-z-polskich-stron', 'eartharoid/dbf.js', 'dwebprotocol/dwebid'], 'intersection_count': 0}, 'var_function-call-11591349540276479849': {'matches': []}, 'var_function-call-11101773524936527845': {'matches': [['lberrocal', 'npm-packages-template']]}, 'var_function-call-15044958810077158212': ['mui-org/material-ui', 'moment/moment', 'lodash/lodash', 'semantic-org/semantic-ui', 'react-native-elements/react-native-elements'], 'var_function-call-3943123244702310293': [{'project': 'mui-org/material-ui', 'forks': 30522}, {'project': 'moment/moment', 'forks': 7201}, {'project': 'lodash/lodash', 'forks': 7109}, {'project': 'semantic-org/semantic-ui', 'forks': 4955}, {'project': 'react-native-elements/react-native-elements', 'forks': 4623}], 'var_function-call-6455380288742000611': [{'project': 'mui-org/material-ui', 'forks': 30522}, {'project': 'rails/rails', 'forks': 21423}, {'project': 'microsoft/typescript', 'forks': 12282}, {'project': 'mozilla/pdf.js', 'forks': 9617}, {'project': 'swagger-api/swagger-ui', 'forks': 8824}, {'project': 'strapi/strapi', 'forks': 7211}, {'project': 'moment/moment', 'forks': 7201}, {'project': 'lodash/lodash', 'forks': 7109}, {'project': 'leaflet/leaflet', 'forks': 5782}, {'project': 'react-navigation/react-navigation', 'forks': 4989}], 'var_function-call-16976381025172976131': [{'Name': '@ec-nordbund/leaflet', 'Version': '1.7.1-436430db4', 'System': 'NPM'}, {'Name': '@ec-nordbund/leaflet', 'Version': '1.7.1-build-81dc2489', 'System': 'NPM'}, {'Name': '@edgarai/strapi-provider-upload-local', 'Version': '3.6.3-devgar-fork.1', 'System': 'NPM'}, {'Name': '@edgarai/strapi-provider-upload-local', 'Version': '3.6.3-devgar-fork.2', 'System': 'NPM'}, {'Name': '@ec-nordbund/leaflet', 'Version': '1.7.1-build', 'System': 'NPM'}, {'Name': '@ec-nordbund/leaflet', 'Version': '1.7.1-build-81dc24892a3f', 'System': 'NPM'}, {'Name': '@dmrvos/infrajs>0.0.5>typescript', 'Version': '2.6.2', 'System': 'NPM'}, {'Name': '@dmrvos/infrajs>0.0.5>typescript', 'Version': '2.6.2', 'System': 'NPM'}, {'Name': '@ec-nordbund/leaflet', 'Version': '1.7.1', 'System': 'NPM'}, {'Name': '@ec-nordbund/leaflet', 'Version': '1.7.1-build-dc24892a3f', 'System': 'NPM'}], 'var_function-call-15137326591718944734': [], 'var_function-call-4782910974271546475': [], 'var_function-call-10496976520741398928': [], 'var_function-call-1366063946142933457': [{'Name': '@dummmy/pack-cli>1.0.8>lodash'}, {'Name': '@dummmy/pack-cli>1.0.9>lodash'}, {'Name': '@dummmy/webpack-cli>1.0.3>lodash'}, {'Name': '@dollarshaveclub/cli>1.0.0>lodash'}, {'Name': '@dollarshaveclub/cli>1.5.1>lodash'}]}

exec(code, env_args)
