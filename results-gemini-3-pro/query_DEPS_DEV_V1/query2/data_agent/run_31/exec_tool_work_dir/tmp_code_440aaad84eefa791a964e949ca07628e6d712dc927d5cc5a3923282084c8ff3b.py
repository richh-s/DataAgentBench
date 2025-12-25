code = """import json
import re

# Same logic
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
        if name.lower() != name:
             project_stats[name.lower()] = forks

with open(locals()['var_function-call-15144337828498858295'], 'r') as f:
    pkgs = json.load(f)
    valid_pkg_set = set()
    for p in pkgs:
        valid_pkg_set.add((p['Name'], p['Version']))

with open(locals()['var_function-call-15144337828498861948'], 'r') as f:
    mappings = json.load(f)

relevant_projects = set()
for m in mappings:
    if (m['Name'], m['Version']) in valid_pkg_set:
        pname = m.get('ProjectName')
        if pname:
            relevant_projects.add(pname)

results = []
for p in relevant_projects:
    forks = 0
    if p in project_stats:
        forks = project_stats[p]
    elif p.lower() in project_stats:
        forks = project_stats[p.lower()]
    
    if forks > 0 or p in project_stats or p.lower() in project_stats:
        results.append({'project': p, 'forks': forks})

results.sort(key=lambda x: x['forks'], reverse=True)
top_5 = results[:5]

print("__RESULT__:")
print(json.dumps(top_5))"""

env_args = {'var_function-call-9453498204060445815': [{'Name': '@discue/ui-components', 'Version': '0.13.0', 'Licenses': '[\n  "MIT"\n]', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 12\n}'}, {'Name': '@dvcol/web-extension-utils', 'Version': '1.1.1', 'Licenses': '[\n  "MIT"\n]', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 7\n}'}, {'Name': '@dxos/client', 'Version': '2.28.20-dev.a2e143d3', 'Licenses': '[\n  "MIT"\n]', 'VersionInfo': '{\n  "IsRelease": false,\n  "Ordinal": 1514\n}'}, {'Name': '@dxos/client', 'Version': '2.28.20-dev.a2e143d3', 'Licenses': '[\n  "MIT"\n]', 'VersionInfo': '{\n  "IsRelease": false,\n  "Ordinal": 1514\n}'}, {'Name': '@eden-network/data', 'Version': '1.0.9-sev.5', 'Licenses': '[\n  "MIT"\n]', 'VersionInfo': '{\n  "IsRelease": false,\n  "Ordinal": 14\n}'}], 'var_function-call-9453498204060445988': [{'Project_Information': 'The project lberrocal/npm-packages-template is hosted on GitHub and currently has 0 open issues, 0 stars, and 0 forks.'}, {'Project_Information': 'The project leaflet/leaflet on GitHub is a popular open-source library that currently has 521 open issues, 38715 stars, and 5782 forks, making it a widely recognized tool in the developer community.'}, {'Project_Information': 'The project leaflet/leaflet.fullscreen on GitHub currently has 29 open issues, 417 stars, and 118 forks, making it a noteworthy contribution to the Leaflet ecosystem.'}, {'Project_Information': 'The project leaflet/leaflet.markercluster is hosted on GitHub and currently has an open issues count of 130, along with a stars count of 3761 and forks count of 988.'}, {'Project_Information': 'The project leandrowd/react-responsive-carousel on GitHub has garnered significant attention, with a total of 2,534 stars and 636 forks, while currently having 23 open issues.'}], 'var_function-call-6934230748163086369': [{'count(*)': '176998'}], 'var_function-call-9232261889426046384': [{'count_star()': '597602'}], 'var_function-call-14844971607820229659': [{'column_name': 'Project_Information', 'column_type': 'VARCHAR', 'null': 'YES', 'key': 'None', 'default': 'None', 'extra': 'None'}, {'column_name': 'Licenses', 'column_type': 'VARCHAR', 'null': 'YES', 'key': 'None', 'default': 'None', 'extra': 'None'}, {'column_name': 'Description', 'column_type': 'VARCHAR', 'null': 'YES', 'key': 'None', 'default': 'None', 'extra': 'None'}, {'column_name': 'Homepage', 'column_type': 'VARCHAR', 'null': 'YES', 'key': 'None', 'default': 'None', 'extra': 'None'}, {'column_name': 'OSSFuzz', 'column_type': 'DOUBLE', 'null': 'YES', 'key': 'None', 'default': 'None', 'extra': 'None'}], 'var_function-call-17935917694381846867': [{'count_star()': '770'}], 'var_function-call-1341069900202570123': 'file_storage/function-call-1341069900202570123.json', 'var_function-call-15144337828498858295': 'file_storage/function-call-15144337828498858295.json', 'var_function-call-15144337828498861948': 'file_storage/function-call-15144337828498861948.json', 'var_function-call-17605324698348961652': [], 'var_function-call-729150113041602230': {'extracted_sample': [], 'mapping_sample': ['easyflux/eslint-config', 'dkoerner/propertyui', 'dpa-connect/bootstrap-theme', 'yeikos/js.merge', 'alastairzotos/eco-client', 'supakornnellika/react-chat-widget', 'hueniverse/hawk', 'docchipl/pobieranie-anime-z-polskich-stron', 'eartharoid/dbf.js', 'dwebprotocol/dwebid'], 'intersection_count': 0}, 'var_function-call-11591349540276479849': {'matches': []}, 'var_function-call-11101773524936527845': {'matches': [['lberrocal', 'npm-packages-template']]}, 'var_function-call-15044958810077158212': ['mui-org/material-ui', 'moment/moment', 'lodash/lodash', 'semantic-org/semantic-ui', 'react-native-elements/react-native-elements']}

exec(code, env_args)
