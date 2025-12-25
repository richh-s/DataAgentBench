code = """import json
import re

# Load project_info
with open(locals()['var_function-call-1341069900202570123'], 'r') as f:
    project_info_list = json.load(f)

def parse_name(text):
    candidates = re.findall(r'\b([\w\-\.]+)\/([\w\-\.]+)\b', text)
    for owner, repo in candidates:
        full = f"{owner}/{repo}"
        if full.lower() not in ['github.com', 'http://', 'https://']:
            return full
    return None

extracted_names = []
for entry in project_info_list:
    info = entry.get('Project_Information', '')
    name = parse_name(info)
    if name:
        extracted_names.append(name)

# Load mappings
with open(locals()['var_function-call-15144337828498861948'], 'r') as f:
    mappings = json.load(f)

# Get some project names from mapping
mapping_names = set()
for m in mappings:
    if m.get('ProjectName'):
        mapping_names.add(m.get('ProjectName'))

print("__RESULT__:")
print(json.dumps({
    "extracted_sample": extracted_names[:10],
    "mapping_sample": list(mapping_names)[:10],
    "intersection_count": len(set(extracted_names).intersection(mapping_names))
}))"""

env_args = {'var_function-call-9453498204060445815': [{'Name': '@discue/ui-components', 'Version': '0.13.0', 'Licenses': '[\n  "MIT"\n]', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 12\n}'}, {'Name': '@dvcol/web-extension-utils', 'Version': '1.1.1', 'Licenses': '[\n  "MIT"\n]', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 7\n}'}, {'Name': '@dxos/client', 'Version': '2.28.20-dev.a2e143d3', 'Licenses': '[\n  "MIT"\n]', 'VersionInfo': '{\n  "IsRelease": false,\n  "Ordinal": 1514\n}'}, {'Name': '@dxos/client', 'Version': '2.28.20-dev.a2e143d3', 'Licenses': '[\n  "MIT"\n]', 'VersionInfo': '{\n  "IsRelease": false,\n  "Ordinal": 1514\n}'}, {'Name': '@eden-network/data', 'Version': '1.0.9-sev.5', 'Licenses': '[\n  "MIT"\n]', 'VersionInfo': '{\n  "IsRelease": false,\n  "Ordinal": 14\n}'}], 'var_function-call-9453498204060445988': [{'Project_Information': 'The project lberrocal/npm-packages-template is hosted on GitHub and currently has 0 open issues, 0 stars, and 0 forks.'}, {'Project_Information': 'The project leaflet/leaflet on GitHub is a popular open-source library that currently has 521 open issues, 38715 stars, and 5782 forks, making it a widely recognized tool in the developer community.'}, {'Project_Information': 'The project leaflet/leaflet.fullscreen on GitHub currently has 29 open issues, 417 stars, and 118 forks, making it a noteworthy contribution to the Leaflet ecosystem.'}, {'Project_Information': 'The project leaflet/leaflet.markercluster is hosted on GitHub and currently has an open issues count of 130, along with a stars count of 3761 and forks count of 988.'}, {'Project_Information': 'The project leandrowd/react-responsive-carousel on GitHub has garnered significant attention, with a total of 2,534 stars and 636 forks, while currently having 23 open issues.'}], 'var_function-call-6934230748163086369': [{'count(*)': '176998'}], 'var_function-call-9232261889426046384': [{'count_star()': '597602'}], 'var_function-call-14844971607820229659': [{'column_name': 'Project_Information', 'column_type': 'VARCHAR', 'null': 'YES', 'key': 'None', 'default': 'None', 'extra': 'None'}, {'column_name': 'Licenses', 'column_type': 'VARCHAR', 'null': 'YES', 'key': 'None', 'default': 'None', 'extra': 'None'}, {'column_name': 'Description', 'column_type': 'VARCHAR', 'null': 'YES', 'key': 'None', 'default': 'None', 'extra': 'None'}, {'column_name': 'Homepage', 'column_type': 'VARCHAR', 'null': 'YES', 'key': 'None', 'default': 'None', 'extra': 'None'}, {'column_name': 'OSSFuzz', 'column_type': 'DOUBLE', 'null': 'YES', 'key': 'None', 'default': 'None', 'extra': 'None'}], 'var_function-call-17935917694381846867': [{'count_star()': '770'}], 'var_function-call-1341069900202570123': 'file_storage/function-call-1341069900202570123.json', 'var_function-call-15144337828498858295': 'file_storage/function-call-15144337828498858295.json', 'var_function-call-15144337828498861948': 'file_storage/function-call-15144337828498861948.json', 'var_function-call-17605324698348961652': []}

exec(code, env_args)
